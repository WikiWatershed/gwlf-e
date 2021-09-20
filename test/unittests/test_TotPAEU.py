import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.Input.Animals import TotPAEU


class TestTotPAEU(VariableUnitTest):

    def test_TotPAEU(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            TotPAEU.TotPAEU_f(z.NumAnimals, z.AvgAnimalWt),
            TotPAEU.TotPAEU(z.NumAnimals, z.AvgAnimalWt), decimal=7)
