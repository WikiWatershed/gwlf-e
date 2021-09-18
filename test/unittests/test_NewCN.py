import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.MultiUse_Fxns.Runoff import NewCN


class TestNewCN(VariableUnitTest):
    def test_NewCN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            NewCN.NewCN_f(z.NRur, z.NUrb, z.CN),
            NewCN.NewCN(z.NRur, z.NUrb, z.CN), decimal=7)
