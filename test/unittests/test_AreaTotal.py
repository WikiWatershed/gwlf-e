import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.Input.LandUse import AreaTotal


class TestAreaTotal(VariableUnitTest):

    def test_AreaTotal(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            AreaTotal.AreaTotal_f(z.Area),
            AreaTotal.AreaTotal(z.NRur, z.NUrb, z.Area), decimal=7)
