import unittest

import numpy as np

from gwlfe import Parser
from gwlfe.AFOS.GrazingAnimals.Losses import GRLossN


class TestGRLossN(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_GRLossN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GRLossN.GRLossN(z.NYrs, z.PctStreams, z.PctGrazing, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt,
                            z.AnimalDailyN, z.GrazingNRate, z.Prec, z.DaysMonth),
            GRLossN.GRLossN_f(z.NYrs, z.PctStreams, z.PctGrazing, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN,
                              z.GrazingNRate, z.Prec, z.DaysMonth), decimal=7)
