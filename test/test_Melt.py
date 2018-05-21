import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import Melt


class TestMelt(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    def test_Melt(self):
        z = self.z
        test = Melt.Melt(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec)
        test1 = Melt.Melt_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec)
        np.testing.assert_array_almost_equal(
            Melt.Melt(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec),
            Melt.Melt_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec), decimal=7)