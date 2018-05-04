import unittest
from unittest import skip
import numpy as np
from gwlfe import Parser
from gwlfe.Outputs.AvAnimalNSum import N7b_1


class TestN7b_1(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    @skip("not ready")
    def test_N7b_1(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            N7b_1.N7b_1_2(),
            N7b_1.N7b_1(), decimal=7)