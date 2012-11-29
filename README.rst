This is my personal collection of templates for Python development.

Usage
=====

::

    $ pip install mr.bob
    $ mrbob https://github.com/iElectric/bobtemplates.ielectric/zipball/master#bobtemplates/ielectric/{TEMPLATE_NAME}


LIST OF TEMPLATES
=================

pyramid
    Opinionated Pyramid skeleton with:

    - Buildout staging/production configuration
    - SQLAlchemy integration
    - Alembic (database migrations)integration
    - Travis-CI integration
    - Jinja2 as default templating engine
    - Babel for internalization and localization
    - pyramid_mailer for sending emails
    - Raven (Sentry) integration
    - dogpile.cache for caching API
python_package
    Replaces paster's `basic_template` with more modern ideas :-)


TODO
====

- add bpython
- Pyramid template
    - pyramid_layout
    - alembic:
        - write tests
        - docs for initial migration
    - docs how to use this package (http://docs.pylonsproject.org/projects/pyramid_mailer/en/latest/, )
    - pyramid_mailer # TODO: provide patch for printing mailer when in debug mode
    - auth + root factory? https://github.com/lazaret/anuket/blob/develop/anuket/models/rootfactory.py 
    - fabric with staging/production deploy scripts
    - setup a way to detect locales/languages http://docs.pylonsproject.org/projects/pyramid/en/latest/narr/i18n.html
    - local command to add new app for pyramid project
- add django template based on https://github.com/kiberpipa/intranet
- add plone template based on https://github.com/niteoweb/niteoweb.skel.plone
