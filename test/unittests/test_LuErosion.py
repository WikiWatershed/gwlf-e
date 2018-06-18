import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import LuErosion


class TestLuErosion(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    # @skip("not ready")
    def test_LuErosion(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            LuErosion.LuErosion_f(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.Acoef, z.KF, z.LS,
                z.C, z.P, z.Area),
            LuErosion.LuErosion(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.NUrb,z.Acoef, z.KF, z.LS,
                z.C, z.P, z.Area), decimal=7)
