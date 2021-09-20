import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.Input.WaterBudget import AvGroundWater


class TestAvGroundWater(VariableUnitTest):

    def test_AvGroundWater(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            AvGroundWater.AvGroundWater_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
                                          z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN,
                                          z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0,
                                          z.RecessionCoef, z.SeepCoef, z.Landuse, z.TileDrainDensity),
            AvGroundWater.AvGroundWater(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
                                        z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN,
                                        z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0,
                                        z.RecessionCoef, z.SeepCoef, z.Landuse, z.TileDrainDensity), decimal=7)
