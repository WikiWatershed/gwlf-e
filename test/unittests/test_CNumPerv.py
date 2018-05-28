import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import CNumPerv


class TestCNumPerv(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    # @skip("not ready")
    def test_CNumPerv(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            CNumPerv.CNumPerv_2(z.NYrs, z.DaysMonth, z.Temp, z.NRur, z.NUrb, z.CNP_0, z.InitSnow_0, z.Prec, z.Grow_0,
                                z.AntMoist_0),
            CNumPerv.CNumPerv(z.NYrs, z.DaysMonth, z.Temp, z.NRur, z.NUrb, z.CNP_0, z.InitSnow_0, z.Prec, z.Grow_0,
                              z.AntMoist_0), decimal=7)
