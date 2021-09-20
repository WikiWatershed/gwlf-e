import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.AFOS.nonGrazingAnimals.Loads import NGAppManN


class TestNGAppManN(VariableUnitTest):
    def test_NGAppManN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            NGAppManN.NGAppManN_f(z.NGPctManApp, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN),
            NGAppManN.NGAppManN(z.NGPctManApp, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN),
            decimal=7)
