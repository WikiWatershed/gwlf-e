import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.BMPs.Stream import NSTAB


class TestNSTAB(VariableUnitTest):

    def test_NSTAB(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            NSTAB.NSTAB_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
                          z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN,
                          z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0,
                          z.RecessionCoef, z.SeepCoef, z.Qretention, z.PctAreaInfil, z.n25b, z.Landuse,
                          z.TileDrainDensity, z.PointFlow, z.StreamWithdrawal, z.GroundWithdrawal,
                          z.NumAnimals, z.AvgAnimalWt, z.StreamFlowVolAdj, z.SedAFactor_0, z.AvKF,
                          z.AvSlope, z.SedAAdjust, z.StreamLength, z.n42b, z.n46c, z.SedNitr, z.BankNFrac, z.n69c),
            NSTAB.NSTAB(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
                        z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN,
                        z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0,
                        z.RecessionCoef, z.SeepCoef, z.Qretention, z.PctAreaInfil, z.n25b, z.Landuse,
                        z.TileDrainDensity, z.PointFlow, z.StreamWithdrawal, z.GroundWithdrawal,
                        z.NumAnimals, z.AvgAnimalWt, z.StreamFlowVolAdj, z.SedAFactor_0, z.AvKF,
                        z.AvSlope, z.SedAAdjust, z.StreamLength, z.n42b, z.n46c, z.SedNitr, z.BankNFrac, z.n69c),
            decimal=7)
