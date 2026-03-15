# OSS Anti Surveillance

Tracking, documenting, opposing, removing, and reversing OS-level surveillance mechanisms in free software distributions.

## Mission

OSS Anti Surveillance exists to document and resist attempts to turn free software distributions into surveillance, classification, or policy-enforcement endpoints.

This project opposes:

- OS-level age verification
- age signaling and age-bracket APIs
- client-side scanning and device-side inspection
- metadata and portal layers repurposed for compliance
- downstream inheritance of surveillance mechanisms
- geo-fencing users out of free software in response to coercive law

Free software distributions must remain general-purpose systems under user control. They must not become infrastructure for categorizing, filtering, or monitoring people on behalf of states, platforms, or third-party services.

## Non-negotiable position

This project does not exist to help design a cleaner implementation path for surveillance mechanisms in free software. It exists to document them, oppose them, and prepare their removal.

The central error in many of the implementation discussions tracked here is not a particular daemon, schema, API, portal, or packaging choice. The central error is accepting the premise that general-purpose free operating systems should be discussing how to build these mechanisms at all.

That premise is rejected here.

No implementation path is acceptable. Not in a user record. Not in account metadata. Not in a portal. Not in an installer. Not as a minimal age bracket. Not as an opaque token. Not as a temporary compromise. Not as a jurisdiction-specific feature.

This project also rejects the coercive pattern that repeatedly appears around these proposals: invoke child safety or public safety, create urgency, apply emotional pressure, and then treat technical or civil-liberties objections as morally suspect. That pattern does not legitimize the mechanism. It is one of the reasons the mechanism must be refused.

No law is above morality or technical scrutiny.

For the project’s political and moral declaration, see [MANIFESTO.md](MANIFESTO.md).

## Why this project exists

A visible implementation path is now emerging across parts of the Linux stack. Public code and discussion have already appeared in components that touch provisioning, account metadata, user records, and app-facing interfaces. That means this issue is no longer purely theoretical.

The immediate concern is not one isolated patch. The concern is an architectural pattern:

- installer or provisioning flow collects age-related data
- account metadata services or user databases store it
- a portal or standard API exposes it
- applications, app stores, or services consume it

The same broader pattern also appears in other policy pushes, including client-side scanning and related "lawful-access" initiatives. The underlying problem is the same: technical pressure to normalize surveillance or classification mechanisms inside user systems. That pressure now arrives through multiple legislative insertion points, including OS-layer mandates, app-store-layer mandates, and client-side scanning pushes.

See [Current Repository Targets](REPO-TARGETS.md), [Technical Architecture](STACK.md), and [Laws and Policy Drivers](LAWS.md).

## Project scope

This project focuses on OS-level surveillance and compliance mechanisms in free software distributions, especially where they affect:

- installers and provisioning systems
- account metadata services
- user databases and user records
- portals and standard application-facing APIs
- downstream packaging and removal strategies

This project's repository is not a general-purpose privacy encyclopedia. It is a focused dossier, tracker, and reversal project for surveillance-related functionality at the distribution and core-platform level.

## What this project does

OSS Anti Surveillance has four core functions.

### 1. Document

This project records relevant laws, policy drivers, mailing-list discussions, issues, pull requests, merge requests, and implementation paths across the Linux stack.

### 2. Track

This project maintains a public evidence index of targeted components, current status, downstream implications, and known dependency relationships.

### 3. Prepare removal and reversal

This project tracks revert paths, downstream patch strategies, packaging notes, and later, where necessary, binary rebuild and distribution strategies.

### 4. Teach

This project exists to help users, packagers, and contributors understand what is changing, why it matters, and how to identify, remove, replace, or rebuild affected components.

## Repository map

Start here, then use the following documents for specific purposes:

- [README.md](README.md): public front page, mission, scope, current direction
- [MANIFESTO.md](MANIFESTO.md): political and moral declaration of the project
- [TRACKER.md](TRACKER.md): operational evidence index and status table
- [LAWS.md](LAWS.md): legal and policy drivers
- [STACK.md](STACK.md): technical architecture and propagation path
- [REPO-TARGETS.md](REPO-TARGETS.md): component-by-component technical targets
- [ACTORS.md](ACTORS.md): model-bill producers, advocacy ecosystem, and public-support map
- [REVERSIONS/README.md](REVERSIONS/README.md): removal, stripping, and reversal strategy
- [CONTRIBUTING.md](CONTRIBUTING.md): contribution standards and evidence rules

## Principles

The project is guided by the following principles.

- No OS-level age verification
- No age signaling or age-bracket APIs at the distribution level
- No client-side scanning or device-side inspection primitives in general-purpose systems
- No normalization of surveillance mechanisms through account metadata, user databases, or portals
- No passive downstream inheritance of surveillance mechanisms and no acceptance of such mechanisms in downstream packages
- No geo-fencing users out of free software as a substitute for technical resistance
- No law is above morality or technical scrutiny
- Free software must remain accessible to all human beings

## Current priorities

The highest current priorities are:

- track and oppose standardization in portal and metadata layers
- track and oppose normalization in core account and user record services
- maintain a public record of downstream integration work
- expand the legal map to track the spread of OS-layer and app-store-layer mandates across U.S. states
- prepare downstream removal and package-level stripping strategies if upstream merges occur
- keep the project precise, linkable, and easy to audit

For the current list of tracked components, see [REPO-TARGETS.md](REPO-TARGETS.md). For the operational evidence index, see [TRACKER.md](TRACKER.md).

## Current tracked targets

The current documented target set includes:

- systemd
- xdg-desktop-portal
- AccountsService
- Ubuntu desktop provisioning
- Archinstall

These components are currently relevant because they represent concrete parts of the active implementation path from provisioning to account metadata to application-facing API exposure.

See [REPO-TARGETS.md](REPO-TARGETS.md) for the component-by-component view and [TRACKER.md](TRACKER.md) for current status.

## Red lines

This project treats the first concrete implementation step as a red line crossed.

That includes:

- adding age-related fields to provisioning or installation flows
- storing age-related data in account metadata or user databases
- standardizing a portal or API for age signaling
- inheriting such mechanisms downstream without stripping them from packages

If upstream projects merge these mechanisms, downstream distributions should remove them from their packages rather than quietly inherit them.

## How to use this project's repository

If you are new to the project:

1. Read [LAWS.md](LAWS.md) for the legal and policy background.
2. Read [STACK.md](STACK.md) for the technical architecture map.
3. Review [REPO-TARGETS.md](REPO-TARGETS.md) for the current component list.
4. Check [TRACKER.md](TRACKER.md) for the live evidence index and current status of each item.
5. Use [REVERSIONS/README.md](REVERSIONS/README.md) to understand the project’s downstream removal and reversal strategy.
6. Read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting new evidence.

## Status labels

The tracker uses these status labels:

- discussion
- draft
- active implementation
- merged
- closed unmerged
- downstream inherited
- downstream stripped
- reverted
- watchlist

These labels are defined operationally in [TRACKER.md](TRACKER.md).

## Contributing

Contributions should be evidence-based, precise, and linkable.

Before contributing, read [CONTRIBUTING.md](CONTRIBUTING.md). New evidence should be added in the appropriate place, with direct links and enough technical detail to explain why the item matters.

## Closing statement

Free software distributions must not be turned into surveillance infrastructure.

OSS Anti Surveillance exists to document these mechanisms, track their spread, oppose their normalization, and prepare their removal where necessary. This project's repository is a public record, a technical map, and a practical starting point for reversal work.

See also: [MANIFESTO.md](MANIFESTO.md), [TRACKER.md](TRACKER.md), [LAWS.md](LAWS.md), [STACK.md](STACK.md), [REPO-TARGETS.md](REPO-TARGETS.md), [ACTORS.md](ACTORS.md), [REVERSIONS/README.md](REVERSIONS/README.md), [CONTRIBUTING.md](CONTRIBUTING.md)
