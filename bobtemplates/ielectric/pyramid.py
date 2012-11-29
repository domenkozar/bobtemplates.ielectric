import copy
import os
import shutil

from templer.core.base import BaseTemplate, LICENSE_CATEGORIES
from templer.core.basic_namespace import LICENSE_DICT
from templer.core.vars import (
    BooleanVar,
    EASY,
    EXPERT,
    ALL,
    StringVar,
    StringChoiceVar,
)


class Pyramid(BaseTemplate):
    _template_dir = 'templates/pyramid'
    summary = "A Pyramid skeleton"
    help = """
    Pyramid skeleton with Buildout, SQLAlchemy, Sphinx, Nose, Travis-CI,
"""
    category = "iElectric set"
    use_cheetah = True
    post_run_msg = """
Before using your package, you must configure the following:

- Enable travis-ci and readthedocs.org git hook on github

- Configure database url and sentry dsn in buildout.d/production.cfg
"""

    def post(self, command, output_dir, vars):
        source = os.path.join(output_dir, 'docs', 'LICENSE.txt')
        dist = os.path.join(output_dir, 'LICENSE')
        shutil.move(source, dist)
        # see https://github.com/collective/templer.core/issues/5
        os.chmod(os.path.join(output_dir, 'pre-commit-check.sh'), 0754)
        super(Pyramid, self).post(command, output_dir, vars)

    vars = copy.deepcopy(BaseTemplate.vars)
    vars += [
        StringVar(
            'projectname',
            title='Project name',
            description='Full name of the project',
            page='Metadata',
            help="""
"""
        ),
        StringVar(
            'project',
            title='Package name',
            description='Python package name',
            page='Metadata',
            help="""
"""
        ),
        StringVar(
            'version',
            title='Version',
            description='Version number for project',
            default='0.1',
            page='Metadata',
            help="""
This becomes the version number of the created package. It will be set
in the egg's setup.py, and may be referred to in other places in the
generated project.
"""
        ),
        StringVar(
            'description',
            title='Description',
            description='One-line description of the project',
            default='',
            page='Metadata',
            help="""
This should be a single-line description of your project. It will be
used in the egg's setup.py, and, for Zope/Plone projects, may be used
in the GenericSetup profile description.
"""
        ),
        StringVar(
            'author',
            title='Author',
            description='Name of author for project',
            modes=(),
            page='Metadata',
            help="""
This should be the name of the author of this project. It will be used
in the egg's setup.py, and, for some templates, in the generated
documentation/README files.
"""
        ),
        StringVar(
            'author_email',
            title='Author Email',
            description='Email of author for project',
            page='Metadata',
            help="""
This should be the name of the author of this project. It will be used
in the egg's setup.py, and, for some templates, in the generated
documentation/README files.
"""
        ),
        StringVar(
            'url',
            title='Project URL',
            description='URL of the homepage for this project',
            page='Metadata',
            help="""
This should be a URL for the homepage for this project (if applicable).
It will be used in the egg's setup.py.
"""
        ),
        StringVar(
            'repo',
            title='Source code repository',
            description='URL to the source code repository',
            page='Metadata',
            help="""
This should be a URL for the homepage for this project (if applicable).
It will be used in the egg's setup.py.
"""
        ),
        StringChoiceVar(
            'license',
            title='Project License',
            description='Name of license for the project',
            default='BSD',
            page='Metadata',
            choices=LICENSE_CATEGORIES.keys(),
            structures=LICENSE_DICT,
            help="""
The license that this project is issued under. It will be used in the
egg's setup.py.

Common choices here are 'GPL' (for the GNU General Public License),
'ZPL' (for the Zope Public License', or 'BSD' (for the BSD license).

%s

""" % BaseTemplate('null').readable_license_options()
        ),
        StringVar(
            'docs_url',
            title='Full URL to documentation',
            description='URL of the hosted documentation of the project',
            page='Metadata',
            help="""""",
        ),
    ]
