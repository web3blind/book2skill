# Output Templates

## Analysis report

```md
## Book2Skill Analysis — <source>

### Practical potential
- Best skill shape: <editor/advisor/coach/decision guide/etc.>
- Main jobs this skill can do:
  - <job 1>
  - <job 2>
  - <job 3>

### Extracted frameworks
- **<name>**: <what it does>
  - Use when: <situation>
  - Procedure: <short steps>

### Principles and rules
- <rule>: <when/how to apply>

### Techniques
- <technique>: <repeatable action>

### Anti-patterns
- <trap>: <why it fails and how to avoid>

### Recommended skill direction
<short recommendation>

### Open questions
- <question if needed>
```

## Practical Skill Spec

```md
# Practical Skill Spec: <skill-name>

## Source
- <title/source, author, format, extraction limits>

## Purpose
<one paragraph: what job the skill performs>

## Proposed frontmatter
- name: `<skill-name>`
- description: <trigger-specific description>

## Modes
### 1. <mode name>
- Use when: <situation>
- Input: <needed input>
- Workflow:
  1. <step>
  2. <step>
  3. <step>
- Output: <format>
- Self-check: <criteria>

## Core frameworks to include in SKILL.md
- **<framework>**: <actionable formulation>

## Reference files
- `references/<file>.md`: <purpose>

## Guardrails
- <limit>

## Validation prompts
- "<test request 1>"
- "<test request 2>"
- "<test request 3>"
```

## Skill creator handoff

```md
Use create-skills to implement this reviewed Practical Skill Spec as an OpenClaw skill.

Target path:
`~/.openclaw/workspace/skills/<skill-name>/`

Requirements:
- concise `SKILL.md` with accurate trigger frontmatter
- long frameworks/checklists/examples in `references/`
- no copyrighted long excerpts
- no external dependency installation unless explicitly approved
- validate file paths and provide 2–3 trigger test prompts

Spec:
<paste reviewed spec here>
```
