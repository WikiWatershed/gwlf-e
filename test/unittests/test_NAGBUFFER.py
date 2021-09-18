import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.BMPs.AgAnimal import NAGBUFFER


class TestNAGBUFFER(VariableUnitTest):

    def test_NAGBUFFER(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            NAGBUFFER.NAGBUFFER_f(z.n42, z.n43, z.n64, z.NYrs, z.NGPctManApp, z.GrazingAnimal_0, z.NumAnimals,
                                  z.AvgAnimalWt, z.AnimalDailyN, z.NGBarnNRate,
                                  z.Prec, z.DaysMonth, z.AWMSNgPct, z.NgAWMSCoeffN, z.RunContPct, z.RunConCoeffN,
                                  z.GRPctManApp, z.PctGrazing, z.GRBarnNRate,
                                  z.AWMSGrPct, z.GrAWMSCoeffN, z.PctStreams, z.NGAppNRate, z.NGPctSoilIncRate,
                                  z.GRAppNRate, z.GRPctSoilIncRate,
                                  z.GrazingNRate),
            NAGBUFFER.NAGBUFFER(z.n42, z.n43, z.n64, z.NYrs, z.NGPctManApp, z.GrazingAnimal_0, z.NumAnimals,
                                z.AvgAnimalWt, z.AnimalDailyN, z.NGBarnNRate,
                                z.Prec, z.DaysMonth, z.AWMSNgPct, z.NgAWMSCoeffN, z.RunContPct, z.RunConCoeffN,
                                z.GRPctManApp, z.PctGrazing, z.GRBarnNRate,
                                z.AWMSGrPct, z.GrAWMSCoeffN, z.PctStreams, z.NGAppNRate, z.NGPctSoilIncRate,
                                z.GRAppNRate, z.GRPctSoilIncRate,
                                z.GrazingNRate), decimal=7)
