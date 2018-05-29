import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import RurEros


class TestRurEros(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_elementwise_RurEros(self):
        z = self.z
        temp = np.load("unittests/RurEros.npy")
        temp2 = RurEros.RurEros(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.Acoef, z.NRur, z.KF, z.LS, z.C, z.P,
                            z.Area)
        for i,j in zip(np.ravel(temp),np.ravel(temp2)):
            print(i,j,abs(i-j)>0.000001)
        np.testing.assert_array_almost_equal(
            np.load("unittests/RurEros.npy"),
            RurEros.RurEros_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.Acoef, z.NRur, z.KF, z.LS, z.C, z.P,
                            z.Area), decimal=7)

    def test_RurEros(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            RurEros.RurEros_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.Acoef, z.NRur, z.KF, z.LS, z.C, z.P,
                              z.Area),
            RurEros.RurEros(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.Acoef, z.NRur, z.KF, z.LS, z.C, z.P,
                            z.Area), decimal=7)
