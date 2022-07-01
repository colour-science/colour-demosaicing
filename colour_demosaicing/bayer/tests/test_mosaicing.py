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

from colour_demosaicing import TESTS_RESOURCES_DIRECTORY
from colour_demosaicing.bayer import mosaicing_CFA_Bayer

__author__ = "Colour Developers"
__copyright__ = "Copyright 2015 Colour Developers"
__license__ = "New BSD License - https://opensource.org/licenses/BSD-3-Clause"
__maintainer__ = "Colour Developers"
__email__ = "colour-developers@colour-science.org"
__status__ = "Production"

__all__ = [
    "BAYER_DIRECTORY",
    "TestMosaicing_CFA_Bayer",
]

BAYER_DIRECTORY: str = os.path.join(
    TESTS_RESOURCES_DIRECTORY, "colour_demosaicing", "bayer"
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
            str(os.path.join(BAYER_DIRECTORY, "Lighthouse.exr"))
        )

        for pattern in ("RGGB", "BGGR", "GRBG", "GBRG"):
            CFA = os.path.join(
                BAYER_DIRECTORY, f"Lighthouse_CFA_{pattern}.exr"
            )
            np.testing.assert_almost_equal(
                mosaicing_CFA_Bayer(image, pattern),
                read_image(str(CFA))[..., 0],
                decimal=7,
            )


if __name__ == "__main__":
    unittest.main()
