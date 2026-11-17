---
this_file: PLAN.md
---

## Functional work order — 2026-11-14

Keep all ten aliases lazy and preserve canonical provider identity, metadata and explicit child imports. Resolve consumer setup and import failures together with App, Pens and the affected Scripts or examples, without introducing mandatory reverse dependencies.

Use small smoke checks and focused regressions for changed behavior and package boundaries. Keep the existing detailed acceptance tasks for a later testing pass; mandatory delivery hooks and current holds remain in force.

## Issue 255 remaining native acceptance

After explicit D43 recovery and admission, verify all ten aliases, both import forms, canonical metadata and child imports from the released wheel/sdist in FontLab arm64 Python 3.11; record host build, hashes and loaded paths. Source, genuine artifact, ordinary external-install and release/download qualification for v1.3.1 is recorded in CHANGELOG. Existing private Pages and Issue 123 holds remain.

## Publication hold

Private Pages configuration, requests, deployment and live `main:/docs` acceptance stay held until the owner lifts the publication hold. Source, build and test work continues; main commits rebuild `docs/` through the repository workflow.

# Forward plan

Issue 123 implementation remains paused; its acceptance backlog is preserved, not resumed. Keep qualified candidates distinct from canonical source, ordinary installed artifacts, native acceptance and publication.

## Native facade acceptance

Keep Fly a small lazy namespace for ten canonical modules. Preserve module identity, import metadata and child imports on FontLab's arm64 Python 3.11 runtime. At native acceptance, test the final wheel and source distribution in FontLab. Check all ten aliases, both import forms, canonical metadata and child imports. Record host version, artifact hashes and loaded source paths.

Run adapted Feature scripts on owned fonts through `fly.ap.fontui.feature_blocks` and explicit `fly.ap` submodule imports. Retain Apply/Undo/Redo/save/reopen evidence in the consuming repositories. Existing import proofs are offline only.

Use the workspace owned-fixture runner. Canonical editable installs can shadow worktree code. Do not install into FontLab for these checks. Historical native alias receipts do not qualify later provider refactors.

## Provider and distribution boundaries

Shared UI, general script helpers and active-font feature helpers belong in App. Fontport owns fontParts/UFO support; Glyport owns Glyphs.app compatibility. Fly adds aliases, not wrappers. Complete installed FontLab native qualification for the released cohort; ordinary external artifact qualification is recorded in CHANGELOG. Keep the detailed open items in TODO.

## Development checks

Use the explicit arm64 Python 3.11 source-test recipe in README. `./test.sh` runs `uv run --no-sync python -m pytest` and requires a prepared environment with pytest; it does not install dependencies.

## Review, integration and cleanup

Use the detailed open tasks in [TODO.md](TODO.md) as the acceptance checklist. Complete one scoped MVP, then run the exact repository checks and unchanged 80% gate for each complete changed production module. Keep source, genuine artifacts, ordinary origins and native behavior separate. Obtain independent review before a milestone commit/push and verify the actual remote head. Reconcile concurrent source and all callers before main integration. Preserve recovery/unique work and fresh owner/worktree attachments before obsolete branch/file cleanup. Update TODO/PLAN and record only scoped verified results in CHANGELOG. Do not drive the owner's FontLab, install into its user folder or publish a site from this proposal.
