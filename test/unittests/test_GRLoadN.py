import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.AFOS.GrazingAnimals.Loads import GRLoadN
from gwlfe.enums import YesOrNo


class TestGRLoadN(VariableUnitTest):
    def test_newGRLoadN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GRLoadN.GRLoadN_f(z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN),
            GRLoadN.GRLoadN(z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN)[
                z.GrazingAnimal_0 == YesOrNo.YES], decimal=7)
