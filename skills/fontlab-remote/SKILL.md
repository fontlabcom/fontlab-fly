---
name: fontlab-remote
description: Control a running FontLab 9 from outside with fontlab-remopy (Python API and CLI over FontLab's authenticated MCP bridge) - launch FontLab, enable MCP, list fonts, run Python inside FontLab and read results, call FontLab's MCP tools, execute .vfpy/.flpy scripts. Use when an agent must inspect or change fonts in FontLab, run or test a FontLab script, or verify an installation from a terminal, notebook or another app such as Glyphs.
---
<!-- this_file: skills/fontlab-remote/SKILL.md -->

# Control FontLab remotely with Remopy

Remopy (`fontlab_remopy`) runs in **ordinary Python 3.11+ outside FontLab**. It
talks to FontLab's bundled `fontlab-mcp` bridge, which holds the authentication
for FontLab's local MCP server.

## Set up

```sh
# arm64 on Apple silicon: an x86_64 Python makes uv build cryptography from source and fail
uv venv --python cpython-3.11-macos-aarch64-none .venv-fontlab && . .venv-fontlab/bin/activate
uv pip install -e /path/to/fontlab-remopy      # needs mcp and anyio from PyPI
fontlab-remopy launch                          # start FontLab if it is not running
fontlab-remopy --timeout 15 setup              # enable MCP once and verify it
fontlab-remopy tools                           # list FontLab's MCP tools
```

`setup` turns on FontLab's `mcp.enabled` preference through a one-off macro and
checks a nonce in its reply. The user can do the same in
**Preferences > Aidus** (allow external MCP clients). The bridge is found from
an explicit argument, `FONTLAB_MCP_COMMAND`, `PATH`, or the FontLab 9 bundle.

## Use from Python

```python
from fontlab_remopy import FontLab

with FontLab() as fl:                     # one authenticated connection
    print(fl.fonts())                     # open fonts
    print(fl.eval("value + 2", value=40)) # an expression; returns 42
    done = fl.run("print(msg); result = {'n': len(msg)}", msg="Łódź")
    print(done.value, done.stdout, done.stderr)

    @fl.python                            # runs inside FontLab
    def metrics(name: str):
        from fly import pr                # imports go inside the body
        return pr.get_glyph_metrics(glyph_name=name)

    print(metrics("A"))
    print(fl.tool("list_fonts"))          # any MCP tool by name
```

- Code runs in an isolated namespace with `fontlab`, `fontgate`, `fontpr` and
  `PythonQt` prebound. Keyword variables are passed as JSON.
- `run` returns `ExecutionResult(value, stdout, stderr)`; set `result` to return
  a value. `eval` returns the value. `@fl.python` functions must be
  self-contained: arguments and return values must be JSON. The capture check
  also matches attribute names against your module's globals, so
  `module.__name__` or `module.__file__` in the body fails with "cannot capture
  globals"; use `getattr(module, "__name" + "__")` or `run`/`eval` instead.
- Named helpers include `current_font`, `current_glyphs`, `glyph("A")`,
  `font_info`, `font_metrics`, `glyph_metrics`, `list_actions`, `run_actions`,
  `output`, plus font open, new, save, close and activate. `tools()` returns
  the live tool schemas.
- `AsyncFontLab` offers the same operations with `async with` and `await`.
- In installed FontLab packages, use the Fly aliases (`from fly import fl, ap`)
  inside `@fl.python` bodies. See the `fontlab-scripting` skill.

CLI equivalents: `fontlab-remopy execute script.flpy`, `fontlab-remopy call list_fonts`.

## Limits and safety

- FontLab gives each execution **5 seconds**, with code up to 32,768 bytes and
  output up to 65,536 bytes. Split long work into several calls. Long tasks
  such as `install.vfpy` must go through `open -a "FontLab 9" file.vfpy`, not Remopy.
- A timeout means the outcome is **unknown**. Remopy never retries. Check the
  state (for example re-read the font) before you repeat anything that changes it.
- Mutating tools change the user's real fonts. Do not save, close or overwrite
  fonts, preferences or the Output panel unless the user asked for it. Prefer
  testing on a new or copied font that you created.
- Errors raise `NativeExecutionError` (the native traceback and partial output
  are in `.payload`) or `ResultTransportError` (the reply is missing, too large
  or not JSON).
- `submit_script()` and `launch()` only submit work, through file association.
  They cannot confirm the script ran; use MCP calls for confirmed results.

## From Glyphs

`glyphs/fontlab_remote.py` in fontlab-remopy uses only the standard library.
Copy it into Glyphs' Scripts folder and use `FontLabClient` with `tools()`,
`call()`, `eval()` and `run_python()`.
