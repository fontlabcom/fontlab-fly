---
this_file: src_docs/md/index.md
---

# Fly: short FontLab imports

Fly gives scripts ten short names for the canonical FontLab scripting modules.
Each alias returns the original module object. Importing `fly` alone loads none
of its providers.

Documentation sources and local builds are available. Private-repository Pages
publication is held by the owner on the current account plan; no public site is
deployed.

```python
from fly import fl, ap
import fly.ap.core.history.glyphs as history
```

Use Fly when writing scripts for FontLab. It keeps imports short while preserving
the provider's module identity and import metadata. It supplies aliases;
the target packages supply the APIs and FontLab supplies the native runtime.

Start with [installation](installation.md), then choose the correct
[import and provider](imports.md). The [development guide](development.md)
explains the host-free checks and their limits.

## Runtime boundaries

FontLab host work targets Python 3.11 on macOS arm64. Installing Fly in an
external Python environment does not provide FontLab's native bindings or
PythonQt. UI and active-font operations must follow the target package's host,
thread and ownership requirements.

The ordinary import tests use stand-in providers. Historical native smoke
results predate later shared-package refactors; current native acceptance
remains open. A working documentation site does not establish native behavior.

## Source and licence

[Source repository](https://github.com/fontlabcom/fontlab-fly) ·
[Apache-2.0 and attribution](licence.md)
