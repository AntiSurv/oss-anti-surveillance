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

This broader pattern is not limited to one country or one bill family. Freedom House’s [*Freedom on the Net 2025*](https://freedomhouse.org/report/freedom-net/2025/uncertain-future-global-internet) report warns that online anonymity is entering a period of crisis and identifies mandatory age-verification systems as a growing threat to privacy, free expression, and access to information. That wider context matters because these laws do not merely regulate one service or one platform; they push toward persistent identity and verification layers across the digital environment.

## U.S. state landscape

The legal pressure in the United States is not an isolated phenomenon. It represents a set of parallel experiments in pushing age verification, classification, parental-consent infrastructure, or disclosure obligations into different layers of the software stack. The current state-level landscape can be grouped into recurring legislative models rather than treated as a random list of unrelated bills. The two most prominent models are **OS-layer age assurance mandates** and **app-store accountability mandates**, each targeting a different technical layer with a different compliance burden.

### OS-layer mandates

These laws or proposals target the operating system itself, pressuring distributions to build in functionality for account-setup age collection and to provide a real-time API or signal for applications to consume.

#### California AB-1043

California AB-1043 is a central trigger for current Linux-stack implementation discussions around OS-level age verification and age signaling. Public discussions around provisioning, user records, account metadata, and app-facing APIs have repeatedly cited this law as a compliance driver. ([Official bill text](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260AB1043))

Within the scope of this project, AB-1043 matters because it pressures operating-system-level components toward collecting and exposing age-related data for application or service use. The core concern is not only the law’s text, but the implementation frame it creates. Once projects begin debating where to store the data, how to expose it, or how to package it, the discussion has already shifted away from the more important question of whether such a mechanism should exist at all.

The state’s own executive-branch signing message makes the intended architecture even clearer. Governor Newsom described AB 1043 as creating a system in which parents who are the main user of a device can configure the device to inform application developers of a child’s age. The signing message also acknowledged that the bill does not fit all product categories well, including streaming services and video game developers, and urged the Legislature to pass follow-up legislation in 2026 before the law’s January 1, 2027 effective date. This matters because it confirms, in an official state document, that AB 1043 is understood as a device-level age-verification and age-signaling framework aimed at disclosure to applications. ([Official signing message](https://www.gov.ca.gov/wp-content/uploads/2025/10/AB-1043-Signing-Message.pdf))

#### Colorado SB 26-051

Colorado SB26-051 is closely associated with the same implementation pressure. It follows the OS-layer age-attestation model and appears alongside California AB-1043 in current discussions as a parallel driver for age-related account and API work. ([Official bill page](https://leg.colorado.gov/bills/sb26-051))

Within the scope of this project, it reinforces the concern that these mechanisms are not being proposed as isolated experiments, but as responses to a growing compliance pattern. That pattern matters because it encourages projects to think in terms of implementation pathways rather than categorical refusal.

### App-store mandates

These laws target the application distribution layer, pressuring app-store providers, account systems, and developers to implement age verification, parental consent mechanisms, and age-gating for content and downloads. They represent a different technical insertion point but are part of the same broader surveillance and control trajectory.

#### Alabama HB 161

Enacted in February 2026, Alabama HB161 requires mobile app store providers to implement age verification and parental consent systems. While its immediate target is the mobile app ecosystem, it is part of the same family of pressure. ([LegiScan](https://legiscan.com/AL/text/HB161/id/3357012))

This law matters to the project because it shows the spread of the pattern to the app store and account layer. Key provisions include requiring app stores to verify a user's age category and obtain verifiable parental consent for minors, establishing a precedent for building verification and gating systems directly into software distribution channels.

#### Louisiana HB 570 / Act 481

This enacted Louisiana law regulates app stores and developers around minors’ app use, age-category data, and parental consent. ([Official bill page](https://www.legis.la.gov/Legis/BillInfo.aspx?i=248616))

Like the Alabama law, it demonstrates how the policy pressure is expanding to control the application distribution layer, reinforcing the need for this project to track mandates beyond the core operating system.

#### Utah HB 498

This bill amends Utah's App Store Accountability Act, adding requirements around pre-installed applications and app-store/provider duties in the same family of measures. ([Official enrolled bill](https://le.utah.gov/Session/2026/bills/enrolled/HB0498.pdf))

Its relevance is in showing the iterative tightening of app-store-layer regulation, confirming this as a durable and evolving pressure point.

#### Texas SB 2420

Texas enacted this app-store accountability model, but its enforcement was preliminarily blocked by a federal court. ([Official bill text](https://capitol.texas.gov/tlodocs/89R/billtext/pdf/SB02420E.pdf), [Reuters](https://www.reuters.com/legal/government/us-judge-blocks-texas-app-store-age-law-meant-protect-children-2025-12-23/))

It belongs in the dossier as an example of both the legislative spread and the potential for legal challenges to interrupt enforcement.

#### Florida SB 1722

This filed bill is an example of the App Store Accountability Act model, requiring app-store age verification, parent-linked minor accounts, and parental consent. ([Official bill page](https://www.flsenate.gov/Session/Bill/2026/1722))

It serves as evidence that the app-store mandate model is not contained to a few states but is an active template for new legislation.

#### Arizona HB 2920

This introduced bill uses the same app-store age category data, parental consent, and developer duties model seen in other states. ([Official bill text](https://www.azleg.gov/legtext/57leg/2R/bills/hb2920p.pdf))

Its presence in the dossier confirms the geographic spread and persistence of this legislative pattern.

## Other jurisdictions

### Brazil Lei 15.211/2025

Brazil Lei 15.211/2025 belongs in this document because the project scope is not limited to one jurisdiction. The project is intended to document state pressure that attempts to normalize surveillance or classification mechanisms in free software distributions, wherever it appears.

As the dossier grows, this document must preserve a structured record of how different laws or proposals pressure technical systems and how those pressures differ across jurisdictions. This ensures the project remains a global resource, not a U.S.-centric one.

## EU Chat Control and related policy pushes

The broader policy context includes EU Chat Control and related "lawful-access" initiatives. These are important to this project because they show a recurring pattern: child-safety or law-enforcement rhetoric is used to normalize technical mechanisms for inspection, classification, access, or logging.

In March 2026, the European Parliament voted to extend the interim ePrivacy derogation allowing voluntary CSAM detection and reporting until 3 August 2027. At the same time, Parliament’s current line has been widely described as a rejection of untargeted mass scanning of private communications, emphasizing targeted, proportionate, and judicially authorized measures instead. Reports also indicate that Parliament’s current line would keep end-to-end encrypted communications outside scope. This represents a meaningful setback for indiscriminate “Chat Control” proposals, but it is not the end of the wider legislative fight, as the permanent legislative regime remains under negotiation between the EU's institutions. ([European Parliament](https://www.europarl.europa.eu/news/en/press-room/20260306IPR37531/child-sexual-abuse-online-support-for-extending-rules-until-august-2027), [TechRadar](https://www.techradar.com/vpn/vpn-privacy-security/chat-control-eu-parliament-said-no-to-big-tech-mass-surveillance-of-your-chats-but-the-battle-for-privacy-isnt-done))

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
