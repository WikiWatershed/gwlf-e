import unittest

import numpy as np

from gwlfe import Parser
from gwlfe.AFOS.nonGrazingAnimals.Loads import NGAccManAppN


class TestNGAccManAppN(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_NGAccManAppN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            NGAccManAppN.NGAccManAppN_f(z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN, z.NGPctManApp),
            NGAccManAppN.NGAccManAppN(z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN, z.NGPctManApp),
            decimal=7)
