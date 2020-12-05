# -*- coding: utf-8 -*-
import codecs
from setuptools import setup

packages = \
['colour_demosaicing',
 'colour_demosaicing.bayer',
 'colour_demosaicing.bayer.demosaicing',
 'colour_demosaicing.bayer.demosaicing.tests',
 'colour_demosaicing.bayer.tests']

package_data = \
{'': ['*'],
 'colour_demosaicing': ['examples/*',
                        'resources/colour-demosaicing-examples-datasets/*',
                        'resources/colour-demosaicing-tests-datasets/*']}

install_requires = \
['colour-science>=0.3.16,<0.4.0']

extras_require = \
{'development': ['biblib-simple',
                 'coverage',
                 'coveralls',
                 'flake8',
                 'invoke',
                 'jupyter',
                 'mock',
                 'nose',
                 'pre-commit',
                 'pytest',
                 'restructuredtext-lint',
                 'sphinx<=3.1.2',
                 'sphinx_rtd_theme',
                 'sphinxcontrib-bibtex',
                 'toml',
                 'twine',
                 'yapf==0.23'],
 'plotting': ['matplotlib'],
 'read-the-docs': ['mock', 'numpy', 'sphinxcontrib-bibtex']}

setup(
    name='colour-demosaicing',
    version='0.1.6',
    description='CFA (Colour Filter Array) Demosaicing Algorithms for Python',
    long_description=codecs.open('README.rst', encoding='utf8').read(),
    author='Colour Developers',
    author_email='colour-developers@colour-science.org',
    maintainer='Colour Developers',
    maintainer_email='colour-developers@colour-science.org',
    url='https://www.colour-science.org/',
    packages=packages,
    package_data=package_data,
    install_requires=install_requires,
    extras_require=extras_require,
    python_requires='>=3.6,<4.0',
)
