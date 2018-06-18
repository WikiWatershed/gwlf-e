import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import WashPerv


class TestPervAccum(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_PervAccum(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            WashPerv.WashPerv_f(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.CNP_0, z.AntMoist_0, z.Grow_0,
                                z.NRur, z.NUrb),
            WashPerv.WashPerv(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.CNP_0, z.AntMoist_0, z.Grow_0,
                              z.NRur, z.NUrb), decimal=7)
