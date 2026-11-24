---
this_file: AGENTS.md
---

## Owner priority: functional progress first (2026-11-15)

Future agents must make large, swift advances in working functionality. Prioritize visible user problems and useful, coherent feature increments. This instruction sets the work order and supersedes older requirements to complete exhaustive testing or build test infrastructure before ordinary implementation.

Keep packages coherent and compatible. Check shared APIs, imports and lazy aliases, data formats, dependency direction, object ownership and lifetime, installers, launchers and examples. Update affected providers and consumers together; preserve existing supported behavior and avoid dependency cycles.

During implementation, use the smallest meaningful smoke checks and focused regression tests for the changed behavior and affected package boundaries. Detailed testing, exhaustive coverage, broad performance studies and full acceptance matrices can follow in a later testing pass. Do not let test harnesses, sandbox/supervisor design, repeated unchanged suites, evidence machinery or review paperwork become the main project. Build such infrastructure only when a concrete functional defect or necessary safety constraint requires it.

Record deferred checks and known limits plainly. Do not call untested native, installed or published behavior verified. Keep existing mandatory delivery hooks, preservation rules, licence/privacy obligations, repository exclusions and explicit native/publication holds intact. When one action is held, continue other authorized functional work instead of expanding unrelated infrastructure.

Choose the next substantial useful feature or shared fix and carry its affected providers and consumers together. Timebox supporting investigation; once focused checks establish a usable increment, continue functionality work. Queue detailed testing for a later pass with its concrete remaining checks instead of letting test infrastructure displace product delivery.

## Issue 233 website lane

The workspace's D40 authorizes the scoped documentation site. Source is in
`src_docs/md`, configuration in `src_docs/mkdocs.yml`, output in `docs`.
ProperDocs uses fly-january 0.3.0 or later with the `fly` plugin, `fontlab` chrome and
the site label `Fly`. Keep the page palette in fixed light mode.
In the hash-locked Python 3.13 docs environment, run `sh src_docs/build.sh`
and `python -m unittest discover -s tests_docs -v`. Every main push builds;
the generated commit gets a separate read-only full rebuild and exact parity check.
The owner's later instruction holds private Pages configuration and publication.
The workflow grants no Pages permission and makes no Pages request. Keep the tested
`src_docs/request-pages.sh` dormant: do not invoke or wire it into private delivery
until the owner lifts that hold. Mocked helper tests remain required. Keep source
qualification, actual publication and native proof distinct.

## Current scope — 2026-11-05

Issue 230 documentation reconciliation is current. Issue 123 remains paused. The qualified Issue 207 isolated candidate is separate from canonical source, installed artifacts, native acceptance and publication. Reconcile that candidate with later work before integration. Issue 210 specifies future architecture; Issue 211 retains unfinished follow-up checks. Retained dated receipts describe their original source and acceptance surface only.

Canonical source inspected for this proposal: `b1ff250b7336`. This is a dated source observation, not an installed or native acceptance claim.

Keep every public lazy alias pointed at its reviewed provider and verify import identity after provider migrations.

Qualify the final genuine wheel/sdist and ordinary installed cohort; keep installed-host behavior separate from host-free import tests.

## Organization and checks

`src/` owns import aliases and the facade; `tests/` covers routing and distributions; `examples/` and `tools/` provide usage and development support.

Use the explicit arm64 Python 3.11 source-test recipe in README. `./test.sh` runs `uv run --no-sync python -m pytest` and requires a prepared environment with pytest; it does not install dependencies.

# Fly rules

Fly provides ten lazy aliases to the exact canonical FontLab scripting modules.

- Target Python 3.11 arm64. A generic `python3.11` can select x86_64 on this Mac;
  request `cpython-3.11-macos-aarch64-none` and verify the interpreter architecture.
- Keep aliases lazy: cold Echopy imports can exceed FontLab's fixed five-second
  `run_python` deadline. Native modules can have `__spec__ = None`; preserve their
  import metadata and object identity. Do not emulate native modules.
- `fly.qt` is native PythonQt: widgets are in `QtGui`, not `QtWidgets`;
  `QObject` is in `PythonQt.private`. Do not substitute PySide or create another
  QApplication to test imports.
- Load App submodules with explicit domain paths, such as
  `import fly.ap.core.history.glyphs as history`. Feature source helpers are in
  `fly.ap.fontui.feature_blocks`. Supported Glyphs-style code uses the public
  `fly.gp.GlyphsApp` module (`fontlab_glyport.GlyphsApp`); its first export access
  needs FontLab's GUI thread or an explicit offline backend.
- Put general UI/shared helpers in fontlabapp; fontParts/UFO code in fontport;
  Glyphs.app compatibility in glyport. Scripts use App through Fly.
- Tests, from this root with uv and access to pytest/build dependencies:
  `PYTHONPATH="$PWD/src" PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 uv run --python cpython-3.11-macos-aarch64-none --no-project --with pytest python -m pytest -q -p no:cacheprovider`.
  Set writable `UV_CACHE_DIR` and `TMPDIR` under a scratch folder
  (`$FONTLAB_SCRATCH`) as shown in README.
- `./test.sh -q -p no:cacheprovider` uses `uv run --no-sync`; it needs an
  existing Python 3.11 arm64 environment with pytest. The default is `.venv`;
  README uses `UV_PROJECT_ENVIRONMENT` to select an external environment.
  Without preparation, uv can create an unsuitable environment without pytest.
- Lint: `ruff check --no-cache src tests examples`. Install Ruff separately;
  it is not a declared project dependency. The packaging test invokes uv to
  build a wheel and needs Hatchling and hatch-vcs available to the build.
- Offline tests use stand-in modules; they are not native proof. For native
  acceptance, use the shared native runner, owned fixtures and final artifacts.
  Record host build and loaded paths.
  Native imports persist across calls: remove stale modules only with no live
  handles, and assert the tested checkout/artifact supplies each target.
- FontLab's canonical editable installs are owner-managed and can shadow this
  worktree. Never install/uninstall in its site-packages or edit live checkouts.
- Stay in the current worktree and branch. Preserve owner files, tags and evidence.
  No reset, clean, stash, checkout, commit, merge or push without explicit scope.
  Read Git with `GIT_OPTIONAL_LOCKS=0 /opt/homebrew/bin/git --no-optional-locks`.
- Keep verified work in CHANGELOG and open work in flat `- [ ]` TODO items.

## Milestones and delivery

Read [PLAN.md](PLAN.md), [TODO.md](TODO.md) and [WORK.md](WORK.md) before work.
Make the smallest complete MVP for one named acceptance task. Find all callers,
tests, fixtures, exports and documentation first. Use graph impact before source
symbol edits; confirm stale or unknown graph results against current source.
Keep product work in isolated successors and preserve the owner's checkout.

Run this repository's exact checks and the unchanged 80% gate for each complete
changed production module. Use an independent review before a milestone commit.
Under the current owner task, commit and push reviewed, passing milestones;
verify remote heads rather than inferring delivery from local tracking refs.
Before main integration, reconcile concurrent work and all consumers, run graph
change analysis and repeat the required acceptance on the combined source.

Before removing obsolete branches or files, prove integration, retain recoverable
unique work and check fresh owner/worktree attachments. Preserve sealed reports,
licences, archives and private data. Do not rewrite history by implication.
Remove verified completed work from PLAN/TODO and record scoped evidence in
CHANGELOG. Keep implemented-only native/artifact checks open in TODO. Issue 123
remains paused; no instruction here authorizes driving the owner's FontLab,
installing into its user folder or publishing a site.

## Integration rounds

After each round of important changes, integrate it into `main` and upstream:
fetch `origin/main`, build the change on top of it in an isolated branch or
worktree, and resolve conflicts by keeping both our work and teammates' work.
Never discard upstream commits, and never force-push. Run the repository's
checks on the merged result, then push to `origin main`. Record the change in
CHANGELOG.md, move verified-solved TODO.md items into CHANGELOG.md, update
PLAN.md, and continue with the next TODO.md item until the list is clear.
`install.vfpy` is shared: keep it byte-identical in every installer repository.

## Isolated successors

Overrides generic bootstrap/MCP.

For graph work in an isolated successor, use the qualified installed CLI or backend with both `GITNEXUS_HOME` and `GITNEXUS_STORAGE_PATH` set to separate task-owned locations before the first invocation, including index discovery and analysis. A private storage path alone can still register the successor in global control files. During ordinary analysis, do not fall back to global MCP defaults, global `list-repos` or global setup/bootstrap, and do not make unreviewed global registry edits. Retain exact command/selected environment and before/after owned metadata; record expected task-owned `.git/info/exclude` additions and preserve unrelated state. If discovery or indexing escapes the owned scope, preserve evidence and obtain independent bounded control-file review before integration. Any necessary recovery must be separately reviewed, use fresh guarded current bytes and reviewed writer coordination, and change only the proven task-owned entry while preserving all other current records and bytes; never restore an old whole global registry.

## Agent workflow (Issue 250, 2026-11-10)

- Plan with `superpowers:subagent-driven-development`: one fresh implementer per task, a separate read-only reviewer, then the controller runs the gates and commits.
- Send bulk, well-specified work to Codex via the `codex-delegate` skill (`node ~/.agents/skills/codex-delegate/scripts/relay.mjs --brief BRIEF --cd WORKTREE`, in the background). Use `claude-delegate` or `cursor-delegate` for second opinions or independent lanes. Delegates never commit, push or tag.
- Work in a fresh worktree of `origin/main` on the workspace data volume; never pull, switch or reset the owner checkout. Merge `origin/main` again before pushing, keep both sides' CHANGELOG/PLAN/TODO entries, rerun the full suite, lint and graph change analysis, push through the pre-push hook where one is installed (never force), verify the remote SHA and the CI run where a workflow is configured. Held private Pages operations (workspace D41) stay held.
- Release: tag the next semver above the latest tag and publish a GitHub release. Install released, gated packages into `~/Library/Application Support/FontLab/FontLab 9/` and test live in FontLab 9. This owner route (Issue 250) supersedes, for released packages only, every older line in this guide that forbids installing into the FontLab user folder or its site-packages, owner-managed editable installs, or starting FontLab for a live test (the owner's canonical editable checkouts themselves stay owner-managed): record the previous installed distribution first so it can be restored, and never touch FontLab preferences (owner fonts and documents: see live font editing below); native work goes through the workspace `verification/issue-104/fl-native.sh` gate.
- Documents: CHANGELOG holds verified completed work; TODO only open or to-verify items; PLAN the major remaining changes; WORK.md the current round only (older WORK bytes are archived on the owner's workspace data volume, not public).
- Native defects: issues at github.com/fontlab/fl; fixes as pull requests to fontlab/Proteus, fontlab/FontGate or fontlab/pyfontgate. Never commit to the local C++ snapshot.
- Older "work directly" or "no delegation" lines in this guide are superseded by this section (Issue 250).
- Live font editing (owner, 2026-11-10; workspace D44): test, verify and edit the font open in FontLab 9, and do not stop because the owner might be working in it. Open a VFJ from `~/Desktop` first (those files are for agents), then add glyphs, kerning pairs, elements, contours, masters or whatever the test needs, and save them freely. This supersedes, for live testing, every older line here that forbids mutating owner fonts or documents or requires owned fixtures only. FontLab preferences, Output folders and global update queues stay untouched. Keep the serialized host lock (`fl-native.sh`, one native run at a time; `--mutating` now allows open fonts); do not quit or restart FontLab and do not close fonts from Python, which has crashed the host.
