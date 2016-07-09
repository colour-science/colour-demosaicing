Colour - Demosaicing
====================

..  image:: https://raw.githubusercontent.com/colour-science/colour-demosaicing/master/docs/_static/Demosaicing_001.png

.. list-table::
    :stub-columns: 1

    * - Status
      - |waffle| |travis| |coveralls| |scrutinizer| |landscape| |gemnasium|
    * - Package
      - |version| |downloads|

.. |waffle| image:: https://badge.waffle.io/colour-science/colour-demosaicing.svg?label=ready&title=Ready
    :target: https://github.com/colour-science/colour-demosaicing/issues
    :alt: Issues Ready
.. |travis| image:: https://img.shields.io/travis/colour-science/colour-demosaicing/develop.svg
    :target: https://travis-ci.org/colour-science/colour-demosaicing
    :alt: Develop Build Status
.. |coveralls| image:: http://img.shields.io/coveralls/colour-science/colour-demosaicing/develop.svg
    :target: https://coveralls.io/r/colour-science/colour-demosaicing
    :alt: Coverage Status
.. |scrutinizer| image:: https://img.shields.io/scrutinizer/g/colour-science/colour-demosaicing/develop.svg
    :target: https://scrutinizer-ci.com/g/colour-science/colour-demosaicing/
    :alt: Code Quality
.. |landscape| image:: https://landscape.io/github/colour-science/colour-demosaicing/master/landscape.png
    :target: https://landscape.io/github/colour-science/colour-demosaicing
    :alt: Code Quality
.. |gemnasium| image:: https://img.shields.io/gemnasium/colour-science/colour-demosaicing.svg
    :target: https://gemnasium.com/colour-science/colour-demosaicing
    :alt: Dependencies Status
.. |version| image:: https://badge.fury.io/py/colour-demosaicing.svg
    :target: https://pypi.python.org/pypi/colour-demosaicing
    :alt: Package Version
.. |downloads| image:: https://img.shields.io/pypi/dm/colour-demosaicing.svg
    :target: https://pypi.python.org/pypi/colour-demosaicing
    :alt: Package Downloads

.. end-badges

A `Python <https://www.python.org/>`_ package implementing various
CFA (Colour Filter Array) demosaicing algorithms and related utilities.

It is open source and freely available under the
`New BSD License <http://opensource.org/licenses/BSD-3-Clause>`_ terms.

Features
--------

The following CFA (Colour Filter Array) demosaicing algorithms are implemented:

-   Bilinear
-   Malvar (2004)
-   DDFAPD - Menon (2007)

Installation
------------

Because of their size, the resources dependencies needed to run the various
examples and unit tests are not provided within the Pypi package. They are
separately available as
`Git Submodules <https://git-scm.com/book/en/v2/Git-Tools-Submodules>`_
when cloning the
`repository <https://github.com/colour-science/colour-demosaicing>`_.

Primary Dependencies
^^^^^^^^^^^^^^^^^^^^

**Colour - Demosaicing** requires various dependencies in order to run:

-  `Python 2.7 <https://www.python.org/download/releases/>`_ or
   `Python 3.5 <https://www.python.org/download/releases/>`_
-  `NumPy <http://www.numpy.org/>`_
-  `OpenImageIO <https://github.com/OpenImageIO/oiio>`_

Pypi
^^^^

Once the dependencies satisfied, **Colour - Demosaicing** can be installed from
the `Python Package Index <http://pypi.python.org/pypi/colour-demosaicing>`_ by
issuing this command in a shell::

	pip install colour-demosaicing

The tests suite dependencies are installed as follows::

    pip install 'colour-demosaicing[tests]'

The documentation building dependencies are installed as follows::

    pip install 'colour-demosaicing[docs]'

Usage
-----

API
^^^

The main reference for `Colour - Demosaicing <https://github.com/colour-science/colour-demosaicing>`_
is the Sphinx `API Reference <http://colour-demosaicing.readthedocs.io/en/latest/>`_.

Examples
^^^^^^^^

Various usage examples are available from the
`examples directory <https://github.com/colour-science/colour-demosaicing/tree/master/colour_demosaicing/examples>`_.

Contributing
------------

If you would like to contribute to `Colour - Demosaicing <https://github.com/colour-science/colour-demosaicing>`_,
please refer to the following `Contributing <http://colour-science.org/contributing/>`_
guide for `Colour <https://github.com/colour-science/colour>`_.

Bibliography
------------

The bibliography is available in the repository in either
`BibTeX <https://github.com/colour-science/colour-demosaicing/blob/develop/BIBLIOGRAPHY.bib>`_
format or `reStructuredText <https://github.com/colour-science/colour-demosaicing/blob/develop/BIBLIOGRAPHY.rst>`_.

About
-----

| **Colour - Demosaicing** by Colour Developers
| Copyright © 2015-2016 – Colour Developers – `colour-science@googlegroups.com <colour-science@googlegroups.com>`_
| This software is released under terms of New BSD License: http://opensource.org/licenses/BSD-3-Clause
| `http://github.com/colour-science/colour-demosaicing <http://github.com/colour-science/colour-demosaicing>`_
