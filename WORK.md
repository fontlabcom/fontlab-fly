---
this_file: WORK.md
---

# Current round — documentation theme migration

Migrated the documentation site to fly-january 0.1.1 with FontLab chrome and
the menu label `Fly`. The Python 3.13 strict build completed without warnings.
An independent rebuild matched all 53 files in `docs/`. All 38 documentation
tests and 35 Python 3.11 arm64 package tests passed. Browser checks are with
the orchestrator. Private Pages publication remains held.

## Issue 255 post-release reconciliation

## 2026-11-14 — Functional work order documented

Updated AGENTS, PLAN and TODO to prioritize useful functional changes and compatible package boundaries, with detailed testing deferred. Existing backlog and prior records are retained. Documentation preservation and policy consistency were checked; no runtime, installed or native checks ran in this documentation-only pass.

Next: reconcile affected Script and example setup with matching Fly/provider imports and explicit child paths; use focused alias/identity checks before the detailed installed/native pass.

[fontlab-fly v1.3.1](https://github.com/fontlabcom/fontlab-fly/releases/tag/v1.3.1) is qualified at `733566ef47938c173bd00c3e6a7ca59c75e77ff8`.

Complete ten-alias source teaching is reviewed, including the remote metrics skill. All nine consumer migrations passed the final source re-audit.

35 source tests, 38 documentation tests and exact 48-file containing-source rebuild parity pass. Both genuine wheel and actual-sdist ordinary cohorts contain 28 compatible packages; all 5 installed Fly payload files match. The combined provider checks preserve 25 canonical alias/metadata pairs and 4 Pens exports.

The source, artifact, ordinary external-install, release and download gates above are verified. This round reconciles their progress records after release; it changes no runtime source, installer, dependency declaration, generated documentation or immutable release asset.

Remaining: After explicit D43 recovery and admission, verify all ten aliases, both import forms, canonical metadata and child imports from the released wheel/sdist in FontLab arm64 Python 3.11; record host build, hashes and loaded paths.

D43 native acceptance remains held and unproved. Issue 123 remains paused; existing private Pages holds and every unrelated acceptance task remain in PLAN/TODO. Prior WORK bytes are retained exactly in the private external delivery ledger, SHA256 `961b20661de46adac7055eb24761063a3fce748a707882d6239ad52536ebe6f0`.
