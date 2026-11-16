# this_file: tests/test_aliases.py
"""Exact alias identities and canonical import metadata, independent of host."""
import importlib
import subprocess
import sys
import types
from pathlib import Path

import pytest

TARGETS = {'fl':'echopy.fontlab','fg':'echopy.fontgate','tr':'typerig','pr':'echopy.fontpr','qt':'PythonQt','ap':'fontlabapp','qs':'pythonqtside','gp':'fontlab_glyport','fp':'fontlab_fontport','pens':'fontlab_pens'}


def test_import_fly_is_lazy_in_fresh_process():
    result = subprocess.run([sys.executable,'-c',"import sys, fly; assert not any(name in sys.modules for name in ['echopy','typerig','PythonQt','fontlabapp','pythonqtside','fontlab_glyport','fontlab_fontport','fontlab_pens'])"],capture_output=True,text=True,check=False)
    assert result.returncode == 0, result.stderr


@pytest.mark.parametrize('alias,target', TARGETS.items())
def test_exact_alias_from_and_import_preserve_target_metadata(monkeypatch,alias,target):
    import fly
    for name in list(sys.modules):
        if name == 'fly.'+alias or name.startswith('fly.'+alias+'.'):
            monkeypatch.delitem(sys.modules,name)
    monkeypatch.delitem(vars(fly),alias,raising=False)
    native = types.ModuleType(target)
    native.__spec__ = None
    native.__loader__ = None
    native.__package__ = target.rpartition('.')[0]
    monkeypatch.setitem(sys.modules,target,native)
    namespace = {}
    exec('from fly import '+alias,namespace)  # noqa: S102 - exercise from-import syntax for each fixed alias.
    assert namespace[alias] is native
    assert importlib.import_module('fly.'+alias) is native
    assert getattr(fly,alias) is native
    assert native.__spec__ is None and native.__loader__ is None
    assert native.__package__ == target.rpartition('.')[0]


def test_missing_qt_has_contextual_error_and_internal_dependency_is_preserved(monkeypatch):
    import fly
    monkeypatch.delitem(vars(fly),'qt',raising=False)
    monkeypatch.delitem(sys.modules,'fly.qt',raising=False)
    monkeypatch.delitem(sys.modules,'PythonQt',raising=False)
    with pytest.raises(ModuleNotFoundError,match='FontLab'):
        _ = fly.qt
    def fail(name):
        raise ModuleNotFoundError('inner dependency missing',name='inner_dependency')
    monkeypatch.setattr(fly,'import_module',fail)
    with pytest.raises(ModuleNotFoundError) as error:
        fly._load('typerig','tr')
    assert error.value.name == 'inner_dependency'


def test_reloading_fly_does_not_duplicate_import_finder():
    import fly
    importlib.reload(fly)
    importlib.reload(fly)
    assert sum(bool(getattr(finder, '_fontlab_fly_alias', False)) for finder in sys.meta_path) == 1


@pytest.mark.parametrize('alias,target', [('gp', 'fontlab_glyport'), ('fp', 'fontlab_fontport'), ('pens', 'fontlab_pens')])
def test_package_alias_when_imported_first_then_children_keep_canonical_identity(tmp_path, alias, target):
    package = tmp_path / target
    package.mkdir()
    (package / '__init__.py').write_text('', encoding='utf-8')
    (package / 'child.py').write_text('VALUE = 42\n', encoding='utf-8')
    code = f"""
import importlib, sys
sys.path.insert(0, {str(tmp_path)!r})
import fly.{alias}
from fly import {alias}
canonical = importlib.import_module({target!r})
assert {alias} is canonical
assert canonical.__name__ == {target!r}
assert canonical.__spec__.name == {target!r}
assert canonical.__package__ == {target!r}
assert importlib.import_module('fly.{alias}.child') is importlib.import_module('{target}.child')
child = {alias}.child
assert child.VALUE == 42
assert child.__name__ == child.__spec__.name == '{target}.child'
assert child.__package__ == {target!r}
assert {alias!r} in fly.__all__ and {alias!r} in dir(fly)
"""
    result = subprocess.run([sys.executable, '-c', code], capture_output=True, text=True, check=False)
    assert result.returncode == 0, result.stderr


@pytest.mark.parametrize('alias,target', [('gp', 'fontlab_glyport'), ('fp', 'fontlab_fontport'), ('pens', 'fontlab_pens')])
def test_missing_package_alias_when_accessed_then_error_names_target(monkeypatch, alias, target):
    import fly

    original_import = fly.import_module

    def fail(name):
        if name == target:
            raise ModuleNotFoundError('target missing', name=target)
        return original_import(name)

    monkeypatch.delitem(vars(fly), alias, raising=False)
    monkeypatch.delitem(sys.modules, 'fly.' + alias, raising=False)
    monkeypatch.setattr(fly, 'import_module', fail)
    with pytest.raises(ModuleNotFoundError, match=f'fly.{alias} requires.*{target}') as error:
        getattr(fly, alias)
    assert error.value.name == target


def test_alias_table_when_compared_to_reviewed_providers_then_exactly_ten_and_equal():
    import fly
    assert fly.ALIASES == TARGETS, "a provider migration must update the reviewed table and this pin together"
    assert fly.__all__ == list(TARGETS) and len(TARGETS) == 10


SIBLINGS = Path(__file__).resolve().parents[2]
REAL_PROVIDERS = [
    ('ap', 'fontlabapp', 'fontlab-fontlabapp', 'kerning.batch'),
    ('gp', 'fontlab_glyport', 'fontlab-glyport', 'affine'),
    ('fp', 'fontlab_fontport', 'fontlab-fontport', 'errors'),
    ('pens', 'fontlab_pens', 'fontlab-python-pens', 'recording'),
]


@pytest.mark.parametrize('alias,target,repository,child', REAL_PROVIDERS)
def test_package_alias_when_real_provider_checkout_present_then_resolves_to_it(alias, target, repository, child):
    """Resolve against the current App/Glyport/Fontport/Pens source heads, not stand-ins."""
    source = SIBLINGS / repository / 'src'
    if not (source / target / '__init__.py').is_file():
        pytest.skip(f'{repository} sibling checkout is not present')
    fly_source = Path(__file__).resolve().parents[1] / 'src'
    code = f"""
import importlib, sys
sys.path[:0] = [{str(fly_source)!r}, {str(source)!r}]
import fly
from fly import {alias}
canonical = importlib.import_module({target!r})
assert {alias} is canonical is fly.{alias}, 'alias is not the canonical provider'
assert canonical.__file__.startswith({str(source / target)!r}), canonical.__file__
assert importlib.import_module('fly.{alias}.{child}') is importlib.import_module('{target}.{child}')
if {alias!r} == 'pens':
    assert canonical.__all__, 'provider must expose its public pen API'
    for name in canonical.__all__:
        assert getattr({alias}, name) is getattr(canonical, name), name
    recording = {alias}.RecordingPen()
    transformed = {alias}.TransformPen(recording, (2, 0, 0, 3, 10, 20))
    transformed.moveTo((1, 2))
    transformed.lineTo((3, 4))
    transformed.closePath()
    assert recording.value == [('moveTo', ((12, 26),)), ('lineTo', ((16, 32),)), ('closePath', ())]
"""
    result = subprocess.run([sys.executable, '-I', '-c', code], capture_output=True, text=True, check=False)
    assert result.returncode == 0, result.stderr
