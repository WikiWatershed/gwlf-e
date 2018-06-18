import numpy as np

from VariableUnittest import VariableUnitTest
from gwlfe import NewCN
from gwlfe import Parser


class TestNewCN(VariableUnitTest):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_NewCN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            NewCN.NewCN_f(z.NRur, z.NUrb, z.CN),
            NewCN.NewCN(z.NRur, z.NUrb, z.CN), decimal=7)
