import numpy as np

from VariableUnittest import VariableUnitTest
from gwlfe.MultiUse_Fxns.Runoff import AvCNUrb
from gwlfe import Parser


class TestAvCNUrb(VariableUnitTest):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    # @skip("Not Ready Yet.")
    def test_AvCNUrb(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            AvCNUrb.AvCNUrb_f(z.NRur, z.NUrb, z.CNI_0, z.CNP_0, z.Imper, z.Area),
            AvCNUrb.AvCNUrb(z.NRur, z.NUrb, z.CNI_0, z.CNP_0, z.Imper, z.Area), decimal=7)
