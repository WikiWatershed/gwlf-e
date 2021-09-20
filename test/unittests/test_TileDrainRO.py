import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.Input.LandUse.Ag import TileDrainRO


class TestTileDrainRO(VariableUnitTest):

    # @skip("not ready")
    def test_TileDrainRO(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            TileDrainRO.TileDrainRO_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.CN, z.AntMoist_0,
                                      z.NUrb, z.Grow_0, z.Landuse, z.Area,
                                      z.TileDrainDensity),
            TileDrainRO.TileDrainRO(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.CN, z.AntMoist_0,
                                    z.NUrb, z.Grow_0, z.Landuse, z.Area,
                                    z.TileDrainDensity), decimal=7)
