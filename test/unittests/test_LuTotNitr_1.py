import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.Output.Loading import LuTotNitr_1


class TestLuTotNitr_1(VariableUnitTest):

    def test_LuTotNitr_1(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            LuTotNitr_1.LuTotNitr_1_f(z.NYrs, z.NRur, z.NUrb, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.AntMoist_0,
                                      z.CN, z.Grow_0, z.Area, z.NitrConc, z.ManNitr, z.ManuredAreas, z.FirstManureMonth,
                                      z.LastManureMonth, z.FirstManureMonth2, z.LastManureMonth2, z.SedDelivRatio_0,
                                      z.KF,
                                      z.LS, z.C, z.P, z.SedNitr, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention,
                                      z.PctAreaInfil, z.LoadRateImp, z.LoadRatePerv, z.Storm, z.UrbBMPRed,
                                      z.FilterWidth, z.PctStrmBuf, z.Acoef, z.CNI_0, z.Nqual, z.ShedAreaDrainLake,
                                      z.RetentNLake, z.AttenFlowDist, z.AttenFlowVel, z.AttenLossRateN),
            LuTotNitr_1.LuTotNitr_1(z.NYrs, z.NRur, z.NUrb, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.AntMoist_0,
                                    z.CN, z.Grow_0, z.Area, z.NitrConc, z.ManNitr, z.ManuredAreas, z.FirstManureMonth,
                                    z.LastManureMonth, z.FirstManureMonth2, z.LastManureMonth2, z.SedDelivRatio_0, z.KF,
                                    z.LS, z.C, z.P, z.SedNitr, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention,
                                    z.PctAreaInfil, z.LoadRateImp, z.LoadRatePerv, z.Storm, z.UrbBMPRed,
                                    z.FilterWidth, z.PctStrmBuf, z.Acoef, z.CNI_0, z.Nqual, z.ShedAreaDrainLake,
                                    z.RetentNLake, z.AttenFlowDist, z.AttenFlowVel, z.AttenLossRateN)[:, :],
            decimal=7)
