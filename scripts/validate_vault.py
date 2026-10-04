#!/usr/bin/env python3
"""Lightweight integrity audit for a historical Obsidian vault.

Stdlib only. The parser intentionally understands only the small top-level
frontmatter subset needed by this skill (type, uid, aliases). It does not try
to be a general YAML parser.
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

ALLOWED_TYPES = {"person", "event", "state", "concept", "comparison", "moc"}
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")


def parse_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def parse_frontmatter(text: str) -> dict:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    lines = text[4:end].splitlines()
    result: dict[str, object] = {}
    current_list: str | None = None
    for raw in lines:
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        m_item = re.match(r"^\s*-\s+(.*)$", raw)
        if m_item and current_list:
            result.setdefault(current_list, []).append(parse_scalar(m_item.group(1)))
            continue
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", raw)
        if not m:
            current_list = None
            continue
        key, value = m.group(1), m.group(2).strip()
        if value == "":
            result[key] = []
            current_list = key
        elif value.startswith("[") and value.endswith("]"):
            parts = [p.strip() for p in value[1:-1].split(",") if p.strip()]
            result[key] = [parse_scalar(p) for p in parts]
            current_list = None
        else:
            result[key] = parse_scalar(value)
            current_list = None
    return result


def normalize_target(raw: str) -> str:
    target = raw.split("|", 1)[0].split("#", 1)[0].strip()
    if target.endswith(".md"):
        target = target[:-3]
    return target.replace("\\", "/")


def audit(vault: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    md_files = [p for p in vault.rglob("*.md") if ".obsidian" not in p.parts]

    by_stem: dict[str, list[Path]] = defaultdict(list)
    by_uid: dict[str, list[Path]] = defaultdict(list)
    alias_to_files: dict[str, list[Path]] = defaultdict(list)
    parsed: dict[Path, tuple[str, dict]] = {}

    for path in md_files:
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            warnings.append(f"Non-UTF8 markdown skipped: {path}")
            continue
        fm = parse_frontmatter(text)
        parsed[path] = (text, fm)
        by_stem[path.stem].append(path)

        uid = fm.get("uid")
        if isinstance(uid, str) and uid:
            by_uid[uid].append(path)

        aliases = fm.get("aliases", [])
        if isinstance(aliases, str):
            aliases = [aliases]
        if isinstance(aliases, list):
            for alias in aliases:
                if isinstance(alias, str) and alias.strip():
                    alias_to_files[alias.strip()].append(path)

        ntype = fm.get("type")
        # Reading records and ordinary notes are allowed to have no canonical type.
        if ntype and ntype not in ALLOWED_TYPES:
            warnings.append(f"Unknown canonical type '{ntype}': {path.relative_to(vault)}")

    for stem, paths in sorted(by_stem.items()):
        if len(paths) > 1:
            warnings.append(
                "Duplicate note title '%s': %s"
                % (stem, ", ".join(str(p.relative_to(vault)) for p in paths))
            )

    for uid, paths in sorted(by_uid.items()):
        if len(paths) > 1:
            errors.append(
                "Duplicate uid '%s': %s"
                % (uid, ", ".join(str(p.relative_to(vault)) for p in paths))
            )

    for alias, paths in sorted(alias_to_files.items()):
        unique = {str(p.resolve()) for p in paths}
        if len(unique) > 1:
            warnings.append(
                "Alias '%s' resolves to multiple notes: %s"
                % (alias, ", ".join(str(p.relative_to(vault)) for p in paths))
            )

    # Best-effort wikilink resolution: exact path, stem, or alias.
    rel_no_ext = {
        str(p.relative_to(vault).with_suffix("")).replace("\\", "/"): p for p in parsed
    }
    stems = {stem for stem in by_stem}
    aliases = set(alias_to_files)

    for path, (text, _fm) in parsed.items():
        for match in WIKILINK_RE.finditer(text):
            target = normalize_target(match.group(1))
            if not target or target.startswith("http://") or target.startswith("https://"):
                continue
            if target in rel_no_ext or target in stems or target in aliases:
                continue
            warnings.append(
                f"Unresolved wikilink [[{match.group(1)}]] in {path.relative_to(vault)}"
            )

    return errors, warnings


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_vault.py <vault-directory>", file=sys.stderr)
        return 2
    vault = Path(sys.argv[1]).expanduser().resolve()
    if not vault.is_dir():
        print(f"ERROR: not a directory: {vault}", file=sys.stderr)
        return 2

    errors, warnings = audit(vault)
    for warning in warnings:
        print(f"WARN: {warning}")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)

    if errors:
        return 1
    print(f"OK: {vault} ({len(warnings)} warning(s))")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
