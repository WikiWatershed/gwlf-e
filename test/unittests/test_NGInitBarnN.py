import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.AFOS.nonGrazingAnimals.Loads import NGInitBarnN


class TestNGInitBarnN(VariableUnitTest):
    def test_NGInitBarnN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            NGInitBarnN.NGInitBarnN_f(z.NGPctManApp, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN),
            NGInitBarnN.NGInitBarnN(z.NGPctManApp, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN)[None,
            :], decimal=7)
