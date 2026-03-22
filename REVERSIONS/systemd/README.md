# systemd: revert `birthDate` userdb merge

Back to Reversions index: [README.md](../README.md)

## Purpose

This document explains the reversal path for the upstream systemd change that added the `birthDate` field to JSON user records. It provides downstream maintainers and technically capable users with a reproducible workflow to strip this surveillance mechanism from their packages.

## Upstream references

- **Pull Request:** [systemd/systemd#40954](https://github.com/systemd/systemd/pull/40954)
- **Merge Commit:** [`acb6624fa19ddd68f9433fb0838db119fe18c3ed`](https://github.com/systemd/systemd/commit/acb6624fa19ddd68f9433fb0838db119fe18c3ed)
- **Context:** This merge introduced age-related fields into the core `systemd` userdb layer, crossing a defined project red line by formalizing a storage substrate for OS-level age signaling.

## Canonical upstream revert command

Because the target is a merge commit (combining two parent commits into the mainline), the canonical command requires the `-m 1` flag. Parent 1 represents the pre-merge mainline.

```bash
git revert -m 1 acb6624fa19ddd68f9433fb0838db119fe18c3ed
```

## Reverse-engineering notes

The merge of PR #40954 touches multiple subsystems. A complete revert must address all of them to ensure clean compilation and test passage. The affected areas include:

- `docs/USER_RECORD.md`
- `man/homectl.xml`
- `src/home/homectl.c`
- `src/shared/user-record.c`
- `src/shared/user-record.h`
- `src/sysupdate/sysupdate-resource.c`
- Related test files and time utility code (`src/basic/time-util.c`, `src/basic/time-util.h`, `src/test/test-time-util.c`, `src/test/test-user-record.c`)

## Reversal workflow

The following workflow is designed as public-facing, reproducible guidance for downstream packagers. It explicitly creates a localized branch rather than assuming internal state.

*NOTE: requires a configured `~/.gitconfig`*

```bash
git clone https://github.com/systemd/systemd.git
cd systemd
git checkout -b revert-birthdate
git revert -m 1 acb6624fa19ddd68f9433fb0838db119fe18c3ed
git show --stat
git diff HEAD~1..HEAD
git format-patch -1 HEAD
```

This sequence generates a clean `.patch` file that reverses the upstream introduction of the `birthDate` user record fields.

## Downstream packaging note

A pre-existing, verified downstream patch file has been generated using the workflow above and is hosted in this repository at:
`patches/0001-Revert-userdb-add-birthDate-field-to-JSON-user-recor.patch`

This exported patch is the candidate downstream patch for integration into systems like Debian or Ubuntu (e.g., via `debian/patches/`). Downstream maintainers do not need to wait for upstream Debian action before applying this reversal; however, as upstream systemd evolves, this patch may eventually require refreshing against newer release tags.

## Use of the AntiSurv/systemd fork

The separate `AntiSurv/systemd` GitHub repository fork may be used as a technical staging area. It can host the `revert-birthdate` branch to provide CI testing, build validation, and easier downstream patch generation. 

While the fork is a useful technical support artifact, **OSS Anti Surveillance remains the canonical documentation home.** The fork complements, but does not replace, the records and instructions contained in this document.
