# Repository Targets

Back to the front page: [README.md](README.md)

## Purpose

This document lists the current technical targets in scope and explains why each matters within the Linux stack.

For live status, pull requests, and issues, see [TRACKER.md](TRACKER.md). For the stack model, see [STACK.md](STACK.md).

## Current targets

### systemd

Repository: [systemd/systemd](https://github.com/systemd/systemd)

Role in the stack: systemd is currently relevant because userdb is being used as a possible storage layer for age-related user data. That makes it a high-impact normalization point inside core system infrastructure.

Why it matters: if age-related attributes become part of the expected user record schema, downstream projects may begin assuming their presence.

Current upstream references:

- [PR #40954](https://github.com/systemd/systemd/pull/40954)
- [Issue #40974](https://github.com/systemd/systemd/issues/40974)

### xdg-desktop-portal

Repository: [flatpak/xdg-desktop-portal](https://github.com/flatpak/xdg-desktop-portal)

Role in the stack: xdg-desktop-portal is relevant because it can provide a standard application-facing interface. That makes it the normalization layer between stored data and application consumption.

Why it matters: if a portal-level interface for age signaling is standardized, the mechanism becomes easier to spread across desktop environments and applications.

Current upstream references:

- [PR #1922](https://github.com/flatpak/xdg-desktop-portal/pull/1922)

### AccountsService

Repository: [accountsservice/accountsservice](https://gitlab.freedesktop.org/accountsservice/accountsservice)

Role in the stack: AccountsService is relevant as an account metadata and D-Bus layer for user properties. It is a natural place for desktop-oriented account data to accumulate and be exposed.

Why it matters: if age-related account properties are normalized here, downstream provisioning and desktop flows can inherit them more easily.

Current upstream references:

- [MR !176](https://gitlab.freedesktop.org/accountsservice/accountsservice/-/merge_requests/176)

### Ubuntu desktop provisioning

Repository: [canonical/ubuntu-desktop-provision](https://github.com/canonical/ubuntu-desktop-provision)

Role in the stack: Ubuntu desktop provisioning is relevant because it represents a downstream integration point where collection of age-related data can be introduced directly into setup flows.

Why it matters: it shows how a distribution can wire together upstream metadata and API work into actual user onboarding.

Current upstream references:

- [PR #1338](https://github.com/canonical/ubuntu-desktop-provision/pull/1338)
- [PR #1339](https://github.com/canonical/ubuntu-desktop-provision/pull/1339)

### Archinstall

Repository: [archlinux/archinstall](https://github.com/archlinux/archinstall)

Role in the stack: Archinstall is relevant because it demonstrates installer-level normalization of age-related account data.

Why it matters: it shows that the collection and storage step can be pushed directly into installation tooling, not just higher-level desktop flows.

Current upstream references:

- [PR #4290](https://github.com/archlinux/archinstall/pull/4290)

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
