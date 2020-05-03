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

import numpy as np
import os
import subprocess  # nosec

import colour

from .bayer import (
    demosaicing_CFA_Bayer_bilinear, demosaicing_CFA_Bayer_DDFAPD,
    demosaicing_CFA_Bayer_Malvar2004, demosaicing_CFA_Bayer_Menon2007,
    masks_CFA_Bayer, mosaicing_CFA_Bayer)

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2015-2020 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = [
    'demosaicing_CFA_Bayer_bilinear', 'demosaicing_CFA_Bayer_DDFAPD',
    'demosaicing_CFA_Bayer_Malvar2004', 'demosaicing_CFA_Bayer_Menon2007',
    'masks_CFA_Bayer', 'mosaicing_CFA_Bayer'
]

RESOURCES_DIRECTORY = os.path.join(os.path.dirname(__file__), 'resources')
EXAMPLES_RESOURCES_DIRECTORY = os.path.join(
    RESOURCES_DIRECTORY, 'colour-demosaicing-examples-datasets')
TESTS_RESOURCES_DIRECTORY = os.path.join(RESOURCES_DIRECTORY,
                                         'colour-demosaicing-tests-datasets')

__application_name__ = 'Colour - Demosaicing'

__major_version__ = '0'
__minor_version__ = '1'
__change_version__ = '5'
__version__ = '.'.join(
    (__major_version__,
     __minor_version__,
     __change_version__))  # yapf: disable

try:
    version = subprocess.check_output(  # nosec
        ['git', 'describe'],
        cwd=os.path.dirname(__file__),
        stderr=subprocess.STDOUT).strip()
    version = version.decode('utf-8')
except Exception:
    version = __version__

colour.utilities.ANCILLARY_COLOUR_SCIENCE_PACKAGES['colour-demosaicing'] = (
    version)

# TODO: Remove legacy printing support when deemed appropriate.
try:
    np.set_printoptions(legacy='1.13')
except TypeError:
    pass
