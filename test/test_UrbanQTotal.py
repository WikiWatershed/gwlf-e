import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import UrbanQTotal


class TestUrbanQTotal(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    @skip("not ready")
    def test_UrbanQTotal(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            UrbanQTotal.UrbanQTotal_2(),
            UrbanQTotal.UrbanQTotal(), decimal=7)