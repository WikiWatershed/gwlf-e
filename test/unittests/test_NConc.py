import unittest

import numpy as np

from gwlfe import NConc
from gwlfe import Parser


class TestNConc(unittest.TestCase):
    def setUp(self):
        input_file = open('integrationtests/test1.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_NConc(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            NConc.NConc_2(z.NRur, z.NUrb, z.NitrConc, z.ManNitr, z.ManuredAreas, z.FirstManureMonth, z.LastManureMonth,
                          z.FirstManureMonth2, z.LastManureMonth2),
            NConc.NConc(z.NRur, z.NUrb, z.NitrConc, z.ManNitr, z.ManuredAreas, z.FirstManureMonth, z.LastManureMonth,
                        z.FirstManureMonth2, z.LastManureMonth2), decimal=7)
