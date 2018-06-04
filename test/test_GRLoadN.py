import unittest
from unittest import skip
import numpy as np
from gwlfe import Parser
from gwlfe.AFOS.GrazingAnimals.Loads import GRLoadN
from gwlfe.enums import YesOrNo


class TestGRLoadN(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_newGRLoadN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GRLoadN.GRLoadN_2(z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN),
            GRLoadN.GRLoadN(z.GrazingAnimal_0,z.NumAnimals,z.AvgAnimalWt,z.AnimalDailyN)[z.GrazingAnimal_0 == YesOrNo.YES], decimal=7)
