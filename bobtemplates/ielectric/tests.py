import unittest2 as unittest
import os
import tempfile
import shutil

from scripttest import TestFileEnvironment


class BaseTemplateTest(unittest.TestCase):

    def setUp(self):
        self.tempdir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tempdir)

        # docs http://pythonpaste.org/scripttest/
        self.env = TestFileEnvironment(os.path.join(self.tempdir,
                                                    'test-output'),
                                       ignore_hidden=False)

        config_file = tempfile.mkstemp()
        with open(config_file, 'w') as f:
            f.write(self.config)
        self.addCleanup(os.remove, config_file)

        root_dir = os.path.join(os.path.dirname(__file__), '../', '../',)
        self.result = self.env.run('%s/bin/mrbob %s --config %s'
                                   % (root_dir, self.template, config_file))


class PyramidTempalteTest(BaseTemplateTest):
    template = 'pyramid'
    config = """
[questions]
    """

    def test_everything(self):
        self.assertEqual(
            self.result.files_created.keys(),
            set([
                'bootstrap.py',
                'buildout.cfg',
                'buildout.d',
                'buildout.d/base.cfg',
                'buildout.d/development.cfg',
                'buildout.d/production.cfg',
                'buildout.d/staging.cfg',
                'buildout.d/versions.cfg',
                'docs',
                'docs/api.rst',
                'docs/conf.py',
                'docs/glossary.rst',
                'docs/index.rst',
                'docs/intro.rst',
                'etc',
                'etc/babel_extractors.ini',
                'etc/development.ini.in',
                'etc/nginx.conf.in',
                'etc/production.ini.in',
                '.gitignore',
                'HISTORY.rst',
                'LICENSE',
                'MANIFEST.in',
                '.pep8',
                'pre-commit-check.sh',
                'README.rst',
                'setup.cfg',
                'setup.py',
                'src',
                'src/proj',
                'src/proj/alembic',
                'src/proj/alembic/env.py',
                'src/proj/alembic/script.py.mako',
                'src/proj/alembic/versions',
                'src/proj/alembic/versions/b219e55ed26_initial_structure.py',
                'src/proj.egg-info',
                'src/proj.egg-info/dependency_links.txt',
                'src/proj.egg-info/entry_points.txt',
                'src/proj.egg-info/not-zip-safe',
                'src/proj.egg-info/PKG-INFO',
                'src/proj.egg-info/requires.txt',
                'src/proj.egg-info/SOURCES.txt',
                'src/proj.egg-info/top_level.txt',
                'src/proj/__init__.py',
                'src/proj/locale',
                'src/proj/locale/proj.pot',
                'src/proj/scripts',
                'src/proj/scripts/__init__.py',
                'src/proj/scripts/migrate_database.py',
                'src/proj/site',
                'src/proj/site/__init__.py',
                'src/proj/site/models.py',
                'src/proj/site/static',
                'src/proj/site/static/style.css',
                'src/proj/site/templates',
                'src/proj/site/templates/index.jinja2',
                'src/proj/site/tests',
                'src/proj/site/tests/__init__.py',
                'src/proj/site/tests/test_views.py',
                'src/proj/site/views.py',
                'src/proj/testing.py',
                'src/proj/tests.py',
                '.travis.yml',
                ])
        )

        self.env.run('python bootstrap.py',
                     cwd=os.path.join(self.env.cwd, 'proj'),
                     expect_stderr=True)
        self.env.run('bin/buildout',
                     cwd=os.path.join(self.env.cwd, 'proj'),
                     expect_stderr=True)
        self.env.run('./pre-commit-check.sh',
                     cwd=os.path.join(self.env.cwd, 'proj'),
                     expect_stderr=True)


class DistributePackageTempalteTest(BaseTemplateTest):
    template = 'distribute'
    config = """
[questions]
    """

    def test_everything(self):
        self.assertEqual(
            set(self.result.files_created.keys()),
            set([
                'docs',
                '.gitignore',
                'HISTORY.rst',
                'LICENSE',
                'MANIFEST.in',
                '.pep8',
                'pre-commit-check.sh',
                'proj',
                'proj.egg-info',
                'proj.egg-info/dependency_links.txt',
                'proj.egg-info/entry_points.txt',
                'proj.egg-info/not-zip-safe',
                'proj.egg-info/PKG-INFO',
                'proj.egg-info/requires.txt',
                'proj.egg-info/SOURCES.txt',
                'proj.egg-info/top_level.txt',
                'proj/__init__.py',
                'README.rst',
                'setup.cfg',
                'setup.py',
                '.travis.yml',
                ]))
