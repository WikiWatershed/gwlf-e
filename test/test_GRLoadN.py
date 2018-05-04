import unittest
from unittest import skip
import numpy as np
from gwlfe import Parser
from gwlfe.AFOS.GrazingAnimals.Loads import GRLoadN


class TestGRLoadN(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    @skip("not ready")
    def test_newGRLoadN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GRLoadN.GRLoadN_2(),
            GRLoadN.GRLoadN(z.GrazingAnimal, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN), decimal=7)
