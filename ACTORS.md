# Actors and Policy Ecosystem

Back to the front page: [README.md](README.md)

## Purpose

This document records the organizations, model-bill producers, advocacy groups, and public-support ecosystem behind OS-level age verification laws and related app-store mandates. It exists to document the policy-production layer that shapes the legal and technical landscape this project tracks.

For legal texts, see [LAWS.md](LAWS.md). For technical implementation status, see [TRACKER.md](TRACKER.md).

## Why this file exists

The legal text and technical implementation of surveillance mechanisms do not arise in a vacuum. They are often preceded by model legislation, technical whitepapers, and coordinated advocacy. This document provides a dedicated, evidence-based home for that context, ensuring that `LAWS.md` can remain focused on final legal text and `TRACKER.md` on technical artifacts.

Documenting this layer is critical to understanding how a policy idea is developed, standardized, and promoted before it becomes law.

## Core actors and ecosystem

### International Centre for Missing & Exploited Children (ICMEC)

ICMEC is a key actor in the production of model legislation for OS-level age verification. The organization has publicly hosted a policy and technical toolkit for a model called the "Digital Age Assurance Act."

This toolkit includes:

- A [model bill](https://cdn.icmec.org/wp-content/uploads/2024/10/Digital-Age-Assurance-Act-2024.pdf) proposing a standardized legal framework for states.
- A [technical whitepaper](https://cdn.icmec.org/wp-content/uploads/2024/10/Digital-Age-Assurance-Act-Technical-Whitepaper-FINAL-Feb-07-2025.pdf) that advocates for device-based age assurance, where the operating system verifies a user's age once, stores it locally, and provides an age-bracket signal to applications via an API.
- A [constitutional analysis](https://cdn.icmec.org/wp-content/uploads/2024/10/The-Digital-Age-Assurance-Act-Constitutional-Analysis-02-07-2025-FINAL.docx.pdf) intended to defend the model against legal challenges.

This work matters because it provides direct evidence that the OS-level model being implemented in laws like California's AB 1043 is not an isolated improvisation, but part of a pre-existing, reusable policy and technical template.

### California AB 1043 support ecosystem

California's enacted AB 1043, which requires OS providers and app stores to provide an age-signal mechanism, received public support from major technology companies.

According to a [press release](https://a14.asmdc.org/press-releases/20250909-google-meta-among-tech-leaders-and-child-advocates-voicing-support-wicks) from bill author Assemblymember Buffy Wicks, the following companies voiced support for the bill:

- Google
- Meta
- Snap
- OpenAI

This matters because it confirms that major platform actors, including those this project tracks in other contexts, publicly endorsed the OS-level signal model in California, lending significant weight to its passage and normalization. The [enacted bill text](https://leginfo.legislature.ca.gov/faces/billVersionsCompareClient.xhtml?bill_id=202520260AB1043) aligns with this model, requiring an interface for users to provide their birth date or age and for applications to request a "signal" from the OS or app store.

### Template ecosystem context

While this project focuses on verifiable primary sources, it is important to note the broader context of competing and complementary legislative templates. Evidence suggests at least two distinct models are being promoted in U.S. states:

1.  **OS-layer mandates** (e.g., California AB 1043), which place the implementation burden on operating system providers.
2.  **App-store mandates** (e.g., Texas SB 2420), which place the burden on app store providers like Apple and Google.

The Texas app-store law was [preliminarily blocked by a federal court](https://www.reuters.com/legal/government/us-judge-blocks-texas-app-store-age-law-meant-protect-children-2025-12-23/) before taking effect, showing that legal outcomes are not uniform across different template families. This project tracks both models because they are part of the same overall push toward age-verification infrastructure.

## Research leads requiring further verification

This section contains claims and synthesis from publicly available analysis that require further independent, primary-source verification before being promoted into core dossier claims.

- The existence of a coordinated, two-template legislative strategy funded by distinct actors with specific financial motivations (e.g., COPPA liability shifting).
- The full funding sources and organizational relationships behind advocacy coalitions like the Digital Childhood Alliance.

These are treated as research hypotheses, not verified facts, until supported by direct evidence such as financial disclosures, lobbying records, or official documents.

## See also

- [README.md](README.md)
- [LAWS.md](LAWS.md)
- [TRACKER.md](TRACKER.md)
- [CONTRIBUTING.md](CONTRIBUTING.md)
