import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.Output.Loading import DisSurfLoad


class TestDisSurfLoad(VariableUnitTest):

    def test_DisSurfLoad(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            DisSurfLoad.DisSurfLoad_f(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.Nqual, z.NRur, z.NUrb,
                                      z.Area, z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA,
                                      z.Qretention, z.PctAreaInfil, z.LoadRateImp, z.LoadRatePerv,
                                      z.Storm, z.UrbBMPRed, z.DisFract, z.FilterWidth, z.PctStrmBuf),
            DisSurfLoad.DisSurfLoad(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.Nqual, z.NRur, z.NUrb,
                                    z.Area, z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA,
                                    z.Qretention, z.PctAreaInfil, z.LoadRateImp, z.LoadRatePerv,
                                    z.Storm, z.UrbBMPRed, z.DisFract, z.FilterWidth, z.PctStrmBuf)[:, :, :, z.NRur:],
            decimal=7)
