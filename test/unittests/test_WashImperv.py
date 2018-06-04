import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import WashImperv


class TestWashImperv(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    def test_WashImperv(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            WashImperv.WashImperv_2(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.CNI_0, z.AntMoist_0, z.Grow_0, z.NRur, z.NUrb),
            WashImperv.WashImperv(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.CNI_0, z.AntMoist_0, z.Grow_0, z.NRur, z.NUrb), decimal=7)