Colour - Demosaicing
====================

.. start-badges

|actions| |coveralls| |codacy| |version|

.. |actions| image:: https://img.shields.io/github/actions/workflow/status/colour-science/colour-demosaicing/.github/workflows/continuous-integration-quality-unit-tests.yml?branch=develop&style=flat-square
    :target: https://github.com/colour-science/colour-demosaicing/actions
    :alt: Develop Build Status
.. |coveralls| image:: http://img.shields.io/coveralls/colour-science/colour-demosaicing/develop.svg?style=flat-square
    :target: https://coveralls.io/r/colour-science/colour-demosaicing
    :alt: Coverage Status
.. |codacy| image:: https://img.shields.io/codacy/grade/2862b4f2217742ae83c972d7e3af44d7/develop.svg?style=flat-square
    :target: https://www.codacy.com/app/colour-science/colour-demosaicing
    :alt: Code Grade
.. |version| image:: https://img.shields.io/pypi/v/colour-demosaicing.svg?style=flat-square
    :target: https://pypi.org/project/colour-demosaicing
    :alt: Package Version

.. end-badges

A `Python <https://www.python.org>`__ package implementing various
CFA (Colour Filter Array) demosaicing algorithms and related utilities.

It is open source and freely available under the
`BSD-3-Clause <https://opensource.org/licenses/BSD-3-Clause>`__ terms.

..  image:: https://raw.githubusercontent.com/colour-science/colour-demosaicing/master/docs/_static/Demosaicing_001.png

.. contents:: **Table of Contents**
    :backlinks: none
    :depth: 2

.. sectnum::

Features
--------

The following CFA (Colour Filter Array) demosaicing algorithms are implemented:

- Bilinear
- Malvar (2004)
- DDFAPD - Menon (2007)

Examples
^^^^^^^^

Various usage examples are available from the
`examples directory <https://github.com/colour-science/colour-demosaicing/tree/master/colour_demosaicing/examples>`__.

User Guide
----------

Installation
^^^^^^^^^^^^

Because of their size, the resources dependencies needed to run the various
examples and unit tests are not provided within the Pypi package. They are
separately available as
`Git Submodules <https://git-scm.com/book/en/v2/Git-Tools-Submodules>`__
when cloning the
`repository <https://github.com/colour-science/colour-demosaicing>`__.

Primary Dependencies
~~~~~~~~~~~~~~~~~~~~

**Colour - Demosaicing** requires various dependencies in order to run:

- `python >= 3.9, < 4 <https://www.python.org/download/releases>`__
- `colour-science >= 4.3 <https://pypi.org/project/colour-science>`__
- `imageio >= 2, < 3 <https://imageio.github.io>`__
- `numpy >= 1.22, < 2 <https://pypi.org/project/numpy>`__
- `scipy >= 1.8, < 2 <https://pypi.org/project/scipy>`__

Pypi
~~~~

Once the dependencies are satisfied, **Colour - Demosaicing** can be installed from
the `Python Package Index <http://pypi.python.org/pypi/colour-demosaicing>`__ by
issuing this command in a shell::

    pip install --user colour-demosaicing

The overall development dependencies are installed as follows::

    pip install --user 'colour-demosaicing[development]'

Contributing
^^^^^^^^^^^^

If you would like to contribute to `Colour - Demosaicing <https://github.com/colour-science/colour-demosaicing>`__,
please refer to the following `Contributing <https://www.colour-science.org/contributing>`__
guide for `Colour <https://github.com/colour-science/colour>`__.

Bibliography
^^^^^^^^^^^^

The bibliography is available in the repository in
`BibTeX <https://github.com/colour-science/colour-demosaicing/blob/develop/BIBLIOGRAPHY.bib>`__
format.

API Reference
-------------

The main technical reference for `Colour - Demosaicing <https://github.com/colour-science/colour-demosaicing>`__
is the `API Reference <https://colour-demosaicing.readthedocs.io/en/latest/reference.html>`__.

Code of Conduct
---------------

The *Code of Conduct*, adapted from the `Contributor Covenant 1.4 <https://www.contributor-covenant.org/version/1/4/code-of-conduct.html>`__,
is available on the `Code of Conduct <https://www.colour-science.org/code-of-conduct>`__ page.

Contact & Social
----------------

The *Colour Developers* can be reached via different means:

- `Email <mailto:colour-developers@colour-science.org>`__
- `Facebook <https://www.facebook.com/python.colour.science>`__
- `Github Discussions <https://github.com/colour-science/colour-demosaicing/discussions>`__
- `Gitter <https://gitter.im/colour-science/colour>`__
- `Twitter <https://twitter.com/colour_science>`__

About
-----

| **Colour - Demosaicing** by Colour Developers
| Copyright 2015 Colour Developers – `colour-developers@colour-science.org <colour-developers@colour-science.org>`__
| This software is released under terms of BSD-3-Clause: https://opensource.org/licenses/BSD-3-Clause
| `https://github.com/colour-science/colour-demosaicing <https://github.com/colour-science/colour-demosaicing>`__
