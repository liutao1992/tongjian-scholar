# Obsidian JSON Canvas Knowledge-Map Rules

Follow JSON Canvas 1.0 for `.canvas` files.

## 1. Top-level structure

```json
{
  "nodes": [],
  "edges": []
}
```

Supported node types:

- `text`
- `file`
- `link`
- `group`

Each node must have:

- `id`
- `type`
- integer `x`, `y`, `width`, `height`

Each edge must have:

- `id`
- `fromNode`
- `toNode`

Use `label` when the edge expresses a historical relationship.

## 2. Prefer file nodes for canonical knowledge

Use file nodes for reusable notes:

```json
{
  "id": "person-wu-qi",
  "type": "file",
  "file": "人物/吴起.md",
  "x": 0,
  "y": 0,
  "width": 300,
  "height": 220
}
```

Why: file nodes keep the Canvas connected to canonical notes and Obsidian backlinks.

Use text nodes for:

- a temporary research question;
- a compact conclusion;
- an unresolved hypothesis;
- a short causal-chain annotation.

Do not turn every text card into a permanent note.

## 3. Semantic edge vocabulary

Prefer concise relationship labels. Examples:

- `支持`
- `反对`
- `任命`
- `推动`
- `执行`
- `依赖`
- `损害利益`
- `受益于`
- `联合`
- `攻伐`
- `继承`
- `约束`
- `导致`
- `触发`
- `制度化为`
- `对比`
- `属于`
- `映射`

Example:

```json
{
  "id": "edge-chu-wuqi-support",
  "fromNode": "person-chu-dao-wang",
  "toNode": "person-wu-qi",
  "label": "支持"
}
```

Avoid vague labels such as `相关`, `有联系`, or unlabeled edges when the relation matters.

## 4. Visual organization

Recommended spatial layers for a thematic Canvas:

```text
人物 / 集团       事件 / 决策       制度 / 机制       比较 / 结论
    →                 →                 →                 →
```

Alternative for chronological maps:

```text
过去 ------------------------------------------------→ 未来
```

Use groups sparingly for meaningful clusters such as:

- `楚国改革环境`
- `秦国改革环境`
- `既得利益集团`
- `权力交接`

Do not use groups solely for decoration.

## 5. Incremental update policy

When editing an existing Canvas:

1. parse the current file first;
2. preserve all unknown fields/extensions;
3. index file nodes by their `file` path;
4. index nodes and edges by ID;
5. reuse an existing file node if its canonical note already appears;
6. preserve existing `id`, `x`, `y`, `width`, `height` unless the user requested re-layout;
7. add new nodes near the relevant cluster;
8. reuse an equivalent existing semantic edge instead of creating duplicates;
9. do not delete user text cards merely because they are not part of the generated schema;
10. change only the minimum region necessary.

### Duplicate definition

Treat two file nodes as duplicates when their normalized `file` paths point to the same note.

Treat two edges as duplicates when they share:

- the same `fromNode`;
- the same `toNode`;
- the same normalized `label`.

## 6. Stable IDs

Prefer deterministic, readable IDs for newly generated nodes when possible:

```text
person-wu-qi
event-wu-qi-reform
concept-succession-risk
comparison-wuqi-shangyang
```

If an existing Canvas already uses opaque/random IDs, preserve them. Do not rename existing IDs just for readability.

## 7. Relation direction

Use direction to encode meaning:

```text
[[楚悼王]] --支持--> [[吴起]]
[[吴起]] --推动--> [[吴起变法]]
[[吴起变法]] --损害利益--> [[楚国贵族]]
[[君主死亡]] --触发--> [[改革反扑]]
```

Do not reverse an edge simply to improve aesthetics.

## 8. Canvas granularity

Create multiple focused canvases instead of one giant graph when the map grows too dense.

Recommended examples:

```text
Maps/
├── 战国改革.canvas
├── 魏文侯用人.canvas
├── 三家分晋.canvas
└── 资治通鉴-总览.canvas
```

The top-level overview should link to thematic maps rather than duplicate every low-level node.

## 9. Validation checklist

Before finalizing:

- JSON parses.
- Node IDs are unique.
- Edge IDs are unique.
- Every edge endpoint exists.
- Every node has valid coordinates and positive dimensions.
- Type-specific required fields exist (`text`, `file`, `url`).
- Optional `color`, file `subpath`, group `backgroundStyle`, and edge labels/sides/ends have valid types and values.
- No duplicate canonical file nodes were accidentally created.
- Semantic edges use meaningful labels where appropriate.
- Existing positions/content are preserved during incremental update.

Run this Skill's validator using the absolute path to `scripts/validate_canvas.py` beneath the directory containing `SKILL.md`. It checks JSON Canvas 1.0 structure plus this Skill's duplicate-file and duplicate-semantic-edge policy; inspect the rendered map separately for layout and historical meaning.
