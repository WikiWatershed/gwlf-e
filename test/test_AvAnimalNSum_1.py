import unittest
from unittest import skip
import numpy as np
from gwlfe import Parser
from gwlfe.Outputs.AvAnimalNSum import AvAnimalNSum_1


class TestAvAnimalNSum_1(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    @skip("not ready")
    def test_AvAnimalNSum_1(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            AvAnimalNSum_1.AvAnimalNSum_1_f(),
            AvAnimalNSum_1.AvAnimalNSum_1(), decimal=7)