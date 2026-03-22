# Tracker

Back to the front page: [README.md](README.md)

## Purpose

This document is the operational evidence index for OSS Anti Surveillance.

It records the currently known components, repositories, issues, pull requests, merge requests, status, and why each item matters. It is the main working index for current implementation activity. Policy-driver entries are included as a watchlist to provide context for technical work but are not automatically active Linux implementation targets.

For legal and policy background, see [LAWS.md](LAWS.md). For the architecture map, see [STACK.md](STACK.md). For component descriptions, see [REPO-TARGETS.md](REPO-TARGETS.md). For removal strategy, see [REVERSIONS/README.md](REVERSIONS/README.md).

## Status labels

The tracker uses the following labels.

- discussion: public discussion exists, but no concrete code path is yet confirmed here
- draft: a draft implementation or draft pull request is visible
- active implementation: live code work is underway
- merged: the change has merged upstream
- closed unmerged: the change was closed without being merged, often after discussion or review
- downstream inherited: a downstream package or distribution is inheriting or integrating the change
- downstream stripped: a downstream package has removed or disabled the change
- reverted: the change has been explicitly reverted
- watchlist: not yet a confirmed implementation target, but worth monitoring

## Current evidence index

### Linux implementation targets

#### Shared upstream / common infrastructure

| Component | Repository | Item | Status | Why it matters | Downstream implications |
| --- | --- | --- | --- | --- | --- |
| systemd | [systemd/systemd](https://github.com/systemd/systemd) | [PR #40954](https://github.com/systemd/systemd/pull/40954) | merged | Adds `birthDate` to JSON user records; the storage substrate is no longer hypothetical and has merged upstream | Creates an upstream identity-data substrate that downstreams may inherit unless actively stripped; raises urgency for containment and increases risk of follow-on consumption |
| systemd | [systemd/systemd](https://github.com/systemd/systemd) | [Issue #40974](https://github.com/systemd/systemd/issues/40974) | closed unmerged | Closed as not planned; maintainers indicated birthDate remains preferred and ageGroup should live elsewhere via a service | Rejects one schema variant in systemd userdb, but leaves the broader service-based age-verification path open |
| systemd | [systemd/systemd](https://github.com/systemd/systemd) | [PR #41179](https://github.com/systemd/systemd/pull/41179) | closed unmerged | Direct upstream attempt to revert the merged `birthDate` field. The maintainer response explicitly defended the change as an optional schema field rather than a policy engine, making the current upstream rationale explicit. | Clarifies the upstream position that critics and downstream packagers must now rebut if they oppose the field’s continued normalization and spread. |
| xdg-desktop-portal | [flatpak/xdg-desktop-portal](https://github.com/flatpak/xdg-desktop-portal) | [PR #1922](https://github.com/flatpak/xdg-desktop-portal/pull/1922) | draft | App-facing portal/API normalization point for age-related querying | Makes the mechanism easier to standardize across desktop environments and applications |
| AccountsService | [accountsservice/accountsservice](https://gitlab.freedesktop.org/accountsservice/accountsservice) | [MR !176](https://gitlab.freedesktop.org/accountsservice/accountsservice/-/merge_requests/176) | discussion | Referenced by related work as a storage and D-Bus layer for `BirthDate` | Represents a likely account metadata layer in the wider stack |

#### Distribution / desktop-specific integrations

| Component | Repository | Item | Status | Why it matters | Downstream implications |
| --- | --- | --- | --- | --- | --- |
| Ubuntu desktop provisioning | [canonical/ubuntu-desktop-provision](https://github.com/canonical/ubuntu-desktop-provision) | [PR #1338](https://github.com/canonical/ubuntu-desktop-provision/pull/1338) | closed unmerged | Closed unmerged after discussion; linked to the related implementation path in #1339 | Shows that implementation paths can be interrupted before merge |
| Ubuntu desktop provisioning | [canonical/ubuntu-desktop-provision](https://github.com/canonical/ubuntu-desktop-provision) | [PR #1339](https://github.com/canonical/ubuntu-desktop-provision/pull/1339) | closed unmerged | Closed unmerged after public objections and internal review | Demonstrates that downstream integration is not inevitable and can be halted before merge |
| Archinstall | [archlinux/archinstall](https://github.com/archlinux/archinstall) | [PR #4290](https://github.com/archlinux/archinstall/pull/4290) | active implementation | Adds a required birth date field during user creation and writes it into userdb | Demonstrates installer-level normalization in a major distro tool |
| elementary settings-useraccounts | [elementary/settings-useraccounts](https://github.com/elementary/settings-useraccounts) | [Issue #260](https://github.com/elementary/settings-useraccounts/issues/260) | discussion | Explicitly frames age-related account setup work as California-law compliance | Shows pressure reaching desktop account-management UI |
| elementary settings-useraccounts | [elementary/settings-useraccounts](https://github.com/elementary/settings-useraccounts) | [PR #270](https://github.com/elementary/settings-useraccounts/pull/270) | draft | Implements age declaration UI in a desktop account-management component | Demonstrates distro/desktop integration of age declaration concepts |
| elementary portals | [elementary/portals](https://github.com/elementary/portals) | [Issue #173](https://github.com/elementary/portals/issues/173) | discussion | Proposes account portal work in a user-information exposure layer | Creates a portal-level integration point in elementary OS |
| elementary portals | [elementary/portals](https://github.com/elementary/portals) | [PR #180](https://github.com/elementary/portals/pull/180) | active implementation | Open multi-commit implementation of the account portal linked to issue #173 | Shows live portal-layer work in a desktop-specific integration path |

### Prototype / reference implementations

| Component | Repository | Item | Status | Why it matters | Downstream implications |
| --- | --- | --- | --- | --- | --- |
| ageverifyd | [outerheaven199X/ageverifyd](https://github.com/outerheaven199X/ageverifyd) | [README](https://github.com/outerheaven199X/ageverifyd) | active implementation | Standalone daemon implementing the proposed Linux `org.freedesktop.AgeVerification1` D-Bus model | Provides reusable plumbing for normalization of age-signaling across Linux distributions and app ecosystems, lowering the barrier to adoption |

### BSD / Unix-like integrations

| Component | Repository | Item | Status | Why it matters | Downstream implications |
| --- | --- | --- | --- | --- | --- |
| MidnightBSD | [MidnightBSD Draft](https://docs.google.com/document/d/1_NKq0bpN1pOrMpHePuilJY7saXqXqhss6LwPTC6nSto/edit) | [Mailing list post](https://lists.freedesktop.org/archives/xdg/2026-March/014777.html) | active implementation | Explicit BSD-side implementation path for age/DOB storage, installer (`bsdinstall`) and user creation (`adduser`) integration, helper tools (`aged`, `agectl`), and package manager (`mport`) / ACL-based access control | Proves the surveillance architecture is spreading beyond the Linux ecosystem into other free Unix-like operating systems |

### Interface / discussion artifacts

| Source | Item | Status | Why it matters | Downstream implications |
| --- | --- | --- | --- | --- |
| freedesktop.org | [xdg-list `AgeVerification1` proposal](https://lists.freedesktop.org/archives/xdg/2026-March/014765.html) | discussion | The primary proposal artifact for the `org.freedesktop.AgeVerification1` D-Bus interface | Represents the starting point for the D-Bus/portal implementation vector |
| freedesktop.org | [Age Assurance Key Considerations](https://lists.freedesktop.org/archives/xdg/2026-March/014794.html) | discussion | Explores legal and technical contradictions around age-bracket storage, jurisdiction handling, and the practical consequences of conflicting state requirements | Shows the implementation discussion expanding beyond interface shape into jurisdiction logic, data-retention questions, and operational compliance assumptions |
| freedesktop.org | [File-based protocol proposal](https://lists.freedesktop.org/archives/xdg/2026-March/014802.html) | discussion | Proposes a file/filesystem-based age attestation model as a more secure alternative to D-Bus | Shows the design space has expanded to include non-D-Bus, anti-circumvention-focused models |
| freedesktop.org | [LSM / xattr implementation proposal](https://lists.freedesktop.org/archives/xdg/2026-March/014779.html) | discussion | Proposes using Linux Security Modules and extended attributes for enforcement | Indicates the problem is expanding to kernel-level and filesystem-level enforcement mechanisms |

### Policy drivers and legal watchlist

| Layer | Jurisdiction / Bill | Status | Why it matters | Downstream implications |
| --- | --- | --- | --- | --- |
| OS-layer | [California AB 1043](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260AB1043) | watchlist | Direct OS-layer mandate relevant to Linux distribution architecture | Key driver for current implementation work in systemd and desktop portals |
| OS-layer | [Colorado SB 26-051](https://leg.colorado.gov/bills/sb26-051) | watchlist | Follows the same OS-layer age-attestation and signaling model as CA | Reinforces the compliance pattern driving OS-level technical changes |
| App-store | [Alabama HB 161](https://legiscan.com/AL/text/HB161/id/3357012) | watchlist | Enacted law showing the pattern spreading to the app-store distribution layer | Establishes precedent for distribution-channel mandates, though not yet a Linux target |
| App-store | [Louisiana HB 570 / Act 481](https://www.legis.la.gov/Legis/BillInfo.aspx?i=248616) | watchlist | Enacted law targeting app stores, reinforcing the app-store layer pattern | Not currently a Linux OS implementation target |
| App-store | [Utah HB 498](https://le.utah.gov/Session/2026/bills/enrolled/HB0498.pdf) | watchlist | App-store accountability model | Not currently a Linux OS implementation target |
| App-store | [Texas SB 2420](https://capitol.texas.gov/tlodocs/89R/billtext/pdf/SB02420E.pdf) | watchlist | Enacted but blocked; app-store model | Not currently a Linux OS implementation target |
| App-store | [Florida SB 1722](https://www.flsenate.gov/Session/Bill/2026/1722) | watchlist | App-store accountability model | Not currently a Linux OS implementation target |
| App-store | [Arizona HB 2920](https://www.azleg.gov/legtext/57leg/2R/bills/hb2920p.pdf) | watchlist | App-store accountability model | Not currently a Linux OS implementation target |

## Primary tracked sources

### Implementation targets and proposals

- [systemd PR #40954](https://github.com/systemd/systemd/pull/40954)
- [systemd Issue #40974](https://github.com/systemd/systemd/issues/40974)
- [systemd PR #41179](https://github.com/systemd/systemd/pull/41179)
- [xdg-desktop-portal PR #1922](https://github.com/flatpak/xdg-desktop-portal/pull/1922)
- [ubuntu-desktop-provision PR #1338](https://github.com/canonical/ubuntu-desktop-provision/pull/1338)
- [ubuntu-desktop-provision PR #1339](https://github.com/canonical/ubuntu-desktop-provision/pull/1339)
- [Archinstall PR #4290](https://github.com/archlinux/archinstall/pull/4290)
- [AccountsService MR !176](https://gitlab.freedesktop.org/accountsservice/accountsservice/-/merge_requests/176)
- [elementary/settings-useraccounts Issue #260](https://github.com/elementary/settings-useraccounts/issues/260)
- [elementary/settings-useraccounts PR #270](https://github.com/elementary/settings-useraccounts/pull/270)
- [elementary/portals Issue #173](https://github.com/elementary/portals/issues/173)
- [elementary/portals PR #180](https://github.com/elementary/portals/pull/180)
- [outerheaven199X/ageverifyd](https://github.com/outerheaven199X/ageverifyd)
- [MidnightBSD Age Verification Draft](https://docs.google.com/document/d/1_NKq0bpN1pOrMpHePuilJY7saXqXqhss6LwPTC6nSto/edit)
- [freedesktop.org `AgeVerification1` proposal thread](https://lists.freedesktop.org/archives/xdg/2026-March/014765.html)
- [freedesktop.org Age Assurance Key Considerations thread](https://lists.freedesktop.org/archives/xdg/2026-March/014794.html)
- [freedesktop.org File-based proposal thread](https://lists.freedesktop.org/archives/xdg/2026-March/014802.html)
- [freedesktop.org LSM / xattr proposal thread](https://lists.freedesktop.org/archives/xdg/2026-March/014779.html)

### Policy drivers and legal watchlist

- [California AB 1043](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260AB1043)
- [Colorado SB 26-051](https://leg.colorado.gov/bills/sb26-051)
- [Alabama HB 161](https://legiscan.com/AL/text/HB161/id/3357012)
- [Louisiana HB 570 / Act 481](https://www.legis.la.gov/Legis/BillInfo.aspx?i=248616)
- [Utah HB 498](https://le.utah.gov/Session/2026/bills/enrolled/HB0498.pdf)
- [Texas SB 2420](https://capitol.texas.gov/tlodocs/89R/billtext/pdf/SB02420E.pdf)
- [Florida SB 1722](https://www.flsenate.gov/Session/Bill/2026/1722)
- [Arizona HB 2920](https://www.azleg.gov/legtext/57leg/2R/bills/hb2920p.pdf)

## Immediate observations

The current evidence shows an implementation path that moves through several layers:

- provisioning and installer flows
- account metadata services and user records
- portal or API exposure
- application or service consumption

That propagation path is why isolated review of one patch is not enough. The project should be read as a stack.

See [STACK.md](STACK.md) for the architecture map.

## How to update this document

Each tracker entry should remain concise, factual, and linked. Use [CONTRIBUTING.md](CONTRIBUTING.md) for contribution rules and [REPO-TARGETS.md](REPO-TARGETS.md) for component-specific technical descriptions.

Every named item in this document should point to its direct primary upstream source using Markdown links.

## See also

- [README.md](README.md)
- [LAWS.md](LAWS.md)
- [STACK.md](STACK.md)
- [REPO-TARGETS.md](REPO-TARGETS.md)
- [REVERSIONS/README.md](REVERSIONS/README.md)
- [CONTRIBUTING.md](CONTRIBUTING.md)
