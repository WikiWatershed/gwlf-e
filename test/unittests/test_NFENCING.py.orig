import unittest
from unittest import skip
import numpy as np
from gwlfe import Parser
from gwlfe.BMPs.AgAnimal import NFENCING


class TestNFENCING(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    def test_NFENCING(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            NFENCING.NFENCING_2(z.PctStreams, z.PctGrazing, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN, z.n42, z.n45, z.n69),
            NFENCING.NFENCING(z.PctStreams, z.PctGrazing, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN, z.n42, z.n45, z.n69), decimal=7)