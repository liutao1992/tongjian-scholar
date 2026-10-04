#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ALLOWED_TYPES = {"text", "file", "link", "group"}
SIDES = {"top", "right", "bottom", "left"}
ENDS = {"none", "arrow"}


def fail(errors, message):
    errors.append(message)


def validate(path: Path) -> list[str]:
    errors = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"Invalid JSON: {exc}"]

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
        if not isinstance(nid, str) or not nid:
            fail(errors, f"{p}.id must be a non-empty string")
        elif nid in node_ids:
            fail(errors, f"Duplicate node id: {nid}")
        else:
            node_ids.add(nid)

        ntype = node.get("type")
        if ntype not in ALLOWED_TYPES:
            fail(errors, f"{p}.type must be one of {sorted(ALLOWED_TYPES)}")

        for key in ("x", "y", "width", "height"):
            value = node.get(key)
            if not isinstance(value, int) or isinstance(value, bool):
                fail(errors, f"{p}.{key} must be an integer")
        for key in ("width", "height"):
            value = node.get(key)
            if isinstance(value, int) and value <= 0:
                fail(errors, f"{p}.{key} must be > 0")

        required = {"text": "text", "file": "file", "link": "url"}.get(ntype)
        if required and (not isinstance(node.get(required), str) or not node.get(required)):
            fail(errors, f"{p}.{required} must be a non-empty string for type '{ntype}'")

        if ntype == "file" and isinstance(node.get("file"), str):
            norm = node["file"].replace("\\", "/").strip().lower()
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
        if not isinstance(eid, str) or not eid:
            fail(errors, f"{p}.id must be a non-empty string")
        elif eid in edge_ids:
            fail(errors, f"Duplicate edge id: {eid}")
        else:
            edge_ids.add(eid)

        frm, to = edge.get("fromNode"), edge.get("toNode")
        if frm not in node_ids:
            fail(errors, f"{p}.fromNode references missing node: {frm}")
        if to not in node_ids:
            fail(errors, f"{p}.toNode references missing node: {to}")

        for key in ("fromSide", "toSide"):
            if key in edge and edge[key] not in SIDES:
                fail(errors, f"{p}.{key} must be one of {sorted(SIDES)}")
        for key in ("fromEnd", "toEnd"):
            if key in edge and edge[key] not in ENDS:
                fail(errors, f"{p}.{key} must be one of {sorted(ENDS)}")

        label = edge.get("label", "")
        signature = (frm, to, label.strip() if isinstance(label, str) else label)
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
