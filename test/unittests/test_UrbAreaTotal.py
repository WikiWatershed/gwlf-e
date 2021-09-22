import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.Input.LandUse.Urb import UrbAreaTotal


class TestUrbAreaTotal(VariableUnitTest):

    def test_UrbAreaTotal(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            UrbAreaTotal.UrbAreaTotal_f(z.NRur, z.NUrb, z.Area),
            UrbAreaTotal.UrbAreaTotal(z.NRur, z.NUrb, z.Area), decimal=7)
