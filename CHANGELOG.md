---
this_file: CHANGELOG.md
---

## Unreleased

- The site uses fly-january 0.4.0 or later (remote theme assets).
- The docs now accept fly-january 0.3.0 or later and lock reproducible builds to 0.3.0.

- Site now uses the fly-january 0.2.1 theme (chrome: fontlab).
- Pinned the PyPI publishing action. Owner setup for the `fontlab-fly` PyPI project: confirm its GitHub trusted publisher is `fontlabcom/fontlab-fly`, workflow `release.yml`, environment `pypi`.
- Issue 271 installer integration and release checks passed at `84d1c76` (v1.3.9). Tests run `44414601076` and Release run `44414716294` succeeded. Both GitHub distributions matched their PyPI hashes, and the source archive contained the tagged installer byte for byte.
- Verified Fly’s ten-alias source routing and all nine consumer migrations in v1.3.1 (`733566ef`). Fly’s runtime, examples, migration tool and skills match that revision at `37fd45d`.
- All six provider and migration cases currently deselected in CI passed locally against the sibling checkouts in the 36-test suite at base `37fd45d`. Future reruns depend on provider or consumer changes.

## 2026-11-18 — Issue 271 source archive installer

Include the unchanged root `install.vfpy` in the explicit sdist input list.
The genuine archive regression verifies its exact root bytes and the complete
allowed top-level payload. The new assertion failed before the input fix; all
36 source tests, six focused packaging tests and wheel/sdist builds now pass.
Released archive and native execution qualification remain separate.


## 2026-11-18 — Issue 271 installer source alignment

The generated installer matches the reviewed Instamix 1.0.18 template: it requires
conflict preflight support, selects compatible local wheels and reports completed
work before an installation failure. Exact reviewed-template byte parity and import-sentinel/wheel-order smoke checks pass. No repository-specific installer test was selected.
Consumer integration, released archives and native execution remain separate checks.

## 2026-11-17 — Installer stub from instamix 1.0.15 (Issue 259 follow-ups)

- `install.vfpy` is now the stub from fontlab-python-instamix 1.0.15. It replaces an
  installed instamix older than 1.0.13 and puts the old copy back if the upgrade
  fails; linked checkouts and local builds are kept. A download that fails for
  lack of root certificates (FontLab 9 for macOS) is retried with the system curl.

## 2026-11-17 — Issue 258 task cleanup

- Marked the TODO row for the six CI-deselected tests as done and low priority (the row stays because `tests/test_workflow.py` requires the node ids in TODO.md): done twice, see the 2026-11-12 entry "Deselected provider tests rerun against current siblings" (Fly `3763ccc`, App `2fc2f07`, Glyport `10b6975`, Fontport `1c8e1ca`; 5 passed, full suite 30 passed) and the 2026-11-11 entry (Fly `c2c8af5`, 30 passed). CI still cannot run them because the siblings are private.
- Merged the duplicate wheel/sdist verification row into the Issue 255 row; the exit 79 busy-fence note is kept there.
- Documentation only; no source, runtime or native change.

## 1.3.2 (2026-11-16)

- `install.vfpy` is now the short fontlab-instamix stub. It installs
  fontlab-instamix from PyPI when it is missing, then installs this checkout from
  its `[tool.fontlab-install]` table. The large legacy installer is gone.
- AGENTS.md names a scratch folder instead of a private volume path.
- README describes the stub install.
## 2026-11-14 — Functional work order documented

- Added the owner's functional-progress-first guidance and repository-specific priorities, including cross-package compatibility and a later detailed testing pass. Existing mandatory hooks, holds and unfinished work remain in force.
- This change updates guidance and planning only; it establishes no new runtime, installed, native or release result.

## 2026-11-13 — Issue 255 verified release qualification

- [fontlab-fly v1.3.1](https://github.com/fontlabcom/fontlab-fly/releases/tag/v1.3.1) is released at `733566ef47938c173bd00c3e6a7ca59c75e77ff8`. Reviewed main/tag delivery, applicable CI and actual downloads match the qualified artifacts.
- Complete ten-alias source teaching is reviewed, including the remote metrics skill. All nine consumer migrations passed the final source re-audit.
- 35 source tests, 38 documentation tests and exact 48-file containing-source rebuild parity pass. Both genuine wheel and actual-sdist ordinary cohorts contain 28 compatible packages; all 5 installed Fly payload files match. The combined provider checks preserve 25 canonical alias/metadata pairs and 4 Pens exports.
- Ordinary external installation is qualified; installed FontLab/native acceptance remains unproved under D43.

## 2026-11-13 — Issue 255 residual remote teaching

The decorated Remopy metrics example selects the native command bridge through
`from fly import pr`; the external Remopy transport remains direct. Current
agent guidance now counts all ten lazy aliases. No runtime alias or dependency
metadata changed.

A structural code-fence regression fails on the direct provider import and
passes on the Fly route. The complete arm64 Python 3.11.14 source suite passes
35 tests (baseline 34); Ruff 0.14.10 passes the documented scope. The exact-lock
external docs preview passes its strict build and 38 tests; a second clean build
has exact 48-file parity. This is a dirty-source preview, not containing-commit
output, new distribution or native evidence. Product generated docs and shared
installer bytes remain unchanged.

## 2026-11-13 — Pens lazy alias

- Added `fly.pens` → `fontlab_pens` and runtime requirement `fontlab-python-pens>=1.0.0`. Fly now exposes ten exact canonical module aliases; App, Fontport and Glyport retain their existing targets. No provider APIs are copied or wrapped.
- Added Pens to import identity, laziness, child metadata, missing-provider, wheel metadata and installed stub-provider checks. The real Pens source test checks every `__all__` export and RecordingPen/TransformPen behavior; its private sibling case is explicitly deselected in CI and retained in TODO.
- Updated current README, dependency, guide and agent-skill references, including Pens-before-Fly installation order. The native smoke already iterates every alias. Dated historical evidence is unchanged.
- Source suite with all four real provider checkouts: 34 passed, 94% Fly coverage; Ruff passed. Hash-locked strict docs build and 38 docs tests passed. Genuine candidate wheel and sdist each installed with real provider wheels: 23 compatible packages, exact four-provider routing/metadata and all 70 Pens exports with a transformed recording check. Independent spec/quality review passed. Final released-artifact and native acceptance remain separate open checks.

## 2026-11-12 — D46 documentation pass (Issue 250)

- Landed this session, all on `main`: M-10 install sync (`0a5cdcd`), the deselected-provider-tests rerun record (`2c872c5`), the `install.vfpy` sync with the App installer (`b50a14f`, App `5cac0d6`, Issue 254). Latest tag is `v1.2.5`.
- PLAN no longer carries the stale Issue 233/230 paragraphs. TODO adds the Issue 254 native check; the deselected-tests row stays open because only the host-free subset runs in CI. WORK.md was already a short pointer to the archived log and is unchanged.
- No code changed.

## 2026-11-12 — install.vfpy matches the App's installer, with Extensions bundle support (Issue 254)

- `install.vfpy` is now byte-identical to `fontlab-fontlabapp/install.vfpy` (pushed in App `5cac0d6`).
  The new code places `[tool.fontlab-install] extensions` bundles; this repository declares none, so
  installs behave as before. `tools/check_install_copies.py` in the App compares the copies by sha256.

## 2026-11-12 - Deselected provider tests rerun against current siblings (Issue 250)

- The five tests the `Tests` workflow deselects (three real-provider alias checks, two App path-migration checks) all
  passed again locally with the siblings at their current remote mains: App `2fc2f07`, Glyport `10b6975`, Fontport
  `1c8e1ca`, Fly `3763ccc` (`-v`: 5 passed, none skipped). The full suite gave 30 passed. Run on arm64 Python 3.11.14 with
  pytest 8.4.2, `PYTHONPATH=src`. Verification only; no source change.

## 2026-11-12 — Installer: unreachable blocked skip removed (Issue 250, review M-10)

- `install.vfpy` synced byte-identically from App (sha256 `2eb71691…` → `bbe8104e…`):
  `remove_old_dist` drops the `path.name in blocked` skip. Every blocked top-level
  name is also held, and a non-empty held refuses before anything is deleted, so the
  skip never ran. App's `tests/test_install_superseded.py` pins that invariant.

## 2026-11-11 — Deselected provider tests run with real siblings

- The five tests the `Tests` workflow deselects (three real-provider alias checks, two App path-migration checks) all passed locally against fresh clones of App `f05d87b`, Glyport `a7cc367` and Fontport `8b9a0bc`: `PYTHONPATH=src uv run --no-project --with pytest==8.4.2 python -m pytest -q tests` gave 30 passed, 0 skipped, on Fly `c2c8af5`.
- No source change. The siblings are private, so CI still cannot run them; the TODO row stays open with this evidence.

## 2026-11-11 — Host-free pytest workflow

- New `.github/workflows/tests.yml` (push/PR to main, read-only, no secrets, one job, the docs.yml action pins, pytest 8.4.2) runs the host-free tests and fails on any skip. Five tests are deselected by exact node ID because they need private sibling checkouts; `tests/test_workflow.py` pins that every deselected ID exists and is named in TODO.md.
- TODO: the cohort row merged into the artifacts row; deselected tests listed.

## 2026-11-11 — Built sdist and wheel contents pinned, installed wheel exercised host-free (Issue 250)

- New `tests/test_artifacts.py` (4 cases) builds the sdist and wheel with `uv build`: the wheel ships only `fly/` and its dist-info, and declares exactly the six provider dependencies with name `fontlab-fly` and `Apache-2.0`. The sdist top-level entries equal the `only-include` set plus `PKG-INFO` and the `.gitignore` that hatchling always adds, with no `src_docs/` or `docs/`, and contains `src/fly/__init__.py`, LICENSE, NOTICE and the tests.
- The wheel is installed with `--no-deps` into a fresh `uv venv` and probed from outside the repository against stub providers: `fly` loads from site-packages, stays lazy, and all nine aliases resolve to the exact stub modules.
- Mutants each fail the file: extra wheel package (`examples`), `docs` added to the sdist, a provider dependency dropped, `gp` retargeted, licence changed to MIT. (Adding `tools` to the wheel packages does not change the wheel, so it is not a mutant.)
- Source suite with App, Glyport and Fontport sibling sources: 28 passed. Without them two existing `tests/test_migrate_app_paths.py` cases fail on a missing App checkout, as before this change.
- The sdist check is an equality, so dropping a declared entry such as `PLAN.md` from `only-include` fails it; dropping `README.md` does not, because hatchling always includes the readme named in the metadata.
- Fly CI (the Documentation workflow) does not run pytest, so these tests run locally and in the pre-push hook, not in CI. They need `uv` on `PATH`.
- Network: `uv build` needs the registry for its build backend (hatchling>=1.27, hatch-vcs) unless the uv cache already holds them. With `UV_OFFLINE=1` and an empty cache it fails ("hatchling was not found in the cache"); with the populated shared cache it builds offline. The tests need the same: `uv` on `PATH` and a populated cache or network.
- Gate: `.metaswarm/quality.sh coverage` with fresh clones of App `be468da`, Glyport `df86604` and Fontport `7a83958` (their `origin/main`) as siblings: 28 passed, 0 changed production modules, "PASS (tests only)". `graph.sh` compare against `origin/main`: `VERDICT: CLEAN` (three changed files, all tests or docs).
- Not established: the genuine ordinary installed cohort with the real provider wheels, and the same check inside FontLab (TODO rows kept open).

## 2026-11-11 — Package aliases verified against the real provider heads (Issue 250)

- `tests/test_aliases.py` already pinned the nine-alias table (`test_alias_table_when_compared_to_reviewed_providers_then_exactly_nine_and_equal`) and canonical identity, but only against stand-in modules and temporary packages. New `test_package_alias_when_real_provider_checkout_present_then_resolves_to_it` imports `fly.ap`, `fly.gp` and `fly.fp` in an isolated process against the sibling App, Glyport and Fontport source checkouts and asserts the alias is the canonical module from that checkout, and that a real child (`kerning.batch`, `affine`, `errors`; host-free and dependency-free) keeps canonical identity. It skips when a sibling is absent.
- Run against App 7f96170, Glyport df86604 and Fontport 63cc935 (their `origin/main`): 3 passed. Mutant: pointing `ap` at `fontlab_glyport` fails it.
- Closes the TODO row "Keep every public lazy alias pointed at its reviewed provider and verify import identity after provider migrations". Installed-host checks stay in the wheel/sdist rows.

## 2026-11-11 — install.vfpy synced to the App WP11A installer (Issue 250)

- `install.vfpy` is now byte-identical to fontlab-fontlabapp 79f7485 (WP11A): it records file hashes in `install.log`, removes only superseded files whose current hash matches the logged hash, keeps edited ones and reports them, refuses entries with `..` or outside the data folder and any unowned entry in the old RECORD, and supports `FONTLAB_INSTALL_DRY_RUN`. Verify with `tools/check_install_copies.py` in the App repository. The native reinstall check is owner-run and stays open in the App TODO.

## 2026-11-11 — alias table pinned (Issue 250)

- `tests/test_aliases.py`: pins `fly.ALIASES` and `__all__` to the nine reviewed providers, so a provider migration must change the table and the test together. TODO row "Keep every public lazy alias pointed at its reviewed provider" stays open: it is a standing check across provider migrations.

## 2026-11-10 — live font editing rule (Issue 250, D44)

- AGENTS.md: agents test and edit the font open in FontLab 9, starting from the Desktop VFJs, and may save them.

## 2026-11-10 — isolated graph guidance proposal

Prepare append-only AGENTS guidance for separate task-owned graph HOME and storage, ordinary-analysis scope and independently reviewed bounded recovery. Preserve existing integration rules and acceptance holds. This documentation proposal records no new runtime, test, native, integration or publication result.

## 2026-11-10 — Immutable-output repair delivered to main

- [Code 663a416d4](https://github.com/fontlabcom/fontlab-fly/commit/663a416d4a7a511754b1c752a601974d70c1298f) is independently accepted with six reviewed paths, ordinary sole-parent/nonforce main integration and complete 124-file committed-source recovery.
- The retained normal gate passes 20 source tests/0.79 s with zero selected production modules, without a new coverage claim. [Exact-source CI 42828775465](https://github.com/fontlabcom/fontlab-fly/actions/runs/42828775465) passes both 38-test jobs, original source epoch and immutable parity; all 48 docs remain exact.
- Retain genuine wheel `1.2.3.dev3+g663a416d4`, six RECORD rows/five hashes and exact legal bytes, without claiming ordinary installation/full provider/native acceptance. Declared TypeRig remains uninstalled.
- Move only verified correction/integration subwork to history. Private Pages, aliases, final wheel/sdist/full ordinary tuple, cleanup and native/history/owner/canonical gates stay open.

## 2026-11-10 — Qualify immutable docs output locally

- Require the declared output at HEAD, an exact sole source parent for a nonempty docs-only generated child, and the source commit's build epoch. Check parity against HEAD and include ignored untracked docs files.
- Preserve the existing publisher, race guards, builders, action pins and private Pages hold. Real Git regressions first exposed eight old-guard assertion failures here; the same ten scenarios now accept two valid states and reject eight invalid states without changing fixture state.
- The corrected unrestricted docs suite passed 38 tests; strict building preserved all 48 generated files. Ruff and actionlint passed. Retain the initial Ruff failure and the explicit `check=False` correction, which preserves expected adverse subprocess results.
- The arm64 Python 3.11 source suite passed 20 tests; a genuine precommit wheel was audited and retained, not installed. Independent combined review, graph analysis, normal main delivery, actual CI/generated qualification and native acceptance remain separate. Private publication remains held.

## 2026-11-10 — install.vfpy always reinstalls scripts and dependencies

- Every install copies all files from `Scripts/` afresh and replaces any file
  already at the same path. A symlinked script folder is replaced by a real
  folder; the link target is never written. A directory where a script file
  belongs is still refused.
- Required packages are installed on every run. Packages that no package
  index carries (the fontlab-* packages, pythonqtside) are installed from
  checkouts beside this one through their own `install.vfpy`, once per run
  and safe against cycles. uv receives every other requirement, so version
  ranges, markers and extras are enforced. Without uv, sibling checkouts are
  still installed and only the remaining missing requirements are reported.
- The installer is byte-identical across all eleven installer repositories.

## 2026-11-06 — Private Pages publication held by owner

- Keep both main-push builds, source epoch and complete generated-output parity;
  remove automatic private Pages requests and Pages write permission.
- Retain the tested request helper as dormant future/public-site support and
  state that this private site is not deployed. Source/build delivery continues.

## 2026-11-06 — Issue 233 pilot review fixes

- Propagate failed origin/main reads before classifying a successful stale head.
- Rebuild both source and generated commits with the original source timestamp,
  preserving complete output parity across UTC dates.
- Add actual unreachable/missing-main Git cases, cross-midnight generated-commit
  rebuild coverage and workflow epoch wiring checks. No product source changes.

## 2026-11-06 — Issue 233 documentation pilot candidate

- Add public installation, import/provider, development and licence guides with
  a ProperDocs/MaterialX/official FontLab theme build fixed to light mode.
- Generate `docs` from `src_docs/md` using `src_docs/mkdocs.yml`; preserve exact
  licence and NOTICE downloads and pin the complete docs dependency environment.
- Add every-main-push build, generated-output-only normal publication and an
  independent immutable-commit rebuild before an explicit branch-source Pages
  request. Reject staged foreign data, stale source, invalid Pages settings and
  failed pushes/API calls; retain the latest-default API race limitation.
- Add real local Git publishing tests and generated route/search/prefix/theme/
  privacy/attribution checks. Product source, dependency metadata and native
  acceptance are unchanged; remote Actions/Pages/live verification is pending.

## 2026-11-05 — independently approved documentation applied

[Task 2 final review](../verification/issue-230/task-2-fix2-review.md) records
SPEC PASS / QUALITY APPROVED. The [78-file application receipt](../verification/issue-230/task-2-apply.json)
includes this repository's six guides and preserves all 21 repository heads,
branches, indexes and non-selected diffs. This is applied documentation evidence,
not a new product test, installed artifact, native result or publication.

The complete earlier handoff/history below retains its proposal-stage statements
and dated source pins. Later review, application and delivery status belong in the
[live workspace ledger](../verification/issue-230/progress.md). Original future,
native, artifact and preservation contracts remain binding.

## 2026-11-05 — documentation reconciliation proposal

Prepared repository-specific organization, test and MVP/delivery guidance from current source/test configuration and retained Issue 207–211 evidence. Distinguished current canonical layout from qualified candidates, future plugin ownership and unfinished native/artifact gates. Preserved all prior work and changelog evidence; no runtime completion, installation or publication is claimed. Historical checked tasks now require receipt/current-scope reconciliation rather than being silently counted complete.

## 2026-11-05 — planning chronology reconciliation

The v0.2.0/0.2.1/0.2.2 migration and17-case source history is already recorded; it is removed from live planning. Nine-alias native/artifact and adapted Feature workflow requirements remain open. Historical passing results retain their dated source and acceptance scope in the entries above and original history below. This documentation change creates no new runtime acceptance.

---
this_file: CHANGELOG.md
---

# Verified changes

## 2026-11-10 — Issue 250 documentation round

- AGENTS.md describes the delegation, integration and release workflow.
- WORK.md reset to the current round; the earlier bytes are archived on the owner's workspace data volume, not public.

## 2026-11-03 — Issue 205 dependency floors

- Require App, Glyport and Fontport >=1.2.0 for their canonical module layouts.
  Align README minimums and dependency notes; Echopy, TypeRig and Pythonqtside
  requirements remain unchanged. The FontLab installer uses these project dependencies.

## 2026-11-03 — Issue 205 canonical module paths

- Teach canonical App domain paths and App ownership of feature helpers in
  the README, agent guidance, scripting skill and open acceptance tasks.
- Document the lazy public `fly.gp.GlyphsApp` API and offline backend binding.
- Reuse the reviewed path migration tool with boundary and idempotence tests.

## 2026-11-03 — installer options, licence and cleanup

- `install.vfpy` reads optional `[tool.fontlab-install]` keys: `name` (the distribution
  record), `packages` (`[]` installs scripts only) and `dependencies` (what FontLab needs,
  instead of `project.dependencies`). Symlinks inside `Scripts/` are not copied.
- Added agent skills in `skills/` (fontlab-setup, fontlab-remote, fontlab-scripting) and
  ship them in the sdist; the Remopy calls in fontlab-remote were run against FontLab 9.

## 2026-11-03 — install.vfpy fixes from runs inside FontLab 9

Verified by installing all nine packages inside FontLab 9 (Python 3.11.6, arm64).
- Dependencies with console scripts (glyphsLib, fontTools) failed: uv writes them to
  `site-packages/../../../bin`, which resolves through the venv link to the FontLab
  folder. `bin`, `share` and `include` there now link back into `.venv`.
- A failed install appends a `"failed"` record with the traceback and uv's output to
  `install.log`; List/Uninstall ignore failed records.
- Package records include `WHEEL`, so `uv pip check` accepts them.
- Scripts are copied file by file into FontLab's `Scripts` folder, from a package's
  `Scripts/` folder (exact case) and from folders listed in `[tool.fontlab-install] scripts`.
  Folders shared by several packages merge, e.g. two packages' `Scripts/Kerning`. The
  installer refuses to overwrite a file another package or the user put there; uninstall
  removes only its own files, their `.pyc`, and folders left empty. An older install's
  folder link (`Scripts/Aidus Code`) is replaced by copied files.
- `*.vfpyc` (FontLab's compiled `install.vfpy`) is ignored by Git.

## 2026-11-03 — install.vfpy creates FontLab's venv

FontLab's `python/3.11/site-packages` is now always a real folder; packages are
symlinked into it, so no `.pth` processing is needed. `install.vfpy` creates `.venv` with
uv from FontLab's exact Python version and processor type, and links the venv's
site-packages to FontLab's folder, so `uv pip install --python .venv/bin/python` installs
into FontLab. An older layout (FontLab's folder linked into `.venv`) is migrated.

## 2026-11-03 — reverse-domain extension id and install.log

`[tool.fontlab-install] id = "com.fontlab.fly"` names this extension. `install.vfpy` keeps
`Extensions/com.fontlab.fly/install.log` (JSON Lines; the last line lists every installed file),
puts copied code in `Extensions/com.fontlab.fly/lib/`, and adds Scripts > Extensions >
List Extensions and Uninstall com.fontlab.fly.

## 2026-11-03 — install.vfpy without uv

`install.vfpy` now needs only FontLab's Python. It asks FontLab for its data folder
(`flPreferences().dataPathDefault`), links a Git checkout or copies a plain folder into
`Extensions/`, and writes a `.pth` plus `.dist-info` into `python/3.11/site-packages`.
uv is used only to add missing dependencies. It never replaces folders it does not own.

## 2026-11-03 — release scripts

Added `build.sh` (uv build into dist/), `publish.sh` (`uv publish`; refuses a dirty
tree or an untagged HEAD) and `install.vfpy` (editable install into FontLab's venv
from inside FontLab). Version stays hatch-vcs from `vX.Y.Z` tags. Relaxed dev-only floors: `fontlab-glyport>=0.1.0`, `fontlab-fontport>=0.1.0`.
## 2026-11-03 — Issue 201 audit

- No file removed and no code changed: every alias target still exists (`echopy.*`, `typerig`,
  `PythonQt`, `fontlabapp`, `pythonqtside`, `fontlab_glyport`, `fontlab_fontport`); `fly.ap.history`
  and `fly.fp.feature_blocks` resolve in the issue-201 App and Fontport; nothing refers to
  `fontlab_fontport.ui`, Glyphs emulation or `fontlabapp.actions` as a package. Evidence in the
  workspace `verification/issue-201/task-15-report.md`.

## v0.2.2 (2026-10-16)

Dependency lower bounds for the gp/fp aliases (fontlab-glyport, fontlab-fontport); NOTICE now ships in the wheel. Release review: verification/issue-106/reviews/X5-fontlab-fly.md (+ X6 fix, APPROVE).

## 2026-10-23 — Distribution portability and provenance

- Document a reader-selected external scratch folder for temporary files and uv
  cache without embedding a machine-specific volume in distribution metadata.

## 1.3.2 (2026-11-16)

- Document App feature helpers at `fly.ap.fontui.feature_blocks` and the explicit
  App import form, `import fly.ap.core.history.glyphs as history`.
- Correct the standalone test instructions: select Python 3.11 arm64 explicitly;
  prepare pytest before using `./test.sh`. Keep caches and temporary build files
  in the external data directory.
- `6cf9dc1`: correct README status to mark dependency minimums and NOTICE
  packaging as released in v0.2.2. This correction is outside the v0.2.2 tag.

## 2026-10-22 — offline verification

- Python 3.11.17 arm64: 17 tests passed, including the wheel LICENSE/NOTICE test
  (exit 0), through direct pytest and `./test.sh` with a prepared environment.
  Ruff passed (exit 0). Local links, alias rows, dependency minimums and Python
  example syntax passed a separate check (exit 0). No docs-specific suite exists.
- Native Feature script and final artifact acceptance remain open.

## v0.2.2

- Include the Echopy provenance NOTICE alongside LICENSE in wheel licensing files;
  add a regression test that builds a wheel and checks both files and metadata.
- Correct README release status: the nine aliases shipped in v0.2.1.
- Resolve Ruff import ordering and test-only lint findings.
- Require `fontlab-glyport>=0.0.2.dev0` and `fontlab-fontport>=0.1.1.dev0`.

## v0.2.1

- Add lazy `fly.gp` and `fly.fp` aliases for `fontlab_glyport` and
  `fontlab_fontport`, including child-module imports and canonical module identity.
- Declare both target distributions as runtime dependencies.
- Update import examples, native smoke output and dependency documentation for
  all nine aliases; extend tests for lazy loading, identity and missing packages.

## 2026-10-15 — completed checklist (moved from TODO.md)

- Record source provenance and baseline.
- Implement complete package migration and scoped modernization.
- Verify wheel, sdist, isolated installs and privacy.
- Verify relevant native behavior in FontLab.
- Pass review and scoped fixes.
- Complete all three project iterations.
- Push, tag, release and verify assets.

No implementation changes verified yet.

- Add modern hatch-vcs package, lazy namespace imports and explicit scope docs.
- Verify standalone identity/error tests and installed native alias/Qt smoke.
- Supply all seven exact aliases with shared canonical module/import metadata.

## v0.2.0 publication verified

Actual publication and independent downloaded-asset verification complete.
Three full-project iterations pass; installed tagged wheel/sdist each457tests.
Downloaded native smoke covers all eight packages and both formats, including
production ACP/native UI and TypeRig composition. Exact release URLs, immutable
code commit and asset digests are in RELEASE.md. This follow-up changes only
completion evidence; release code and tag are unchanged.

## 2026-10-15 — workspace plan and checklist reconciliation

Completed repository scope archived after reading WORK.md and checking the
workspace evidence. Workspace release/integration gates remain in the parent
PLAN.md. Historical verification limits below remain part of the record.

### Archived PLAN.md

# Plan

No open work in this repository. Its issue 101 migration scope is complete and released as verified v0.2.0 (see README.md "Status" and RELEASE.md). Cross-package work for the expanded ecosystem (joint regression in the three expanded iterations, R050/P11, and any new release) is tracked in the workspace PLAN.md.

### Archived TODO.md

# Tasks

No open tasks. Workspace-level work is tracked in the parent TODO.md.


## 2026-11-07 — Exact frontend notices and English search assets

Added exact upstream frontend notices and source-map provenance for the existing MaterialX 10.1.8 payload. Explicit English configuration and a small build hook reject language, corpus, reference, asset-set or hash drift before omitting the 35 unused language helpers. All nine retained core assets, original product legal files, guides, catalogue rows, media, runtime and dependency/build locks are preserved.

The strict site build and all 35 documentation tests pass. The complete new hook has 100% statement/branch coverage; real Git staging, checkout and archives preserve exact legal bytes. An independently installed matching lock reproduces all 48 output bytes and modes. Existing immutable source/output, epoch, concurrency and full-parity workflow checks remain active. Browser and independent review evidence are separate from these local checks.

Private Pages configuration, grants, requests and publication remain owner-held; this source follow-up adds none.
No product release or installation is claimed. Prior ordinary artifacts remain bound to their recorded revisions; a later Git revision changes genuine hatch-vcs metadata. Full current source archives include these documentation additions; no unchanged-sdist or whole-wheel identity is asserted. Native acceptance and owner installation remain separate.

A separate inherited desktop search stacking defect was reproduced on the exact frozen baseline: the viewport overlay intercepted a visible Development heading for the ordinary query "aliases". Two wheel attempts could not move the non-scrolling panel. The existing local override now gives the already-positioned search panel z-index 2 above the overlay at 1. No external theme or another repository stylesheet changes. Fresh visible-heading desktop/mobile navigation and complete affected build/parity checks qualify this correction separately.


## 2026-11-07 — installed icon path-tuple inventory refinement

The current HTML/CSS contains 45 distinct ordered SVG path tuples. A complete scan of the four installed MaterialX icon families finds 43 exact installed matches and two unmatched Lucide tuples, refining the earlier known-candidate inventory. The additional installed match is the Font Awesome version caret-down. Its existing CSS header and full notice retain Font Awesome Free 7.1.0, Fonticons and CC-BY-4.0 icon attribution. The official NPM caret SVG has different raw path bytes; no unmodified-primary SVG, whole-geometry or optimizer-recipe equivalence is claimed. The two unmatched Lucide tuples retain their pinned SCSS source attribution.

A new actual-output regression derives these counts and checks installed matches, unmatched CSS references and the caret header. It fails against the prior 42 count and passes with the corrected metadata. All 36 current documentation tests pass; full strict and independent exact-lock builds match every output byte and mode. Only the legal paragraph, corresponding inventory and legal search row change in the site. Runtime, packaging, generators, vendor assets, full notices, existing guidance and the Fly search fix remain exact. Fresh browser verification and independent review are recorded separately. No private Pages operation, delivery, installed-product upgrade or native acceptance is claimed.
