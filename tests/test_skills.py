# this_file: tests/test_skills.py
"""Current executable teaching selects FontLab APIs through Fly."""

import ast
from pathlib import Path


def test_remote_metrics_when_python_fence_parsed_then_bridge_uses_fly():
    skill = Path(__file__).parents[1] / "skills/fontlab-remote/SKILL.md"
    source = skill.read_text().split("```python\n", 1)[1].split("\n```", 1)[0]
    metrics = next(
        node
        for node in ast.walk(ast.parse(source))
        if isinstance(node, ast.FunctionDef) and node.name == "metrics"
    )
    imports = [node for node in metrics.body if isinstance(node, ast.ImportFrom)]
    assert len(imports) == 1
    assert imports[0].module == "fly"
    assert [(alias.name, alias.asname) for alias in imports[0].names] == [("pr", None)]
    result = next(node for node in metrics.body if isinstance(node, ast.Return))
    assert ast.unparse(result.value) == "pr.get_glyph_metrics(glyph_name=name)"
