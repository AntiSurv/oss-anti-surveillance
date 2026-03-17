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

### Digital Childhood Alliance (DCA)

The Digital Childhood Alliance is a key advocacy coalition that publicly promotes app-store accountability legislation. It has been described as a coalition of over 50 child advocacy organizations and has testified in favor of these bills across multiple states.

This actor matters because it represents a major advocacy vehicle for the app-store legislative track. Public reporting by outlets such as Bloomberg has indicated that Meta Platforms, Inc. is a funder of the DCA. The precise legal and registration structure of the DCA is a subject of ongoing external research.

### California AB 1043 support ecosystem

California's enacted AB 1043, which requires OS providers and app stores to provide an age-signal mechanism, received public support from major technology companies.

According to a [press release](https://a14.asmdc.org/press-releases/20250909-google-meta-among-tech-leaders-and-child-advocates-voicing-support-wicks) from bill author Assemblymember Buffy Wicks, the following companies voiced support for the bill:

- Google
- Meta
- Snap
- OpenAI

This matters because it confirms that major platform actors, including those this project tracks in other contexts, publicly endorsed the OS-level signal model in California, lending significant weight to its passage and normalization. The [enacted bill text](https://leginfo.legislature.ca.gov/faces/billVersionsCompareClient.xhtml?bill_id=202520260AB1043) aligns with this model, requiring an interface for users to provide their birth date or age and for applications to request a "signal" from the OS or app store.

## Legislative template ecosystems

The legal pressure for OS-level and app-store-level age verification is not arising from random, isolated bills. Evidence points to at least two distinct, recurring legislative models being promoted by different advocacy ecosystems.

### OS-layer age assurance mandates

This model, exemplified by California's AB-1043, places the compliance burden on the operating system provider. The core architecture involves the OS collecting a user's age and providing a standardized signal for applications to consume. This approach is promoted by organizations like the International Centre for Missing & Exploited Children (ICMEC).

### App-store accountability mandates

This model, seen in laws like the one passed in Louisiana, places the compliance burden on app store providers like Apple and Google. The core architecture involves the app store gating downloads and in-app purchases based on verifiable parental consent. This approach is promoted by coalitions such as the Digital Childhood Alliance.

## Scientific and technical opposition

Scientific and technical opposition to age-verification mandates has also become more explicit. An [open letter](https://csa-scientist-open-letter.org/ageverif-Feb2026) signed by hundreds of researchers warns that age-assurance initiatives may cause more harm than good, can create censorship-enabling infrastructure, are frequently easy to bypass, and would impose major privacy costs. The letter is especially relevant to this project because it explicitly warns against browser- and OS-level enforcement models that would give software manufacturers greater control over what users can access, and it calls for a moratorium until scientific consensus exists on feasibility, benefits, and harms.

See also: [Politico coverage](https://www.politico.eu/article/age-check-social-media-scientist-warning/) and [Reason coverage](https://reason.com/2026/03/04/computer-scientists-caution-against-internet-age-verification-mandates/).

This matters because it confirms opposition is not merely political or activist, but comes from technical and scientific experts and directly addresses the kinds of OS-level enforcement models this project tracks.

## Related external research

This project is aware of external investigations into the policy and lobbying ecosystem surrounding these legislative efforts. The TBOTE Project, for example, provides deep-dive research into lobbying records, funding structures, and actor relationships.

- **TBOTE Project Home:** `https://tboteproject.com/`
- **TBOTE Research Repository:** `https://tboteproject.com/git/hekate/attestation-findings`

OSS Anti Surveillance may use such projects for discovery and contextual analysis, but will continue to anchor its own core dossier claims in direct legal, technical, and primary-source evidence, per the project's contribution standards.

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
