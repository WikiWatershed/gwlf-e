import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import CNum


class TestCNum(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_elementwise_CNum(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            np.load("unittests/CNum.npy"),
            CNum.CNum_1(z.NYrs, z.DaysMonth, z.Temp, z.Prec, z.InitSnow_0, z.AntMoist_0, z.CN, z.NRur, z.NUrb,
                        z.Grow_0), decimal=7)

    def test_CNum(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            CNum.CNum(z.NYrs, z.DaysMonth, z.Temp, z.Prec, z.InitSnow_0, z.AntMoist_0, z.CN, z.NRur, z.NUrb, z.Grow_0),
            CNum.CNum_2(z.NYrs, z.DaysMonth, z.Temp, z.Prec, z.InitSnow_0, z.AntMoist_0, z.CN, z.NRur, z.NUrb,
                        z.Grow_0), decimal=7)
