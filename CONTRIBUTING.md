# Contributing

Back to the front page: [README.md](README.md)

## Purpose

This project depends on precise, verifiable, and navigable evidence. Contributions should make the dossier stronger, easier to audit, and easier to act on.

Contributors should help:

- add direct evidence of surveillance-related implementation work
- clarify technical relationships between components
- record downstream implications
- improve removal and reversal notes
- keep terminology and scope consistent

## Where to add information

Use the document that matches the content.

- Add implementation evidence, issues, pull requests, merge requests, and status updates to [TRACKER.md](TRACKER.md).
- Add legal and policy background to [LAWS.md](LAWS.md).
- Add architecture relationships and propagation paths to [STACK.md](STACK.md).
- Add component-specific technical detail to [REPO-TARGETS.md](REPO-TARGETS.md).
- Add removal and stripping notes to [REVERSIONS/README.md](REVERSIONS/README.md).

Do not place information in the wrong file just because it is related in a broad sense. The project depends on sharp document roles.

## Contribution standards

Every contribution should be:

- source-linked
- specific
- technically legible
- scoped to the project mission
- placed in the correct file
- written in consistent terminology

## Required evidence quality

When adding a new tracker entry or updating an existing one, include:

- component name
- upstream repository
- direct link to the issue, PR, or MR
- current status
- a concise description of what changed or is proposed
- why it matters architecturally
- any known downstream implications

Whenever possible, use the direct primary source:

- GitHub pull request or issue
- GitLab merge request or issue
- mailing-list archive permalink
- forum thread permalink
- official law, bill, or policy source

Do not leave a named tracked item unlinked when the direct source exists.

### Legal and policy source standards

For policy-driver entries in [LAWS.md](LAWS.md) or [TRACKER.md](TRACKER.md), use official primary sources wherever practical. The link text must accurately label the source.

- **Preferred:** Official legislature bill pages, enrolled bill PDFs, or official fiscal notes. Label these accurately (e.g., "Official bill text").
- **Acceptable:** Legislative trackers such as LegiScan may be included as supplementary links, but should not be the only source when an official source is available. Label these truthfully (e.g., "LegiScan").

Policy items added to the tracker must include the bill name and jurisdiction, the technical layer targeted (e.g., OS-layer, App-store layer), current legislative status, and a direct primary source link.

## Linking standards

Use direct Markdown links to primary sources wherever possible.

Examples of acceptable sources include:

- upstream GitHub PRs and issues
- upstream GitLab MRs and issues
- mailing-list archive pages
- forum threads
- official policy and legal texts

Avoid relying on:

- screenshots when a primary URL exists
- secondary summaries when the upstream item is public
- vague references such as "there was a thread" without a direct link

## Preferred terminology

Use these terms consistently unless quoting external material:

- OS-level age verification
- age signaling
- age-bracket API
- surveillance mechanism
- policy-enforcement endpoint
- downstream removal
- geo-fencing

Avoid drifting into inconsistent variants that weaken the dossier or blur the scope.

## What not to submit

Do not submit:

- vague rumors without direct links
- screenshots without source URLs
- duplicate tracker entries
- broad claims without technical or documentary support
- unrelated privacy issues outside the project scope
- placeholder text or speculative prose without evidence

## Updating the tracker

When updating [TRACKER.md](TRACKER.md):

- preserve the existing column structure
- update the status field carefully
- keep the summary factual
- record downstream implications where known
- add cross-links to [LAWS.md](LAWS.md), [STACK.md](STACK.md), or [REVERSIONS/README.md](REVERSIONS/README.md) where relevant
- ensure every named item is a direct Markdown link to its primary upstream source

## Updating technical targets

When updating [REPO-TARGETS.md](REPO-TARGETS.md):

- keep entries component-specific
- explain the component’s role in the stack
- avoid duplicating the entire tracker entry
- point readers back to [TRACKER.md](TRACKER.md) for live status
- include direct Markdown links for current upstream references

## Updating reversions

When adding notes to [REVERSIONS/README.md](REVERSIONS/README.md):

- distinguish clearly between strategy and completed work
- state whether the note concerns upstream rejection, downstream stripping, or a full revert path
- record known dependencies and likely breakage risks if relevant

## Internal link discipline

Before submitting a change, check that:

- internal links exist and resolve
- filenames match the canonical repository names
- the new content is linked from at least one appropriate parent document
- no dangling section or orphan file is introduced
- all named tracked items and upstream references are linked directly when a primary source exists

## Style and formatting

Use high-quality Markdown. Keep headings clean, lists consistent, and prose precise. Prefer direct links and structured summaries over vague or repetitive prose. This project should be severe in substance and disciplined in presentation.

## See also

- [README.md](README.md)
- [MANIFESTO.md](MANIFESTO.md)
- [TRACKER.md](TRACKER.md)
- [LAWS.md](LAWS.md)
- [STACK.md](STACK.md)
- [REPO-TARGETS.md](REPO-TARGETS.md)
- [REVERSIONS/README.md](REVERSIONS/README.md)
