import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.MultiUse_Fxns import PtSrcFlow


class TestPrecipitation(VariableUnitTest):

    def test_PtSrcFlow(self):
        z = self.z
        np.testing.assert_array_almost_equal(PtSrcFlow.PtSrcFlow_f(z.NYrs, z.PointFlow),
                                             PtSrcFlow.PtSrcFlow(z.NYrs, z.PointFlow), decimal=7)

    def test_AvPtSrcFlow(self):
        z = self.z
        z.PtSrcFlow = PtSrcFlow.PtSrcFlow_f(z.NYrs, z.PointFlow)
        np.testing.assert_array_almost_equal(PtSrcFlow.AvPtSrcFlow_f(z.PointFlow),
                                             PtSrcFlow.AvPtSrcFlow(z.NYrs, z.PtSrcFlow), decimal=7)
