# this_file: examples/native_smoke.py
"""Run inside FontLab with all target distributions installed."""
import importlib

import fly

for alias, target in fly.ALIASES.items():
    assert getattr(fly, alias) is importlib.import_module(target)
    assert importlib.import_module('fly.' + alias) is getattr(fly, alias)
assert 'app' not in vars(fly.ap)
print(f'All {len(fly.ALIASES)} exact aliases passed')
