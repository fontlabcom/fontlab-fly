---
name: fontlab-setup
description: Install, update, list and uninstall the FontLab 9 Python ecosystem (Fly, Echopy, Fontlabapp, Pythonqtside, Glyport, Fontport, Pens, Grablab, Remopy, Aidus Code, the Python examples and Scriptmix) into FontLab's user data folder with each package's install.vfpy. Use when asked to set up FontLab scripting, install or update a fontlab-* package or its scripts, add a third-party package to FontLab's Python, or diagnose why a package or script is missing in FontLab.
---
<!-- this_file: skills/fontlab-setup/SKILL.md -->

# Set up the FontLab Python ecosystem

FontLab 9 embeds Python 3.11 (arm64 on Apple silicon). It has no `python`
executable and no pip. Every package installs from its own checkout by opening
that checkout's `install.vfpy` in FontLab.

## Where things go

The user data folder is `~/Library/Application Support/FontLab/FontLab 9`
(inside FontLab: `fontlab.flPreferences().dataPathDefault`).

| Path in the data folder | Contents |
| --- | --- |
| `python/3.11/site-packages/` | FontLab's package folder; packages are symlinks to a checkout (editable) or to `Extensions/<id>/lib/` |
| `.venv/` | uv venv with FontLab's Python version; its site-packages *is* the folder above |
| `Extensions/<id>/install.log` | JSON Lines: one record per install, uninstall or failure; the last install lists every file it created |
| `Scripts/` | The Scripts menu; extensions' `Scripts/` folders are merged in file by file |
| `Scripts/Extensions/` | **List Extensions** and **Uninstall <id>** launchers |

## Install

Prerequisites: FontLab 9 installed and started once; `uv`
(https://docs.astral.sh/uv/) installed; the repositories cloned side by side
from `github.com/fontlabcom/<name>`.

The fontlab-* packages are not on PyPI, and each installer resolves its
dependencies through uv. Install them in dependency order, so each one finds
the ones it needs already in FontLab:

1. `fontlab-echopy`
2. `fontlab-fontlabapp`
3. `pythonqtside`
4. `fontlab-glyport` (pulls glyphsLib and fissix from PyPI)
5. `fontlab-fontport` (pulls fontParts, defcon, ufoLib2 and fontTools)
6. `fontlab-python-pens` (Pen and PointPen protocols; no runtime dependencies)
7. `fontlab-fly` (pulls TypeRig)
8. any of: `fontlab-grablab`, `fontlab-remopy`, `fontlab-aidus-agentus`,
   `fontlab-python-examples`, `fontlab-python-scriptmix`

For each repository, open its `install.vfpy` in FontLab: double-click it, drop
it onto FontLab, or from a shell run:

```sh
open -a "FontLab 9" /path/to/fontlab-fly/install.vfpy
```

Then confirm it finished. `open` returns immediately, and FontLab's Output panel
may be closed, so read the last line of the log:

```sh
tail -n 1 "$HOME/Library/Application Support/FontLab/FontLab 9/Extensions/com.fontlab.fly/install.log"
```

`"action": "install"` means success. `"action": "failed"` carries the traceback
and uv's output in `"error"`. The extension id is `[tool.fontlab-install] id` in
the repository's `pyproject.toml`. Restart FontLab afterwards so it imports the
new packages.

A Git checkout installs **linked**: edits in the checkout take effect after a
FontLab restart. A plain folder (ZIP, sdist) installs **copied** into
`Extensions/<id>/lib/`. Reinstalling is safe and updates in place.

## Scripts

Files under a repository's `Scripts/` are copied into FontLab's `Scripts/`.
Folders that several extensions share (for example `Contours/`) merge. The
installer refuses to overwrite a file that another extension or the user put
there, and changes nothing in that case. Read the `failed` record, then rename
or remove the conflicting file. Choose **Scripts > Refresh Scripts** or restart
FontLab to see new scripts.

## Add another package to FontLab

```sh
uv pip install --python "$HOME/Library/Application Support/FontLab/FontLab 9/.venv/bin/python" <package>
```

This installs straight into FontLab's site-packages. Never use pip against
FontLab's folder, and never install into FontLab's application bundle.

## List and uninstall

Inside FontLab: **Scripts > Extensions > List Extensions** and
**Scripts > Extensions > Uninstall <id>**. Uninstalling removes only that
extension's files, the `.pyc` files FontLab compiled beside its scripts, and
folders left empty. A linked checkout itself is never touched.

## Troubleshooting

- *Package missing after install*: restart FontLab; it reads site-packages at start.
- *`failed` with "No solution found"*: a fontlab-* dependency is not installed
  yet; install it first (see the order above).
- *"Refusing to replace"*: another extension or the user owns that path.
- *"uv not found"*: install uv; packages still install, but dependencies do not.
- *Wrong Python in `.venv`*: the installer moves it to `.venv.backup-*` and
  recreates it with FontLab's exact Python version.
- `uv pip check --python <data>/.venv/bin/python` reports conflicts across everything installed.

To run code in FontLab from outside, for example to check an install,
use the `fontlab-remote` skill.
