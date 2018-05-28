import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import Retention


class TestRetention(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    @skip("not ready")
    def test_Retention(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            Retention.Retention_2(z.NYrs, z.DaysMonth, z.Temp, z.Prec, z.InitSnow_0, z.AntMoist_0, z.NRur, z.NUrb, z.CN, z.Grow_0),
            Retention.Retention(z.NYrs, z.DaysMonth, z.Temp, z.Prec, z.InitSnow_0, z.AntMoist_0, z.NRur, z.NUrb, z.CN, z.Grow_0), decimal=7)