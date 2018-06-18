import unittest

import numpy as np

from gwlfe import DailyArrayConverter
from gwlfe import Parser
from gwlfe import gwlfe
from numpy.random import rand


class TestDailyArrayConverter(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_get_value_from_yesterday_initial(self):
        z = self.z
        test = rand(z.NYrs,12,31)
        for Y in range(z.NYrs):
            for i in range(12):
                for j in range(z.DaysMonth[Y][i]):
                    try:
                        np.testing.assert_array_almost_equal(
                            DailyArrayConverter.get_value_for_yesterday(test, 0, Y, i, j, z.NYrs, z.DaysMonth),
                            DailyArrayConverter.get_value_for_yesterday_2(test, 0, Y, i, j, z.NYrs, z.DaysMonth), decimal=7)
                    except AssertionError as e:
                        print(Y,i,j)
                        raise e
