import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.MultiUse_Fxns import LossFactAdj


class TestLossFactAdj(VariableUnitTest):
    def test_LossFactAdj(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            LossFactAdj.LossFactAdj(z.NYrs, z.Prec, z.DaysMonth),
            LossFactAdj.LossFactAdj_f(z.Prec, z.DaysMonth), decimal=7)
