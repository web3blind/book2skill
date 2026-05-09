# Practical Skill Spec

Use this as the intermediate artifact before generating a final skill.

## Required fields

### 1. Source
- title/source name
- author or origin, if known
- source format
- extraction quality and limits
- source permission/privacy note: author-approved, user-owned/internal, open-licensed, or conservative transform-only handling

### 2. Practical purpose
Answer: what should the future skill help the user do?

Examples:
- edit unclear text into concise human prose
- review architecture decisions
- plan a marketing launch
- diagnose product strategy gaps
- apply negotiation frameworks before a call

### 3. Target users and context
- primary user
- typical inputs
- expected output style
- language and tone

### 4. Core operating model
Define how the skill behaves:
- advisor
- editor
- critic
- coach
- decision guide
- checklist runner
- implementation assistant
- reference navigator

### 5. Modes
Each mode should have:
- trigger/argument pattern
- when to use
- input needed
- workflow steps
- output format
- self-check

Prefer 3–7 modes. Too many modes make the skill noisy.

### 6. Extracted knowledge
Transform book knowledge into:
- frameworks: named models with when/how to use
- principles: rules for decisions
- techniques: repeatable procedures
- diagnostics: questions to ask
- anti-patterns: traps and failure modes
- examples: abstracted patterns, not copied text

### 7. References to create
Common files:
- `references/frameworks.md`
- `references/checklists.md`
- `references/examples.md`
- `references/anti-patterns.md`
- `references/chapter-index.md`

Only create files that will be useful on demand.

### 8. Guardrails
Include:
- scope limits: book-derived guidance, not universal truth
- source limits: extraction gaps, missing chapters, poor OCR
- legal/privacy limits: whether raw source, extracted text, quotes, and excerpts may be stored or must stay local/transformed only
- style limits: preserve user voice where relevant
- safety/domain limits where needed

### 9. Validation prompts
Write 2–3 realistic requests that should trigger the skill and exercise its main workflow.

## Design rules

- Optimize for repeated use, not a one-time answer.
- A skill should perform a job; references should store supporting knowledge.
- Frontmatter description must be trigger-specific and concise.
- The first screen of `SKILL.md` should teach the agent how to act, not explain the book.
- Prefer actionable verbs: diagnose, rewrite, plan, decide, review, critique, generate.
- If the book is mostly conceptual, turn concepts into questions and decision rules.
- If the book is technical, turn content into decision guides, implementation playbooks, and review checklists.


## Staff+ upgrade trigger

When the user wants a durable repo-backed skill, private/team/author workflow, skill-creation handoff, evals, release, or implementation plan, do not stop at this Practical Skill Spec. Produce a Staff+ Skill Delivery Plan using `references/staff-plus-plan.md`. For quick personal experiments, keep the Practical Skill Spec only unless the user asks for Staff+ planning.
