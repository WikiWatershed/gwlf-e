import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import AgQTotal


class TestAgQTotal(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_AgQTotal(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            AgQTotal.AgQTotal_f(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.CN, z.AntMoist_0, z.NUrb,
                                z.Grow_0, z.Landuse, z.Area),
            AgQTotal.AgQTotal(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.CN, z.AntMoist_0, z.NUrb,
                              z.Grow_0, z.Landuse, z.Area), decimal=7)
