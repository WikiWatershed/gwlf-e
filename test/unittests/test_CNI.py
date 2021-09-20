import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.MultiUse_Fxns.Runoff import CNI


class TestCNI(VariableUnitTest):

    def test_CNI(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            CNI.CNI_f(z.NRur, z.NUrb, z.CNI_0),
            CNI.CNI(z.NRur, z.NUrb, z.CNI_0), decimal=7)
