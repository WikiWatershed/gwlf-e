import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.AFOS.nonGrazingAnimals.Loads import InitNgN


class TestInitNgN(VariableUnitTest):
    def test_InitNgN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            InitNgN.InitNgN_f(z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN),
            InitNgN.InitNgN(z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN), decimal=7)
