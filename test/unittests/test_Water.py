import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import Water


class TestWater(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_Water_ground_truth(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            np.load("unittests/Water.npy"),
            Water.Water(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec), decimal=7)


    def test_Water(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            Water.Water_f(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec),
            Water.Water(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec), decimal=7)