# Technical Architecture

Back to the front page: [README.md](README.md)

## Purpose

This document describes the architecture path through which surveillance, classification, or policy-enforcement mechanisms can propagate across a Linux distribution stack.

For the live evidence index, see [TRACKER.md](TRACKER.md). For component-specific descriptions, see [REPO-TARGETS.md](REPO-TARGETS.md).

## Core propagation path

The currently visible path is:

Installer or provisioning flow
Account metadata service or user record storage
Portal or standard application-facing API
Applications, app stores, or services

This path matters because a surveillance mechanism does not need to appear in one dramatic component to become real. It can spread incrementally across several layers until the overall system functions as a policy-enforcement endpoint.

## Regulatory insertion points

Different laws and policy proposals target different layers of the technology stack. The project tracks these together because they all push toward classification, verification, gating, inspection, or control, but it is important to distinguish the technical insertion points.

- **OS layer**
  This includes provisioning flows, account metadata services, user records, and operating-system-level APIs. Mandates at this layer pressure the core distribution.

- **App-store layer**
  This includes store accounts, parental-consent infrastructure, developer-facing age/consent data, and the software distribution channel itself.

- **Service / app-consumption layer**
  This includes application-side enforcement, download gating, and launch-time age handling by individual applications that consume data from the layers above.

## Layer-by-layer explanation

### 1. Installer or provisioning flow

This is where user-facing data collection can become normalized. If age-related data is requested during setup, the implementation burden has already entered the user onboarding path.

Examples currently relevant to this layer include Ubuntu desktop provisioning and Archinstall.

### 2. Account metadata service or user records

Once age-related data is stored in account metadata or user records, the mechanism becomes persistent. This layer is especially important because it turns a transient question into a durable system attribute.

Examples currently relevant to this layer include AccountsService and systemd userdb.

### 3. Portal or standard API

Once a portal or application-facing interface exists, the mechanism becomes easier for applications and services to consume. This is the normalization layer where the functionality becomes reusable across the desktop ecosystem.

The current relevant example is xdg-desktop-portal.

### 4. Applications, app stores, or services

Once the previous layers exist, application and service consumption becomes much easier. This is why portal and metadata work should not be dismissed as merely preparatory. They create the substrate.

## Why this architecture matters

The project’s central concern is not just one patch, one file, or one package. The real concern is the stack.

A system can become a surveillance or classification platform through incremental layering:

- collection
- storage
- exposure
- consumption

That is why the project documents related components together rather than as isolated incidents.

## Strategic implication

The highest-leverage intervention points are usually the standardization and normalization layers, especially account metadata services, user record systems, and application-facing portals. If those layers reject the category of functionality, downstream integration becomes much harder.

For the current component list, see [REPO-TARGETS.md](REPO-TARGETS.md). For current status and activity, see [TRACKER.md](TRACKER.md).

## See also

- [README.md](README.md)
- [TRACKER.md](TRACKER.md)
- [REPO-TARGETS.md](REPO-TARGETS.md)
- [LAWS.md](LAWS.md)
- [REVERSIONS/README.md](REVERSIONS/README.md)
