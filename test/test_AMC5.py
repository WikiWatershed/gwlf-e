import unittest
from unittest import skip
from mock import patch
import pickle
import numpy as np
from gwlfe import Parser
from gwlfe import AMC5
from gwlfe import DailyArrayConverter


class TestAMC5(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_AMC5(self):
        z = self.z

        yesterday_amc5 = np.ravel(AMC5.AMC5_yesterday(z.NYrs, z.DaysMonth, z.Temp, z.Prec, z.InitSnow_0, z.AntMoist_0))
        amc5 = np.ravel(AMC5.AMC5(z.NYrs, z.DaysMonth, z.Temp, z.Prec, z.InitSnow_0, z.AntMoist_0))
        np.testing.assert_array_almost_equal(
            yesterday_amc5[1:],amc5[:-1], decimal=7)