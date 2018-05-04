import unittest
from unittest import skip
import numpy as np
from gwlfe import Parser
from gwlfe.AFOS.GrazingAnimals.Loads import GRInitBarnN


class TestGRInitBarnN(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_GRInitBarnN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GRInitBarnN.GRInitBarnN(z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN, z.GRPctManApp,
                                    z.PctGrazing),
            GRInitBarnN.GRInitBarnN_2(z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN, z.GRPctManApp,
                                      z.PctGrazing), decimal=7)
