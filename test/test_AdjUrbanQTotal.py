import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import AdjUrbanQTotal


class TestAdjUrbanQTotal(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    @skip("not ready")
    def test_AdjUrbanQTotal(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            AdjUrbanQTotal.AdjUrbanQTotal_2(),
            AdjUrbanQTotal.AdjUrbanQTotal(), decimal=7)