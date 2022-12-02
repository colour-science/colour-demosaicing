# !/usr/bin/env python
"""
Define the unit tests for the
:mod:`colour_demosaicing.bayer.demosaicing.menon2007` module.
"""

from __future__ import annotations

import numpy as np
import os
import unittest

from colour import read_image

from colour_demosaicing import ROOT_RESOURCES_TESTS
from colour_demosaicing.bayer import demosaicing_CFA_Bayer_Menon2007

__author__ = "Colour Developers"
__copyright__ = "Copyright 2015 Colour Developers"
__license__ = "New BSD License - https://opensource.org/licenses/BSD-3-Clause"
__maintainer__ = "Colour Developers"
__email__ = "colour-developers@colour-science.org"
__status__ = "Production"

__all__ = [
    "ROOT_RESOURCES_BAYER",
    "TestDemosaicing_CFA_Bayer_Menon2007",
]

ROOT_RESOURCES_BAYER: str = os.path.join(
    ROOT_RESOURCES_TESTS, "colour_demosaicing", "bayer"
)


class TestDemosaicing_CFA_Bayer_Menon2007(unittest.TestCase):
    """
    Define :func:`colour_demosaicing.bayer.demosaicing.menon2007.\
demosaicing_CFA_Bayer_Menon2007` definition unit tests methods.
    """

    def test_demosaicing_CFA_Bayer_Menon2007(self):
        """
        Test :func:`colour_demosaicing.bayer.demosaicing.menon2007.\
demosaicing_CFA_Bayer_Menon2007` definition.
        """

        for pattern in ("RGGB", "BGGR", "GRBG", "GBRG"):
            CFA = os.path.join(
                ROOT_RESOURCES_BAYER, f"Lighthouse_CFA_{pattern}.exr"
            )
            RGB = os.path.join(
                ROOT_RESOURCES_BAYER, f"Lighthouse_Menon2007_{pattern}.exr"
            )

            np.testing.assert_array_almost_equal(
                demosaicing_CFA_Bayer_Menon2007(
                    read_image(str(CFA))[..., 0], pattern
                ),
                read_image(str(RGB)),
                decimal=7,
            )

            RGB = os.path.join(
                ROOT_RESOURCES_BAYER, f"Lighthouse_Menon2007_NR_{pattern}.exr"
            )
            np.testing.assert_array_almost_equal(
                demosaicing_CFA_Bayer_Menon2007(
                    read_image(str(CFA))[..., 0],
                    pattern,
                    refining_step=False,
                ),
                read_image(str(RGB)),
                decimal=7,
            )


if __name__ == "__main__":
    unittest.main()
