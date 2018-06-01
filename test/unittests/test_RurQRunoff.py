import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import RurQRunoff


class TestRurQRunoff(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_RurQRunoff(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            RurQRunoff.RurQRunoff_2(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.AntMoist_0, z.NRur, z.NUrb,
                                    z.CN, z.Grow_0),
            np.swapaxes(
                RurQRunoff.RurQRunoff(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.AntMoist_0, z.NRur, z.NUrb,
                                      z.CN, z.Grow_0), 1, 2)[:, :, :z.NRur], decimal=7)
