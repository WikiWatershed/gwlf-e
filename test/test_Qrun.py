import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import Qrun


class TestQrun(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    @skip("not ready")
    def test_Qrun(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            Qrun.Qrun_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.CN, z.AntMoist_0, z.Grow),
            Qrun.Qrun(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.CN, z.AntMoist_0, z.Grow), decimal=7)