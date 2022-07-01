Installation Guide
==================

Because of their size, the resources dependencies needed to run the various
examples and unit tests are not provided within the Pypi package. They are
separately available as
`Git Submodules <https://git-scm.com/book/en/v2/Git-Tools-Submodules>`__
when cloning the
`repository <https://github.com/colour-science/colour-demosaicing>`__.

Primary Dependencies
--------------------

**Colour - Demosaicing** requires various dependencies in order to run:

- `python >= 3.8, < 4 <https://www.python.org/download/releases/>`__
- `colour-science >= 4 <https://pypi.org/project/colour-science/>`__
- `imageio >= 2, < 3 <https://imageio.github.io/>`__
- `numpy >= 1.19, < 2 <https://pypi.org/project/numpy/>`__
- `scipy >= 1.5, < 2 <https://pypi.org/project/scipy/>`__

Pypi
----

Once the dependencies are satisfied, **Colour - Demosaicing** can be installed from
the `Python Package Index <http://pypi.python.org/pypi/colour-demosaicing>`__ by
issuing this command in a shell::

    pip install --user colour-demosaicing

The overall development dependencies are installed as follows::

    pip install --user 'colour-demosaicing[development]'
