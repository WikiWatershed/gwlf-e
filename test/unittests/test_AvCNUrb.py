import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.MultiUse_Fxns.Runoff import AvCNUrb


class TestAvCNUrb(VariableUnitTest):
    # @skip("Not Ready Yet.")
    def test_AvCNUrb(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            AvCNUrb.AvCNUrb_f(z.NRur, z.NUrb, z.CNI_0, z.CNP_0, z.Imper, z.Area),
            AvCNUrb.AvCNUrb(z.NRur, z.NUrb, z.CNI_0, z.CNP_0, z.Imper, z.Area), decimal=7)
