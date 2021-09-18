import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.MultiUse_Fxns.Runoff import RetentionEff


class TestRetentionEff(VariableUnitTest):

    def test_RetentionEff(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            RetentionEff.RetentionEff_f(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.Qretention, z.NRur, z.NUrb,
                                        z.Area, z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA,
                                        z.PctAreaInfil),
            RetentionEff.RetentionEff(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.Qretention, z.NRur, z.NUrb,
                                      z.Area, z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA,
                                      z.PctAreaInfil), decimal=7)
