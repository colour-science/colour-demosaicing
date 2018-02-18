Colour - Demosaicing
====================

..  image:: https://raw.githubusercontent.com/colour-science/colour-demosaicing/master/docs/_static/Demosaicing_001.png

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

The main reference for
`Colour - Demosaicing <https://github.com/colour-science/colour-demosaicing>`_
is the manual:

.. toctree::
    :maxdepth: 4

    manual

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

The bibliography is available in the repository in
`BibTeX <https://github.com/colour-science/colour-demosaicing/blob/develop/BIBLIOGRAPHY.bib>`_
format.

About
-----

| **Colour - Demosaicing** by Colour Developers
| Copyright © 2015-2018 – Colour Developers – `colour-science@googlegroups.com <colour-science@googlegroups.com>`_
| This software is released under terms of New BSD License: http://opensource.org/licenses/BSD-3-Clause
| `http://github.com/colour-science/colour-demosaicing <http://github.com/colour-science/colour-demosaicing>`_
