import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.AFOS.GrazingAnimals.Loads import GRInitBarnN


class TestGRInitBarnN(VariableUnitTest):

    def test_GRInitBarnN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GRInitBarnN.GRInitBarnN(z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN, z.GRPctManApp,
                                    z.PctGrazing)[None, :],
            GRInitBarnN.GRInitBarnN_f(z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN, z.GRPctManApp,
                                      z.PctGrazing), decimal=7)
