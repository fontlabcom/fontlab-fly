---
this_file: WORK.md
---

# Release and planning housekeeping

The v1.3.9 tag and remote main both pointed to `84d1c76` at verification.
The Tests and Release workflows passed for that commit. Both GitHub release
files matched the PyPI hashes, and the sdist contained the tagged installer
byte for byte.

The release workflow uses the `pypi` environment and GitHub OIDC. The pinned
publisher passed actionlint. All 36 package tests and 38 documentation tests
passed locally. Owner actions and native checks are listed in [TODO.md](TODO.md).
