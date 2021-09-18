import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.AFOS.GrazingAnimals.Loads import GrazingN


class TestGrazingN(VariableUnitTest):
    def test_GrazingN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GrazingN.GrazingN(z.PctGrazing, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN)[None, :],
            GrazingN.GrazingN_f(z.PctGrazing, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN),
            decimal=7)
