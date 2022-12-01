"""
Bayer CFA Masks
===============

*Bayer* CFA (Colour Filter Array) masks generation.
"""

from __future__ import annotations

import numpy as np

from colour.hints import Literal, NDArray, Tuple, Union
from colour.utilities import validate_method

__author__ = "Colour Developers"
__copyright__ = "Copyright 2015 Colour Developers"
__license__ = "New BSD License - https://opensource.org/licenses/BSD-3-Clause"
__maintainer__ = "Colour Developers"
__email__ = "colour-developers@colour-science.org"
__status__ = "Production"

__all__ = [
    "masks_CFA_Bayer",
]


def masks_CFA_Bayer(
    shape: Union[int, Tuple[int, ...]],
    pattern: Union[Literal["RGGB", "BGGR", "GRBG", "GBRG"], str] = "RGGB",
) -> Tuple[NDArray, ...]:
    """
    Return the *Bayer* CFA red, green and blue masks for given pattern.

    Parameters
    ----------
    shape
        Dimensions of the *Bayer* CFA.
    pattern
        Arrangement of the colour filters on the pixel array.

    Returns
    -------
    :class:`tuple`
        *Bayer* CFA red, green and blue masks.

    Examples
    --------
    >>> from pprint import pprint
    >>> shape = (3, 3)
    >>> pprint(masks_CFA_Bayer(shape))
    (array([[ True, False,  True],
           [False, False, False],
           [ True, False,  True]], dtype=bool),
     array([[False,  True, False],
           [ True, False,  True],
           [False,  True, False]], dtype=bool),
     array([[False, False, False],
           [False,  True, False],
           [False, False, False]], dtype=bool))
    >>> pprint(masks_CFA_Bayer(shape, "BGGR"))
    (array([[False, False, False],
           [False,  True, False],
           [False, False, False]], dtype=bool),
     array([[False,  True, False],
           [ True, False,  True],
           [False,  True, False]], dtype=bool),
     array([[ True, False,  True],
           [False, False, False],
           [ True, False,  True]], dtype=bool))
    """

    pattern = validate_method(
        pattern,
        ["RGGB", "BGGR", "GRBG", "GBRG"],
        '"{0}" CFA pattern is invalid, it must be one of {1}!',
    ).upper()

    channels = {channel: np.zeros(shape, dtype="bool") for channel in "RGB"}
    for channel, (y, x) in zip(pattern, [(0, 0), (0, 1), (1, 0), (1, 1)]):
        channels[channel][y::2, x::2] = 1

    return tuple(channels.values())
