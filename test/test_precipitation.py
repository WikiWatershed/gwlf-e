import unittest
import numpy as np
from gwlfe import Parser
from gwlfe import Precipitation


class TestPrecipitation(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_Precipitation(self):
        z = self.z
        np.testing.assert_array_almost_equal(Precipitation.Precipitation_2(z.Prec),
                                             Precipitation.Precipitation(z.NYrs, z.DaysMonth, z.Prec), decimal=7)

    def test_AvPrecipitation(self):
        z = self.z
        np.testing.assert_array_almost_equal(Precipitation.AvPrecipitation_2(z.Precipitation),
                                             Precipitation.AvPrecipitation(z.NYrs,z.Precipitation), decimal=7)
