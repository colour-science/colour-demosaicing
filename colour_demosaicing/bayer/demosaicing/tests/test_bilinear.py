# !/usr/bin/env python
"""
Defines the unit tests for the
:mod:`colour_demosaicing.bayer.demosaicing.bilinear` module.
"""

from __future__ import annotations

import numpy as np
import os
import unittest

from colour import read_image

from colour_demosaicing import TESTS_RESOURCES_DIRECTORY
from colour_demosaicing.bayer import demosaicing_CFA_Bayer_bilinear

__author__ = "Colour Developers"
__copyright__ = "Copyright 2015 Colour Developers"
__license__ = "New BSD License - https://opensource.org/licenses/BSD-3-Clause"
__maintainer__ = "Colour Developers"
__email__ = "colour-developers@colour-science.org"
__status__ = "Production"

__all__ = [
    "BAYER_DIRECTORY",
    "TestDemosaicing_CFA_Bayer_bilinear",
]

BAYER_DIRECTORY: str = os.path.join(
    TESTS_RESOURCES_DIRECTORY, "colour_demosaicing", "bayer"
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
            CFA = os.path.join(
                BAYER_DIRECTORY, f"Lighthouse_CFA_{pattern}.exr"
            )
            RGB = os.path.join(
                BAYER_DIRECTORY, f"Lighthouse_Bilinear_{pattern}.exr"
            )

            np.testing.assert_almost_equal(
                demosaicing_CFA_Bayer_bilinear(
                    read_image(str(CFA))[..., 0], pattern
                ),
                read_image(str(RGB)),
                decimal=7,
            )


if __name__ == "__main__":
    unittest.main()
