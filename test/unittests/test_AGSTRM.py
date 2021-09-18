import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.Input.LandUse.Ag import AGSTRM


class TestAGSTRM(VariableUnitTest):

    def test_AGSTRM(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            AGSTRM.AGSTRM_f(z.AgLength, z.StreamLength),
            AGSTRM.AGSTRM(z.AgLength, z.StreamLength), decimal=7)
