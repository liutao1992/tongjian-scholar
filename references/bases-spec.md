# Obsidian Bases 视图设计

本 Skill 不直接规定 `.base` 的具体语法；如果安装了 `obsidian-bases`，由它负责生成当前版本兼容的文件。本文件只定义需要表达的知识视图。

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
