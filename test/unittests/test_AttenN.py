import numpy as np

from VariableUnittest import VariableUnitTest
from gwlfe.MultiUse_Fxns.AttenN import AttenN


class TestAttenN(VariableUnitTest):

    def test_AttenN(self):
        z = self.z
        np.testing.assert_array_almost_equal(0.077884625, AttenN(z.AttenFlowDist, z.AttenFlowVel, z.AttenLossRateN),
                                             decimal=7)
