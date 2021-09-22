import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.AFOS.GrazingAnimals.Loads import GRAccManAppN


class TestGRAccManAppN(VariableUnitTest):

    def test_GRAccManAppN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GRAccManAppN.GRAccManAppN(z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN, z.GRPctManApp,
                                      z.PctGrazing)[None, :],
            GRAccManAppN.GRAccManAppN_f(z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN, z.GRPctManApp,
                                        z.PctGrazing), decimal=7)
