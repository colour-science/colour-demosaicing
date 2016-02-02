# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Defines unit tests for :mod:`colour_demosaicing.bayer.demosaicing.malvar2004`
module.
"""

from __future__ import division, unicode_literals

import numpy as np
import os
import unittest

import colour

from colour_demosaicing import TESTS_RESOURCES_DIRECTORY
from colour_demosaicing.bayer import demosaicing_CFA_Bayer_Malvar2004

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2015-2016 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = ['BAYER_DIRECTORY',
           'TestDemosaicing_CFA_Bayer_Malvar2004']

BAYER_DIRECTORY = os.path.join(
    TESTS_RESOURCES_DIRECTORY, 'colour_demosaicing', 'bayer')


class TestDemosaicing_CFA_Bayer_Malvar2004(unittest.TestCase):
    """
    Defines :func:`colour_demosaicing.bayer.demosaicing.malvar2004.\
demosaicing_CFA_Bayer_Malvar2004` definition unit tests methods.
    """

    def test_demosaicing_CFA_Bayer_Malvar2004(self):
        """
        Tests :func:`colour_demosaicing.bayer.demosaicing.malvar2004.\
demosaicing_CFA_Bayer_Malvar2004` definition.
        """

        for pattern in ('RGGB', 'BGGR', 'GRBG', 'GBRG'):
            np.testing.assert_almost_equal(
                demosaicing_CFA_Bayer_Malvar2004(
                    colour.read_image(
                        str(os.path.join(
                            BAYER_DIRECTORY,
                            'Lighthouse_CFA_{0}.exr'.format(pattern)))),
                    pattern),
                colour.read_image(
                    str(os.path.join(
                        BAYER_DIRECTORY,
                        'Lighthouse_Malvar2004_{0}.exr'.format(pattern)))),
                decimal=7)


if __name__ == '__main__':
    unittest.main()
