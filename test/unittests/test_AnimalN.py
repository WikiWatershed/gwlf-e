import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.Output.AvAnimalNSum import AnimalN


class TestAnimalN(VariableUnitTest):
    def test_AnimalN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            AnimalN.AnimalN_f(z.NYrs, z.NGPctManApp, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN,
                              z.NGAppNRate, z.Prec, z.DaysMonth,
                              z.NGPctSoilIncRate, z.GRPctManApp, z.GRAppNRate, z.GRPctSoilIncRate, z.NGBarnNRate,
                              z.AWMSNgPct, z.NgAWMSCoeffN,
                              z.RunContPct, z.RunConCoeffN, z.PctGrazing, z.GRBarnNRate, z.AWMSGrPct, z.GrAWMSCoeffN,
                              z.PctStreams, z.GrazingNRate),
            AnimalN.AnimalN(z.NYrs, z.NGPctManApp, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN,
                            z.NGAppNRate, z.Prec, z.DaysMonth,
                            z.NGPctSoilIncRate, z.GRPctManApp, z.GRAppNRate, z.GRPctSoilIncRate, z.NGBarnNRate,
                            z.AWMSNgPct, z.NgAWMSCoeffN,
                            z.RunContPct, z.RunConCoeffN, z.PctGrazing, z.GRBarnNRate, z.AWMSGrPct, z.GrAWMSCoeffN,
                            z.PctStreams, z.GrazingNRate), decimal=7)
