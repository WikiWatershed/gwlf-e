import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import CNum


class TestCNum(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    # @skip("not ready")
    def test_elementwise_CNum(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            np.load("CNum.npy"),
            CNum.CNum_1(z.NYrs, z.DaysMonth, z.Temp, z.Prec, z.InitSnow_0, z.AntMoist_0, z.CN, z.NRur, z.NUrb, z.Grow), decimal=7)

    # @skip("not ready")
    def test_CNum(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            CNum.CNum(z.NYrs, z.DaysMonth, z.Temp, z.Prec, z.InitSnow_0, z.AntMoist_0, z.CN, z.NRur, z.NUrb, z.Grow),
            CNum.CNum_2(z.NYrs, z.DaysMonth, z.Temp, z.Prec, z.InitSnow_0, z.AntMoist_0, z.CN, z.NRur, z.NUrb, z.Grow), decimal=7)