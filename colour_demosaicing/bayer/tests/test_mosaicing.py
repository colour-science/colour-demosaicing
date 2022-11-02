# !/usr/bin/env python
"""
Define the unit tests for the :mod:`colour_demosaicing.bayer.mosaicing`
module.
"""

from __future__ import annotations

import numpy as np
import os
import unittest

from colour import read_image

from colour_demosaicing import ROOT_RESOURCES_TESTS
from colour_demosaicing.bayer import mosaicing_CFA_Bayer

__author__ = "Colour Developers"
__copyright__ = "Copyright 2015 Colour Developers"
__license__ = "New BSD License - https://opensource.org/licenses/BSD-3-Clause"
__maintainer__ = "Colour Developers"
__email__ = "colour-developers@colour-science.org"
__status__ = "Production"

__all__ = [
    "ROOT_RESOURCES_BAYER",
    "TestMosaicing_CFA_Bayer",
]

ROOT_RESOURCES_BAYER: str = os.path.join(
    ROOT_RESOURCES_TESTS, "colour_demosaicing", "bayer"
)


class TestMosaicing_CFA_Bayer(unittest.TestCase):
    """
    Define :func:`colour_demosaicing.bayer.mosaicing.mosaicing_CFA_Bayer`
    definition unit tests methods.
    """

    def test_mosaicing_CFA_Bayer(self):
        """
        Test :func:`colour_demosaicing.bayer.mosaicing.mosaicing_CFA_Bayer`
        definition.
        """

        image = read_image(
            str(os.path.join(ROOT_RESOURCES_BAYER, "Lighthouse.exr"))
        )

        for pattern in ("RGGB", "BGGR", "GRBG", "GBRG"):
            CFA = os.path.join(
                ROOT_RESOURCES_BAYER, f"Lighthouse_CFA_{pattern}.exr"
            )
            np.testing.assert_array_almost_equal(
                mosaicing_CFA_Bayer(image, pattern),
                read_image(str(CFA))[..., 0],
                decimal=7,
            )


if __name__ == "__main__":
    unittest.main()
