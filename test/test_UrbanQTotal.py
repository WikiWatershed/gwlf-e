import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import UrbanQTotal


class TestUrbanQTotal(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    # @skip("not ready")
    def test_UrbanQTotal(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            UrbanQTotal.UrbanQTotal_2(z.NYrs, z.DaysMonth, z.NRur, z.NUrb, z.Temp, z.InitSnow_0, z.Prec, z.Area, z.CNI_0,
                                      z.AntMoist_0, z.Grow, z.CNP_0, z.Imper, z.ISRR, z.ISRA),
            UrbanQTotal.UrbanQTotal(z.NYrs, z.DaysMonth, z.NRur, z.NUrb, z.Temp, z.InitSnow_0, z.Prec, z.Area, z.CNI_0,
                                      z.AntMoist_0, z.Grow, z.CNP_0, z.Imper, z.ISRR, z.ISRA), decimal=7)