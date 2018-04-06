import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import UrbanQTotal_1


class TestUrbanQTotal_1(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    @skip("not ready")
    def test_UrbanQTotal_1(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            UrbanQTotal_1.UrbanQTotal_1_2(),
            UrbanQTotal_1.UrbanQTotal_1(), decimal=7)