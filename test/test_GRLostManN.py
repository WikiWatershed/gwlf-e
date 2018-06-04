import unittest

import numpy as np

from gwlfe import Parser
from gwlfe.AFOS.GrazingAnimals.Losses import GRLostManN


class TestGRLostManN(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_GRLostManN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GRLostManN.GRLostManN(z.NYrs, z.GRPctManApp, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN,
                                  z.GRAppNRate, z.Prec, z.DaysMonth, z.GRPctSoilIncRate),
            GRLostManN.GRLostManN_2(z.NYrs, z.GRPctManApp, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt,
                                    z.AnimalDailyN, z.GRAppNRate, z.Prec, z.DaysMonth, z.GRPctSoilIncRate), decimal=7)
