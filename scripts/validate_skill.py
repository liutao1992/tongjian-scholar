#!/usr/bin/env python3
"""Validate the local skill package structure with stdlib only."""

from __future__ import annotations

import re
import sys
from pathlib import Path


def extract_frontmatter(text: str) -> str | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    return text[4:end]


def scalar(frontmatter: str, key: str) -> str | None:
    m = re.search(rf"(?m)^{re.escape(key)}:\s*(.+?)\s*$", frontmatter)
    if not m:
        return None
    value = m.group(1).strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        value = value[1:-1]
    return value.strip() or None


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]).resolve()
    errors: list[str] = []
    warnings: list[str] = []

    skill = root / "SKILL.md"
    if not skill.exists():
        print("ERROR: missing SKILL.md", file=sys.stderr)
        return 1

    text = skill.read_text(encoding="utf-8")
    fm = extract_frontmatter(text)
    if fm is None:
        errors.append("SKILL.md must start with YAML frontmatter")
        fm = ""

    name = scalar(fm, "name")
    desc = scalar(fm, "description")
    version_match = re.search(r'(?m)^\s*version:\s*["\']?([^\n"\']+)', fm)
    version = version_match.group(1).strip() if version_match else None

    if not name:
        errors.append("frontmatter missing name")
    if not desc:
        errors.append("frontmatter missing description")
    if name and root.name != name:
        warnings.append(f"folder name '{root.name}' differs from skill name '{name}'")
    if not version:
        warnings.append("metadata.version not found")

    # Ensure package-local paths mentioned in inline code exist.
    refs = sorted(set(re.findall(r'`((?:references|scripts)/[^`\n]+)`', text)))
    for rel in refs:
        # Ignore command examples with arguments.
        rel = rel.strip().split()[0]
        if not (root / rel).exists():
            errors.append(f"referenced file missing: {rel}")

    readme = root / "README.md"
    if readme.exists() and version:
        rtext = readme.read_text(encoding="utf-8")
        if version not in rtext:
            warnings.append(f"README.md does not mention version {version}")

    for w in warnings:
        print(f"WARN: {w}")
    for e in errors:
        print(f"ERROR: {e}", file=sys.stderr)

    if errors:
        return 1
    print(f"OK: {root} ({len(warnings)} warning(s))")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
