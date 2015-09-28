#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Bayer CFA Masks
===============

*Bayer* CFA (Colour Filter Array) masks generation.
"""

from __future__ import division, unicode_literals

import numpy as np

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2015 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = ['masks_CFA_Bayer']


def masks_CFA_Bayer(shape, pattern='RGGB'):
    """
    Returns the *Bayer* CFA red, green and blue masks for given pattern.

    Parameters
    ----------
    shape : array_like
        Dimensions of the *Bayer* CFA.
    pattern : unicode, optional
        **{'RGGB', 'BGGR', 'GRBG', 'GBRG'}**
        Arrangement of the colour filters on the pixel array.

    Returns
    -------
    tuple
        *Bayer* CFA red, green and blue masks.

    Examples
    --------
    >>> from pprint import pprint
    >>> shape = (3, 3)
    >>> pprint(masks_CFA_Bayer(shape))
    (array([[ 1.,  0.,  1.],
           [ 0.,  0.,  0.],
           [ 1.,  0.,  1.]]),
     array([[ 0.,  1.,  0.],
           [ 1.,  0.,  1.],
           [ 0.,  1.,  0.]]),
     array([[ 0.,  0.,  0.],
           [ 0.,  1.,  0.],
           [ 0.,  0.,  0.]]))
    >>> pprint(masks_CFA_Bayer(shape, 'BGGR'))
    (array([[ 0.,  0.,  0.],
           [ 0.,  1.,  0.],
           [ 0.,  0.,  0.]]),
     array([[ 0.,  1.,  0.],
           [ 1.,  0.,  1.],
           [ 0.,  1.,  0.]]),
     array([[ 1.,  0.,  1.],
           [ 0.,  0.,  0.],
           [ 1.,  0.,  1.]]))
    """

    pattern = pattern.upper()

    channels = dict((channel, np.zeros(shape)) for channel in 'RGB')
    for channel, (y, x) in zip(pattern, [(0, 0), (0, 1), (1, 0), (1, 1)]):
        channels[channel][y::2, x::2] = 1

    return tuple(channels[c] for c in 'RGB')
