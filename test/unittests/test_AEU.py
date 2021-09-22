import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.Input.Animals import AEU


class TestAEU(VariableUnitTest):

    def test_AEU(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            AEU.AEU_f(z.NumAnimals, z.AvgAnimalWt, z.Area),
            AEU.AEU(z.NumAnimals, z.AvgAnimalWt, z.NRur, z.NUrb, z.Area), decimal=7)
