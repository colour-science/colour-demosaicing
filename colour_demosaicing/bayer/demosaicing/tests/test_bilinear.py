# !/usr/bin/env python
"""
Define the unit tests for the
:mod:`colour_demosaicing.bayer.demosaicing.bilinear` module.
"""

from __future__ import annotations

import os
import unittest

import numpy as np
from colour import read_image
from colour.constants import TOLERANCE_ABSOLUTE_TESTS

from colour_demosaicing import ROOT_RESOURCES_TESTS
from colour_demosaicing.bayer import demosaicing_CFA_Bayer_bilinear
from colour_demosaicing.bayer import mosaicing_CFA_Bayer

__author__ = "Colour Developers"
__copyright__ = "Copyright 2015 Colour Developers"
__license__ = "BSD-3-Clause - https://opensource.org/licenses/BSD-3-Clause"
__maintainer__ = "Colour Developers"
__email__ = "colour-developers@colour-science.org"
__status__ = "Production"

__all__ = [
    "ROOT_RESOURCES_BAYER",
    "TestDemosaicing_CFA_Bayer_bilinear",
]

ROOT_RESOURCES_BAYER: str = os.path.join(
    ROOT_RESOURCES_TESTS, "colour_demosaicing", "bayer"
)


class TestDemosaicing_CFA_Bayer_bilinear(unittest.TestCase):
    """
    Define :func:`colour_demosaicing.bayer.demosaicing.bilinear.\
demosaicing_CFA_Bayer_bilinear` definition unit tests methods.
    """

    def test_demosaicing_CFA_Bayer_bilinear(self):
        """
        Test :func:`colour_demosaicing.bayer.demosaicing.bilinear.\
demosaicing_CFA_Bayer_bilinear` definition.
        """

        for pattern in ("RGGB", "BGGR", "GRBG", "GBRG"):
            CFA = os.path.join(ROOT_RESOURCES_BAYER, f"Lighthouse_CFA_{pattern}.exr")
            RGB = os.path.join(
                ROOT_RESOURCES_BAYER, f"Lighthouse_Bilinear_{pattern}.exr"
            )

            np.testing.assert_allclose(
                demosaicing_CFA_Bayer_bilinear(read_image(str(CFA))[..., 0], pattern),
                read_image(str(RGB)),
                atol=TOLERANCE_ABSOLUTE_TESTS,
            )

    def test_demosaicing_CFA_Bayer_bilinear_interpolant(self):
        """
        Tests whether the result of :func:`colour_demosaicing.bayer.\
        demosaicing.bilinear.demosaicing_CFA_Bayer_bilinear` agrees
        with the original values.
        """

        for pattern in ('RGGB', 'BGGR', 'GRGB', 'GBRG'):
            CFA_file = os.path.join(BAYER_DIRECTORY, 'Lighthouse_CFA_{0}.exr')

            CFA = read_image(str(CFA_file.format(pattern)))
            RGB = demosaicing_CFA_Bayer_bilinear(CFA, pattern)
            CFA_from_RGB = mosaicing_CFA_Bayer(RGB, pattern)
            np.testing.assert_almost_equal(CFA_from_RGB, CFA, decimal=7)


if __name__ == "__main__":
    unittest.main()
