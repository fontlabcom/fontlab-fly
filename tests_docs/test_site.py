# this_file: tests_docs/test_site.py
"""Check the actual generated payload, routes and public source boundaries."""
import hashlib
import json
import os
import shutil
import subprocess
import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'docs'
PREFIX = '/fontlab-fly/'
PAGES = ['index.html', 'installation/index.html', 'imports/index.html', 'development/index.html', 'licence/index.html']


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.tags = []
        self.ids = set()
        self.links = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append((tag, attrs))
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        for name in ('href', 'src'):
            if name in attrs:
                self.links.append(attrs[name])


class SiteTests(unittest.TestCase):
    def test_all_generated_internal_links_and_fragments_resolve(self):
        for path in SITE.rglob('*.html'):
            for link in Page(path.read_text()).links:
                url = urlsplit(link)
                if url.scheme or url.netloc:
                    continue
                target = unquote(url.path)
                if target.startswith('/'):
                    self.assertTrue(target.startswith(PREFIX), (path, link))
                    dest = SITE / target.removeprefix(PREFIX)
                else:
                    dest = path.parent / target if target else path
                if dest.is_dir():
                    dest = dest / 'index.html'
                self.assertTrue(dest.is_file(), (path, link, dest))
                self.assertTrue(dest.resolve().is_relative_to(SITE.resolve()), link)
                if url.fragment and dest.suffix == '.html':
                    self.assertIn(unquote(url.fragment), Page(dest.read_text()).ids, (path, link))

    def test_pages_have_fly_assets_fontlab_chrome_local_search_and_correct_canonical(self):
        for route in [*PAGES, '404.html']:
            page = Page((SITE / route).read_text())
            with self.subTest(route=route):
                self.assertFalse(any('assets/fly/' in link for link in page.links))
                for asset in ('fly.css', 'fly-bridge.js', 'fly.js'):
                    self.assertEqual(page.links.count('https://fontlab.dev/fontlab-www-docstheme/fly/latest/' + asset), 1)
                self.assertEqual(page.links.count('https://i.fontlab.com/menu/fontlab.js'), 1)
                menus = [attrs for tag, attrs in page.tags if tag == 'fontlab-menu']
                self.assertEqual(len(menus), 1)
                self.assertEqual(menus[0]['site-label'], 'Fly')
                self.assertEqual(menus[0]['mobile-menu'], 'materialx')
                self.assertEqual(menus[0]['mobile-search'], 'materialx')
                self.assertEqual([tag for tag, _ in page.tags if tag == 'fontlab-footer'], ['fontlab-footer'])
                self.assertEqual([attrs.get('data-md-color-scheme') for tag, attrs in page.tags if tag == 'body'], ['default'])
                search = [attrs for tag, attrs in page.tags if attrs.get('data-md-component') == 'search-query']
                self.assertEqual(len(search), 1)
                self.assertFalse(any(attrs.get('data-md-component') == 'palette' for _, attrs in page.tags))
                canonical = [attrs['href'] for tag, attrs in page.tags if attrs.get('rel') == 'canonical']
                expected = [] if route == '404.html' else [
                    'https://fontlabcom.github.io/fontlab-fly/' + route.removesuffix('index.html')]
                self.assertEqual(canonical, expected)

    def test_search_indexes_every_authored_page(self):
        search = json.loads((SITE / 'search/search_index.json').read_text())
        locations = {row['location'].split('#')[0] for row in search['docs']}
        self.assertEqual(locations, {'', 'installation/', 'imports/', 'development/', 'licence/'})
        text = ' '.join(row['text'] for row in search['docs'])
        for term in ('PythonQt', 'ModuleNotFoundError', 'fontlab_glyport', 'Apache'):
            self.assertIn(term, text)

    def test_attribution_downloads_are_exact_and_no_private_payload_is_published(self):
        for name in ('LICENSE', 'NOTICE'):
            self.assertEqual((ROOT / name).read_bytes(), (SITE / 'assets' / name).read_bytes())
        self.assertTrue((SITE / '.nojekyll').is_file())
        private_markers = (b'/Users/', b'/Volumes/', b'/private/', b'ghp_', b'github_pat_', b'-----BEGIN PRIVATE KEY-----')
        source = (ROOT / 'src/fly/__init__.py').read_bytes()
        for path in SITE.rglob('*'):
            if path.is_file():
                self.assertNotIn('.DS_Store', path.parts)
                self.assertNotIn(path.suffix, ('.py', '.pyi', '.vfpy', '.whl', '.zip'))
                payload = path.read_bytes()
                for marker in private_markers:
                    self.assertFalse(marker in payload, (path, marker))
                self.assertFalse(source in payload, path)

    def test_workflow_builds_every_main_push_and_requalifies_immutable_output(self):
        workflow = yaml.safe_load((ROOT / '.github/workflows/docs.yml').read_text())
        events = workflow.get('on', workflow.get(True))
        self.assertEqual(events['push'], {'branches': ['main']})
        self.assertNotIn('concurrency', workflow)
        build = workflow['jobs']['build']
        verify = workflow['jobs']['qualify-generated-output']
        self.assertNotIn('concurrency', build)
        self.assertEqual(verify['needs'], 'build')
        self.assertEqual(build['outputs']['epoch'], '${{ steps.epoch.outputs.value }}')
        for job, epoch in ((build, '${{ steps.epoch.outputs.value }}'), (verify, '${{ needs.build.outputs.epoch }}')):
            build_step = next(s for s in job['steps'] if s.get('run') == 'sh src_docs/build.sh')
            self.assertEqual(build_step['env']['SOURCE_DATE_EPOCH'], epoch)
        self.assertEqual(verify['steps'][0]['with']['ref'], '${{ needs.build.outputs.sha }}')
        self.assertEqual(verify['steps'][0]['with']['fetch-depth'], 2)
        lineage = next(step for step in verify['steps']
                       if step.get('name') == 'Verify immutable output lineage')
        self.assertEqual(lineage['env'], {
            'SOURCE_SHA': '${{ github.sha }}',
            'OUTPUT_SHA': '${{ needs.build.outputs.sha }}',
            'SOURCE_DATE_EPOCH': '${{ needs.build.outputs.epoch }}',
        })
        build_index = next(i for i, step in enumerate(verify['steps'])
                           if step.get('run') == 'sh src_docs/build.sh')
        self.assertLess(verify['steps'].index(lineage), build_index)
        self.assertEqual(verify['permissions'], {'contents': 'read'})
        for job in (build, verify):
            runs = '\n'.join(step.get('run', '') for step in job['steps'])
            self.assertIn('sh src_docs/build.sh', runs)
            self.assertIn('--require-hashes -r src_docs/requirements.txt', runs)
        self.assertIn('git diff --exit-code HEAD -- docs', '\n'.join(s.get('run', '') for s in verify['steps']))
        self.assertIn('git ls-files --others -- docs', '\n'.join(s.get('run', '') for s in verify['steps']))
        self.assertFalse(any('publish.sh' in s.get('run', '') for s in verify['steps']))

    def test_private_pages_hold_removes_automatic_request_and_permission(self):
        workflow = yaml.safe_load((ROOT / '.github/workflows/docs.yml').read_text())
        self.assertNotIn('pages', workflow['permissions'])
        for name, job in workflow['jobs'].items():
            with self.subTest(job=name):
                self.assertNotIn('pages', job['permissions'])
                commands = '\n'.join(step.get('run', '') for step in job['steps'])
                self.assertNotIn('request-pages.sh', commands)
                self.assertNotIn('/pages/builds', commands)

    def _qualification_git(self, repo: Path, env: dict[str, str], *args: str,
                           read_only: bool = False) -> str:
        """Use real fixture Git; read through a fresh matching private index."""
        git = shutil.which('git')
        assert git is not None, 'Git is required for qualification fixtures'
        with tempfile.TemporaryDirectory(dir=repo.parent) as temp:
            call_env = dict(env)
            if read_only:
                original = Path(env.get('GIT_INDEX_FILE', str(repo / '.git/index')))
                reader = Path(temp) / 'index'
                reader.touch(mode=0o600)
                shutil.copyfile(original, reader)
                call_env['GIT_INDEX_FILE'] = str(reader)
            result = subprocess.run([git, '-C', str(repo), *args], env=call_env,
                                    text=True, capture_output=True, check=True,
                                    stdin=subprocess.DEVNULL, timeout=10)
            return result.stdout.strip()

    def _qualification_state(self, repo: Path, env: dict[str, str]) -> dict[str, object]:
        """Include ignored worktree files, actual index and logical reader state."""
        files = {str(p.relative_to(repo)): [hashlib.sha256(p.read_bytes()).hexdigest(),
                                           p.stat().st_mode & 0o777]
                 for p in sorted(repo.rglob('*'))
                 if p.is_file() and '.git' not in p.relative_to(repo).parts}
        return {
            'head': self._qualification_git(repo, env, 'rev-parse', 'HEAD', read_only=True),
            'stage': self._qualification_git(repo, env, 'ls-files', '--stage', read_only=True),
            'flags': self._qualification_git(repo, env, 'ls-files', '-v', read_only=True),
            'actual_index': hashlib.sha256((repo / '.git/index').read_bytes()).hexdigest(),
            'exclude': (repo / '.git/info/exclude').read_text(),
            'worktree': files,
        }

    def _qualification_result(self, case: str) -> subprocess.CompletedProcess[str]:
        """Run the actual current YAML guards; an absent lineage step adds no code."""
        workflow = yaml.safe_load((ROOT / '.github/workflows/docs.yml').read_text())
        qualifiers = [job['steps'] for name, job in workflow['jobs'].items()
                      if name.startswith('qualify-')]
        self.assertEqual(len(qualifiers), 1)
        steps = qualifiers[0]
        parity = next(step['run'] for step in steps
                      if step.get('name') == 'Require committed output parity')
        lineage = [step['run'] for step in steps
                   if step.get('name') == 'Verify immutable output lineage']
        self.assertLessEqual(len(lineage), 1)
        guards = '\n'.join([*lineage, parity])
        with tempfile.TemporaryDirectory(dir=os.environ.get('TMPDIR')) as temp:
            repo = Path(temp) / 'repo'
            repo.mkdir()
            env = dict(os.environ, GIT_CONFIG_NOSYSTEM='1', GIT_CONFIG_GLOBAL=os.devnull,
                       GIT_OPTIONAL_LOCKS='0', GIT_AUTHOR_NAME='Fixture',
                       GIT_AUTHOR_EMAIL='fixture@example.invalid', GIT_COMMITTER_NAME='Fixture',
                       GIT_COMMITTER_EMAIL='fixture@example.invalid',
                       GIT_AUTHOR_DATE='2026-11-05T12:00:00Z',
                       GIT_COMMITTER_DATE='2026-11-05T12:00:00Z')
            env.pop('GIT_INDEX_FILE', None)
            self._qualification_git(repo, env, 'init', '-b', 'main')
            (repo / 'docs').mkdir()
            (repo / 'docs/index.html').write_text('committed source output')
            (repo / 'source.txt').write_text('source')
            self._qualification_git(repo, env, 'add', 'docs', 'source.txt')
            self._qualification_git(repo, env, 'commit', '-m', 'source')
            source = self._qualification_git(repo, env, 'rev-parse', 'HEAD', read_only=True)
            epoch = self._qualification_git(repo, env, 'show', '-s', '--format=%ct', 'HEAD',
                                            read_only=True)
            env.update(GIT_AUTHOR_DATE='2026-11-07T00:00:01Z',
                       GIT_COMMITTER_DATE='2026-11-07T00:00:01Z')
            if case == 'wrong-parent':
                self._qualification_git(repo, env, 'commit', '--allow-empty', '-m', 'other parent')
            if case in ('generated', 'wrong-output', 'wrong-parent', 'multiple-parent', 'non-doc'):
                (repo / 'docs/index.html').write_text('generated output')
                if case == 'non-doc':
                    (repo / 'source.txt').write_text('unexpected source change')
                self._qualification_git(repo, env, 'add', 'docs', 'source.txt')
                self._qualification_git(repo, env, 'commit', '-m', 'generated')
            if case == 'multiple-parent':
                child = self._qualification_git(repo, env, 'rev-parse', 'HEAD', read_only=True)
                tree = self._qualification_git(repo, env, 'rev-parse', 'HEAD^{tree}', read_only=True)
                merge = self._qualification_git(repo, env, 'commit-tree', tree,
                                                '-p', source, '-p', child, '-m', 'two parents')
                self._qualification_git(repo, env, 'checkout', '--detach', merge)
            if case == 'empty-child':
                self._qualification_git(repo, env, 'commit', '--allow-empty', '-m', 'empty child')
            if case == 'staged-docs':
                (repo / 'docs/index.html').write_text('staged drift')
                self._qualification_git(repo, env, 'add', 'docs')
            if case == 'ignored-extra':
                (repo / '.git/info/exclude').write_text('docs/ignored-extra.txt\n')
                (repo / 'docs/ignored-extra.txt').write_text('unexpected ignored payload')
            output = self._qualification_git(repo, env, 'rev-parse', 'HEAD', read_only=True)
            env.update(SOURCE_SHA=source, OUTPUT_SHA=source if case == 'wrong-output' else output,
                       SOURCE_DATE_EPOCH=str(int(epoch) + 1) if case == 'wrong-epoch' else epoch)
            reader = Path(temp) / 'guard.index'
            reader.touch(mode=0o600)
            shutil.copyfile(repo / '.git/index', reader)
            env['GIT_INDEX_FILE'] = str(reader)
            before = self._qualification_state(repo, env)
            reader_before = hashlib.sha256(reader.read_bytes()).hexdigest()
            self.assertEqual(reader_before, before['actual_index'],
                             'Guard reader must exactly retain the staged fixture index')
            result = subprocess.run(['bash', '--noprofile', '--norc', '-e', '-o', 'pipefail',
                                     '-c', guards], cwd=repo, env=env, text=True,
                                    capture_output=True, stdin=subprocess.DEVNULL, timeout=10,
                                    check=False)
            after = self._qualification_state(repo, env)
            print(json.dumps({'qualification_case': case, 'source': source, 'output': output,
                              'guard_env': {name: env[name] for name in
                                            ('SOURCE_SHA', 'OUTPUT_SHA', 'SOURCE_DATE_EPOCH')},
                              'guard_sha256': hashlib.sha256(guards.encode()).hexdigest(),
                              'before': before, 'after': after, 'exit': result.returncode,
                              'reader_before': reader_before,
                              'reader_after': hashlib.sha256(reader.read_bytes()).hexdigest(),
                              'stdout': result.stdout, 'stderr': result.stderr}), flush=True)
            self.assertEqual(before, after, f'{case}: qualification must preserve fixture state')
            return result

    def test_qualification_accepts_valid_committed_output(self) -> None:
        for case in ('source', 'generated'):
            with self.subTest(case=case):
                result = self._qualification_result(case)
                self.assertEqual(result.returncode, 0, f'{case}: {result.stderr}')

    def test_qualification_rejects_invalid_git_states(self) -> None:
        for case in ('staged-docs', 'ignored-extra', 'wrong-output', 'wrong-parent',
                     'multiple-parent', 'non-doc', 'empty-child', 'wrong-epoch'):
            with self.subTest(case=case):
                result = self._qualification_result(case)
                self.assertNotEqual(result.returncode, 0,
                                    f'{case}: actual workflow qualification accepted invalid state')
