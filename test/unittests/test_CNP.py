import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.MultiUse_Fxns.Runoff import CNP


class TestCNP(VariableUnitTest):

    def test_CNP(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            CNP.CNP_f(z.NRur, z.NUrb, z.CNP_0),
            CNP.CNP(z.NRur, z.NUrb, z.CNP_0), decimal=7)
