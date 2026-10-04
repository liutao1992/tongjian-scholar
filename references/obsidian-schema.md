# Obsidian 知识库结构

本文件定义《资治通鉴》知识库的推荐 Schema。

## 1. 笔记类型

推荐控制在以下六类：

- `person`：人物
- `event`：事件
- `state`：国家/政权
- `concept`：制度、机制、政治概念
- `comparison`：跨案例比较
- `moc`：主题地图 / Map of Content

不要为每一个小结论建立独立文件。

## 1.1 Canonical identity properties

Canonical notes should prefer stable metadata:

```yaml
---
type: person
uid: person:战国:吴起
name: 吴起
aliases:
  - 吴子
status: canonical
---
```

Rules:

- `uid` is optional for old notes but recommended for new canonical notes; once assigned, preserve it.
- `uid` should be human-readable and unique inside the Vault; do not rename it merely for style.
- `aliases` absorbs alternate names and spelling variants instead of creating duplicate files.
- `status` may use values such as `canonical`, `draft`, `contested`, or `open-question` when useful.
- reading logs/process notes do not need canonical `uid`.
- `source` identifies a work, while `source_refs` records verifiable locations for consequential claims; neither a work title nor an empty locator proves a claim.
- Each `source_refs` entry should contain the known parts of `作品｜卷/篇｜纪年/段落｜版本或 URL`. Do not save placeholders as if they were checked references.
- Put the locator next to the claim in `史料与出处` when several claims use different passages. Include work, volume/chapter, year or passage, and edition/URL when available. Mark any unresolved locator as unverified instead of guessing.

Before creating a new note, search title, aliases, and (when present) `uid`.

---

## 2. 推荐目录

```text
资治通鉴/
├── 00-MOC/
├── 人物/
├── 事件/
├── 国家/
├── 概念/
├── 比较/
└── 阅读记录/
```

目录只负责粗分类，真正的组织方式依赖 `[[双链]]`。

---

## 3. Person 模板

```markdown
---
type: person
uid: person:战国:吴起
name: 吴起
aliases: []
status: canonical
era: 战国
states:
  - "[[魏国]]"
  - "[[楚国]]"
themes:
  - "[[改革]]"
  - "[[用人]]"
  - "[[政治联盟]]"
source:
  - 资治通鉴
source_refs: []
---

# 吴起

## 一句话定位

## 身份与经历

## 目标

## 核心能力

## 掌握资源

## 主要约束

## 关键决策

## 利益关系

## 成功之处

## 失败机制

## 史料与出处

## 相关事件

- [[吴起变法]]

## 对比人物

- [[商鞅]]

## 我的判断

## 待继续追问
```

---

## 4. Event 模板

```markdown
---
type: event
uid: event:战国:吴起变法
status: canonical
era: 战国
states:
  - "[[楚国]]"
people:
  - "[[吴起]]"
themes:
  - "[[改革]]"
  - "[[权力交接]]"
source:
  - 资治通鉴
source_refs: []
---

# 吴起变法

## 事件概述

## 前置条件

## 行动者

| 行动者 | 目标 | 获益/受损 | 资源 | 态度 |
|---|---|---|---|---|

## 决策过程

## 利益重分配

## 因果链

## 短期效果

## 长期结果

## 制度化程度

## 关键脆弱点

## 司马光视角

## 对比案例

- [[商鞅变法]]

## 可抽象机制

## 史料与出处

## 待继续追问
```

---

## 5. Concept 模板

```markdown
---
type: concept
uid: concept:权力交接风险
status: canonical
category: historical-mechanism
source_refs: []
---

# 权力交接风险

## 定义

## 机制

## 典型因果链

## 适用条件

## 失效条件

## 《资治通鉴》案例

- [[吴起变法]]

## 史料与出处

## 对比案例

## 现代映射

## 注意事项
```

---

## 6. Comparison 模板

```markdown
---
type: comparison
uid: comparison:吴起变法-vs-商鞅变法
status: canonical
source_refs: []
cases:
  - "[[吴起变法]]"
  - "[[商鞅变法]]"
themes:
  - "[[改革]]"
  - "[[制度化]]"
---

# 吴起变法 vs 商鞅变法

## 比较问题

为什么两次强力改革都遭到既得利益集团反对，但改革者死后的制度命运不同？

## 控制变量比较

| 维度 | 吴起变法 | 商鞅变法 |
|---|---|---|
| 政治环境 | | |
| 君主支持 | | |
| 受损集团 | | |
| 新受益集团 | | |
| 执行体系 | | |
| 制度化 | | |
| 权力交接 | | |
| 最终结果 | | |

## 决定性差异

## 共同机制

## 我的结论

## 仍不确定的问题

## 史料与出处
```

---

## 7. MOC 模板

```markdown
---
type: moc
uid: moc:战国改革
status: canonical
---

# 战国改革 MOC

## 核心案例

- [[吴起变法]]
- [[商鞅变法]]

## 核心人物

- [[吴起]]
- [[楚悼王]]
- [[商鞅]]
- [[秦孝公]]

## 核心机制

- [[改革与既得利益]]
- [[政治联盟]]
- [[制度化]]
- [[权力交接风险]]
- [[新受益集团]]

## 关键比较

- [[吴起变法 vs 商鞅变法]]

## 当前判断

## 尚未解决的问题
```

---

## 8. 关系表达

Obsidian 原生 Graph 不显示边标签，因此在正文中用关系句保留语义：

```markdown
## 关系

- [[楚悼王]] **支持** [[吴起]]
- [[吴起]] **推动** [[吴起变法]]
- [[楚国贵族]] **受损于** [[吴起变法]]
- [[吴起变法]] **依赖** [[楚悼王]] 的政治保护
- [[吴起变法]] **对比** [[商鞅变法]]
```

如果之后生成 Canvas，可以把粗体动词作为边标签。

---

## 9. 节点创建原则

创建新节点前问：

1. 以后会不会再次链接到它？
2. 它是否有独立解释价值？
3. 它是否能连接两个以上案例？

三个问题几乎都是否时，不要单独建节点。

---

## 8. Canonical note 与阅读记录边界

`阅读记录/` 保存过程：完整问题、临时假设、聊天思路、尚未验证的判断。

其他 canonical 目录只保存沉淀后的知识。

推荐流程：

```text
阅读记录
   ↓ 反复出现 / 已验证 / 可复用
canonical note
   ↓
MOC / Bases / Canvas
```

不要把每次对话直接复制成一个新的概念或人物节点。具体合并规则见 `vault-merge.md`。
