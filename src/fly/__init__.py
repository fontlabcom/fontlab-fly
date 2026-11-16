# this_file: src/fly/__init__.py
"""Ten lazy aliases sharing exact canonical module objects."""
from __future__ import annotations

import sys
from importlib import import_module, util
from importlib.abc import Loader, MetaPathFinder
from importlib.machinery import ModuleSpec
from types import ModuleType
from typing import Any

ALIASES = {"fl": "echopy.fontlab", "fg": "echopy.fontgate", "tr": "typerig",
           "pr": "echopy.fontpr", "qt": "PythonQt", "ap": "fontlabapp", "qs": "pythonqtside",
           "gp": "fontlab_glyport", "fp": "fontlab_fontport", "pens": "fontlab_pens"}
__all__ = list(ALIASES)
_METADATA = ("__spec__", "__loader__", "__package__", "__path__", "__file__", "__cached__")


def _load(target: str, alias: str) -> ModuleType:
    try:
        return import_module(target)
    except ModuleNotFoundError as error:
        if error.name and (target == error.name or target.startswith(error.name + ".")):
            context = "native PythonQt inside FontLab" if alias == "qt" else f"the package providing {target}"
            raise ModuleNotFoundError(f"fly.{alias} requires {context}", name=error.name) from error
        raise


class _AliasLoader(Loader):
    def __init__(self, module: ModuleType) -> None:
        self.module = module
        self.metadata = {name: module.__dict__[name] for name in _METADATA if name in module.__dict__}

    def create_module(self, spec: ModuleSpec) -> ModuleType:
        return self.module

    def exec_module(self, module: ModuleType) -> None:
        for name in _METADATA:
            if name in self.metadata:
                module.__dict__[name] = self.metadata[name]
            else:
                module.__dict__.pop(name, None)


class _AliasFinder(MetaPathFinder):
    _fontlab_fly_alias = True

    def find_spec(self, fullname: str, path: Any = None, target: Any = None) -> ModuleSpec | None:
        if not fullname.startswith("fly."):
            return None
        alias, dot, suffix = fullname[4:].partition(".")
        if alias not in ALIASES:
            return None
        canonical = ALIASES[alias] + (dot + suffix if dot else "")
        module = _load(canonical, alias)
        return util.spec_from_loader(fullname, _AliasLoader(module), is_package=hasattr(module, "__path__"))


if not any(getattr(finder, "_fontlab_fly_alias", False) for finder in sys.meta_path):
    sys.meta_path.insert(0, _AliasFinder())


def __getattr__(name: str) -> ModuleType:
    if name not in ALIASES:
        raise AttributeError(name)
    module = import_module(__name__ + "." + name)
    globals()[name] = module
    return module


def __dir__() -> list[str]:
    return sorted(set(globals()) | set(ALIASES))
