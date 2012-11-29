# -*- coding: utf-8 -*-

import os

from setuptools import setup
from setuptools import find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


setup(
    name='bobtemplates.ielectric',
    version='0.1',
    description="Collection of `mr.bob` templates for my personal use.",
    long_description=read('README.rst') + read('HISTORY.rst')
                                        + read('LICENSE'),
    classifiers=[
        "Programming Language :: Python",
    ],
    author='Domen Kožar',
    author_email='domen@dev.si',
    url='https://github.com/iElectric/bobtemplates.ielectric',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    namespace_packages=['bobtemplates'],
    install_requires=[
        'setuptools',
        'mr.bob',
    ],
    entry_points="""
    """,
)
