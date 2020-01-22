# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Defines unit tests for :mod:`colour_demosaicing.bayer.demosaicing.menon2007`
module.
"""

from __future__ import division, unicode_literals

import numpy as np
import os
import unittest

from colour import read_image

from colour_demosaicing import TESTS_RESOURCES_DIRECTORY
from colour_demosaicing.bayer import demosaicing_CFA_Bayer_Menon2007

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2015-2020 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = ['BAYER_DIRECTORY', 'TestDemosaicing_CFA_Bayer_Menon2007']

BAYER_DIRECTORY = os.path.join(TESTS_RESOURCES_DIRECTORY, 'colour_demosaicing',
                               'bayer')


class TestDemosaicing_CFA_Bayer_Menon2007(unittest.TestCase):
    """
    Defines :func:`colour_demosaicing.bayer.demosaicing.menon2007.\
demosaicing_CFA_Bayer_Menon2007` definition unit tests methods.
    """

    def test_demosaicing_CFA_Bayer_Menon2007(self):
        """
        Tests :func:`colour_demosaicing.bayer.demosaicing.menon2007.\
demosaicing_CFA_Bayer_Menon2007` definition.
        """

        for pattern in ('RGGB', 'BGGR', 'GRBG', 'GBRG'):
            CFA = os.path.join(BAYER_DIRECTORY, 'Lighthouse_CFA_{0}.exr')
            RGB = os.path.join(BAYER_DIRECTORY, 'Lighthouse_Menon2007_{0}.exr')

            np.testing.assert_almost_equal(
                demosaicing_CFA_Bayer_Menon2007(
                    read_image(str(CFA.format(pattern)))[..., 0], pattern),
                read_image(str(RGB.format(pattern))),
                decimal=7)

            RGB = os.path.join(BAYER_DIRECTORY,
                               'Lighthouse_Menon2007_NR_{0}.exr')
            np.testing.assert_almost_equal(
                demosaicing_CFA_Bayer_Menon2007(
                    read_image(str(CFA.format(pattern)))[..., 0],
                    pattern,
                    refining_step=False),
                read_image(str(RGB.format(pattern))),
                decimal=7)


if __name__ == '__main__':
    unittest.main()
