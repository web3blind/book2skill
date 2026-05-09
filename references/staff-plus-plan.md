# Staff+ Skill Delivery Plan

Use this reference when the user wants to create a skill from a book or author methodology and asks for a high-quality plan, production plan, private repo plan, author-approved plan, or anything that should be robust enough to hand to another agent or engineer.

The Staff+ plan is not just a longer Practical Skill Spec. It is a delivery plan for turning a source into a maintained, testable, private or public OpenClaw skill.

## When to produce a Staff+ plan

Produce this plan when any of these are true:

- the user asks for a plan before creating the skill;
- the skill will live in a Git repo;
- the skill is for authors, a client, a team, or future reuse;
- source permission, privacy, or provenance matters;
- the user mentions skill creation, implementation handoff, GitHub, PR, upstream, private repo, release, evals, or tests;
- the source is a whole book, course, methodology, or expert system rather than a small note;
- the skill may become a template for future book-to-skill work.

Do not force the Staff+ plan for tiny personal experiments unless the user asks for it. For small one-off requests, use the Practical Skill Spec only.

## Staff+ plan objective

The plan should design an **author methodology runtime**, not a summary of the source.

It must explain how to create:

1. a source layer;
2. a knowledge layer;
3. a runtime skill layer;
4. an evaluation layer;
5. a release and maintenance loop.

## Core architecture

Use this four-layer model:

```text
source layer
  raw source, extracted text, metadata, section index, quote bank

knowledge layer
  frameworks, diagnostics, checklists, playbooks, examples, anti-patterns

runtime layer
  SKILL.md router, mode selection, required context, output contracts

evaluation layer
  smoke prompts, regression prompts, golden outputs, expected behaviors, rubric
```

The source layer preserves fidelity. The knowledge layer turns the source into operational material. The runtime layer keeps the skill fast and usable. The evaluation layer prevents regressions.

## Required sections

A Staff+ plan must include the following sections. Keep them explicit and actionable.

### 1. Executive summary

State:

- source name and author/origin;
- target skill name;
- target repo or install path if known;
- permission/privacy context;
- what the skill will do;
- what it must not become.

### 2. Product thesis

Define the skill as a working assistant:

- advisor;
- editor;
- critic;
- coach;
- decision guide;
- implementation assistant;
- source-backed navigator.

Answer: what repeated job should the skill perform better than a generic chat?

### 3. Success definition

Separate:

- product success;
- technical success;
- source fidelity success;
- runtime usability success.

### 4. Naming, repository, and install topology

Include:

- final skill name;
- repo name;
- local canonical path;
- runtime symlink path;
- target agent;
- OpenClaw registry verification command.

Example:

```bash
openclaw skills list --agent <agent-id> --eligible | grep <skill-name>
```

### 5. Source and permission policy

Do not assume all books have the same policy. Ask or infer permission state.

Supported permission modes:

#### A. Private author-approved source

Use when the user says they have author/rights-holder permission or the source is internal.

Policy:

- raw source may be stored in the private repo;
- extracted text may be stored;
- quote banks and excerpts are allowed when useful;
- repo must remain private unless explicitly approved;
- add `PRIVATE-NOTICE.md`;
- add `sources/manifest.yaml`.

#### B. User-owned/internal source

Use for internal docs, transcripts, courses, team playbooks.

Policy:

- source may be stored if the user wants reproducibility;
- label privacy constraints;
- avoid accidental public sharing.

#### C. Copyrighted third-party source without explicit redistribution permission

Use the conservative policy:

- do not commit raw source;
- do not store long excerpts;
- store transformed workflows only;
- keep source local/tmp;
- include a copyright handling note.

#### D. Public/open-licensed source

Use the license terms:

- store source if license permits;
- include license notice;
- preserve attribution;
- note license restrictions.

### 6. Source provenance manifest

For any durable repo, plan `sources/manifest.yaml`.

Template:

```yaml
source_id: <stable-id>
title: "<title>"
authors:
  - "<author>"
format:
  original: "<PDF/EPUB/FB2/notes/etc>"
  extracted_text: "sources/extracted/full_text.txt"
permission:
  status: "<author_approved_private_skill|user_owned|copyrighted_transform_only|open_license>"
  granted_to: "<person/team if known>"
  allowed_uses:
    - "<use>"
  restrictions:
    - "<restriction>"
runtime_policy:
  default_load: "references_only"
  source_lookup: "on_demand"
```

### 7. Repository structure

Use this default structure for Staff+ plans:

```text
<skill-name>/
  SKILL.md
  README.md
  PRIVATE-NOTICE.md              # when private/source-sensitive
  GOVERNANCE.md
  QUALITY_RUBRIC.md
  CHANGELOG.md
  sources/
    manifest.yaml
    <raw-source-file>             # only when allowed/useful
    extracted/
      metadata.json
      full_text.txt               # only when allowed/useful
      section-index.md
      chapter-map.md
  references/
    frameworks.md
    diagnostics.md
    checklists.md
    playbooks.md
    examples.md                   # optional
    anti-patterns.md
    source-quotes.md              # when quotes are allowed/useful
    validation-prompts.md
  evals/
    cases.yaml
    expected-behaviors.md
    run-evals.sh
    golden/
      <golden-output>.md
  feedback/
    failed-prompts.md
    author-notes.md
  scripts/
    extract-source.sh             # optional
    build-section-index.py        # optional
    check-private-source.sh       # optional
  tests/
    smoke-prompts.md
    regression-prompts.md
```

Adjust names to the source domain, but keep the source/knowledge/runtime/eval split.

### 8. `SKILL.md` contract

The plan must specify that `SKILL.md` stays concise and acts as a router.

It should include:

- frontmatter with trigger-specific description;
- when to use;
- when not to use;
- required context;
- mode router;
- reference loading map;
- source lookup policy;
- output style;
- guardrails;
- self-check.

Do not put full book content in `SKILL.md`.

### 9. Runtime modes

Define 3-7 modes by default, each with:

- trigger examples;
- workflow;
- output contract;
- self-check;
- references to consult.

For large methodology skills, add a source-backed mode when source is allowed or useful.

Mode template:

````md
### Mode <N>: <name>

Use when:
- ...

Workflow:
1. ...
2. ...
3. ...

Output contract:
```md
## <section>
...
```

Self-check:
- ...
````

### 10. Reference file specs

For every planned reference file, define:

- purpose;
- required contents;
- required format;
- acceptance criteria.

This prevents vague file lists.

### 11. Governance

Plan `GOVERNANCE.md` when the skill is for a team, authors, private source, or repo release.

Include:

- owners;
- repo visibility;
- source change rules;
- reference change rules;
- release policy;
- review policy;
- public demo policy.

### 12. Quality rubric

Plan `QUALITY_RUBRIC.md` with scoring dimensions.

Recommended dimensions:

1. Practicality;
2. faithfulness to source;
3. strategic depth;
4. output usability;
5. brevity/context control;
6. mode routing accuracy;
7. domain realism;
8. source citation handling;
9. maintainability.

Define release gates, for example:

```text
v0.1.0: average >= 4.0, no critical failures
v0.2.0: average >= 4.2, author/team feedback incorporated
v1.0.0: average >= 4.3, 20+ real cases, stable regressions
```

### 13. Evals

Plan structured evals, not just test prompts.

Files:

- `evals/cases.yaml`;
- `evals/expected-behaviors.md`;
- `evals/run-evals.sh`;
- `evals/golden/*.md`;
- `tests/smoke-prompts.md`;
- `tests/regression-prompts.md`.

Each eval case should include:

- id;
- prompt;
- expected mode;
- must_include;
- must_not_include;
- failure signs.

### 14. Book2Skill -> skill-creation handoff

Include a ready-to-paste handoff for the locally configured skill-creation workflow.

It must state:

- target skill name;
- permission policy;
- source summary;
- product goal;
- target paths;
- architecture;
- required files;
- modes;
- quality requirements.

### 15. Implementation route

For OpenClaw skill creation, route through the local skill creator flow and the user's selected development/implementation skill:

```text
/book2skill finalize <skill-name> from extracted source with <permission policy>
<skill-creator-command> <handoff>
<development-skill-command> implement <skill-name> private/public skill repo from skill-creator output contract
```

Do not hardcode a specific development command. Use the environment's selected development skill (for example `/coding`, `/sho`, or another local command) and preserve the stage gates: Book2Skill spec -> skill packaging -> implementation -> verification.

### 16. Git workflow

Plan:

- branch name;
- commit sequence;
- pre-push checklist;
- privacy check;
- tag/release.

### 17. Installation and verification

Plan symlink/config/allowlist steps and registry verification.

Include commands when paths are known.

### 18. Smoke and regression tests

Give concrete prompts.

Smoke prompts prove the skill works. Regression prompts prevent bad behavior.

### 19. Author/team review packet

For author-approved or team skills, plan a compact review packet. The reviewers should review outputs, not the entire repo.

Include questions:

- Does this match the methodology?
- Where is the agent generic?
- Where does it distort the source?
- What terms must be preserved?
- What advice should never be given?
- Which mode is most valuable?

### 20. Observability and feedback loop

Plan `feedback/failed-prompts.md` and `feedback/author-notes.md`.

Every real failure should create at least one of:

- updated reference;
- updated routing instruction;
- new regression prompt;
- new golden output;
- author note.

### 21. Compatibility map

List upstream and downstream skills/tools.

Example:

- `book2skill`: source extraction and practical spec;
- local skill-creation workflow: production packaging;
- selected development/implementation skill: implementation;
- domain-specific downstream skills: publishing, research, design, analytics.

Also state boundaries: what this skill owns and does not own.

### 22. Rollback plan

Include:

- runtime rollback;
- config rollback;
- repo rollback;
- private source incident handling when relevant.

### 23. Release plan

Define expected scope for:

- `v0.1.0`;
- `v0.2.0`;
- `v1.0.0`.

### 24. Definition of Done

Write a checklist that can be verified mechanically where possible.

### 25. Final operator checklist

Include commands to verify files, install state, registry readiness, git status, and tag.

## Output format

When the user asks for the plan in chat, return a compact but complete Markdown plan.

When the user asks for a file, write the plan to a `.md` file and send it as a document if the chat supports attachments.

## Quality bar

A Staff+ plan should be specific enough that another agent can implement the skill without asking what “good” means.

It is acceptable for the plan to be long. It is not acceptable for it to be vague.
