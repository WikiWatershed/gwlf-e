import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.AFOS.nonGrazingAnimals.Loads import NGAccManAppN


class TestNGAccManAppN(VariableUnitTest):

    def test_NGAccManAppN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            NGAccManAppN.NGAccManAppN_f(z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN, z.NGPctManApp),
            NGAccManAppN.NGAccManAppN(z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN, z.NGPctManApp),
            decimal=7)
