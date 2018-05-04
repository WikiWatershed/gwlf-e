import unittest
from unittest import skip
import numpy as np
from gwlfe import Parser
from gwlfe.AFOS.GrazingAnimals.Loads import GrazingN


class TestGrazingN(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()
    @skip("not ready")
    def test_GrazingN(self):
        z = self.z
        np.testing.assert_array_almost_equal(GrazingN.GrazingN(z.PctGrazing, z.InitGrN),
                                             GrazingN.GrazingN_2(z.PctGrazing, z.InitGrN), decimal=7)
