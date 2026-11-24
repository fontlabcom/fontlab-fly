---
this_file: PLAN.md
---

# Remaining work

## Providers and consumers

Keep Fly's ten aliases lazy. Each must return the canonical provider object with its metadata and explicit child imports intact. App owns shared UI and Feature helpers, Fontport owns fontParts/UFO support, and Glyport owns Glyphs.app compatibility. Address consumer setup failures with the affected provider, preserving dependency direction.

When a provider or consuming Script changes, compare the affected examples with the App and Pens imports and rerun the relevant sibling tests locally. Enable the six cases listed in TODO when CI can check out their repositories.

## FontLab acceptance

- Issue 255 requires explicit D43 recovery and admission after the runner returned exit 79. Use the serialized native runner for both released formats on arm64 Python 3.11. Check all ten aliases through both import forms, canonical metadata, and child-module identity. Record artifact hashes, host build and loaded paths to detect shadowing by editable installs.
- For Issue 254, compare the current Fly and App installer bytes with the App's comparison tool. Cover the post-install alias check in the Issue 255 run.
- For Issue 271, confirm independent installer cohort review and run the released installer in FontLab on macOS and Windows once the native queue admits each run.
- Verify the adapted Feature scripts on a test font using `fly.ap.fontui.feature_blocks` and explicit App child imports. Keep Apply, Undo, Redo, save and reopen results with the consuming repositories.

## Release, cleanup and holds

- The PyPI project owner confirms the Trusted Publisher for `fontlabcom/fontlab-fly`, workflow `release.yml`, environment `pypi`.
- After qualified main integration, inspect current branch and worktree attachments before removing stale branches or files. Preserve recoverable unique work.
- Private Pages configuration, deployment and live `main:/docs` acceptance await the owner's release of the publication hold.
- Issue 123 and its acceptance backlog remain paused until the owner resumes them.

Use the README's arm64 Python 3.11 recipe for source tests. Preserve the 80% gate for each complete changed production module, independent milestone review and required delivery hooks. Verify release artifacts, ordinary installations and native execution on their respective targets.
