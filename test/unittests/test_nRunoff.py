import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.MultiUse_Fxns.Runoff import nRunoff


class TestnRunoff(VariableUnitTest):
    def test_nRunoff(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            nRunoff.nRunoff_f(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.AntMoist_0, z.NRur, z.NUrb, z.CN,
                              z.Grow_0, z.Area, z.NitrConc, z.ManNitr, z.ManuredAreas, z.FirstManureMonth,
                              z.LastManureMonth, z.FirstManureMonth2, z.LastManureMonth2),
            nRunoff.nRunoff(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.AntMoist_0, z.NRur, z.NUrb, z.CN,
                            z.Grow_0, z.Area, z.NitrConc, z.ManNitr, z.ManuredAreas, z.FirstManureMonth,
                            z.LastManureMonth, z.FirstManureMonth2, z.LastManureMonth2), decimal=7)
