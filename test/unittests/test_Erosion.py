import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import Erosion


class TestErosion(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_elementwise_Erosion(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            np.load("unittests/Erosion.npy"),
            Erosion.Erosion(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.Acoef, z.NRur, z.KF, z.LS, z.C, z.P,
                             z.Area), decimal=7)

    def test_Erosion(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            Erosion.Erosion_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.Acoef, z.NRur, z.KF, z.LS, z.C, z.P,
                              z.Area),
            Erosion.Erosion(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.Acoef, z.NRur, z.KF, z.LS, z.C, z.P,
                            z.Area), decimal=7)
