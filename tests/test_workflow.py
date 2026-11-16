# this_file: tests/test_workflow.py
"""Keep the CI test workflow's deselect list honest and documented."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / '.github' / 'workflows' / 'tests.yml'


def _deselected():
    return re.findall(r'--deselect "([^"]+)"', WORKFLOW.read_text(encoding='utf-8'))


def test_workflow_when_deselecting_then_each_node_id_exists_and_is_named_in_todo():
    todo = (ROOT / 'TODO.md').read_text(encoding='utf-8')
    ids = _deselected()
    assert len(ids) == 6, ids
    for node in ids:
        path, name = node.split('::', 1)
        source = (ROOT / path).read_text(encoding='utf-8')
        assert re.search(rf'def {re.escape(name.split("[")[0])}\(', source), f'{node} no longer exists'
        assert node in todo, f'{node} is deselected in CI but not named in TODO.md'


def test_workflow_when_run_then_read_only_single_job_and_rejects_skips():
    text = WORKFLOW.read_text(encoding='utf-8')
    assert 'contents: read' in text and not re.search(r': write\b', text)
    assert text.count('runs-on:') == 1 and 'matrix' not in text and 'secrets' not in text
    assert 'set -eo pipefail' in text and 'grep -q "SKIPPED"' in text and 'pytest==8.4.2' in text
