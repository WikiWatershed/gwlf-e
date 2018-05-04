import unittest
from unittest import skip
import numpy as np
from gwlfe import Parser
from gwlfe.AFOS.GrazingAnimals.Loads import GrazingN


class TestGrazingN(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_GrazingN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GrazingN.GrazingN(z.PctGrazing, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN),
            GrazingN.GrazingN_2(z.PctGrazing, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN),
            decimal=7)
