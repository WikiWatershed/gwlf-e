import numpy as np

from VariableUnittest import VariableUnitTest
from gwlfe import GrazingAnimal
from gwlfe.enums import YesOrNo


class TestGrazingAnimal(VariableUnitTest):
    def test_GrazingAnimal(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GrazingAnimal.GrazingAnimal_2(z.GrazingAnimal_0),
            GrazingAnimal.GrazingAnimal(z.GrazingAnimal_0) == YesOrNo.YES, decimal=7)
