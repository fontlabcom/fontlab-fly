---
this_file: src_docs/md/installation.md
---

# Installation

Fly requires Python 3.11 or later. FontLab host work targets Python 3.11 arm64.
Use the project checkout or an artifact supplied by its maintainer. This guide
does not assume that current compatible provider releases are on PyPI.

## For a FontLab script

Install Fly and the required canonical providers into the same FontLab runtime
using the maintainer's supported installation procedure. FontLab supplies
PythonQt. Editable installations in FontLab are owner-managed; a standalone
virtual environment is a separate runtime.

Current metadata declares these minimums:

| Distribution | Minimum |
| --- | --- |
| `fontlab-echopy` | `0.1.0` |
| `typerig` | `0.1.0` |
| `fontlab-fontlabapp` | `1.2.0` |
| `pythonqtside` | `0.1.0` |
| `fontlab-glyport` | `1.2.0` |
| `fontlab-fontport` | `1.2.0` |
| `fontlab-python-pens` | `1.0.0` |

Install `fontlab-python-pens` before Fly.

These are metadata minimums, not a guarantee that every newer script works with
those versions. Meet each target package's own requirements. Install compatible
providers from their reviewed checkouts or artifacts when released distributions
are unavailable.

## Standalone development

Run these commands from your Fly checkout. They create a separate environment
for Fly's host-free tests, without resolving or installing its providers:

```sh
uv venv --python cpython-3.11-macos-aarch64-none .venv
uv pip install --python .venv/bin/python pytest
uv pip install --python .venv/bin/python --no-deps -e .
./test.sh -q -p no:cacheprovider
```

This macOS arm64 recipe needs uv and a suitable Python, plus access to the pytest
and build dependencies. It must not target FontLab's environment. See the
repository README for the external scratch-directory recipe.

## Missing providers

Accessing an alias imports its target. A missing target raises
`ModuleNotFoundError` with alias context. An error caused by a missing internal
dependency keeps its original error. Other provider exceptions propagate.
Check that the required distribution is installed in the runtime actually
executing your script; installing it in another virtual environment has no effect.
