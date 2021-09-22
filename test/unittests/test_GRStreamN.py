import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.AFOS.GrazingAnimals.Losses import GRStreamN


class TestPercolation(VariableUnitTest):
    def test_GRStreamN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GRStreamN.GRStreamN_f(z.PctStreams, z.PctGrazing, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt,
                                  z.AnimalDailyN),
            GRStreamN.GRStreamN(z.PctStreams, z.PctGrazing, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt,
                                z.AnimalDailyN)[None, :], decimal=7)

    def test_AvGRStreamN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GRStreamN.AvGRStreamN_f(z.PctStreams, z.PctGrazing, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt,
                                    z.AnimalDailyN),
            GRStreamN.AvGRStreamN(z.PctStreams, z.PctGrazing, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt,
                                  z.AnimalDailyN),
            decimal=7)
