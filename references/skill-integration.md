# Companion Skill Integration

This Skill acts as the historical-domain orchestrator. Generic Obsidian/file-format execution should be delegated to specialized installed skills when they are available.

## Responsibility boundary

`tongjian-scholar` remains authoritative for:

- fact vs inference vs Sima Guang judgment vs modern mapping;
- actor / interest / coalition / institution analysis;
- canonical knowledge granularity;
- comparison dimensions;
- whether a relation or concept deserves persistence;
- merge decisions (`CREATE / UPDATE / LINK / PROMOTE / COMPARE / DEFER`).

Companion skills own execution details in their domain.

## Preferred routing for the user's current stack

| Skill | Use it for | Do not let it decide |
|---|---|---|
| `obsidian-cli` | search/read/write Vault, inspect existing files, locate MOCs/Canvas | historical interpretation or note granularity |
| `obsidian-markdown` | frontmatter, wikilinks, callouts, Obsidian Markdown syntax | whether a concept deserves a canonical node |
| `obsidian-bases` | `.base` views and syntax | which fields matter historically |
| `json-canvas` | `.canvas` syntax, node/edge editing, layout | historical relation semantics |
| `llm-wiki` | wiki-style organization, overlap detection, cross-link suggestions | upgrading an inference into fact |
| `knap` | template + JSON/CSV batch generation after schema is fixed | canonicalization or deciding what to create |
| `defuddle` | convert/clean a web page into Markdown for later analysis | source credibility or historical truth |

Other deep-reading, historian, research, brainstorming, or verification skills may be used when present, following the same boundary principle.

## Default multi-skill workflows

### A. Continue reading only

```text
tongjian-scholar
```

No Obsidian skill is needed unless the user asks to persist the result.

### B. Add one discussion to an existing Vault

```text
tongjian-scholar
  1. extract candidate nodes/relations
        ↓
obsidian-cli
  2. inventory existing notes/aliases/MOC/Canvas
        ↓
llm-wiki (optional)
  3. flag possible overlaps / near-duplicates
        ↓
tongjian-scholar
  4. resolve canonical identity + Merge Plan
        ↓
obsidian-markdown
  5. minimally update/create notes
        ↓
obsidian-bases (only if affected)
  6. refresh relevant structured view
        ↓
json-canvas (only if relationships changed)
  7. incrementally update map
        ↓
validation
```

### C. Import a historical web article

```text
defuddle
  1. clean article into Markdown
        ↓
tongjian-scholar
  2. separate claims / evidence / interpretation
        ↓
research/historian skill (optional)
  3. verify or compare sources
        ↓
Vault merge workflow
```

`defuddle` improves the input format; it does not establish source reliability.

### D. Batch import many structured items

Use `knap` only after:

1. canonical identities are resolved;
2. note type/schema is fixed;
3. a merge plan says which rows are actually `CREATE` or `UPDATE`.

Never point `knap` at raw extracted entities and let batch generation decide the knowledge architecture.

## Bases routing

This Skill decides desired fields and views. Use `obsidian-bases` for compatible `.base` syntax when available. Otherwise use the minimal fallback in `bases-spec.md` and the linked official syntax reference.

Read `bases-spec.md` for the semantic view requirements.

## Conflict rules

When two skills conflict:

1. obey system/developer/user instructions first;
2. for historical semantics, canonicalization, and merge action, prefer this Skill;
3. for Markdown/Canvas/Bases syntax, prefer the specialized format skill;
4. for Vault I/O mechanics, prefer `obsidian-cli`;
5. preserve user-authored content and existing layout over automatic reorganization.

## Avoid skill explosion

Do not call every available skill.

Examples:

- `defuddle` is irrelevant for a supplied book excerpt already in clean text;
- `knap` is unnecessary for three manual note updates;
- `json-canvas` is unnecessary if no important relation changed;
- `obsidian-bases` is unnecessary if the user only wants a narrative MOC;
- `llm-wiki` is unnecessary when canonical identity is obvious.

The goal is the smallest reliable composition.
