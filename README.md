# Book2Skill

Book2Skill is an OpenClaw skill for turning books, long articles, courses, notes, or author methods into practical AI-agent skills.

It is not a summarizer. The goal is to extract useful working structure from source material and turn it into a reusable skill: workflows, decision rules, checklists, modes, guardrails, reference files, and when needed a production-grade delivery plan.

## What it helps with

Use Book2Skill when you have a source such as a PDF, EPUB, FB2, Markdown notes, a course transcript, or a long methodology article, and you want to create a practical OpenClaw skill from it.

Typical outputs:

- a practical skill specification;
- a Staff+ skill delivery plan for durable/repo-backed skills;
- clear modes and workflows;
- source-derived frameworks and decision rules;
- checklists and anti-patterns;
- reference files for the final skill;
- validation prompts and eval cases for testing whether the new skill works;
- a ready-to-paste handoff for the local skill-creation / implementation workflow.

## What it deliberately avoids

Book2Skill is designed to avoid weak “book summary” skills.

It should not:

- create chapter-by-chapter summaries as the final product;
- turn a book into generic motivational advice;
- dump full source text into SKILL.md;
- store restricted source material when permission is unknown or conservative;
- ignore author-approved, user-owned, internal, or open-license permission context when source archival would improve fidelity;
- install extraction dependencies without explicit approval.

## Staff+ planning mode

When the user wants to make a durable skill from a book or methodology, especially with a repo-backed implementation, private/team/client/author context, release, evals, or skill-creation handoff, Book2Skill should produce a **Staff+ Skill Delivery Plan**.

The Staff+ plan designs the full delivery system:

1. source layer — raw/extracted source, metadata, section index, quote bank;
2. knowledge layer — frameworks, diagnostics, checklists, playbooks, anti-patterns;
3. runtime layer — concise SKILL.md router, modes, output contracts;
4. evaluation layer — smoke tests, regression prompts, golden outputs, quality rubric;
5. governance/release loop — owners, permissions, private notice, changelog, rollback.

This mode is documented in references/staff-plus-plan.md.

## How it works

The skill follows this flow:

1. Identify the source material and the practical job the future skill should perform.
2. Extract text and metadata when the source is local and permission/context is clear.
3. Convert the material into frameworks, rules, techniques, diagnostics, anti-patterns, and examples.
4. Produce a Practical Skill Spec for human review.
5. If the user wants a durable implementation, repo, release, author/team workflow, evals, or skill-creation handoff, produce a Staff+ Skill Delivery Plan.
6. Hand the reviewed spec/plan to the skill-creation workflow.
7. Keep long supporting material in `references/` or `sources/`, while keeping `SKILL.md` concise.

## Included files

- `SKILL.md` — main OpenClaw skill instructions.
- `references/practical-skill-spec.md` — required shape for the intermediate skill spec.
- `references/book-type-patterns.md` — patterns for different source types: writing, technical, product, marketing, psychology, reference books, and mixed books.
- `references/output-templates.md` — templates for analysis reports, specs, Staff+ delivery plans, and handoff prompts.
- `references/staff-plus-plan.md` — production-grade planning framework for durable book-to-skill delivery with repo, governance, evals, and skill-creation handoff.
- `scripts/extract_book.py` — local extractor for `.txt`, `.md`, `.pdf`, `.epub`, `.fb2`, and `.fb2.zip` files. It uses only available local tools/libraries and does not install dependencies.

## Source books and artifacts

This repository does not include books, PDFs, EPUBs, FB2 files, extraction outputs, or generated artifacts.

That is intentional:

- source books may be copyrighted, private, or large;
- extraction artifacts can be private;
- generated skills should usually contain transformed practical guidance, not copied source text;
- each user should provide their own source material locally.

However, Book2Skill now supports explicit permission modes:

- **author-approved/private source** — plan source archival, extracted text, quote bank, `PRIVATE-NOTICE.md`, and `sources/manifest.yaml` only when the user has storage rights/permission, even if the repo is private;
- **user-owned/internal source** — plan privacy-preserving archival and provenance;
- **restricted third-party source** — keep raw source local and store transformed references only;
- **open-licensed source** — preserve license and attribution.

The `.gitignore` excludes common book and artifact formats by default for this Book2Skill repo. Generated skill repos may choose a different policy when permission allows.

## Example requests

- Use book2skill to turn this EPUB about product strategy into a practical planning skill.
- Analyze this PDF and design a skill that helps me review architecture decisions using the author methodology.
- Create a practical skill spec from these course notes. Do not create the skill yet; I want to review the spec first.
- Make a Staff+ plan for a private GitHub skill repo from this author-approved book, with skill-creation handoff and evals.

## Security and privacy notes

- No source books are committed to this Book2Skill repository.
- The extractor writes to a chosen output directory and should be used with temporary folders for source analysis.
- External tools or repositories should go through a security review before use.
- Secrets, tokens, environment files, and private keys are excluded by .gitignore.
- For generated skill repos, source storage must follow the permission mode captured in the plan and sources/manifest.yaml.

## Status

This is a practical OpenClaw skill extracted from real workflow needs: turning useful knowledge sources into agent workflows that can be reused, tested, improved, and shipped through a reliable skill-creation pipeline.
