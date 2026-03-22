# Patch Notice and Licensing Context

This directory contains the downstream candidate patch for reverting the `birthDate` userdb merge in `systemd`.

## Provenance
- The patch `0001-Revert-userdb-add-birthDate-field-to-JSON-user-recor.patch` is derived directly from upstream `systemd/systemd` source code.
- It explicitly reverts merge commit `acb6624fa19ddd68f9433fb0838db119fe18c3ed`.
- Upstream repository URL: https://github.com/systemd/systemd

## Licensing
This patch is derived from upstream `systemd` source changes. The `systemd` project utilizes per-file SPDX license identifiers. 

Unless otherwise noted, the project sources are licensed under **LGPL-2.1-or-later**. 

Downstream users and packagers must consult the upstream file headers and the upstream `LICENSES/README.md` for the exact licensing of affected files. This notice provides context for the patch artifact but does not alter or replace the upstream licensing declarations.
