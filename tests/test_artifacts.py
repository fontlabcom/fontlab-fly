# this_file: tests/test_artifacts.py
"""Built sdist and wheel contents, and the installed wheel's ten aliases, host-free."""
import subprocess
import sys
import tarfile
import textwrap
from email.parser import BytesParser
from pathlib import Path
from zipfile import ZipFile

import pytest

ROOT = Path(__file__).resolve().parents[1]
ALIASES = {'fl': 'echopy.fontlab', 'fg': 'echopy.fontgate', 'tr': 'typerig', 'pr': 'echopy.fontpr',
           'qt': 'PythonQt', 'ap': 'fontlabapp', 'qs': 'pythonqtside', 'gp': 'fontlab_glyport',
           'fp': 'fontlab_fontport', 'pens': 'fontlab_pens'}
SDIST_ENTRIES = {'install.vfpy', 'src', 'tests', 'examples', 'skills', 'pyproject.toml', 'README.md', 'PLAN.md',
                      'TODO.md', 'LICENSE', 'NOTICE', 'CHANGELOG.md', 'DEPENDENCIES.md', 'test.sh',
                      '.gitignore'}  # hatchling always adds .gitignore


def _run(*cmd, cwd=ROOT, env=None):
    result = subprocess.run(cmd, cwd=cwd, env=env, capture_output=True, text=True, timeout=180, check=False)
    assert result.returncode == 0, f'{cmd}: {result.stdout}\n{result.stderr}'
    return result


@pytest.fixture(scope='module')
def dist(tmp_path_factory):
    out = tmp_path_factory.mktemp('dist')
    _run('uv', 'build', '--out-dir', str(out))
    (sdist,) = out.glob('*.tar.gz')
    (wheel,) = out.glob('*.whl')
    return sdist, wheel


def test_wheel_when_built_then_ships_only_the_fly_package_and_metadata(dist):
    with ZipFile(dist[1]) as wheel:
        names = wheel.namelist()
    outside = [n for n in names if not (n.startswith('fly/') or '.dist-info/' in n)]
    assert outside == [], f'Wheel carries files outside fly/ and dist-info: {outside}'
    assert 'fly/__init__.py' in names


def test_wheel_when_built_then_metadata_declares_the_seven_provider_dependencies(dist):
    with ZipFile(dist[1]) as wheel:
        path = next(n for n in wheel.namelist() if n.endswith('.dist-info/METADATA'))
        metadata = BytesParser().parsebytes(wheel.read(path))
    requires = {r.split('>')[0].split(';')[0].strip() for r in metadata.get_all('Requires-Dist', []) if 'extra' not in r}
    assert requires == {'fontlab-echopy', 'typerig', 'fontlab-fontlabapp', 'pythonqtside',
                        'fontlab-glyport', 'fontlab-fontport', 'fontlab-python-pens'}
    assert 'fontlab-python-pens>=1.0.0' in metadata.get_all('Requires-Dist', [])
    assert metadata['Name'] == 'fontlab-fly' and metadata['License-Expression'] == 'Apache-2.0'


def test_sdist_when_built_then_contains_only_declared_top_level_entries(dist):
    with tarfile.open(dist[0]) as sdist:
        names = sdist.getnames()
    top = {n.split('/', 2)[1] for n in names if n.count('/') >= 1 and n.split('/', 2)[1]}
    expected = SDIST_ENTRIES | {'PKG-INFO'}
    assert top == expected, f'sdist missing {expected - top}, unexpected {top - expected}'
    assert not any('/src_docs/' in n or '/docs/' in n for n in names), 'Website sources leaked into the sdist'
    for required in ('src/fly/__init__.py', 'LICENSE', 'NOTICE', 'tests/test_aliases.py'):
        assert any(n.endswith('/' + required) for n in names), f'sdist omits {required}'


def test_sdist_when_built_then_preserves_the_installer_bytes(dist):
    with tarfile.open(dist[0]) as sdist:
        installer = sdist.getnames()[0].split('/')[0] + '/install.vfpy'
        assert sdist.extractfile(installer).read() == (ROOT / 'install.vfpy').read_bytes()


def test_installed_wheel_when_providers_are_stubs_then_all_ten_aliases_resolve_exactly(dist, tmp_path):
    venv = tmp_path / 'venv'
    _run('uv', 'venv', '--python', sys.executable, str(venv))
    python = venv / 'bin' / 'python'
    _run('uv', 'pip', 'install', '--python', str(python), '--no-deps', str(dist[1]))
    stubs = tmp_path / 'stubs'
    for target in ALIASES.values():
        parts = target.split('.')
        for i in range(1, len(parts) + 1):
            pkg = stubs.joinpath(*parts[:i])
            pkg.mkdir(parents=True, exist_ok=True)
            (pkg / '__init__.py').touch()
    probe = textwrap.dedent(f'''
        import importlib, sys
        import fly
        assert 'site-packages' in fly.__file__, fly.__file__
        assert not any(m in sys.modules for m in ('echopy', 'typerig', 'PythonQt', 'fontlabapp', 'pythonqtside', 'fontlab_glyport', 'fontlab_fontport', 'fontlab_pens'))
        for alias, target in {ALIASES!r}.items():
            mod = importlib.import_module('fly.' + alias)
            assert mod is importlib.import_module(target), alias
            assert getattr(fly, alias) is mod and sorted(fly.__all__) == sorted({list(ALIASES)!r})
        print('ok')
    ''')
    env = {'PATH': '/usr/bin:/bin', 'PYTHONPATH': str(stubs)}
    assert _run(str(python), '-c', probe, cwd=tmp_path, env=env).stdout.strip() == 'ok'
