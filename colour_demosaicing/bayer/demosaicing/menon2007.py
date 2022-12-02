"""
DDFAPD - Menon (2007) Bayer CFA Demosaicing
===========================================

*Bayer* CFA (Colour Filter Array) DDFAPD - *Menon (2007)* demosaicing.

References
----------
-   :cite:`Menon2007c` : Menon, D., Andriani, S., & Calvagno, G. (2007).
    Demosaicing With Directional Filtering and a posteriori Decision. IEEE
    Transactions on Image Processing, 16(1), 132-141.
    doi:10.1109/TIP.2006.884928
"""

from __future__ import annotations

import numpy as np
from scipy.ndimage.filters import convolve, convolve1d

from colour.hints import ArrayLike, Boolean, Literal, NDArray, Union
from colour.utilities import as_float_array, ones, tsplit, tstack

from colour_demosaicing.bayer import masks_CFA_Bayer

__author__ = "Colour Developers"
__copyright__ = "Copyright 2015 Colour Developers"
__license__ = "New BSD License - https://opensource.org/licenses/BSD-3-Clause"
__maintainer__ = "Colour Developers"
__email__ = "colour-developers@colour-science.org"
__status__ = "Production"

__all__ = [
    "demosaicing_CFA_Bayer_Menon2007",
    "demosaicing_CFA_Bayer_DDFAPD",
    "refining_step_Menon2007",
]


def _cnv_h(x: ArrayLike, y: ArrayLike) -> NDArray:
    """Perform horizontal convolution."""

    return convolve1d(x, y, mode="mirror")


def _cnv_v(x: ArrayLike, y: ArrayLike) -> NDArray:
    """Perform vertical convolution."""

    return convolve1d(x, y, mode="mirror", axis=0)


def demosaicing_CFA_Bayer_Menon2007(
    CFA: ArrayLike,
    pattern: Union[Literal["RGGB", "BGGR", "GRBG", "GBRG"], str] = "RGGB",
    refining_step: Boolean = True,
):
    """
    Return the demosaiced *RGB* colourspace array from given *Bayer* CFA using
    DDFAPD - *Menon (2007)* demosaicing algorithm.

    Parameters
    ----------
    CFA
        *Bayer* CFA.
    pattern
        Arrangement of the colour filters on the pixel array.
    refining_step
        Perform refining step.

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
    :cite:`Menon2007c`

    Examples
    --------
    >>> CFA = np.array(
    ...     [
    ...         [0.30980393, 0.36078432, 0.30588236, 0.3764706],
    ...         [0.35686275, 0.39607844, 0.36078432, 0.40000001],
    ...     ]
    ... )
    >>> demosaicing_CFA_Bayer_Menon2007(CFA)
    array([[[ 0.30980393,  0.35686275,  0.39215687],
            [ 0.30980393,  0.36078432,  0.39607844],
            [ 0.30588236,  0.36078432,  0.39019608],
            [ 0.32156864,  0.3764706 ,  0.40000001]],
    <BLANKLINE>
           [[ 0.30980393,  0.35686275,  0.39215687],
            [ 0.30980393,  0.36078432,  0.39607844],
            [ 0.30588236,  0.36078432,  0.39019609],
            [ 0.32156864,  0.3764706 ,  0.40000001]]])
    >>> CFA = np.array(
    ...     [
    ...         [0.3764706, 0.36078432, 0.40784314, 0.3764706],
    ...         [0.35686275, 0.30980393, 0.36078432, 0.29803923],
    ...     ]
    ... )
    >>> demosaicing_CFA_Bayer_Menon2007(CFA, "BGGR")
    array([[[ 0.30588236,  0.35686275,  0.3764706 ],
            [ 0.30980393,  0.36078432,  0.39411766],
            [ 0.29607844,  0.36078432,  0.40784314],
            [ 0.29803923,  0.3764706 ,  0.42352942]],
    <BLANKLINE>
           [[ 0.30588236,  0.35686275,  0.3764706 ],
            [ 0.30980393,  0.36078432,  0.39411766],
            [ 0.29607844,  0.36078432,  0.40784314],
            [ 0.29803923,  0.3764706 ,  0.42352942]]])
    """

    CFA = as_float_array(CFA)
    R_m, G_m, B_m = masks_CFA_Bayer(CFA.shape, pattern)

    h_0 = as_float_array([0.0, 0.5, 0.0, 0.5, 0.0])
    h_1 = as_float_array([-0.25, 0.0, 0.5, 0.0, -0.25])

    R = CFA * R_m
    G = CFA * G_m
    B = CFA * B_m

    G_H = np.where(G_m == 0, _cnv_h(CFA, h_0) + _cnv_h(CFA, h_1), G)
    G_V = np.where(G_m == 0, _cnv_v(CFA, h_0) + _cnv_v(CFA, h_1), G)

    C_H = np.where(R_m == 1, R - G_H, 0)
    C_H = np.where(B_m == 1, B - G_H, C_H)

    C_V = np.where(R_m == 1, R - G_V, 0)
    C_V = np.where(B_m == 1, B - G_V, C_V)

    D_H = np.abs(C_H - np.pad(C_H, ((0, 0), (0, 2)), mode="reflect")[:, 2:])
    D_V = np.abs(C_V - np.pad(C_V, ((0, 2), (0, 0)), mode="reflect")[2:, :])

    del h_0, h_1, CFA, C_V, C_H

    k = as_float_array(
        [
            [0.0, 0.0, 1.0, 0.0, 1.0],
            [0.0, 0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 3.0, 0.0, 3.0],
            [0.0, 0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0, 0.0, 1.0],
        ]
    )

    d_H = convolve(D_H, k, mode="constant")
    d_V = convolve(D_V, np.transpose(k), mode="constant")

    del D_H, D_V

    mask = d_V >= d_H
    G = np.where(mask, G_H, G_V)
    M = np.where(mask, 1, 0)

    del d_H, d_V, G_H, G_V

    # Red rows.
    R_r = np.transpose(np.any(R_m == 1, axis=1)[None]) * ones(R.shape)
    # Blue rows.
    B_r = np.transpose(np.any(B_m == 1, axis=1)[None]) * ones(B.shape)

    k_b = as_float_array([0.5, 0, 0.5])

    R = np.where(
        np.logical_and(G_m == 1, R_r == 1),
        G + _cnv_h(R, k_b) - _cnv_h(G, k_b),
        R,
    )

    R = np.where(
        np.logical_and(G_m == 1, B_r == 1) == 1,
        G + _cnv_v(R, k_b) - _cnv_v(G, k_b),
        R,
    )

    B = np.where(
        np.logical_and(G_m == 1, B_r == 1),
        G + _cnv_h(B, k_b) - _cnv_h(G, k_b),
        B,
    )

    B = np.where(
        np.logical_and(G_m == 1, R_r == 1) == 1,
        G + _cnv_v(B, k_b) - _cnv_v(G, k_b),
        B,
    )

    R = np.where(
        np.logical_and(B_r == 1, B_m == 1),
        np.where(
            M == 1,
            B + _cnv_h(R, k_b) - _cnv_h(B, k_b),
            B + _cnv_v(R, k_b) - _cnv_v(B, k_b),
        ),
        R,
    )

    B = np.where(
        np.logical_and(R_r == 1, R_m == 1),
        np.where(
            M == 1,
            R + _cnv_h(B, k_b) - _cnv_h(R, k_b),
            R + _cnv_v(B, k_b) - _cnv_v(R, k_b),
        ),
        B,
    )

    RGB = tstack([R, G, B])

    del R, G, B, k_b, R_r, B_r

    if refining_step:
        RGB = refining_step_Menon2007(RGB, tstack([R_m, G_m, B_m]), M)

    del M, R_m, G_m, B_m

    return RGB


demosaicing_CFA_Bayer_DDFAPD = demosaicing_CFA_Bayer_Menon2007


def refining_step_Menon2007(
    RGB: ArrayLike, RGB_m: ArrayLike, M: ArrayLike
) -> NDArray:
    """
    Perform the refining step on given *RGB* colourspace array.

    Parameters
    ----------
    RGB
        *RGB* colourspace array.
    RGB_m
        *Bayer* CFA red, green and blue masks.
    M
        Estimation for the best directional reconstruction.

    Returns
    -------
    :class:`numpy.ndarray`
        Refined *RGB* colourspace array.

    Examples
    --------
    >>> RGB = np.array(
    ...     [
    ...         [
    ...             [0.30588236, 0.35686275, 0.3764706],
    ...             [0.30980393, 0.36078432, 0.39411766],
    ...             [0.29607844, 0.36078432, 0.40784314],
    ...             [0.29803923, 0.37647060, 0.42352942],
    ...         ],
    ...         [
    ...             [0.30588236, 0.35686275, 0.3764706],
    ...             [0.30980393, 0.36078432, 0.39411766],
    ...             [0.29607844, 0.36078432, 0.40784314],
    ...             [0.29803923, 0.37647060, 0.42352942],
    ...         ],
    ...     ]
    ... )
    >>> RGB_m = np.array(
    ...     [
    ...         [[0, 0, 1], [0, 1, 0], [0, 0, 1], [0, 1, 0]],
    ...         [[0, 1, 0], [1, 0, 0], [0, 1, 0], [1, 0, 0]],
    ...     ]
    ... )
    >>> M = np.array([[0, 1, 0, 1], [1, 0, 1, 0]])
    >>> refining_step_Menon2007(RGB, RGB_m, M)
    array([[[ 0.30588236,  0.35686275,  0.3764706 ],
            [ 0.30980393,  0.36078432,  0.39411765],
            [ 0.29607844,  0.36078432,  0.40784314],
            [ 0.29803923,  0.3764706 ,  0.42352942]],
    <BLANKLINE>
           [[ 0.30588236,  0.35686275,  0.3764706 ],
            [ 0.30980393,  0.36078432,  0.39411766],
            [ 0.29607844,  0.36078432,  0.40784314],
            [ 0.29803923,  0.3764706 ,  0.42352942]]])
    """

    R, G, B = tsplit(RGB)
    R_m, G_m, B_m = tsplit(RGB_m)
    M = as_float_array(M)

    del RGB, RGB_m

    # Updating of the green component.
    R_G = R - G
    B_G = B - G

    FIR = ones(3) / 3

    B_G_m = np.where(
        B_m == 1,
        np.where(M == 1, _cnv_h(B_G, FIR), _cnv_v(B_G, FIR)),
        0,
    )
    R_G_m = np.where(
        R_m == 1,
        np.where(M == 1, _cnv_h(R_G, FIR), _cnv_v(R_G, FIR)),
        0,
    )

    del B_G, R_G

    G = np.where(R_m == 1, R - R_G_m, G)
    G = np.where(B_m == 1, B - B_G_m, G)

    # Updating of the red and blue components in the green locations.
    # Red rows.
    R_r = np.transpose(np.any(R_m == 1, axis=1)[None]) * ones(R.shape)
    # Red columns.
    R_c = np.any(R_m == 1, axis=0)[None] * ones(R.shape)
    # Blue rows.
    B_r = np.transpose(np.any(B_m == 1, axis=1)[None]) * ones(B.shape)
    # Blue columns.
    B_c = np.any(B_m == 1, axis=0)[None] * ones(B.shape)

    R_G = R - G
    B_G = B - G

    k_b = as_float_array([0.5, 0.0, 0.5])

    R_G_m = np.where(
        np.logical_and(G_m == 1, B_r == 1),
        _cnv_v(R_G, k_b),
        R_G_m,
    )
    R = np.where(np.logical_and(G_m == 1, B_r == 1), G + R_G_m, R)
    R_G_m = np.where(
        np.logical_and(G_m == 1, B_c == 1),
        _cnv_h(R_G, k_b),
        R_G_m,
    )
    R = np.where(np.logical_and(G_m == 1, B_c == 1), G + R_G_m, R)

    del B_r, R_G_m, B_c, R_G

    B_G_m = np.where(
        np.logical_and(G_m == 1, R_r == 1),
        _cnv_v(B_G, k_b),
        B_G_m,
    )
    B = np.where(np.logical_and(G_m == 1, R_r == 1), G + B_G_m, B)
    B_G_m = np.where(
        np.logical_and(G_m == 1, R_c == 1),
        _cnv_h(B_G, k_b),
        B_G_m,
    )
    B = np.where(np.logical_and(G_m == 1, R_c == 1), G + B_G_m, B)

    del B_G_m, R_r, R_c, G_m, B_G

    # Updating of the red (blue) component in the blue (red) locations.
    R_B = R - B
    R_B_m = np.where(
        B_m == 1,
        np.where(M == 1, _cnv_h(R_B, FIR), _cnv_v(R_B, FIR)),
        0,
    )
    R = np.where(B_m == 1, B + R_B_m, R)

    R_B_m = np.where(
        R_m == 1,
        np.where(M == 1, _cnv_h(R_B, FIR), _cnv_v(R_B, FIR)),
        0,
    )
    B = np.where(R_m == 1, R - R_B_m, B)

    del R_B, R_B_m, R_m

    return tstack([R, G, B])
