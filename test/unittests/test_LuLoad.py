import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.Output.Loading import LuLoad


class TestLuLoad(VariableUnitTest):

    def test_LuLoad(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            LuLoad.LuLoad_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                            z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention, z.PctAreaInfil,
                            z.Nqual, z.LoadRateImp, z.LoadRatePerv, z.Storm, z.UrbBMPRed, z.FilterWidth, z.PctStrmBuf),
            LuLoad.LuLoad(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                          z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention, z.PctAreaInfil,
                          z.Nqual, z.LoadRateImp, z.LoadRatePerv, z.Storm, z.UrbBMPRed,
                          z.FilterWidth, z.PctStrmBuf)[:, z.NRur:], decimal=7)
