import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.Output.Loading import NConc


class TestNConc(VariableUnitTest):
    def test_NConc(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            NConc.NConc_f(z.NRur, z.NUrb, z.NitrConc, z.ManNitr, z.ManuredAreas, z.FirstManureMonth, z.LastManureMonth,
                          z.FirstManureMonth2, z.LastManureMonth2),
            NConc.NConc(z.NRur, z.NUrb, z.NitrConc, z.ManNitr, z.ManuredAreas, z.FirstManureMonth, z.LastManureMonth,
                        z.FirstManureMonth2, z.LastManureMonth2), decimal=7)
