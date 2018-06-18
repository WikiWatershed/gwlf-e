import unittest
from unittest import skip
import numpy as np
from gwlfe import Parser
from gwlfe.Outputs.AvAnimalNSum import N7b


class Testn7b(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    @skip("not ready")
    def test_n7b(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            N7b.n7b_f(),
            N7b.N7b(), decimal=7)