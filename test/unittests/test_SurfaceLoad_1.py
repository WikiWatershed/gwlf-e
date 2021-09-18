import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.Output.Loading import SurfaceLoad_1


class TestSurfaceLoad_1(VariableUnitTest):

    def test_SurfaceLoad_1(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            SurfaceLoad_1.SurfaceLoad_1_f(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.NUrb, z.Area,
                                          z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA,
                                          z.Qretention, z.PctAreaInfil, z.Nqual, z.LoadRateImp, z.LoadRatePerv, z.Storm,
                                          z.UrbBMPRed, z.FilterWidth, z.PctStrmBuf),
            SurfaceLoad_1.SurfaceLoad_1(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.NUrb, z.Area,
                                        z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention,
                                        z.PctAreaInfil, z.Nqual, z.LoadRateImp, z.LoadRatePerv, z.Storm, z.UrbBMPRed,
                                        z.FilterWidth, z.PctStrmBuf)[:, :, :, z.NRur:], decimal=7)
