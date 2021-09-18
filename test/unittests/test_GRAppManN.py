import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.AFOS.GrazingAnimals.Loads import GRAppManN


class TestGrAppManN(VariableUnitTest):
    def test_GrAppManN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GRAppManN.GRAppManN(z.GRPctManApp, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN),
            GRAppManN.GRAppManN_f(z.GRPctManApp, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN),
            decimal=7)
