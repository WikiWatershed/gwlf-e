import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import InitSnow


class TestInitSnow(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    # @skip("not ready")
    def test_InitSnow(self):
        z = self.z
        # initsnow, _ = InitSnow.InitSnow_2(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec)
        np.testing.assert_array_almost_equal(
            InitSnow.InitSnow_2(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec),
            InitSnow.InitSnow(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec), decimal=7)