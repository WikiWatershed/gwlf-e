import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import Erosiv


class TestErosiv(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_elementwise_Erosiv(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            np.load("unittests/Erosiv.npy"),
            Erosiv.Erosiv(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.Acoef), decimal=7)

    def test_Erosiv(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            Erosiv.Erosiv_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.Acoef),
            Erosiv.Erosiv(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.Acoef), decimal=20)
