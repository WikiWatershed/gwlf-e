import unittest
from unittest import skip
import numpy as np
from gwlfe import Parser
from gwlfe.AFOS.GrazingAnimals.Loads import GRAccManAppN


class TestGRAccManAppN(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_GRAccManAppN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GRAccManAppN.GRAccManAppN(z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN, z.GRPctManApp,
                                      z.PctGrazing),
            GRAccManAppN.GRAccManAppN_2(z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN, z.GRPctManApp,
                                        z.PctGrazing), decimal=7)
