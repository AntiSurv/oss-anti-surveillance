# Repository Targets

Back to the front page: [README.md](README.md)

## Purpose

This document lists the current technical targets in scope and explains why each matters. These targets are often linked to broader legal drivers which are mapped in detail in [LAWS.md](LAWS.md). It now tracks both Linux-centered implementation targets and broader free Unix-like integration paths where the same surveillance architecture is being proposed.

For live status, pull requests, and issues, see [TRACKER.md](TRACKER.md). For the stack model, see [STACK.md](STACK.md).

## Current targets

### Linux: Shared infrastructure targets

#### systemd

Repository: [systemd/systemd](https://github.com/systemd/systemd)

Role in the stack: systemd is currently relevant because userdb is now an upstream merged storage layer for age-related user data. That makes it a high-impact normalization point inside core system infrastructure.

Why it matters: now that age-related attributes are part of the expected user record schema, downstream projects may begin assuming their presence. This increases the risk of propagation into downstream consumers and adjacent components.

Current upstream references:

- [PR #40954](https://github.com/systemd/systemd/pull/40954)
- [Issue #40974](https://github.com/systemd/systemd/issues/40974)
- [PR #41179](https://github.com/systemd/systemd/pull/41179)

A direct upstream revert attempt was later submitted as PR #41179 and closed. In that discussion, maintainers defended the merged `birthDate` field as optional schema standardization rather than a policy engine. This is relevant because it makes the current upstream posture explicit and clarifies the rationale that critics of the field must now address.

#### xdg-desktop-portal

Repository: [flatpak/xdg-desktop-portal](https://github.com/flatpak/xdg-desktop-portal)

Role in the stack: xdg-desktop-portal is relevant because it can provide a standard application-facing interface. That makes it the normalization layer between stored data and application consumption.

Why it matters: if a portal-level interface for age signaling is standardized, the mechanism becomes easier to spread across desktop environments and applications.

Current upstream references:

- [PR #1922](https://github.com/flatpak/xdg-desktop-portal/pull/1922)

#### AccountsService

Repository: [accountsservice/accountsservice](https://gitlab.freedesktop.org/accountsservice/accountsservice)

Role in the stack: AccountsService is relevant because MR !176 would turn it into a persistent birth-date storage and retrieval layer for desktop account data, with PolicyKit-gated D-Bus methods and `libaccountsservice` client-side support. It bridges AccountsService keyfile storage for non-homed users and JSON user-record data for homed / JSON-backed users.

Why it matters: This is not merely a passive schema extension. It makes AccountsService a standard desktop account-data service for age-related personal data, increasing the likelihood that settings panels, account UIs, and other desktop consumers will normalize birth-date handling as part of the broader age-verification architecture. Operationally, MR !176 is an advanced, near-merge implementation risk.

Current upstream references:

- [MR !176](https://gitlab.freedesktop.org/accountsservice/accountsservice/-/merge_requests/176)

### Linux: Distribution / desktop integration targets

#### Ubuntu desktop provisioning

Repository: [canonical/ubuntu-desktop-provision](https://github.com/canonical/ubuntu-desktop-provision)

Role in the stack: Ubuntu desktop provisioning is relevant because it represents a downstream integration point where collection of age-related data can be introduced directly into setup flows.

Why it matters: it shows how a distribution can wire together upstream metadata and API work into actual user onboarding.

Current upstream references:

- [PR #1338](https://github.com/canonical/ubuntu-desktop-provision/pull/1338)
- [PR #1339](https://github.com/canonical/ubuntu-desktop-provision/pull/1339)

#### Archinstall

Repository: [archlinux/archinstall](https://github.com/archlinux/archinstall)

Role in the stack: Archinstall is relevant because it demonstrates installer-level normalization of age-related account data.

Why it matters: it shows that the collection and storage step can be pushed directly into installation tooling, not just higher-level desktop flows.

Current upstream references:

- [PR #4290](https://github.com/archlinux/archinstall/pull/4290)

#### elementary/settings-useraccounts

Repository: [elementary/settings-useraccounts](https://github.com/elementary/settings-useraccounts)

Role in the stack: This component is relevant because it sits in the desktop account-management and user-declaration layer. It is a direct integration point for UI related to age collection during account setup.

Why it matters: This shows the surveillance and classification pattern spreading to another desktop-specific ecosystem, demonstrating that the pressure is not isolated to one or two distributions.

Current upstream references:

- [Issue #260](https://github.com/elementary/settings-useraccounts/issues/260)
- [PR #270](https://github.com/elementary/settings-useraccounts/pull/270)

#### elementary/portals

Repository: [elementary/portals](https://github.com/elementary/portals)

Role in the stack: This component is relevant because it provides a desktop-specific portal and user-information exposure layer. It can act as the bridge between stored user data and applications that consume it.

Why it matters: This shows a desktop-specific implementation of the portal layer, which is a critical part of the architectural propagation path for normalizing surveillance mechanisms.

Current upstream references:

- [Issue #173](https://github.com/elementary/portals/issues/173)
- [PR #180](https://github.com/elementary/portals/pull/180)

### Reference implementations / prototypes

#### ageverifyd

Repository: [outerheaven199X/ageverifyd](https://github.com/outerheaven199X/ageverifyd)

Role in the stack: ageverifyd acts as a reference implementation of a standalone OS-level daemon for age verification and bracket storage.

Why it matters: It demonstrates that the architecture is moving beyond theoretical discussion into ready-to-use plumbing (implementing `org.freedesktop.AgeVerification1`), designed specifically to help distributions and app stores comply with legislative mandates like California AB-1043.

Current upstream references:

- [Repository README](https://github.com/outerheaven199X/ageverifyd)

### BSD / Unix-like integration targets

#### MidnightBSD age verification (`aged`)

Repository: [MidnightBSD/src](https://github.com/MidnightBSD/src)

Role in the stack: This is a merged, base-system implementation of an OS-level age verification architecture for a BSD-based operating system. It includes a standalone daemon (`aged`), an admin tool (`agectl`), per-user age/DOB storage, a Unix socket for queries, and `rc` startup integration.

Why it matters: This is critical evidence that the surveillance architecture is not a Linux-specific problem but a pattern spreading to other free Unix-like operating systems. Unlike discussion drafts, this is a merged upstream artifact. Post-merge commits have expanded the subsystem to include age-based group membership changes, showing a drift from passive signaling toward active policy enforcement.

Current upstream references:

- [PR #302](https://github.com/MidnightBSD/src/pull/302) (Initial merge)
- [`usr.sbin/aged` commit history](https://github.com/MidnightBSD/src/commits/master/usr.sbin/aged) (Post-merge expansion)
- [Historical design draft](https://docs.google.com/document/d/1_NKq0bpN1pOrMpHePuilJY7saXqXqhss6LwPTC6nSto/edit)

## Watchlist concept

This project may later add a watchlist section for adjacent components that are not yet confirmed active targets but are technically positioned to become relevant. Such items should appear in [TRACKER.md](TRACKER.md) only when there is evidence.

## How this file differs from the tracker

This document explains why each component matters technically. It is not the place for detailed status logging or repeated PR summaries.

Use [TRACKER.md](TRACKER.md) for the operational index, live status, and downstream implications.

Every named upstream item in this document should be linked directly to its primary source.

## See also

- [README.md](README.md)
- [TRACKER.md](TRACKER.md)
- [STACK.md](STACK.md)
- [LAWS.md](LAWS.md)
- [CONTRIBUTING.md](CONTRIBUTING.md)
