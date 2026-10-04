# Changelog

## 1.3.2

- 为关键历史判断增加可核查的来源位置，并收紧司马光明确判断的定义。
- 增强 Canvas 校验器对畸形输入与可选字段的检查。
- 明确跨目录调用校验脚本的方法，并提供不依赖 companion Skill 的 Bases 最小模板。

## 1.3.1

- Rename the Skill to `tongjian-scholar`.
- Align README, SKILL metadata, examples, and companion-skill routing with the new name.

## 1.3.0

- 新增 Vault 增量知识合并策略。
- 新增 `CREATE / UPDATE / LINK / PROMOTE / COMPARE / DEFER` 六类 merge action。
- 新增 canonical resolution、alias/近义节点去重与冲突观点保留规则。
- 明确阅读记录层与 canonical knowledge 层分离。
- 针对现有 `obsidian-cli / obsidian-markdown / obsidian-bases / json-canvas / defuddle / knap / llm-wiki` 增加专用路由规则。
- 新增 `bases-spec.md`，定义人物、事件、概念、比较、待追问等视图语义。
- 新增 `validate_vault.py`，轻量检查 duplicate uid、同名笔记、alias 冲突与悬空 wikilink。
- 保持 Canvas 增量更新、已有节点位置与用户内容保护策略。

## 1.2.0

- 增加 companion-skill orchestration。
- 增加 JSON Canvas 增量更新规则和校验脚本。
