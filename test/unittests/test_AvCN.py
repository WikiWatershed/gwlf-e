import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.MultiUse_Fxns.Runoff import AvCN


class TestAvCN(VariableUnitTest):

    def test_AvCN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            AvCN.AvCN_f(z.NRur, z.NUrb, z.CNI_0, z.CNP_0, z.CN, z.Imper, z.Area),
            AvCN.AvCN(z.NRur, z.NUrb, z.CNI_0, z.CNP_0, z.CN, z.Imper, z.Area), decimal=7)
