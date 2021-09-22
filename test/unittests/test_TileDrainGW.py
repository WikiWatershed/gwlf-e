import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.Input.LandUse.Ag import TileDrainGW


class TestTileDrainGW(VariableUnitTest):

    def test_TileDrainGW_ground_truth(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            np.load(self.basepath + "/TileDrainGW.npy"),
            TileDrainGW.TileDrainGW(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
                                    z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN,
                                    z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0,
                                    z.RecessionCoef, z.SeepCoef, z.Landuse, z.TileDrainDensity), decimal=7)

    def test_TileDrainGW(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            TileDrainGW.TileDrainGW_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
                                      z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN,
                                      z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0,
                                      z.RecessionCoef, z.SeepCoef, z.Landuse, z.TileDrainDensity),
            TileDrainGW.TileDrainGW(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
                                    z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN,
                                    z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0,
                                    z.RecessionCoef, z.SeepCoef, z.Landuse, z.TileDrainDensity), decimal=7)
