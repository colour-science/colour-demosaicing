#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Colour - Demosaicing
====================

CFA (Colour Filter Array) Demosaicing algorithms for *Python*.

Subpackages
-----------
-   bayer: *Bayer* CFA mosaicing and demosaicing computations.
"""

from __future__ import absolute_import

import os

from .bayer import *  # noqa
from . import bayer  # noqa

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2015-2016 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = []
__all__ += bayer.__all__

RESOURCES_DIRECTORY = os.path.join(
    os.path.dirname(__file__), 'resources')
EXAMPLES_RESOURCES_DIRECTORY = os.path.join(
    RESOURCES_DIRECTORY, 'colour-demosaicing-examples-dataset')
TESTS_RESOURCES_DIRECTORY = os.path.join(
    RESOURCES_DIRECTORY, 'colour-demosaicing-tests-dataset')

__application_name__ = 'Colour - Demosaicing'

__major_version__ = '0'
__minor_version__ = '1'
__change_version__ = '1'
__version__ = '.'.join((__major_version__,
                        __minor_version__,
                        __change_version__))
