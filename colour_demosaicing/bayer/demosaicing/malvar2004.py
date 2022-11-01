"""
Malvar (2004) Bayer CFA Demosaicing
===================================

*Bayer* CFA (Colour Filter Array) *Malvar (2004)* demosaicing.

References
----------
-   :cite:`Malvar2004a` : Malvar, H. S., He, L.-W., Cutler, R., & Way, O. M.
    (2004). High-Quality Linear Interpolation for Demosaicing of
    Bayer-Patterned Color Images. International Conference of Acoustic, Speech
    and Signal Processing, 5-8.
    http://research.microsoft.com/apps/pubs/default.aspx?id=102068
"""

from __future__ import annotations

import numpy as np
from scipy.ndimage.filters import convolve

from colour.hints import ArrayLike, Literal, NDArray, Union
from colour.utilities import as_float_array, ones, tstack

from colour_demosaicing.bayer import masks_CFA_Bayer

__author__ = "Colour Developers"
__copyright__ = "Copyright 2015 Colour Developers"
__license__ = "New BSD License - https://opensource.org/licenses/BSD-3-Clause"
__maintainer__ = "Colour Developers"
__email__ = "colour-developers@colour-science.org"
__status__ = "Production"

__all__ = [
    "demosaicing_CFA_Bayer_Malvar2004",
]


def demosaicing_CFA_Bayer_Malvar2004(
    CFA: ArrayLike,
    pattern: Union[Literal["RGGB", "BGGR", "GRBG", "GBRG"], str] = "RGGB",
) -> NDArray:
    """
    Return the demosaiced *RGB* colourspace array from given *Bayer* CFA using
    *Malvar (2004)* demosaicing algorithm.

    Parameters
    ----------
    CFA
        *Bayer* CFA.
    pattern
        Arrangement of the colour filters on the pixel array.

    Returns
    -------
    :class:`numpy.ndarray`
        *RGB* colourspace array.

    Notes
    -----
    -   The definition output is not clipped in range [0, 1] : this allows for
        direct HDRI image generation on *Bayer* CFA data and post
        demosaicing of the high dynamic range data as showcased in this
        `Jupyter Notebook <https://github.com/colour-science/colour-hdri/\
blob/develop/colour_hdri/examples/\
examples_merge_from_raw_files_with_post_demosaicing.ipynb>`__.

    References
    ----------
    :cite:`Malvar2004a`

    Examples
    --------
    >>> CFA = np.array(
    ...     [
    ...         [0.30980393, 0.36078432, 0.30588236, 0.3764706],
    ...         [0.35686275, 0.39607844, 0.36078432, 0.40000001],
    ...     ]
    ... )
    >>> demosaicing_CFA_Bayer_Malvar2004(CFA)
    array([[[ 0.30980393,  0.31666668,  0.32941177],
            [ 0.33039216,  0.36078432,  0.38112746],
            [ 0.30588236,  0.32794118,  0.34877452],
            [ 0.36274511,  0.3764706 ,  0.38480393]],
    <BLANKLINE>
           [[ 0.34828432,  0.35686275,  0.36568628],
            [ 0.35318628,  0.38186275,  0.39607844],
            [ 0.3379902 ,  0.36078432,  0.3754902 ],
            [ 0.37769609,  0.39558825,  0.40000001]]])
    >>> CFA = np.array(
    ...     [
    ...         [0.3764706, 0.360784320, 0.40784314, 0.3764706],
    ...         [0.35686275, 0.30980393, 0.36078432, 0.29803923],
    ...     ]
    ... )
    >>> demosaicing_CFA_Bayer_Malvar2004(CFA, "BGGR")
    array([[[ 0.35539217,  0.37058825,  0.3764706 ],
            [ 0.34264707,  0.36078432,  0.37450981],
            [ 0.36568628,  0.39607844,  0.40784314],
            [ 0.36568629,  0.3764706 ,  0.3882353 ]],
    <BLANKLINE>
           [[ 0.34411765,  0.35686275,  0.36200981],
            [ 0.30980393,  0.32990197,  0.34975491],
            [ 0.33039216,  0.36078432,  0.38063726],
            [ 0.29803923,  0.30441178,  0.31740197]]])
    """

    CFA = as_float_array(CFA)
    R_m, G_m, B_m = masks_CFA_Bayer(CFA.shape, pattern)

    GR_GB = (
        as_float_array(
            [
                [0.0, 0.0, -1.0, 0.0, 0.0],
                [0.0, 0.0, 2.0, 0.0, 0.0],
                [-1.0, 2.0, 4.0, 2.0, -1.0],
                [0.0, 0.0, 2.0, 0.0, 0.0],
                [0.0, 0.0, -1.0, 0.0, 0.0],
            ]
        )
        / 8
    )

    Rg_RB_Bg_BR = (
        as_float_array(
            [
                [0.0, 0.0, 0.5, 0.0, 0.0],
                [0.0, -1.0, 0.0, -1.0, 0.0],
                [-1.0, 4.0, 5.0, 4.0, -1.0],
                [0.0, -1.0, 0.0, -1.0, 0.0],
                [0.0, 0.0, 0.5, 0.0, 0.0],
            ]
        )
        / 8
    )

    Rg_BR_Bg_RB = np.transpose(Rg_RB_Bg_BR)

    Rb_BB_Br_RR = (
        as_float_array(
            [
                [0.0, 0.0, -1.5, 0.0, 0.0],
                [0.0, 2.0, 0.0, 2.0, 0.0],
                [-1.5, 0.0, 6.0, 0.0, -1.5],
                [0.0, 2.0, 0.0, 2.0, 0.0],
                [0.0, 0.0, -1.5, 0.0, 0.0],
            ]
        )
        / 8
    )

    R = CFA * R_m
    G = CFA * G_m
    B = CFA * B_m

    del G_m

    G = np.where(np.logical_or(R_m == 1, B_m == 1), convolve(CFA, GR_GB), G)

    RBg_RBBR = convolve(CFA, Rg_RB_Bg_BR)
    RBg_BRRB = convolve(CFA, Rg_BR_Bg_RB)
    RBgr_BBRR = convolve(CFA, Rb_BB_Br_RR)

    del GR_GB, Rg_RB_Bg_BR, Rg_BR_Bg_RB, Rb_BB_Br_RR

    # Red rows.
    R_r = np.transpose(np.any(R_m == 1, axis=1)[None]) * ones(R.shape)
    # Red columns.
    R_c = np.any(R_m == 1, axis=0)[None] * ones(R.shape)
    # Blue rows.
    B_r = np.transpose(np.any(B_m == 1, axis=1)[None]) * ones(B.shape)
    # Blue columns
    B_c = np.any(B_m == 1, axis=0)[None] * ones(B.shape)

    del R_m, B_m

    R = np.where(np.logical_and(R_r == 1, B_c == 1), RBg_RBBR, R)
    R = np.where(np.logical_and(B_r == 1, R_c == 1), RBg_BRRB, R)

    B = np.where(np.logical_and(B_r == 1, R_c == 1), RBg_RBBR, B)
    B = np.where(np.logical_and(R_r == 1, B_c == 1), RBg_BRRB, B)

    R = np.where(np.logical_and(B_r == 1, B_c == 1), RBgr_BBRR, R)
    B = np.where(np.logical_and(R_r == 1, R_c == 1), RBgr_BBRR, B)

    del RBg_RBBR, RBg_BRRB, RBgr_BBRR, R_r, R_c, B_r, B_c

    return tstack([R, G, B])
