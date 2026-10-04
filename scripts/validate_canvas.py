#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path

ALLOWED_TYPES = {"text", "file", "link", "group"}
SIDES = {"top", "right", "bottom", "left"}
ENDS = {"none", "arrow"}
BACKGROUND_STYLES = {"cover", "ratio", "repeat"}
COLOR_RE = re.compile(
    r"^(?:[1-6]|#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8}))$"
)


def fail(errors, message):
    errors.append(message)


def nonempty_string(value):
    return isinstance(value, str) and bool(value.strip())


def check_color(errors, item, path):
    if "color" in item and (
        not isinstance(item["color"], str) or not COLOR_RE.fullmatch(item["color"])
    ):
        fail(errors, f"{path}.color must be a preset '1'–'6' or a hex color string")


def reject_non_json_constant(value):
    raise ValueError(f"non-JSON numeric literal: {value}")


def validate(path: Path) -> list[str]:
    errors = []
    try:
        data = json.loads(
            path.read_text(encoding="utf-8"), parse_constant=reject_non_json_constant
        )
    except (OSError, UnicodeError, ValueError) as exc:
        return [f"Cannot read valid JSON: {exc}"]

    if not isinstance(data, dict):
        return ["Top-level value must be an object"]

    nodes = data.get("nodes", [])
    edges = data.get("edges", [])
    if not isinstance(nodes, list):
        fail(errors, "'nodes' must be an array")
        nodes = []
    if not isinstance(edges, list):
        fail(errors, "'edges' must be an array")
        edges = []

    node_ids = set()
    files = {}
    for i, node in enumerate(nodes):
        p = f"nodes[{i}]"
        if not isinstance(node, dict):
            fail(errors, f"{p} must be an object")
            continue
        nid = node.get("id")
        if not nonempty_string(nid):
            fail(errors, f"{p}.id must be a non-empty string")
        elif nid in node_ids:
            fail(errors, f"Duplicate node id: {nid}")
        else:
            node_ids.add(nid)

        ntype = node.get("type")
        if not isinstance(ntype, str) or ntype not in ALLOWED_TYPES:
            fail(errors, f"{p}.type must be one of {sorted(ALLOWED_TYPES)}")

        for key in ("x", "y", "width", "height"):
            value = node.get(key)
            if type(value) is not int:
                fail(errors, f"{p}.{key} must be an integer")
            elif key in ("width", "height") and value <= 0:
                fail(errors, f"{p}.{key} must be > 0")

        check_color(errors, node, p)

        required = (
            {"text": "text", "file": "file", "link": "url"}.get(ntype)
            if isinstance(ntype, str)
            else None
        )
        if required and not nonempty_string(node.get(required)):
            fail(errors, f"{p}.{required} must be a non-empty string for type '{ntype}'")

        if ntype == "file" and "subpath" in node and (
            not isinstance(node["subpath"], str) or not node["subpath"].startswith("#")
        ):
            fail(errors, f"{p}.subpath must be a string starting with '#'")

        if ntype == "group":
            for key in ("label", "background"):
                if key in node and not isinstance(node[key], str):
                    fail(errors, f"{p}.{key} must be a string")
            if "backgroundStyle" in node and (
                not isinstance(node["backgroundStyle"], str)
                or node["backgroundStyle"] not in BACKGROUND_STYLES
            ):
                fail(
                    errors,
                    f"{p}.backgroundStyle must be one of {sorted(BACKGROUND_STYLES)}",
                )

        if ntype == "file" and nonempty_string(node.get("file")):
            norm = node["file"].replace("\\", "/").strip().casefold()
            if norm in files:
                fail(errors, f"Duplicate file node for '{node['file']}' ({files[norm]} and {nid})")
            else:
                files[norm] = nid

    edge_ids = set()
    seen_edges = set()
    for i, edge in enumerate(edges):
        p = f"edges[{i}]"
        if not isinstance(edge, dict):
            fail(errors, f"{p} must be an object")
            continue
        eid = edge.get("id")
        if not nonempty_string(eid):
            fail(errors, f"{p}.id must be a non-empty string")
        elif eid in edge_ids:
            fail(errors, f"Duplicate edge id: {eid}")
        else:
            edge_ids.add(eid)

        frm, to = edge.get("fromNode"), edge.get("toNode")
        if not nonempty_string(frm):
            fail(errors, f"{p}.fromNode must be a non-empty string")
        elif frm not in node_ids:
            fail(errors, f"{p}.fromNode references missing node: {frm}")
        if not nonempty_string(to):
            fail(errors, f"{p}.toNode must be a non-empty string")
        elif to not in node_ids:
            fail(errors, f"{p}.toNode references missing node: {to}")

        for key in ("fromSide", "toSide"):
            if key in edge and (not isinstance(edge[key], str) or edge[key] not in SIDES):
                fail(errors, f"{p}.{key} must be one of {sorted(SIDES)}")
        for key in ("fromEnd", "toEnd"):
            if key in edge and (not isinstance(edge[key], str) or edge[key] not in ENDS):
                fail(errors, f"{p}.{key} must be one of {sorted(ENDS)}")
        check_color(errors, edge, p)

        label = edge.get("label", "")
        if not isinstance(label, str):
            fail(errors, f"{p}.label must be a string")
        if nonempty_string(frm) and nonempty_string(to) and isinstance(label, str):
            signature = (frm, to, label.strip())
            if signature in seen_edges:
                fail(errors, f"Duplicate semantic edge: {signature}")
            else:
                seen_edges.add(signature)

    return errors


def main():
    if len(sys.argv) != 2:
        print("Usage: validate_canvas.py <file.canvas>", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    errors = validate(path)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"OK: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
