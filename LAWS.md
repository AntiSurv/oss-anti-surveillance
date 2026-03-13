# Laws and Policy Drivers

Back to the front page: [README.md](README.md)

## Purpose

This document records the legal and policy drivers that are currently relevant to the project scope. It is not the operational evidence index. For implementation status and code activity, see [TRACKER.md](TRACKER.md).

This document exists to show where the pressure comes from. It does not treat these laws or policy pushes as morally or technically self-legitimating. The existence of a law does not obligate free software projects to normalize surveillance mechanisms in response.

## Why legal and policy context matters

The project tracks technical changes, but those changes do not arise in a vacuum. They are often driven by laws, bills, regulatory pressure, or policy agendas that attempt to push surveillance, classification, logging, or access mechanisms into general-purpose systems. These pressures can target different layers of the stack. This project distinguishes between:

- **OS-layer mandates** that pressure general-purpose distributions (e.g., California AB-1043).
- **App-store mandates** that pressure the mobile application ecosystem and its account layers (e.g., Alabama HB161).
- **Client-side scanning mandates** that push for device-side inspection (e.g., EU Chat Control).

A recurring pattern matters here:

- invoke child safety, public safety, or law-enforcement necessity
- create urgency
- pressure platforms and distributions to build new technical mechanisms
- present technical resistance as morally suspect or socially irresponsible

This project rejects that framing. The point of documenting the policy layer is not to help design cleaner compliance. It is to explain the pressure pathway and make the normalization attempt legible.

## Current legal and policy drivers

### California AB-1043

California AB-1043 is a central trigger for current Linux-stack implementation discussions around OS-level age verification and age signaling. Public discussions around provisioning, user records, account metadata, and app-facing APIs have repeatedly cited this law as a compliance driver.

Within the scope of this project, AB-1043 matters because it pressures operating-system-level components toward collecting and exposing age-related data for application or service use.

The core concern is not only the law’s text, but the implementation frame it creates. Once projects begin debating where to store the data, how to expose it, or how to package it, the discussion has already shifted away from the more important question of whether such a mechanism should exist at all.

### Colorado SB26-051

Colorado SB26-051 is closely associated with the same implementation pressure. It appears alongside California AB-1043 in current discussions as a parallel driver for age-related account and API work.

Within the scope of this project, it reinforces the concern that these mechanisms are not being proposed as isolated experiments, but as responses to a growing compliance pattern. That pattern matters because it encourages projects to think in terms of implementation pathways rather than categorical refusal.

### Brazil Lei 15.211/2025

Brazil Lei 15.211/2025 belongs in this document because the project scope is not limited to one jurisdiction. The project is intended to document state pressure that attempts to normalize surveillance or classification mechanisms in free software distributions.

As the dossier grows, this document should preserve a structured record of how each law or proposal pressures technical systems and how those pressures differ across jurisdictions.

### Alabama HB161 (2026)

Enacted in February 2026, Alabama HB161 requires mobile app store providers to implement age verification and parental consent systems. While its immediate target is the mobile app ecosystem (phones and tablets running mobile operating systems) rather than general-purpose Linux distributions, it is part of the same broader surveillance and control trajectory.

This law matters to the project because it shows the spread of the pattern to a different technical insertion point: the app store and account layer. Key provisions include requiring app stores to verify a user's age category using commercially available systems and to obtain verifiable parental consent for minors. This establishes a precedent for building verification and gating systems directly into software distribution channels.

### EU Chat Control and related policy pushes

The broader policy context includes EU Chat Control and related "lawful-access" initiatives. These are important to this project because they show a recurring pattern: child-safety or law-enforcement rhetoric is used to normalize technical mechanisms for inspection, classification, access, or logging.

This project treats those developments as part of the same family of pressure, even where the exact mechanism differs. The point is not that every proposal is identical. The point is that they repeatedly seek to establish technical capabilities that reframe user systems as points of inspection, disclosure, or control.

## What this file is not

This document is not a full legal encyclopedia, a litigation database, or a substitute for the operational evidence index.

It should not become:

- a catch-all tracker for code changes
- a dumping ground for packaging notes
- a generic privacy-policy archive
- a neutral summary that obscures the project’s position

Its job is to record the legal and policy drivers clearly enough that the technical work in [TRACKER.md](TRACKER.md), [STACK.md](STACK.md), and [REPO-TARGETS.md](REPO-TARGETS.md) can be understood in context.

## How to use this file

Use this document to understand:

- which laws or proposals are currently driving implementation pressure
- why apparently separate technical changes may share a common policy origin
- how legal pressure maps onto technical architecture
- why the same coercive framing can recur across different jurisdictions and technical proposals

Then move to [TRACKER.md](TRACKER.md), [STACK.md](STACK.md), and [REPO-TARGETS.md](REPO-TARGETS.md) for the implementation-facing side.

## Maintenance notes

This document should remain focused on laws, policy texts, and official policy pushes. Do not use it as a catch-all tracker for code changes, distro packaging, or technical dependency analysis.

When updating this file, keep two standards in mind:

- preserve factual clarity about what a law or proposal does
- do not let the framing drift into the idea that surveillance mechanisms become acceptable merely because a law pressures projects to consider them

## See also

- [README.md](README.md)
- [TRACKER.md](TRACKER.md)
- [STACK.md](STACK.md)
- [REPO-TARGETS.md](REPO-TARGETS.md)
- [CONTRIBUTING.md](CONTRIBUTING.md)
