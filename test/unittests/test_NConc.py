import numpy as np

from VariableUnittest import VariableUnitTest
from gwlfe.Output.Loading import NConc
from gwlfe import Parser


class TestNConc(VariableUnitTest):
    def setUp(self):
        input_file = open('integrationtests/test1.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_NConc(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            NConc.NConc_f(z.NRur, z.NUrb, z.NitrConc, z.ManNitr, z.ManuredAreas, z.FirstManureMonth, z.LastManureMonth,
                          z.FirstManureMonth2, z.LastManureMonth2),
            NConc.NConc(z.NRur, z.NUrb, z.NitrConc, z.ManNitr, z.ManuredAreas, z.FirstManureMonth, z.LastManureMonth,
                        z.FirstManureMonth2, z.LastManureMonth2), decimal=7)
