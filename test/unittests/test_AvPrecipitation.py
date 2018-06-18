import unittest
from unittest import skip
import numpy as np
from gwlfe import Parser
from gwlfe.MultiUse_Fxns import AvPrecipitation


class TestAvPrecipitation(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    # def test_AvPrecipitation(self):
    #     z = self.z
    #     np.testing.assert_array_almost_equal(AvPrecipitation.AvPrecipitation_f(z.Prec),
    #                                          AvPrecipitation.AvPrecipitation(z.NYrs, z.Prec), decimal=7)
