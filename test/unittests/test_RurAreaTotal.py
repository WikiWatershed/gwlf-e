import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.Input.LandUse import RurAreaTotal


class TestRurAreaTotal(VariableUnitTest):

    def test_RurAreaTotal(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            RurAreaTotal.RurAreaTotal_f(z.NRur, z.Area),
            RurAreaTotal.RurAreaTotal(z.NRur, z.Area), decimal=7)
