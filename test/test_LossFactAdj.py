import unittest
import numpy as np
from gwlfe import Parser
from gwlfe.MultiUse_Fxns import LossFactAdj


class TestLossFactAdj(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_LossFactAdj(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            LossFactAdj.LossFactAdj(z.NYrs, z.Prec, z.DaysMonth),
            LossFactAdj.LossFactAdj_2(z.Prec, z.DaysMonth), decimal=7)
