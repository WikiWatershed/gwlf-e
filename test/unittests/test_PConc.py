import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.Output.Loading import PConc


class TestPConc(VariableUnitTest):
    def test_PConc(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            PConc.PConc_f(z.NRur, z.NUrb, z.PhosConc, z.ManPhos, z.ManuredAreas, z.FirstManureMonth, z.LastManureMonth,
                          z.FirstManureMonth2,
                          z.LastManureMonth2),
            PConc.PConc(z.NRur, z.NUrb, z.PhosConc, z.ManPhos, z.ManuredAreas, z.FirstManureMonth, z.LastManureMonth,
                        z.FirstManureMonth2,
                        z.LastManureMonth2), decimal=7)
