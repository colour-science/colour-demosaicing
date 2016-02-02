# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Defines unit tests for :mod:`colour_demosaicing.bayer.masks` module.
"""

from __future__ import division, unicode_literals

import numpy as np
import os
import unittest

import colour

from colour_demosaicing import TESTS_RESOURCES_DIRECTORY
from colour_demosaicing.bayer import masks_CFA_Bayer

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2015-2016 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = ['BAYER_DIRECTORY',
           'TestMasks_CFA_Bayer']

BAYER_DIRECTORY = os.path.join(
    TESTS_RESOURCES_DIRECTORY, 'colour_demosaicing', 'bayer')


class TestMasks_CFA_Bayer(unittest.TestCase):
    """
    Defines :func:`colour_demosaicing.bayer.masks.masks_CFA_Bayer` definition
    unit tests methods.
    """

    def test_masks_CFA_Bayer(self):
        """
        Tests :func:`colour_demosaicing.bayer.masks.masks_CFA_Bayer`
        definition.
        """

        for pattern in ('RGGB', 'BGGR', 'GRBG', 'GBRG'):
            np.testing.assert_almost_equal(
                colour.tstack(masks_CFA_Bayer((8, 8), pattern)),
                colour.read_image(
                    str(os.path.join(BAYER_DIRECTORY,
                                     '{0}_Masks.exr'.format(pattern)))),
                decimal=7)


if __name__ == '__main__':
    unittest.main()
