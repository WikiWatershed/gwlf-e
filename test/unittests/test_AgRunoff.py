import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import AgRunoff


class TestAgRunoff(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    # @skip("not ready")
    def test_AgRunoff(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            AgRunoff.AgRunoff_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.CN, z.AntMoist_0, z.NUrb, z.Grow_0, z.Landuse, z.Area),
            AgRunoff.AgRunoff(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.CN, z.AntMoist_0, z.NUrb, z.Grow_0, z.Landuse, z.Area), decimal=7)