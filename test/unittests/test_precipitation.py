import unittest
from unittest import skip
import numpy as np
from gwlfe import Parser
from gwlfe import Precipitation


class TestPrecipitation(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    @skip("not ready")
    def test_Precipitation(self):
        z = self.z
        np.testing.assert_array_almost_equal(Precipitation.Precipitation_2(z.Prec),
                                             Precipitation.Precipitation(z.NYrs, z.DaysMonth, z.Prec), decimal=7)

    @skip("not ready")
    def test_AvPrecipitation(self):
        z = self.z
        np.testing.assert_array_almost_equal(Precipitation.AvPrecipitation_2(z.Prec),
                                             Precipitation.AvPrecipitation(z.NYrs,z.DaysMonth,z.Prec), decimal=7)
