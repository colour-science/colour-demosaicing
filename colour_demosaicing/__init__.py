"""
Colour - Demosaicing
====================

CFA (Colour Filter Array) Demosaicing algorithms for *Python*.

Subpackages
-----------
-   bayer: *Bayer* CFA mosaicing and demosaicing computations.
"""

from __future__ import annotations

import contextlib
import numpy as np
import os
import subprocess

import colour

from .bayer import (
    demosaicing_CFA_Bayer_bilinear,
    demosaicing_CFA_Bayer_DDFAPD,
    demosaicing_CFA_Bayer_Malvar2004,
    demosaicing_CFA_Bayer_Menon2007,
    masks_CFA_Bayer,
    mosaicing_CFA_Bayer,
)

__author__ = "Colour Developers"
__copyright__ = "Copyright 2015 Colour Developers"
__license__ = "BSD-3-Clause - https://opensource.org/licenses/BSD-3-Clause"
__maintainer__ = "Colour Developers"
__email__ = "colour-developers@colour-science.org"
__status__ = "Production"

__all__ = [
    "demosaicing_CFA_Bayer_bilinear",
    "demosaicing_CFA_Bayer_DDFAPD",
    "demosaicing_CFA_Bayer_Malvar2004",
    "demosaicing_CFA_Bayer_Menon2007",
    "masks_CFA_Bayer",
    "mosaicing_CFA_Bayer",
]

ROOT_RESOURCES: str = os.path.join(os.path.dirname(__file__), "resources")
ROOT_RESOURCES_EXAMPLES: str = os.path.join(
    ROOT_RESOURCES, "colour-demosaicing-examples-datasets"
)
ROOT_RESOURCES_TESTS: str = os.path.join(
    ROOT_RESOURCES, "colour-demosaicing-tests-datasets"
)

__application_name__ = "Colour - Demosaicing"

__major_version__ = "0"
__minor_version__ = "2"
__change_version__ = "4"
__version__ = ".".join(
    (__major_version__, __minor_version__, __change_version__)
)

try:
    _version: str = (
        subprocess.check_output(
            ["git", "describe"],  # noqa: S603, S607
            cwd=os.path.dirname(__file__),
            stderr=subprocess.STDOUT,
        )
        .strip()
        .decode("utf-8")
    )
except Exception:
    _version: str = __version__

colour.utilities.ANCILLARY_COLOUR_SCIENCE_PACKAGES[  # pyright: ignore
    "colour-demosaicing"
] = _version

del _version

# TODO: Remove legacy printing support when deemed appropriate.
with contextlib.suppress(TypeError):
    np.set_printoptions(legacy="1.13")
