---
this_file: TODO.md
---

- [ ] After the owner reconciles the D43 timeout (exit 79) and admits a native run, verify Issue 255's ten aliases from the released wheel and sdist in FontLab 9 on arm64 Python 3.11. Check both import forms, provider identity, metadata and child imports. Record host build, artifact hashes and loaded paths for each format.
- [ ] For Issue 254, compare the current Fly and App installers with the App's `tools/check_install_copies.py`. Use the Issue 255 host run to confirm alias resolution after installation.
- [ ] For Issue 271, confirm independent cohort review of the released installer and verify it in FontLab on macOS and Windows after serialized admission.
- [ ] Run the adapted Feature scripts through `fly.ap.fontui.feature_blocks` on a test font. Verify Apply, Undo, Redo, save and reopen in the consuming repositories.
- [ ] When a private provider or consuming Script changes, verify affected examples, explicit child imports and alias identity with the relevant sibling checks. Enable all six in CI when the runner can access the siblings. The deselected cases are `tests/test_aliases.py::test_package_alias_when_real_provider_checkout_present_then_resolves_to_it[ap-fontlabapp-fontlab-fontlabapp-kerning.batch]`, `tests/test_aliases.py::test_package_alias_when_real_provider_checkout_present_then_resolves_to_it[gp-fontlab_glyport-fontlab-glyport-affine]`, `tests/test_aliases.py::test_package_alias_when_real_provider_checkout_present_then_resolves_to_it[fp-fontlab_fontport-fontlab-fontport-errors]`, `tests/test_aliases.py::test_package_alias_when_real_provider_checkout_present_then_resolves_to_it[pens-fontlab_pens-fontlab-python-pens-recording]`, `tests/test_migrate_app_paths.py::test_rewrite_when_paths_overlap_then_preserve_boundaries_and_bindings`, `tests/test_migrate_app_paths.py::test_migrate_when_archive_present_then_leave_it_untouched`.
- [ ] Owner: confirm the PyPI publisher for `fontlab-fly` is configured for `fontlabcom/fontlab-fly`, workflow `release.yml`, environment `pypi`.
- [ ] After qualified main integration, inventory obsolete branches and files. Check worktree attachments and preserve unique work before removing verified stale items.
- [ ] After the owner lifts the private Pages hold, verify configuration, deployment and live `main:/docs` output.
- [ ] Keep Issue 123 paused until the owner resumes its existing acceptance backlog.
