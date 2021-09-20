import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.BMPs.Stream import UrbLoadRed


class TestUrbLoadRed(VariableUnitTest):

    def test_UrbLoadRed(self):
        z = self.z
        # UrbLoadRed.UrbLoadRed_1(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
        #                         z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention,
        #                         z.PctAreaInfil, z.Nqual, z.Storm, z.UrbBMPRed)
        # UrbLoadRed.UrbLoadRed_f(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
        #                         z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention,
        #                         z.PctAreaInfil, z.Nqual, z.Storm, z.UrbBMPRed)
        # UrbLoadRed.UrbLoadRed_3(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
        #                         z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention,
        #                         z.PctAreaInfil, z.Nqual, z.Storm, z.UrbBMPRed)
        np.testing.assert_array_almost_equal(
            UrbLoadRed.UrbLoadRed_f(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                                    z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention,
                                    z.PctAreaInfil, z.Nqual, z.Storm, z.UrbBMPRed),
            UrbLoadRed.UrbLoadRed(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                                  z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention,
                                  z.PctAreaInfil, z.Nqual, z.Storm, z.UrbBMPRed), decimal=7)
