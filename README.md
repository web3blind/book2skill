# Book2Skill

Book2Skill is an OpenClaw skill for turning books, long articles, courses, notes, or author methods into practical AI-agent skills.

It is not a summarizer. The goal is to extract useful working structure from source material and turn it into a reusable skill: workflows, decision rules, checklists, modes, guardrails, and reference files.

## What it helps with

Use Book2Skill when you have a source such as a PDF, EPUB, FB2, Markdown notes, a course transcript, or a long methodology article, and you want to create a practical OpenClaw skill from it.

Typical outputs:

- a practical skill specification;
- clear modes and workflows;
- source-derived frameworks and decision rules;
- checklists and anti-patterns;
- reference files for the final skill;
- validation prompts for testing whether the new skill works.

## What it deliberately avoids

Book2Skill is designed to avoid weak “book summary” skills.

It should not:

- copy large passages from copyrighted books;
- create chapter-by-chapter summaries as the final product;
- store source books inside the generated skill;
- turn a book into generic motivational advice;
- install extraction dependencies without explicit approval.

## How it works

The skill follows this flow:

1. Identify the source material and the practical job the future skill should perform.
2. Extract text and metadata when the source is local and permission/context is clear.
3. Convert the material into frameworks, rules, techniques, diagnostics, anti-patterns, and examples.
4. Produce a Practical Skill Spec for human review.
5. Hand the reviewed spec to the skill-creation workflow.
6. Keep long supporting material in `references/`, while keeping `SKILL.md` concise.

## Included files

- `SKILL.md` — main OpenClaw skill instructions.
- `references/practical-skill-spec.md` — required shape for the intermediate skill spec.
- `references/book-type-patterns.md` — patterns for different source types: writing, technical, product, marketing, psychology, reference books, and mixed books.
- `references/output-templates.md` — templates for analysis reports, specs, and handoff prompts.
- `scripts/extract_book.py` — local extractor for `.txt`, `.md`, `.pdf`, `.epub`, `.fb2`, and `.fb2.zip` files. It uses only available local tools/libraries and does not install dependencies.

## Source books and artifacts

This repository does not include books, PDFs, EPUBs, FB2 files, extraction outputs, or generated artifacts.

That is intentional:

- source books may be copyrighted;
- extraction artifacts can be large or private;
- generated skills should contain transformed practical guidance, not copied source text;
- each user should provide their own source material locally.

The `.gitignore` excludes common book and artifact formats by default.

## Example requests

```text
Use book2skill to turn this EPUB about product strategy into a practical planning skill.
```

```text
Analyze this PDF and design a skill that helps me review architecture decisions using the author's framework.
```

```text
Create a practical skill spec from these course notes. Do not create the skill yet; I want to review the spec first.
```

## Security and privacy notes

- No source books are committed to this repository.
- The extractor writes to a chosen output directory and should be used with temporary folders for source analysis.
- External tools or repositories should go through a security review before use.
- Secrets, tokens, environment files, and private keys are excluded by `.gitignore`.

## Status

This is a practical OpenClaw skill extracted from real workflow needs: turning useful knowledge sources into agent workflows that can be reused, tested, and improved.
