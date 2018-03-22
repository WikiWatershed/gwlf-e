import unittest
import numpy as np
from gwlfe import Parser
from gwlfe import GrazingN


class TestGrazingN(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_GrazingN(self):
        z = self.z
        np.testing.assert_array_almost_equal(GrazingN.GrazingN(z.PctGrazing, z.InitGrN),
                                             GrazingN.GrazingN_2(z.PctGrazing, z.InitGrN), decimal=7)
