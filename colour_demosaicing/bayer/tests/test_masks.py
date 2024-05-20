"""Define the unit tests for the :mod:`colour_demosaicing.bayer.masks` module."""

from __future__ import annotations

import os

import numpy as np
from colour import read_image
from colour.constants import TOLERANCE_ABSOLUTE_TESTS
from colour.utilities import tstack

from colour_demosaicing import ROOT_RESOURCES_TESTS
from colour_demosaicing.bayer import masks_CFA_Bayer

__author__ = "Colour Developers"
__copyright__ = "Copyright 2015 Colour Developers"
__license__ = "BSD-3-Clause - https://opensource.org/licenses/BSD-3-Clause"
__maintainer__ = "Colour Developers"
__email__ = "colour-developers@colour-science.org"
__status__ = "Production"

__all__ = [
    "ROOT_RESOURCES_BAYER",
    "TestMasks_CFA_Bayer",
]

ROOT_RESOURCES_BAYER: str = os.path.join(
    ROOT_RESOURCES_TESTS, "colour_demosaicing", "bayer"
)


class TestMasks_CFA_Bayer:
    """
    Define :func:`colour_demosaicing.bayer.masks.masks_CFA_Bayer` definition
    unit tests methods.
    """

    def test_masks_CFA_Bayer(self):
        """
        Test :func:`colour_demosaicing.bayer.masks.masks_CFA_Bayer`
        definition.
        """

        for pattern in ("RGGB", "BGGR", "GRBG", "GBRG"):
            mask = os.path.join(ROOT_RESOURCES_BAYER, f"{pattern}_Masks.exr")
            np.testing.assert_allclose(
                tstack(masks_CFA_Bayer((8, 8), pattern)),
                read_image(str(mask)),
                atol=TOLERANCE_ABSOLUTE_TESTS,
            )
