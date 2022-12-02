"""
Colour - Demosaicing - Setup
============================
"""

import codecs
from setuptools import setup

packages = [
    "colour_demosaicing",
    "colour_demosaicing.bayer",
    "colour_demosaicing.bayer.demosaicing",
    "colour_demosaicing.bayer.demosaicing.tests",
    "colour_demosaicing.bayer.tests",
]

package_data = {
    "": ["*"],
    "colour_demosaicing": [
        "examples/*",
        "resources/colour-demosaicing-examples-datasets/*",
        "resources/colour-demosaicing-tests-datasets/*",
    ],
}

install_requires = [
    "colour-science>=0.4.2",
    "imageio>=2,<3",
    "numpy>=1.20,<2",
    "scipy>=1.7,<2",
    "typing-extensions>=4,<5",
]

extras_require = {
    "development": [
        "biblib-simple",
        "black",
        "blackdoc",
        "coverage!=6.3",
        "coveralls",
        "flake8",
        "flynt",
        "invoke",
        "jupyter",
        "mypy",
        "pre-commit",
        "pydata-sphinx-theme",
        "pydocstyle",
        "pytest",
        "pytest-cov",
        "pyupgrade",
        "restructuredtext-lint",
        "sphinx>=4,<5",
        "sphinxcontrib-bibtex",
        "toml",
        "twine",
    ],
    "plotting": ["matplotlib>=3.5,!=3.5.0,!=3.5.1"],
    "read-the-docs": [
        "matplotlib>=3.5,!=3.5.0,!=3.5.1",
        "pydata-sphinx-theme",
        "sphinxcontrib-bibtex",
    ],
}

setup(
    name="colour-demosaicing",
    version="0.2.3",
    description="CFA (Colour Filter Array) Demosaicing Algorithms for Python",
    long_description=codecs.open("README.rst", encoding="utf8").read(),
    author="Colour Developers",
    author_email="colour-developers@colour-science.org",
    maintainer="Colour Developers",
    maintainer_email="colour-developers@colour-science.org",
    url="https://www.colour-science.org/",
    packages=packages,
    package_data=package_data,
    install_requires=install_requires,
    extras_require=extras_require,
    python_requires=">=3.9,<3.12",
)
