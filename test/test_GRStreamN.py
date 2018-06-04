import unittest
from unittest import skip

import numpy as np

from gwlfe import Parser
from gwlfe.AFOS.GrazingAnimals.Losses import GRStreamN


class TestGRStreamN(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_GRStreamN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GRStreamN.GRStreamN_2(z.PctStreams, z.PctGrazing, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN),
            GRStreamN.GRStreamN(z.PctStreams, z.PctGrazing, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN)[None,:], decimal=7)

    @skip("not ready")
    def test_AvGRStreamN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GRStreamN.AvGRStreamN_2(),
            GRStreamN.AvGRStreamN(),
            decimal=7)
