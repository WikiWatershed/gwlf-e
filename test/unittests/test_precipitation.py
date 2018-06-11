import unittest
from unittest import skip
import numpy as np
from gwlfe import Parser
from gwlfe.MultiUse_Fxns import Precipitation


class TestPrecipitation(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    def test_Precipitation(self):
        z = self.z
        temp_2 = Precipitation.Precipitation_2(z.Prec)
        temp = Precipitation.Precipitation(z.NYrs, z.DaysMonth, z.Prec)
        np.testing.assert_array_almost_equal(Precipitation.Precipitation_2(z.Prec),
                                             Precipitation.Precipitation(z.NYrs, z.DaysMonth, z.Prec), decimal=7)

