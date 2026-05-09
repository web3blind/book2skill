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

## Staff+ Skill Delivery Plan

Use this when the user asks for a production-grade plan, GitHub/private repo plan, author-approved methodology skill, skill-creation/development handoff, release/eval plan, or a plan another agent should be able to implement.

````md
# Staff+ Plan: <skill-name>

## Executive summary
- Source: <title, author/origin, format>
- Permission context: <author-approved/private/internal/open/conservative>
- Target skill: `<skill-name>`
- Target repo/path: <repo/path if known>
- Runtime target: <agent/runtime if known>
- Goal: <what repeated job this skill performs>
- Non-goals: <what it must not become>

## Product thesis
<Define the skill as an operational methodology assistant, not a summary.>

## Success definition
- Product success:
- Technical success:
- Source fidelity success:
- Runtime usability success:

## Architecture
```text
source layer      -> raw/extracted source, metadata, section index, quote bank
knowledge layer   -> frameworks, diagnostics, checklists, playbooks, anti-patterns
runtime layer     -> SKILL.md router, modes, output contracts
evaluation layer  -> smoke tests, regression prompts, golden outputs, quality rubric
```

## Repository structure
<tree with SKILL.md, README.md, source/provenance files, references, evals, feedback, tests>

## Source and permission policy
<What can be stored, quoted, transformed, or must remain local. Include manifest/private notice requirements.>

## SKILL.md contract
<Frontmatter, when to use, when not to use, context questions, mode router, reference map, source lookup policy, guardrails.>

## Runtime modes
<3-7 modes. Each mode has trigger examples, workflow, output contract, self-check.>

## Reference file specs
<For every reference file: purpose, required contents, format, acceptance criteria.>

## Governance
<Owners, repo visibility, source changes, reference changes, release/review/public demo policy.>

## Quality rubric
<Scoring dimensions and release gates.>

## Evals
<cases.yaml structure, smoke prompts, regression prompts, golden outputs.>

## Book2Skill -> skill-creation handoff
<Ready-to-paste artifact for the locally configured skill-creation workflow.>

## Implementation route
`/book2skill` -> `<skill-creator-command> <handoff>` -> `<development-skill-command> implement` -> verify -> commit/push -> install -> eval -> release.

Use the user's selected development skill instead of hardcoding one. For example, one environment may use `/coding`, another may use `/sho`, and another may use a different command.

## Git workflow
<branch, commit sequence, pre-push checks, privacy checks, tags.>

## Install and verification
<symlink/config/allowlist/restart/registry checks.>

## Rollback
<runtime, config, repo, private source incident handling if relevant.>

## Release plan
<v0.1.0, v0.2.0, v1.0.0 scopes.>

## Definition of Done
<mechanically verifiable checklist.>
````
