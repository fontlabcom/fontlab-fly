# this_file: tests/test_dependency_floors.py
"""Fly's canonical alias targets require the package layout introduced in 1.2."""

import tomllib
from pathlib import Path


def test_dependencies_when_read_then_layout_targets_require_1_2_0():
    config = tomllib.loads((Path(__file__).parents[1] / "pyproject.toml").read_text())
    dependencies = config["project"]["dependencies"]
    for name in ("fontlab-fontlabapp", "fontlab-glyport", "fontlab-fontport"):
        assert f"{name}>=1.2.0" in dependencies, f"{name} needs the 1.2 layout"
    for name in ("fontlab-echopy", "typerig", "pythonqtside"):
        assert f"{name}>=0.1.0" in dependencies, f"{name}'s floor must stay unchanged"
    assert "fontlab-python-pens>=1.0.0" in dependencies
    assert config["tool"]["fontlab-install"].get("dependencies", dependencies) == dependencies
