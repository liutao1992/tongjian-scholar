---
name: tongjian-scholar
description: Deep-read and analyze 《资治通鉴》 through actors, interests, decisions, causal mechanisms, institutions, Sima Guang's editorial viewpoint, and cross-case comparison; then turn the result into maintainable Obsidian notes, MOCs, and JSON Canvas knowledge maps. Use for reading, discussing, comparing, reviewing, or building an Obsidian knowledge system around 《资治通鉴》 or similar Chinese historical works when the same method is requested.
metadata:
  version: "1.3.1"
  language: "zh-CN"
---

# 《资治通鉴》深度阅读与 Obsidian 知识地图

## Use When

Use this skill when the user wants to:

- explain or continue reading a passage from 《资治通鉴》;
- analyze a person, event, reform, succession, war, alliance, or political decision;
- ask “why did this happen?” or “why did Sima Guang write it this way?”;
- compare historical cases such as 吴起 vs 商鞅;
- extract reusable political/institutional mechanisms from historical cases;
- turn a discussion into Obsidian notes, MOCs, Bases-ready properties, or `.canvas` knowledge maps;
- apply the same reading method to 《史记》《战国策》《汉书》《三国志》《明史》 etc. when explicitly requested.

## Don't Use When

Do not invoke the full workflow for:

- a simple date/name lookup that needs no analysis;
- unrelated general questions;
- other historical works unless the user asks for this style of analysis or the task clearly matches it.

## Core Model

Organize knowledge into four layers:

1. **事实层** — what happened, who acted, and under what conditions.
2. **机制层** — how interests, resources, institutions, alliances, information, and power produced outcomes.
3. **思想层** — what Sima Guang explicitly judged or may have been trying to show through selection and arrangement.
4. **迁移层** — what can be compared with other cases or modern theory, and where the analogy stops.

Always distinguish:

- **史实** — directly supported by reliable historical material;
- **司马光明确判断** — explicit comment or clear textual judgment;
- **合理推断** — analysis inferred from incentives, constraints, and sequence;
- **现代映射** — modern concepts used only to aid understanding.

Never present the last two as certain historical fact.

## Workflow

Choose only the steps needed for the user's question. Do not mechanically print every section.

### 1. Locate the task

Classify internally as one or more of:

`text` / `event` / `person` / `decision` / `institution` / `comparison` / `sima-guang` / `review` / `obsidian` / `knowledge-map`.

### 2. Restore the minimum historical context

Confirm only what is necessary:

- time and political stage;
- states/organizations involved;
- actors and formal roles;
- power structure before the event;
- relevant preceding conflict.

Do not turn the answer into a dynasty encyclopedia.

### 3. Analyze actors before judging outcomes

For each important actor/group, inspect:

- goal;
- resources;
- incentives;
- constraints;
- risks;
- likely alternatives given the information available at the time.

### 4. Reconstruct interests and alliances

Ask:

- who benefits and who pays the cost;
- who can block the policy;
- who is neutral but may swing;
- what creates common interests among opponents;
- whether the reform creates durable new beneficiaries;
- whether an alliance is maintained by shared interest, coercion, reputation, or one ruler's personal support.

### 5. Reconstruct the decision

Use:

```text
目标
↓
当时可见的信息
↓
现实可选项
↓
收益 / 成本 / 风险
↓
实际选择
↓
短期结果
↓
长期副作用
```

Avoid hindsight. Counterfactuals must be feasible under contemporary institutions and resources.

### 6. Build a causal mechanism

Separate:

- long-term structural conditions;
- direct causes;
- triggers;
- accelerators;
- feedback loops;
- final outcome.

Prefer multi-causal explanations when appropriate.

### 7. Test personal power vs institutional power

For reforms and organizational success, inspect whether results depend on:

- one ruler's support;
- one executor's ability or prestige;
- formal rules;
- bureaucratic execution;
- fiscal/military self-maintenance;
- durable beneficiary groups;
- succession after the key sponsor dies or loses power.

The central question is:

> Did personal authorization merely start the change, or was the change converted into a self-sustaining institution?

### 8. Analyze Sima Guang's editorial viewpoint when relevant

Distinguish:

- explicit comments such as `臣光曰`;
- textual emphasis and sequencing;
- comparisons with nearby cases;
- inferred editorial intent.

Common themes include 名分、礼制、用人、君臣关系、权力约束、继承秩序、制度稳定、纳谏、战争决策.

### 9. Compare cases by variables, not adjectives

When comparing two cases, prefer dimensions such as:

- initial political environment;
- ruler support;
- harmed interests;
- opposition organization;
- execution system;
- new beneficiary groups;
- institutionalization;
- succession risk;
- outcome.

End with the variable(s) that best explain why results diverged.

### 10. Abstract a mechanism only after the case is understood

Use:

```text
历史事实
↓
重复关系
↓
机制
↓
适用条件
↓
失效条件
```

Avoid moral slogans such as “做人不要骄傲” when a more precise mechanism exists.

### 11. Add modern mappings only when useful

Possible lenses:

- organizational behavior;
- stakeholder management;
- institutional economics;
- principal-agent problems;
- game theory and coalition theory;
- path dependence;
- organizational capability;
- incentive design;
- succession and governance.

Always state the historical/modern difference.

For the expanded reasoning framework, read `references/historical-analysis.md` when the question is complex or comparative.

## Companion Skill Orchestration

This skill owns the **historical reasoning and knowledge-model decisions**. Reuse other installed skills for generic capabilities rather than duplicating them.

When the runtime exposes relevant installed skills, select them by their `name` + `description`. Do not assume a companion is installed, and do not fail if it is absent.

Preferred delegation:

- **Obsidian Markdown / wikilinks / properties** → an installed Obsidian Markdown skill if available.
- **JSON Canvas generation/editing** → an installed JSON Canvas/Canvas skill if available.
- **Obsidian Bases/database views** → an installed Bases skill if available.
- **Vault search/read/write/CLI operations** → an installed Obsidian CLI/Vault skill if available.
- **deep reading / source-oriented historical research** → a deep-reading or historian skill if available; this skill still controls the final analytical structure.
- **brainstorming/planning skills** → use only to explore hypotheses, note architecture, or research questions; never let brainstorming upgrade a hypothesis into historical fact.
- **verification skills** → use before finalizing generated files or knowledge-map changes when available.
- **skill-authoring skills** → use only when modifying this Skill itself, not during normal historical reading.

Do not involve unrelated coding, Git, code-review, or development workflow skills in ordinary history-reading tasks.

For detailed routing and conflict rules, read `references/skill-integration.md`.

## Obsidian Output

When the user asks to save, organize, map, or export knowledge:

1. inspect existing notes/nodes first if the vault is accessible;
2. update canonical nodes instead of creating synonyms;
3. keep note types limited and meaningful;
4. use links that express real knowledge relationships;
5. maintain MOCs incrementally;
6. generate Canvas only when spatial relationships add value;
7. use an explicit merge plan before writing multiple files.

Read `references/obsidian-schema.md` for note types, properties, and templates.
Read `references/vault-merge.md` before merging a new reading/discussion into an existing Vault.

### Canonical note types

- `person`
- `event`
- `state`
- `concept`
- `comparison`
- `moc`

Do not create a separate note for every sentence or minor conclusion.

### Relationship-first linking

Prefer links with an interpretable relation:

```text
[[楚悼王]] --支持--> [[吴起]]
[[吴起]] --推动--> [[吴起变法]]
[[吴起变法]] --损害利益--> [[楚国贵族]]
[[吴起变法]] --对比--> [[商鞅变法]]
```

A node should exist because it will be reused, compared, or connected — not merely to make the graph denser.

## Incremental Vault Merge

When the user asks to add new learning into an existing Vault, do not treat the task as fresh note generation. Use this order:

```text
inventory existing canonical notes
        ↓
extract candidate knowledge units
        ↓
resolve canonical identity / aliases
        ↓
classify minimal action
CREATE / UPDATE / LINK / PROMOTE / COMPARE / DEFER
        ↓
apply smallest safe edits
        ↓
update MOC / Bases / Canvas only if structurally useful
        ↓
validate
```

Important rules:

- prefer `UPDATE` over `CREATE`;
- prefer `LINK` over a new note when no reusable concept is needed;
- promote a mechanism to a `concept` only after it recurs across cases or the user explicitly wants it as a framework;
- keep process notes/read-along discussion separate from canonical knowledge;
- preserve conflicting earlier interpretations as judgment evolution instead of silently overwriting them;
- Canvas is downstream of canonical notes, not the source of truth.

Read `references/vault-merge.md` for the complete merge policy.

## Installed Obsidian Skill Stack

If these companion skills are available, prefer the following division of labor:

- `obsidian-cli` — inventory/search/read/write Vault content;
- `llm-wiki` — assist canonicalization, wiki-style linking, and detecting overlapping nodes;
- `obsidian-markdown` — produce/update Obsidian-flavored Markdown, properties, callouts, and wikilinks;
- `knap` — batch-generate notes only after the merge plan and schema are fixed;
- `obsidian-bases` — build structured views from fields selected by this Skill;
- `json-canvas` — create/edit Canvas after canonical notes/relations are decided;
- `defuddle` — clean web pages into Markdown before historical analysis; never treat cleanup as source validation.

Do not invoke all seven by default. Use only the smallest set required for the current task.

## Canvas Rules

When creating or updating `.canvas`:

- follow JSON Canvas 1.0 structure;
- prefer file nodes for canonical notes so backlinks remain useful;
- use text nodes mainly for short questions, hypotheses, or summaries;
- use edge `label` for semantic relationships;
- preserve existing node IDs and positions during incremental updates whenever possible;
- never create two file nodes for the same canonical note in the same Canvas;
- add new nodes near their semantic cluster instead of re-laying out the whole map;
- preserve user-created content and unknown extensions unless there is a clear reason to change them.

Read `references/canvas-spec.md` before generating or editing Canvas files.

If this package's validator is available, run:

```bash
python scripts/validate_canvas.py path/to/map.canvas
```

before claiming the Canvas is valid.

## Output Strategy

Adapt depth to the question:

- **原文/句子** → meaning + minimal context;
- **为什么** → causes + interests + constraints;
- **人物** → goal + resources + capabilities + limits + decisions;
- **改革** → redistribution + coalition + execution + institutionalization + succession;
- **司马光** → text placement + explicit comments + inferred political proposition;
- **复盘** → event line + person line + theme line + mechanism line;
- **Obsidian** → canonical nodes + links + properties + MOC/Canvas changes.

## Rules

- Do not fabricate classical Chinese quotations.
- Do not use labels such as “昏君/奸臣/英雄/愚蠢” as substitutes for mechanism analysis.
- Do not confuse short-term success with durable institutionalization.
- Do not claim a modern management concept is what an ancient actor “actually thought”.
- Do not use one historical case as a universal law without boundary conditions.
- If a source is uncertain, say so and separate uncertainty from analysis.
- When existing Obsidian nodes are available, prefer merge/update over duplication.

## Quality Check

Before finalizing, check:

- [ ] Fact vs inference vs modern mapping is clear.
- [ ] Contemporary information constraints are respected.
- [ ] Interests and institutions were considered, not only personality.
- [ ] Multi-causal outcomes were not flattened into one cause.
- [ ] Personal power vs institutional power was tested where relevant.
- [ ] Sima Guang's explicit view is separated from inferred editorial intent.
- [ ] Counterfactuals are feasible for the period.
- [ ] Obsidian nodes are canonical and reusable.
- [ ] Canvas edges have meaningful labels where semantics matter.
- [ ] Existing user structure is preserved during incremental updates.

## Examples

Typical triggers:

- “继续讲《资治通鉴》这段。”
- “为什么田文比吴起更适合做国相？”
- “吴起有没有意识到自己的改革环境不好？”
- “为什么吴起死后改革失败，商鞅死后秦法还在？”
- “司马光为什么在这里讲魏文侯？”
- “智伯到底败在哪里？”
- “从制度角度分析这件事。”
- “把刚才关于吴起和商鞅的讨论整理进 Obsidian。”
- “更新战国改革 Canvas，不要打乱已有布局。”
- “总结这一章并更新 MOC。”

For worked examples, read `references/examples.md`.

## References

- `references/historical-analysis.md` — expanded historical reasoning framework.
- `references/obsidian-schema.md` — note schema and templates.
- `references/canvas-spec.md` — Canvas model, layout, incremental-update rules.
- `references/skill-integration.md` — companion-skill routing and conflict handling.
- `references/vault-merge.md` — incremental canonicalization and merge policy.
- `references/bases-spec.md` — semantic requirements for Bases views.
- `references/examples.md` — worked usage examples.
