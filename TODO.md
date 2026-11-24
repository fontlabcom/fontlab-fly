---
this_file: TODO.md
---

- [ ] Issue 271: independently review and integrate the generated installer through repository gates, verify exact-SHA CI/archives, and qualify macOS/Windows native execution after serialized admission.



# Next steps (functional first)

1. Row 'Issue 255' below: verify the ten aliases from the released wheel/sdist in FontLab 9 (blocked on D43 admission and the native queue).
2. Reconcile Script/example setup with Fly/provider imports (source, no native needed).
3. Verify Feature scripts on owned fonts (live).
4. Issue 254 native check (owner).
5. Everything else (branch inventory, Pages hold) is housekeeping.

# Open tasks

- [ ] Reconcile affected Script and example setup with matching Fly/provider imports and explicit child paths; use focused alias/identity checks before the detailed installed/native pass.

- [ ] Issue 255: After explicit D43 recovery and admission, verify all ten aliases, both import forms, canonical metadata and child imports from the released wheel/sdist in FontLab arm64 Python 3.11; record host build, hashes and loaded paths. The 2026-11-13 attempt is pending: the shared runner returned exit 79 for an earlier timed-out native run with unknown status; preserve the busy fence until its owner reconciles it.

- [ ] Keep private Pages configuration/deployment and live main:/docs acceptance held until the owner explicitly lifts the publication hold.

- [ ] After qualified main integration, inventory obsolete branches/files, preserve unique work and remove only proven stale items with recovery evidence.

- [ ] Verify Feature scripts on owned fonts through `fly.ap.fontui.feature_blocks` and explicit `fly.ap` submodule imports; record Apply/Undo/Redo/save/reopen evidence with the consuming repositories.

- [ ] Issue 254 native check (owner): after the App `install.vfpy` (main at or after 5cac0d6), confirm in FontLab 9 that the nine Fly aliases still resolve and `install.vfpy` from this repository is byte-identical to the App copy (`tools/check_install_copies.py` in the App).

- [ ] Low priority, kept because `tests/test_workflow.py` requires every CI-deselected node id to be named here. Passed locally against real siblings on 2026-11-12 (see CHANGELOG 2026-11-17 entry); rerun only after a sibling changes. The GitHub `Tests` workflow runs only the host-free tests because the App, Glyport, Fontport and Pens siblings are private. Run these deselected tests locally with siblings checked out (the first four need the real providers, the last two need an App checkout): `tests/test_aliases.py::test_package_alias_when_real_provider_checkout_present_then_resolves_to_it[ap-fontlabapp-fontlab-fontlabapp-kerning.batch]`; `tests/test_aliases.py::test_package_alias_when_real_provider_checkout_present_then_resolves_to_it[gp-fontlab_glyport-fontlab-glyport-affine]`; `tests/test_aliases.py::test_package_alias_when_real_provider_checkout_present_then_resolves_to_it[fp-fontlab_fontport-fontlab-fontport-errors]`; `tests/test_aliases.py::test_package_alias_when_real_provider_checkout_present_then_resolves_to_it[pens-fontlab_pens-fontlab-python-pens-recording]`; `tests/test_migrate_app_paths.py::test_rewrite_when_paths_overlap_then_preserve_boundaries_and_bindings`; `tests/test_migrate_app_paths.py::test_migrate_when_archive_present_then_leave_it_untouched`. Last local run with real siblings (2026-11-12, Fly `3763ccc`, App `2fc2f07`, Glyport `10b6975`, Fontport `1c8e1ca`): all five passed, and the full suite gave 30 passed. Add them to CI once the siblings are reachable; rerun locally after a sibling changes.
