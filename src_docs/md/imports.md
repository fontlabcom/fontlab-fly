---
this_file: src_docs/md/imports.md
---

# Imports and providers

Both `from fly import ...` and `import fly.<alias>` route to the original
canonical module. Child imports use the same routing and preserve metadata,
including native modules whose `__spec__` is `None`.

| Alias | Canonical module | Responsibility |
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

## Identity and child imports

```python
from fly import gp, fp, pens
import fly.gp
import fly.fp
import fly.pens
import fontlab_glyport
import fontlab_fontport
import fontlab_pens

assert gp is fly.gp is fontlab_glyport
assert fp is fly.fp is fontlab_fontport
assert pens is fly.pens is fontlab_pens
```

Keep App's explicit domain paths when importing its submodules:

```python
import fly.ap.core.history.glyphs as history
from fly.ap.fontui.feature_blocks import read_feature_blocks, write_feature_blocks
from fly.fp.pens import FontGatePointPen
```

Feature source helpers belong to App's `fontui.feature_blocks`. The shared
`fly.ap.core.scripting` module also exposes lazy wrappers. General UI and shared
script helpers belong in App; Fontport owns fontParts/UFO support and Glyport
owns Glyphs.app compatibility.

## Pens

`fly.pens` exposes the complete canonical `fontlab_pens` module, including its
public exports and submodules. App, Fontport and Glyport follow the same exact
module routing; Fly does not select or wrap their APIs.

```python
from fly import pens

recording = pens.RecordingPen()
transformed = pens.TransformPen(recording, (2, 0, 0, 3, 10, 20))
transformed.moveTo((1, 2))
transformed.lineTo((3, 4))
transformed.closePath()
assert recording.value[0] == ("moveTo", ((12, 26),))
```

Recording and transforms work outside FontLab. Native pens retain the provider's
host requirements; Fly supplies no native emulation.

## Glyport's public API

```python
from fly import gp

Glyphs = gp.GlyphsApp.Glyphs
```

`gp.GlyphsApp` is the lazy public `fontlab_glyport.GlyphsApp` module. First access
to `Glyphs` binds a FontLab GUI-thread session. Outside FontLab, first bind an
explicit backend with `gp.GlyphsApp.use_backend(backend)`, then call
`gp.GlyphsApp.unbind()` when finished. The backend must satisfy Glyport's
contract; Fly does not supply one or broaden its compatibility guarantees.

## PythonQt and App

`qt` requires native PythonQt. Widgets are in `QtGui`; `QObject` is in
`PythonQt.private`. Do not substitute a separate PySide runtime or construct
another QApplication to exercise these imports.

Accessing `ap` alone does not construct App's Application or preference library.
Native imports remain loaded in the host process, so a reused session is not a
cold-import test.
