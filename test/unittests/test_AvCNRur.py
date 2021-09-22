import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.MultiUse_Fxns.Runoff import AvCNRur


class TestAvCNRur(VariableUnitTest):
    def test_AvCNRur(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            AvCNRur.AvCNRur_f(z.NRur, z.Area, z.CN),
            AvCNRur.AvCNRur(z.NRur, z.Area, z.CN), decimal=7)
