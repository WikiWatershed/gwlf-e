import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.Input.Animals import TotLAEU


class TestTotLAEU(VariableUnitTest):

    def test_TotLAEU(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            TotLAEU.TotLAEU_f(z.NumAnimals, z.AvgAnimalWt),
            TotLAEU.TotLAEU(z.NumAnimals, z.AvgAnimalWt), decimal=7)
