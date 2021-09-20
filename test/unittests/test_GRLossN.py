import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.AFOS.GrazingAnimals.Losses import GRLossN


class TestGRLossN(VariableUnitTest):

    def test_GRLossN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GRLossN.GRLossN(z.NYrs, z.PctStreams, z.PctGrazing, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt,
                            z.AnimalDailyN, z.GrazingNRate, z.Prec, z.DaysMonth),
            GRLossN.GRLossN_f(z.NYrs, z.PctStreams, z.PctGrazing, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt,
                              z.AnimalDailyN,
                              z.GrazingNRate, z.Prec, z.DaysMonth), decimal=7)
