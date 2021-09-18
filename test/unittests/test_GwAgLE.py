import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.Input.LandUse.Ag import GwAgLE


class TestGwAgLE(VariableUnitTest):

    def test_GwAgLE(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GwAgLE.GwAgLE_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                            z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV,
                            z.PcntET,
                            z.DayHrs, z.MaxWaterCap, z.SatStor_0, z.RecessionCoef, z.SeepCoef, z.Landuse),
            GwAgLE.GwAgLE(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                          z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET,
                          z.DayHrs, z.MaxWaterCap, z.SatStor_0, z.RecessionCoef, z.SeepCoef, z.Landuse), decimal=7)
