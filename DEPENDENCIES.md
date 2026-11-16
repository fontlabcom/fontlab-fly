---
this_file: DEPENDENCIES.md
---

# Dependencies

- hatchling/hatch-vcs: distribution builds and Git-tag versions.
- pytest: focused identity/error regressions.
- fontlab-echopy, typerig, pythonqtside: alias targets (floors unchanged).
- fontlab-fontlabapp>=1.2.0: canonical App domain paths for `fly.ap`.
- fontlab-glyport>=1.2.0: canonical `fontlab_glyport` package for the lazy `fly.gp` alias.
- fontlab-fontport>=1.2.0: canonical `fontlab_fontport` package for the lazy `fly.fp` alias.
- fontlab-python-pens>=1.0.0: canonical `fontlab_pens` package for the lazy `fly.pens` alias.
- Native PythonQt: provided by FontLab for qt.
- Standard importlib: lazy alias routing preserving canonical module identity.

- Docs only: ProperDocs 1.6.7, MkDocs 1.6.1, MaterialX 10.1.8 and PyMdown 11.0.1
  follow the official FontLab theme starter. `src_docs/requirements.txt` locks
  their transitive packages and hashes; they are separate from host dependencies.
- CI setup uses pinned checkout and setup-uv actions with uv 0.13.7. The FontLab
  theme and menu load from their official CDN; no target provider is imported.
