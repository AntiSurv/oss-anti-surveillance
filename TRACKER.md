# Tracker

Back to the front page: [README.md](README.md)

## Purpose

This document is the operational evidence index for OSS Anti Surveillance.

It records the currently known components, repositories, issues, pull requests, merge requests, status, and why each item matters. It is the main working index for current implementation activity.

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

| Component | Repository | Item | Status | Why it matters | Downstream implications |
| --- | --- | --- | --- | --- | --- |
| systemd | [systemd/systemd](https://github.com/systemd/systemd) | [PR #40954](https://github.com/systemd/systemd/pull/40954) | active implementation | Adds `birthDate` to JSON user records for age-verification-related use, normalizing age-related metadata in a core userdb path | Creates a core storage substrate that downstreams may consume or inherit |
| systemd | [systemd/systemd](https://github.com/systemd/systemd) | [Issue #40974](https://github.com/systemd/systemd/issues/40974) | closed unmerged | Closed as not planned; maintainers indicated birthDate remains preferred and ageGroup should live elsewhere via a service | Rejects one schema variant in systemd userdb, but leaves the broader service-based age-verification path open |
| xdg-desktop-portal | [flatpak/xdg-desktop-portal](https://github.com/flatpak/xdg-desktop-portal) | [PR #1922](https://github.com/flatpak/xdg-desktop-portal/pull/1922) | draft | App-facing portal/API normalization point for age-related querying | Makes the mechanism easier to standardize across desktop environments and applications |
| Ubuntu desktop provisioning | [canonical/ubuntu-desktop-provision](https://github.com/canonical/ubuntu-desktop-provision) | [PR #1338](https://github.com/canonical/ubuntu-desktop-provision/pull/1338) | closed unmerged | Closed unmerged after discussion; linked to the related implementation path in #1339 | Shows that implementation paths can be interrupted before merge |
| Ubuntu desktop provisioning | [canonical/ubuntu-desktop-provision](https://github.com/canonical/ubuntu-desktop-provision) | [PR #1339](https://github.com/canonical/ubuntu-desktop-provision/pull/1339) | closed unmerged | Closed unmerged after public objections and internal review | Demonstrates that downstream integration is not inevitable and can be halted before merge |
| Archinstall | [archlinux/archinstall](https://github.com/archlinux/archinstall) | [PR #4290](https://github.com/archlinux/archinstall/pull/4290) | active implementation | Adds a required birth date field during user creation and writes it into userdb | Demonstrates installer-level normalization in a major distro tool |
| AccountsService | [accountsservice/accountsservice](https://gitlab.freedesktop.org/accountsservice/accountsservice) | [MR !176](https://gitlab.freedesktop.org/accountsservice/accountsservice/-/merge_requests/176) | discussion | Referenced by related work as a storage and D-Bus layer for `BirthDate` | Represents a likely account metadata layer in the wider stack |
| Mobile App Ecosystem | N/A (Legislation) | [Alabama HB161 (2026)](https://legiscan.com/AL/bill/HB161/2026) | watchlist | Policy driver for verification/gating in app stores; shows pattern spreading to ecosystem layer | Establishes precedent for distribution-channel mandates, though not currently impacting Linux stack |

## Primary source links

These are the primary upstream items currently tracked in this project:

- [systemd PR #40954](https://github.com/systemd/systemd/pull/40954)
- [systemd Issue #40974](https://github.com/systemd/systemd/issues/40974)
- [xdg-desktop-portal PR #1922](https://github.com/flatpak/xdg-desktop-portal/pull/1922)
- [ubuntu-desktop-provision PR #1338](https://github.com/canonical/ubuntu-desktop-provision/pull/1338)
- [ubuntu-desktop-provision PR #1339](https://github.com/canonical/ubuntu-desktop-provision/pull/1339)
- [Archinstall PR #4290](https://github.com/archlinux/archinstall/pull/4290)
- [AccountsService MR !176](https://gitlab.freedesktop.org/accountsservice/accountsservice/-/merge_requests/176)

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
