---
this_file: src_docs/md/development.md
---

# Development

Fly's runtime is in `src/fly`; `tests` checks aliases, migration helpers and
licence packaging. `examples/native_smoke.py` is a host smoke example.
It requires FontLab and all providers; do not run it as a standalone native test.

## Host-free tests

After preparing the [standalone environment](installation.md#standalone-development),
run from the checkout:

```sh
./test.sh -q -p no:cacheprovider
```

The script uses `uv run --no-sync`: pytest must already be installed. The
packaging test builds an actual wheel and verifies the exact Apache licence,
NOTICE and licensing metadata. Alias tests use stand-in modules, preserving the
boundary between routing checks and real provider behavior.

Current native acceptance must check all ten aliases, both import forms,
canonical metadata and child imports against the final artifacts. Active-font
Feature workflows additionally need owned fonts and Apply/Undo/Redo/save/reopen
proof. Those are separate from this website build.

## Build these pages

Build from the repository root in a separate Python 3.13 environment.

```sh
uv venv --python 3.13 .docs-venv
uv pip install --python .docs-venv/bin/python --require-hashes -r src_docs/requirements.txt
export PATH="$PWD/.docs-venv/bin:$PATH"
sh src_docs/build.sh
python -m unittest discover -s tests_docs -v
```

ProperDocs reads `src_docs/mkdocs.yml` and the Markdown in `src_docs/md`, then
rebuilds `docs/` in strict mode. The theme, fly-january 0.4.0 or later (remote theme assets), supplies the FontLab
menu and footer. The menu labels this guide `Fly`. Search uses MaterialX's local index.
`src_docs/build.sh` defaults `SOURCE_DATE_EPOCH` to the checkout's commit timestamp.
CI captures the source commit's timestamp once and passes it to both builds;
the generated commit's timestamp and later UTC dates do not change the output.

## Main-branch automation

Every push to `main` starts the repository's documentation workflow, including
code-only changes. A first job builds and checks the source commit. If it is
still current, it commits only changed generated `docs` and pushes normally.
A stale run leaves current main untouched; a push failure is a failed run.

A dependent job checks out the resulting immutable commit, rebuilds the entire
site, and requires byte-identical generated output. This second build also
qualifies generated bot commits, whose token push does not recursively trigger
another workflow. Unchanged output keeps the original commit and still gets the
full verification. A passing build qualifies source and output, not deployment.

## Publication hold

Private-repository Pages publication is held by the owner: the current account
plan does not support this private site, and no public site has been deployed.
The workflow has no Pages write permission or automatic Pages request. Main-branch
source work and generated-docs commits continue under that hold.

`src_docs/request-pages.sh` remains test-covered and dormant for qualified public
reuse or future explicitly authorized publication. Do not invoke it or wire it
into private delivery while the hold applies. Its local mocked tests remain part
of the suite; they do not contact GitHub or establish a real deployment.

Any later authorized publication needs actual branch-source `main:/docs` settings,
a qualified deployment SHA and live verification. The helper's Pages API builds
the latest default branch and cannot atomically target an arbitrary SHA; existing
head checks expose concurrent changes but cannot revoke a queued build.
