---
name: book2skill
description: Use when the user invokes /book2skill or asks to turn a book, PDF, EPUB, long article, course, notes, or author methodology into a practical OpenClaw skill. Produces a task-oriented skill spec or Staff+ delivery plan, avoids mere summaries, and hands final implementation to create-skill/skill creator after human review.
---

# book2skill

Turn a book or body of knowledge into a practical OpenClaw skill: a reusable working instrument with modes, workflows, checks, examples, and references.

## Core principle

Do **not** create a book summary skill by default. Create a practical skill that helps the user do something with the book's methods.

Good output:
- task modes and workflows
- decision rules and checklists
- author-derived principles turned into actions
- anti-patterns and self-checks
- compact references loaded on demand

Weak output:
- chapter-by-chapter retelling
- long quotations
- generic “key takeaways” with no workflow
- copying restricted text into the final skill without permission or purpose

## Workflow

### 1. Intake

Identify:
- source: PDF, EPUB, FB2, extracted text, notes, article, course, or prior analysis
- desired outcome: what the future skill should help the user do
- target users and context
- preferred language
- source type from `references/book-type-patterns.md`
- whether the user wants `analyze only`, `spec only`, or `create skill after review`

Ask only for blocking missing information. If the source exists locally, inspect it only after permission/context is clear.

### 2. Source handling and extraction

Use the safest available path:
- If text/notes are provided: analyze them directly.
- If a local `.txt`, `.md`, `.pdf`, `.epub`, `.fb2`, or `.fb2.zip` file is provided: use `scripts/extract_book.py` to extract text and metadata into a temporary directory.
- If an external tool or repo is suggested: do not install it automatically. Run the security gate before adopting code.
- For copyrighted books without explicit permission: summarize and transform into original workflows; do not store substantial copied passages in generated skills. If the user states the source is author-approved, user-owned, internal, or open-licensed, record that permission context and plan source archival/quotes according to `references/staff-plus-plan.md`.

Extractor command, resolving the script path relative to this skill directory:

```bash
python3 <skill-dir>/scripts/extract_book.py <source-file> --out-dir /tmp/book2skill_extract
```

Optional preview/cost-control mode for very large books:

```bash
python3 <skill-dir>/scripts/extract_book.py <source-file> --out-dir /tmp/book2skill_extract --max-chars 120000
```

Then read:
- `/tmp/book2skill_extract/metadata.json` for format, method, size, detected chapters, and quality hints
- `/tmp/book2skill_extract/full_text.txt` for analysis

Do not install missing dependencies automatically. If PDF/EPUB/FB2 extraction fails, report the missing extractor options and ask whether to install dependencies or accept exported text.

### 3. Extract practical material

Extract structure, not prose:
- named frameworks and exact terms
- principles and decision rules
- techniques and step-by-step methods
- diagnostics/questions the author would ask
- anti-patterns and failure modes
- examples worth abstracting into reusable patterns
- areas where chapter references are useful later

Use `references/practical-skill-spec.md` as the target shape.

### 4. Design the practical skill

Create a **Practical Skill Spec** before writing files. It must include:
- proposed skill name and trigger description
- use cases
- modes/commands or argument patterns
- workflow for each mode
- inputs and outputs
- guardrails and limits
- reference files to create
- validation/test prompts
- open questions

Use `references/output-templates.md`.

If the user asks for a production-grade plan, private/public GitHub repo plan, author-approved methodology skill, implementation plan, or anything that should be handed to `create-skill`/`shaw`, also produce a **Staff+ Skill Delivery Plan** using `references/staff-plus-plan.md`.

### 5. Staff+ delivery plan gate

When the user wants to make a real skill from the source, especially with a repo, team/client/authors, private source, release, evals, or create-skill handoff, produce a Staff+ plan before implementation.

Use `references/staff-plus-plan.md` and include:
- product thesis and non-goals
- source permission/provenance policy
- source/knowledge/runtime/eval architecture
- repo structure and install topology
- `SKILL.md` contract and mode contracts
- reference file specs with acceptance criteria
- governance, quality rubric, evals, golden outputs, feedback loop
- ready-to-paste `/create-skill extract` handoff
- implementation route through `create-skill` and `shaw`
- git workflow, verification, rollback, release plan, Definition of Done

Permission handling must be explicit:
- if author-approved/private/internal source is allowed, plan source archival, quote bank, `sources/manifest.yaml`, and `PRIVATE-NOTICE.md`;
- if permission is unknown or conservative, plan transformed references only and do not store raw source in the generated skill repo;
- if open-licensed, preserve attribution and license terms.

### 6. Human review gate

Before creating or overwriting a generated skill, show the spec and ask for confirmation unless the user explicitly pre-approved creation.

If the user requests changes, revise the spec first.

### 7. Handoff to skill creator

For final implementation, use the `create-skills` workflow as the build/refactor stage:
- create/update only under `~/.openclaw/workspace/skills/<target-skill>/`
- keep `SKILL.md` concise
- move long examples/checklists into `references/`
- add scripts only for deterministic repeated steps
- validate paths and smoke-check triggers

When handing off, provide the reviewed Practical Skill Spec plus the required file list and validation prompts.

### 8. Final report

Report:
- created/updated files
- how to invoke the new skill
- 2–3 realistic test requests
- any source/extraction limits or assumptions

## References

- `references/practical-skill-spec.md` — required spec fields and design rules
- `references/book-type-patterns.md` — patterns for different kinds of books
- `references/output-templates.md` — templates for analysis, spec, Staff+ delivery plan, and skill-creator handoff
- `references/staff-plus-plan.md` — production-grade planning framework for durable book-to-skill delivery with repo, governance, evals, and create-skill handoff
