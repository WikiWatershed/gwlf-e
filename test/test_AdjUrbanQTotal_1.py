import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import AdjUrbanQTotal_1


class TestAdjUrbanQTotal_1(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    @skip("not ready")
    def test_AdjUrbanQTotal_1(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            AdjUrbanQTotal_1.AdjUrbanQTotal_1_2(),
            AdjUrbanQTotal_1.AdjUrbanQTotal_1(), decimal=7)