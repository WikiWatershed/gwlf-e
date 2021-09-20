import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.Output.Loading import SurfaceLoad


class TestSurfaceLoad(VariableUnitTest):

    def test_SurfaceLoad(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            SurfaceLoad.SurfaceLoad_f(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.NUrb, z.Area,
                                      z.CNI_0,
                                      z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention,
                                      z.PctAreaInfil, z.Nqual, z.LoadRateImp, z.LoadRatePerv, z.Storm, z.UrbBMPRed),
            SurfaceLoad.SurfaceLoad(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                                    z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention,
                                    z.PctAreaInfil, z.Nqual, z.LoadRateImp, z.LoadRatePerv, z.Storm, z.UrbBMPRed)[:, :,
            :, z.NRur:],
            decimal=7)
