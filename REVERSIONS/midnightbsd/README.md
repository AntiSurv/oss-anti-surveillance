# MidnightBSD: Untested Guide to Remove the `aged` Subsystem

Back to Reversions index: [README.md](../README.md)

## Purpose

This document records a theoretical downstream rollback path for the merged MidnightBSD `aged` subsystem. It exists because the upstream merge is a high-signal event demonstrating the spread of surveillance architecture to non-Linux free operating systems.

The instructions herein are an **untested theoretical guide** derived from upstream commit history. They have **not been validated** against a live MidnightBSD build and should not be represented as a verified, working procedure.

## Evidence Basis

The `aged` subsystem was merged into the MidnightBSD `master` branch on 9 March 2026. This introduced a daemon, a control utility, per-user age/DOB storage, and base-system integration. Post-merge commits later expanded the subsystem with default assumptions for system accounts and logic for age-based group membership, showing a drift toward policy enforcement.

- **Initial Subsystem Merge:** [MidnightBSD/src#302](https://github.com/MidnightBSD/src/pull/302)
- **Post-Merge Expansion:** [`usr.sbin/aged` commit history](https://github.com/MidnightBSD/src/commits/master/usr.sbin/aged)

This guide documents what can be inferred from that public history, not a certified build result.

## Untested Theoretical Guidance

The following steps are an **untested theoretical guide**. They are provided to give downstream maintainers and developers a starting point for a proper revert. They may require significant adjustment to account for ancillary files outside `usr.sbin/aged`, build system integration, `rc` scripts, and manpages. This guide is not a substitute for careful, build-verified testing.

## Scope of Rollback: Substrate vs. Escalation

A clean removal should distinguish between two layers of changes, each with a distinct architectural role.

### 1. Post-Merge Escalation Commits

These commits introduced enforcement-oriented logic after the initial subsystem was merged. Reverting them first represents an immediate containment strategy that strips the most aggressive behavior.

- `0cacaff` — Assume 18+ for root user if undefined.
- `b1cdf99` — Set a default of 18+ for service accounts.
- `b883117` — Add/remove users from groups based on age.
- `15790a1` — Move group-membership logic into `agectl` as `aged` does not run as root.

### 2. Initial Merged Substrate

These commits represent the core `aged` subsystem introduced in PR #302.

- `6e4e5df` — `Create an age verification daemon called aged to query and store age verification data. (#302)`
- `7da7413` — `Use syslog logging for aged(8) (#304)`

A full rollback would need to revert this set, along with any related changes to build files, `rc` scripts, or manpages included in the original PR.

## Untested Rollback Strategy

A two-tier rollback model is recommended.

### Tier A: Immediate Containment (Lower Risk)

First, revert the post-merge escalation commits. This removes the policy-enforcement layer while leaving the storage/query substrate in place, providing a smaller and likely safer initial patch.

```bash
# UNTESTED - FOR GUIDANCE ONLY
git revert 15790a1 b883117 b1cdf99 0cacaff
```

### Tier B: Full Subsystem Removal (Higher Risk)

After containing the enforcement logic, a full removal would target the initial substrate. Due to the nature of the multi-commit merge in PR #302, a simple revert of one commit may be insufficient. A careful analysis of the PR's full commit set and file changes is required to create a clean revert patch.

The PR's file list includes changes in:
- `etc/rc.d/`
- `lib/libc/`
- `man/`
- `sbin/`
- `share/`
- `usr.sbin/`

A full removal requires reversing changes across all these areas.

## Capability-Based Validation Checklist

A successful rollback should be verified by capability removal, not merely by a successful `git revert` command. After applying any patches, confirm that:

- [ ] The `aged` daemon is no longer built or started at boot.
- [ ] The `agectl` utility is no longer built or installed.
- [ ] The `/var/run/aged/aged.sock` Unix socket is no longer created.
- [ ] The `/var/db/aged/aged.db` SQLite database is no longer created or used.
- [ ] No user-facing or programmatic interface for setting or querying age/DOB remains.
- [ ] No age-based group membership logic is present in the system.
- [ ] The `aged` `rc` script and manpages have been removed.

## Known Uncertainties

- This rollback path is incomplete until validated on a live MidnightBSD source tree.
- The exact set of commits to revert for a full subsystem removal may be more complex than listed here.
- This guide is included because the upstream signal is high, not because the platform is strategically central. Further refinement depends on community members performing and reporting a verified revert and build test.
