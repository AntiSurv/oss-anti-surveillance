# Reversions and Downstream Removal

Back to the front page: [README.md](../README.md)

## Purpose

This document defines the project’s approach to stripping, reverting, or otherwise removing surveillance-related changes from downstream packages and related distribution components.

For the live evidence index, see [TRACKER.md](../TRACKER.md). For current component targets, see [REPO-TARGETS.md](../REPO-TARGETS.md).

## Why this document exists

Documentation alone is not enough. If upstream projects merge surveillance-related functionality, downstream distributions may still need to remove it from their packages. This document exists to keep that strategy visible and organized.

The project’s position is not that these mechanisms should be tolerated if they are packaged carefully. The project’s position is that they should not exist in free software distributions at all. Downstream removal matters because upstream projects may still choose to merge them.

## Core position

If upstream merges surveillance mechanisms, downstream distributions should strip them from their packages rather than inherit them silently.

Refusal does not end at authorship. A distribution cannot claim clean hands simply because it did not write the original patch itself. If a package ships the mechanism, the mechanism is still present. That is why downstream stripping, revert paths, and maintained deltas are part of this project’s core strategy.

No implementation path is acceptable. No passive inheritance path is acceptable either.

## Current strategy

The project’s current strategy is staged.

### 1. Track

First, record the exact component, repository, issue, PR, MR, and status in [TRACKER.md](../TRACKER.md).

### 2. Map dependencies

Second, determine where the change sits in the stack and what depends on it. Use [STACK.md](../STACK.md) and [REPO-TARGETS.md](../REPO-TARGETS.md) to understand the propagation path.

### 3. Prepare downstream removal

Third, once a change becomes concrete enough, record the likely downstream stripping or revert path. This may include:

- excluding a patch from package builds
- reverting an upstream commit in a downstream packaging branch
- disabling a feature path in packaging
- maintaining a clean downstream delta until upstream reverses course

### 4. Escalate only when necessary

Full distro forks are expensive. The preferred order is:

- reject upstream where possible
- strip downstream if upstream merges the change
- maintain package-level deltas where practical
- escalate to broader forks only when package-level maintenance becomes insufficient

This sequence is about efficiency, not concession. Package-level removal is usually the fastest way to keep a distribution clean while preserving usability and reach.

## Red lines for downstream packaging

The following should be treated as red-line candidates for downstream stripping if merged upstream:

- age-related fields added to provisioning or installation flows
- age-related fields added to account metadata or user record schemas
- portal or API exposure for age signaling or age-bracket queries
- client-side scanning or device-side inspection primitives
- other surveillance, classification, or policy-enforcement mechanisms added under coercive legal framing

These categories are tracked in [TRACKER.md](../TRACKER.md) and explained structurally in [STACK.md](../STACK.md).

## Planned contents

As the project grows, this directory contains component-specific reversal notes and downstream stripping strategies.

Currently active reversal documentation:
- [systemd: revert `birthDate` userdb merge](systemd/README.md)

## Current status

The project tracks concrete removal strategies for merged components. As specific removal notes mature, they are added to this directory and linked from [TRACKER.md](../TRACKER.md).

## See also

- [README.md](../README.md)
- [TRACKER.md](../TRACKER.md)
- [STACK.md](../STACK.md)
- [REPO-TARGETS.md](../REPO-TARGETS.md)
- [CONTRIBUTING.md](../CONTRIBUTING.md)
