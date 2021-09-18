import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.Output.Loading import LuTotPhos


class TestLuTotPhos(VariableUnitTest):
    def test_LuTotPhos(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            LuTotPhos.LuTotPhos_f(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.AntMoist_0, z.NRur, z.NUrb, z.CN,
                                  z.Grow_0, z.Area, z.PhosConc, z.ManPhos, z.ManuredAreas, z.FirstManureMonth,
                                  z.LastManureMonth, z.FirstManureMonth2, z.LastManureMonth2, z.SedDelivRatio_0, z.KF,
                                  z.LS, z.C, z.P, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention, z.PctAreaInfil,
                                  z.Nqual,
                                  z.LoadRateImp, z.LoadRatePerv, z.Storm, z.UrbBMPRed, z.FilterWidth, z.PctStrmBuf,
                                  z.Acoef, z.SedPhos, z.CNI_0),
            LuTotPhos.LuTotPhos(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.AntMoist_0, z.NRur, z.NUrb, z.CN,
                                z.Grow_0, z.Area, z.PhosConc, z.ManPhos, z.ManuredAreas, z.FirstManureMonth,
                                z.LastManureMonth, z.FirstManureMonth2, z.LastManureMonth2, z.SedDelivRatio_0, z.KF,
                                z.LS, z.C, z.P, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention, z.PctAreaInfil, z.Nqual,
                                z.LoadRateImp, z.LoadRatePerv, z.Storm, z.UrbBMPRed, z.FilterWidth, z.PctStrmBuf,
                                z.Acoef, z.SedPhos, z.CNI_0), decimal=7)
