# this_file: tests/test_packaging.py
"""Built wheels retain the alias loader's licence and provenance."""
import subprocess
from email.parser import BytesParser
from pathlib import Path
from zipfile import ZipFile


def test_wheel_when_built_then_includes_declared_licence_and_notice(tmp_path):
    root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        ['uv', 'build', '--wheel', '--out-dir', str(tmp_path)],
        cwd=root, capture_output=True, text=True, timeout=60, check=False,
    )
    assert result.returncode == 0, result.stderr
    wheels = list(tmp_path.glob('*.whl'))
    assert len(wheels) == 1, f'Expected one wheel, got {wheels}'
    with ZipFile(wheels[0]) as wheel:
        metadata_path = next(name for name in wheel.namelist() if name.endswith('.dist-info/METADATA'))
        metadata = BytesParser().parsebytes(wheel.read(metadata_path))
        for filename in ('LICENSE', 'NOTICE'):
            path = metadata_path.removesuffix('METADATA') + 'licenses/' + filename
            assert path in wheel.namelist(), f'Wheel omits {filename}'
            assert wheel.read(path) == (root / filename).read_bytes(), f'Wheel changes {filename}'
            assert filename in metadata.get_all('License-File', []), f'Metadata omits {filename}'
