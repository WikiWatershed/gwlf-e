import unittest
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import GRLoadN
from gwlfe import gwlfe


class TestGRLoadN(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_GRLoadN(self):
        z = self.z
        result,z = gwlfe.run(z)
        np.testing.assert_array_almost_equal(
            z.GRLoadNStorage,
            GRLoadN.GRLoadN(z.GrazingAnimal, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN), decimal=7)

    def test_newGRLoadN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GRLoadN.GRLoadN_2(),
            GRLoadN.GRLoadN(z.GrazingAnimal, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN), decimal=7)
