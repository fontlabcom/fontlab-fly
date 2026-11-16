---
name: fontlab-scripting
description: Write Python scripts and small tools for FontLab 9 using the Fly aliases (fl, fg, tr, pr, qt, ap, qs, gp, fp, pens) over Echopy, TypeRig, Fontlabapp, Pythonqtside, Glyport, Fontport and Pens - where each kind of code belongs, how scripts reach the Scripts menu, and how to test them. Use when asked to write, port or fix a FontLab script, port a Glyphs or fontParts/RoboFont script to FontLab, or build a FontLab panel or dialog.
---
<!-- this_file: skills/fontlab-scripting/SKILL.md -->

# Write FontLab scripts with Fly

Install the ecosystem first (skill `fontlab-setup`). Scripts run in FontLab's
Python 3.11 with PythonQt; a separate Python cannot load FontLab's native
modules.

## Imports

```python
from fly import fl, fg, tr, pr, qt, ap, qs, gp, fp, pens
```

| Alias | Module | Use for |
| --- | --- | --- |
| `fl` | `echopy.fontlab` | FontLab application, font, glyph and layer objects |
| `fg` | `echopy.fontgate` | FontGate font data |
| `pr` | `echopy.fontpr` | FontLab's command bridge (the same calls MCP exposes) |
| `tr` | `typerig` | TypeRig high-level glyph and font editing |
| `qt` | `PythonQt` | Host Qt (`qt.QtGui` for widgets) |
| `qs` | `pythonqtside` | PySide-style names on top of PythonQt |
| `ap` | `fontlabapp` | Shared script and UI helpers: dialogs, panels, history |
| `gp` | `fontlab_glyport` | Run or port Glyphs.app scripts and plugins |
| `fp` | `fontlab_fontport` | fontParts and UFO interoperability |
| `pens` | `fontlab_pens` | Pen and PointPen protocols, recording and transforms |

Each alias exposes the complete original module, and nothing loads until it is used.
For submodules, use dotted imports: `import fly.ap.core.history.glyphs as history`,
`from fly.fp.pens import FontGatePointPen`,
`from fly.pens.recording import RecordingPen`.

Supported Glyphs-style code uses Glyport's public module:

```python
from fly import gp

Glyphs = gp.GlyphsApp.Glyphs
layer = Glyphs.font.selectedLayers[0]
```

`gp.GlyphsApp` is `fontlab_glyport.GlyphsApp`. First export access binds a
FontLab GUI-thread session. Outside FontLab, call
`gp.GlyphsApp.use_backend(backend)` before accessing exports; call
`gp.GlyphsApp.unbind()` when done. Glyport implements supported Glyphs APIs;
check its compatibility guide before porting a script or plugin.

Feature source helpers live in `fly.ap.fontui.feature_blocks`; general script
helpers live in `fly.ap.core.scripting`.

## Where code belongs

- **A menu script** is one `.py` file under a repository's `Scripts/<Category>/`
  (for example `fontlab-python-scriptmix/Scripts/Kerning/`); its file name is
  the menu item. Keep scripts thin: import what they reuse from packages.
- **Reusable UI or helpers** go in Fontlabapp (`ap`). Glyphs compatibility goes
  in Glyport (`gp`). fontParts and UFO code goes in Fontport (`fp`);
  Pen/PointPen protocols belong in Pens (`pens`).
- **Tutorial-style examples** go in `fontlab-python-examples/Scripts/`; collected
  production tools go in `fontlab-python-scriptmix/Scripts/`.
- For tools used repeatedly, prefer a non-modal panel to a modal dialog.
  Fontlabapp has helpers for both.

After adding a script, rerun that repository's `install.vfpy` so it is copied
into FontLab's `Scripts/` folder. Then choose **Scripts > Refresh Scripts**.
An extension with only scripts sets
`[tool.fontlab-install] packages = []` in `pyproject.toml`, and lists what FontLab
needs under `dependencies`.

## Editing fonts safely

- Make each script edit one Undo step: `fly.ap.core.history.glyphs.commit(title, layers,
  glyphs, mutate, operation=...)` runs `mutate` as a single FontLab Undo step and
  refuses unsafe states before writing anything. Read its docstring first.
- Work on the current font or selection only. Never save, close or
  overwrite user files unless asked.
- Report results in a window or the Output panel; do not clear the Output panel.

## Test

1. Test logic that does not need FontLab with pytest outside FontLab, using
   each repository's own test recipe (README or AGENTS.md).
2. Check behaviour inside FontLab with Remopy (skill `fontlab-remote`). For example:

   ```python
   from fontlab_remopy import FontLab
   with FontLab() as fl:
       print(fl.eval("__import__('fly').ap.__name__"))
       print(fl.execute_script("Scripts/Kerning/My Tool.py"))
   ```

   FontLab allows 5 seconds per execution. Keep checks short and use a test font
   you created.
3. Finally, run the script from the Scripts menu once to see its UI.
