# Obsidian Bases 视图设计

优先使用已安装的 `obsidian-bases` 处理格式细节。没有该 Skill 时，可按下方最小模板直接创建 `.base` 文件，并参考 [Obsidian 官方 Bases 语法](https://obsidian.md/help/bases/syntax)核对当前版本。已有 Base 应先读取再局部修改，保留其他视图与自定义字段。

## 无 companion Skill 时的最小模板

以下内容保存为 `.base` 文件；`type`、`era` 等字段来自本 Skill 的笔记 frontmatter。按 Vault 实际字段与目标笔记类型调整过滤条件和列。需要使用 Obsidian 的 Bases 核心插件查看结果。

```yaml
filters:
  and:
    - 'file.ext == "md"'
    - 'note.type == "person"'
views:
  - type: table
    name: 人物
    order:
      - file.name
      - note.era
      - note.states
      - note.status
```

创建后在 Obsidian 中打开，确认筛选结果和列名；若目标版本语法有变化，按官方语法调整。不要为生成视图而改写用户原有笔记字段。

## 1. 人物视图

字段建议：

- `name`
- `era`
- `states`
- `themes`
- `status`
- `aliases`

用途：快速查看某一时期/国家/主题下的人物。

## 2. 事件视图

字段建议：

- `era`
- `states`
- `people`
- `themes`
- `status`

推荐过滤：

- 战国改革；
- 权力交接；
- 用人；
- 战争决策。

## 3. 概念/机制视图

字段建议：

- `category`
- `themes`
- `status`
- `case_count`（若运行环境能计算）

重点发现：

- 只有 1 个案例支撑的概念；
- 已有多个案例、值得提升优先级的机制；
- 尚未验证的理论节点。

## 4. Comparison 视图

字段建议：

- `cases`
- `themes`
- `status`

用于查看跨案例比较，不把 comparison 混入人物/事件列表。

## 5. 待继续追问视图

如果 Vault 约定了 `status: open-question` 或类似字段，可建立专门视图展示：

- 未解决史实问题；
- 需要查证的来源冲突；
- 需要更多案例验证的机制；
- 尚未完成的 comparison。

## 6. Bases 与 MOC 的边界

- **MOC**：解释性导航，强调“为什么这些节点属于一个主题”。
- **Bases**：结构化浏览、筛选、排序。

不要用 Bases 取代 MOC，也不要把 MOC 做成字段表格的复制品。
