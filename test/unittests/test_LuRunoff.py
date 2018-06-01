import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import LuRunoff


class TestLuRunoff(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_LuRunoff(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            LuRunoff.LuRunoff_2(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.NUrb, z.CNI_0, z.CNP_0,
                                z.AntMoist_0, z.Grow_0, z.Imper, z.ISRR, z.ISRA, z.CN),
            LuRunoff.LuRunoff(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.NUrb, z.CNI_0, z.CNP_0,
                              z.AntMoist_0, z.Grow_0, z.Imper, z.ISRR, z.ISRA, z.CN), decimal=7)
