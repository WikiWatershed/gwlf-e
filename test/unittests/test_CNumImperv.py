import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import CNumImperv


class TestCNumImperv(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    # @skip("not ready")
    def test_CNumImperv(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            CNumImperv.CNumImperv_2(z.NYrs, z.NRur, z.NUrb, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.CNI_0, z.Grow_0, z.AntMoist_0),
            CNumImperv.CNumImperv(z.NYrs, z.NRur, z.NUrb, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.CNI_0, z.Grow_0, z.AntMoist_0), decimal=7)