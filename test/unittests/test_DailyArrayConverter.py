import unittest

import numpy as np

from gwlfe import DailyArrayConverter
from gwlfe import Parser


class TestDailyArrayConverter(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_get_value_from_yesterday(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            DailyArrayConverter.get_value_for_yesterday(z.Perc, 0, 0, 0, 0, z.NYrs, z.DaysMonth),
            [], decimal=7)
