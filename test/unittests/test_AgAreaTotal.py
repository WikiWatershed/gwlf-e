import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import AgAreaTotal


class TestAgAreaTotal(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_AgAreaTotal(self):
        pass
        # z = self.z
        # np.testing.assert_array_almost_equal(
        #     AgAreaTotal.AgAreaTotal_f(z.Landuse, z.Area),
        #     AgAreaTotal.AgAreaTotal(z.NRur, z.Landuse, z.Area), decimal=7)
