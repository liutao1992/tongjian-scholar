# tongjian-scholar

面向《资治通鉴》深度阅读、历史机制分析与 Obsidian 知识地图构建的 Agent Skill。

当前版本：`1.3.2`

## 核心能力

- 原文与最小历史背景理解
- 人物、资源、利益、联盟与约束分析
- 决策重建与因果机制分析
- 个人能力 vs 制度能力
- 改革、既得利益与权力交接
- 司马光叙事/政治思想分析
- 跨案例控制变量比较
- Obsidian canonical notes + MOC
- JSON Canvas 知识地图及增量更新
- Vault 增量知识合并（CREATE / UPDATE / LINK / PROMOTE / COMPARE / DEFER）
- 冲突观点保留与判断演化
- 关键史实和争议判断的来源定位
- 复用本地已安装的 Obsidian / Canvas / wiki / batch-generation 类 Skills

## 目录

```text
tongjian-scholar/
├── SKILL.md
├── README.md
├── CHANGELOG.md
├── references/
│   ├── historical-analysis.md
│   ├── obsidian-schema.md
│   ├── canvas-spec.md
│   ├── skill-integration.md
│   ├── vault-merge.md
│   ├── bases-spec.md
│   └── examples.md
└── scripts/
    ├── validate_canvas.py
    ├── validate_vault.py
    └── validate_skill.py
```

## Skill 组合思路

本 Skill 负责历史领域逻辑，不重复实现所有通用能力。

如果运行环境存在相应 companion skill，可按需组合：

```text
tongjian-scholar
        ↓ 历史节点与关系
obsidian-cli
        ↓ 盘点现有节点 / canonical resolution
llm-wiki
        ↓ 辅助识别近义/重叠节点
obsidian-markdown
        ↓ 最小化更新 canonical notes
knap（仅批量场景）
        ↓ 按已确认 Schema 批量生成
obsidian-bases
        ↓ 更新结构化视图
json-canvas
        ↓ 知识地图增量更新
validate_vault / validate_canvas
        ↓ 最终检查
```

没有 companion skill 时，本 Skill 仍可独立工作。
若需要直接生成 `.base`，可使用 `references/bases-spec.md` 中的最小模板。

## 增量合并

新讨论进入已有 Vault 时，先生成 Merge Plan：

```text
CREATE / UPDATE / LINK / PROMOTE / COMPARE / DEFER
```

默认优先 UPDATE，而不是重复创建文件。过程性讨论进入 `阅读记录/`，稳定知识进入 canonical notes。

## 校验

```bash
python scripts/validate_skill.py
python scripts/validate_vault.py /path/to/vault
python scripts/validate_canvas.py "Maps/战国改革.canvas"
```

`validate_skill.py` 检查 Skill 包结构和内部引用；`validate_vault.py` 会做轻量级重复 UID、同名笔记、alias 冲突和 wikilink 完整性检查；`validate_canvas.py` 检查 Canvas JSON、节点/边引用与重复关系。

上述命令从仓库根目录执行。安装到其他位置后，从任意工作目录调用时，应使用 Skill 目录下脚本的绝对路径。Canvas 校验覆盖 JSON Canvas 1.0 的结构字段与本 Skill 的去重规则，不校验历史解释或视觉布局。

## 安装

把整个 `tongjian-scholar` 目录放入运行环境可发现的 Skills 目录，并确保 `SKILL.md` 可被 Agent 发现。
