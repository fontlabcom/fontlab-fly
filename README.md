---
this_file: README.md
---

# Fly: short FontLab imports

Fly gives FontLab scripts ten short imports. Each alias returns the original
module object. It adds no native API emulation or alternative alias targets.
Importing `fly` alone loads none of the target packages.

| Alias | Canonical module | Use |
| --- | --- | --- |
| `fl` | `echopy.fontlab` | FontLab bindings |
| `fg` | `echopy.fontgate` | FontGate bindings |
| `tr` | `typerig` | TypeRig library |
| `pr` | `echopy.fontpr` | FontLab command bridge |
| `qt` | `PythonQt` | Host Qt binding |
| `ap` | `fontlabapp` | Shared script and UI helpers |
| `qs` | `pythonqtside` | PySide-style access to host PythonQt |
| `gp` | `fontlab_glyport` | Glyphs.app compatibility |
| `fp` | `fontlab_fontport` | fontParts/UFO interoperability |
| `pens` | `fontlab_pens` | Pen and PointPen protocols |

## Install

To install into FontLab 9, open `install.vfpy` from a checkout in FontLab
(double-click it or drop it onto FontLab), then restart FontLab. The file is a
short stub that hands the work to
[fontlab-instamix](https://github.com/fontlabcom/fontlab-python-instamix); if
instamix is not installed yet, the stub installs it from PyPI first. Instamix
installs the package into FontLab's own `site-packages` and records the install
under the extension id `com.fontlab.fly`.

Requires Python 3.11 or later. FontLab host work targets Python 3.11 arm64.
FontLab supplies PythonQt. A separate Python environment cannot supply the
native FontLab runtime by installing Fly.

For standalone development, use the external environment recipe under
[Test and lint](#test-and-lint). It installs Fly without its target dependencies,
which is sufficient for Fly's offline tests. For real use, install the target
distributions from their checkouts or artifacts into the same runtime.
Declared minimums:

- `fontlab-echopy>=0.1.0`, `typerig>=0.1.0`;
- `fontlab-fontlabapp>=1.2.0`, `pythonqtside>=0.1.0`;
- `fontlab-glyport>=1.2.0`, `fontlab-fontport>=1.2.0`;
- `fontlab-python-pens>=1.0.0`.

Install `fontlab-python-pens` before Fly.

Meet the target packages' own requirements: metadata minimums do not guarantee
compatibility with every newer script.
Editable installs into FontLab are owner-managed. Do not run these standalone
installation commands against FontLab's site-packages.

## Use inside FontLab

```python
from fly import fl, fg, tr, pr, qt, ap, qs, gp, fp, pens
import fly.fl
import fly.gp
import fly.fp
import fly.pens
import fontlab_glyport
import fontlab_fontport
import fontlab_pens

assert fly.fl is fl
assert gp is fly.gp is fontlab_glyport
assert fp is fly.fp is fontlab_fontport
assert pens is fly.pens is fontlab_pens
```

Both import forms keep the canonical module identity and metadata, including
native modules whose `__spec__` is `None`. Child imports use the same routing:

```python
from fly.fp.pens import FontGatePointPen
from fly.ap.fontui.feature_blocks import read_feature_blocks, write_feature_blocks
import fly.ap.core.history.glyphs as history
```

Feature source helpers belong to App's `fontui.feature_blocks`; the shared
`fly.ap.core.scripting` module also exports lazy wrappers. Load App submodules
with their explicit domain paths as above.

For supported Glyphs-style code, use the public Glyport API through Fly:

```python
from fly import gp

Glyphs = gp.GlyphsApp.Glyphs
```

`gp.GlyphsApp` is the lazy public `fontlab_glyport.GlyphsApp` module. First
access to `Glyphs` binds a FontLab GUI-thread session. Outside FontLab, bind an
explicit backend with `gp.GlyphsApp.use_backend(backend)` first; call
`gp.GlyphsApp.unbind()` when done. See Glyport's compatibility guide for limits.

Accessing an alias imports its target. Accessing `ap` alone does not construct
App's Application or preference library. `qt` requires native PythonQt; a
missing target raises `ModuleNotFoundError` with alias context. A missing internal
dependency keeps its original error. Other exceptions propagate from the target.
PythonQt uses `QtGui` for widgets and `PythonQt.private` for `QObject`.

General UI/shared helpers belong in fontlabapp. Fontport owns fontParts/UFO
support; Glyport owns Glyphs.app compatibility. Pens owns the Pen/PointPen
protocols. Each alias exposes its complete canonical module; Fly adds no API
subset or wrappers. Scripts use App through Fly.

## Agent skills

[skills/](skills/) provides agent instructions for the FontLab ecosystem:

| Skill | Covers |
| --- | --- |
| [fontlab-setup](skills/fontlab-setup/SKILL.md) | Installing every package and script collection with `install.vfpy`, in dependency order; listing, uninstalling, troubleshooting |
| [fontlab-remote](skills/fontlab-remote/SKILL.md) | Controlling a running FontLab from outside with Remopy: MCP setup, `run`/`eval`/`@fl.python`, tools, limits and safety |
| [fontlab-scripting](skills/fontlab-scripting/SKILL.md) | Writing scripts with the Fly aliases, where code belongs, one-step Undo, testing |

Link the skill folders into the skills directory used by your agent.

## Module and file map

| Path | Role |
| --- | --- |
| [src/fly/__init__.py](src/fly/__init__.py) | Alias map, lazy attributes, import finder and metadata-preserving loader |
| [examples/native_smoke.py](examples/native_smoke.py) | Ten-alias identity smoke for a fresh FontLab import session |
| [tests/test_aliases.py](tests/test_aliases.py) | Lazy loading, identity, metadata, reload, child imports and errors |
| [tests/test_packaging.py](tests/test_packaging.py) | Builds a wheel; checks byte-exact LICENSE/NOTICE and licence metadata |
| [test.sh](test.sh) | Runs pytest through `uv run --no-sync` |
| [pyproject.toml](pyproject.toml) | Runtime requirements, pytest paths, Hatch build and Git-tag versioning |
| [DEPENDENCIES.md](DEPENDENCIES.md) | Dependency roles |
| [PLAN.md](PLAN.md), [TODO.md](TODO.md) | Current goals and open acceptance tasks |
| [CHANGELOG.md](CHANGELOG.md), [WORK.md](WORK.md), [RELEASE.md](RELEASE.md) | Changes, test evidence and historical release evidence |

## Documentation website

[Fly guide sources](src_docs/md/index.md) build locally; Pages is not deployed.
Private Pages publication is held by the owner on the current account plan.
The site uses fly-january 0.1.1 with the FontLab menu and footer. Install the
hash-locked `src_docs/requirements.txt` in a Python 3.13 docs environment.
`sh src_docs/build.sh` reads `src_docs/mkdocs.yml` and rebuilds `docs/` in strict
mode. The [development guide](src_docs/md/development.md) covers local checks and CI.

## Test and lint

Run from this repository root on macOS arm64. Install uv first. The selected
Python must be installed or available for uv to download. Pytest and the wheel
build dependencies (Hatchling and hatch-vcs) must be available from the package
index or cache. Set `FONTLAB_SCRATCH` to a writable external-drive folder first.

```sh
: "${FONTLAB_SCRATCH:?Set FONTLAB_SCRATCH to a writable external-drive folder}"
export TMPDIR="$FONTLAB_SCRATCH/tmp" UV_CACHE_DIR="$FONTLAB_SCRATCH/fontlab-fly-cache"
mkdir -p "$TMPDIR" "$UV_CACHE_DIR" || exit 1
export PYTHONPATH="$PWD/src"
export PYTHONDONTWRITEBYTECODE=1 PYTEST_DISABLE_PLUGIN_AUTOLOAD=1
export GIT_OPTIONAL_LOCKS=0
uv run --python cpython-3.11-macos-aarch64-none --no-project --with pytest \
  python -m pytest -q -p no:cacheprovider
```

`PYTHONPATH` is required by subprocess tests when Fly is not installed.
The explicit Python selector prevents accidental x86_64 or Python 3.12 use.
Tests use stand-in target modules; installing the target packages is not needed.

For a reusable standalone environment, use the same exports and prepare it first:

```sh
uv venv --python cpython-3.11-macos-aarch64-none "$TMPDIR/fontlab-fly-venv"
uv pip install --python "$TMPDIR/fontlab-fly-venv/bin/python" pytest
uv pip install --python "$TMPDIR/fontlab-fly-venv/bin/python" --no-deps -e .
UV_PROJECT_ENVIRONMENT="$TMPDIR/fontlab-fly-venv" ./test.sh -q -p no:cacheprovider
```

`./test.sh` runs `uv run --no-sync`. It requires a prepared Python 3.11 arm64
environment with pytest; it does not install pytest or select the host Python.
Without `UV_PROJECT_ENVIRONMENT`, it uses the project's `.venv`. A missing
`.venv` can cause uv to create an unsuitable environment and fail without pytest.
The editable install above affects only the standalone environment.

Ruff is installed separately:

```sh
ruff check --no-cache src tests examples
```

To build both distributions, keep the same cache/temp exports and run:

```sh
uv build --out-dir "$TMPDIR/fontlab-fly-dist"
```

Builds use Hatchling and hatch-vcs; versioning uses Git tags. Building artifacts
alone does not prove that they work in FontLab.

The suite includes a real wheel build and tests target routing
with stand-in modules. The separate `tests_docs/` suite checks publishing and generated pages.
On 2026-10-22, the offline suite passed on Python 3.11.17 arm64 (exit 0, 17 passed);
Ruff passed (exit 0). These checks do not prove native FontLab behavior.

Run `examples/native_smoke.py` inside FontLab with all targets available and a
fresh App import state. It also checks that importing `ap` has not created
`app`; a reused session can already contain it. The smoke proves alias identity,
not child-module behavior or full target functionality. Native acceptance uses
the workspace runner, owned fixtures and loaded-path checks because canonical
editable installs can shadow the worktree.

WORK.md retains historical FontLab 9.0.9783/Python 3.11.6/Qt 5.15.19 wheel/sdist
checks predating the provider refactor. Current native acceptance remains open.

## Releases and licence
v0.2.0 shipped the original seven aliases. v0.2.1 added `gp` and `fp`.
v0.2.2 set their dependency minimums and included NOTICE in wheel licence files.

[Apache-2.0](LICENSE); [NOTICE](NOTICE) credits Echopy. Providers retain their own licences.
