import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import ErosWashoff


class TestErosWashoff(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_ErosWashoff(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            ErosWashoff.ErosWashoff_f(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.Acoef, z.KF, z.LS,
                                      z.C, z.P, z.Area),
            np.swapaxes(ErosWashoff.ErosWashoff(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.NUrb, z.Acoef, z.KF,
                                    z.LS, z.C, z.P, z.Area)[:,:z.NRur],1,2), decimal=7)
