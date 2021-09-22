import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.Output.AvAnimalNSum import N7b


class Testn7b(VariableUnitTest):

    def test_n7b_groundtruth(self):
        z = self.z

        np.testing.assert_array_almost_equal(43530.36750559382,
                                             N7b.N7b(z.NYrs, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt,
                                                     z.AnimalDailyN, z.NGAppNRate,
                                                     z.NGPctSoilIncRate, z.GRAppNRate, z.GRPctSoilIncRate,
                                                     z.GrazingNRate, z.GRPctManApp, z.PctGrazing,
                                                     z.GRBarnNRate, z.Prec, z.DaysMonth, z.AWMSGrPct, z.GrAWMSCoeffN,
                                                     z.RunContPct, z.RunConCoeffN,
                                                     z.n41b, z.n85h, z.NGPctManApp, z.AWMSNgPct, z.NGBarnNRate,
                                                     z.NgAWMSCoeffN, z.n41d, z.n85j, z.n41f,
                                                     z.n85l, z.PctStreams, z.n42, z.n45, z.n69, z.n43, z.n64),
                                             decimal=7)

    def test_n7b(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            N7b.N7b_f(z.NYrs, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN, z.NGAppNRate,
                      z.NGPctSoilIncRate, z.GRAppNRate, z.GRPctSoilIncRate, z.GrazingNRate, z.GRPctManApp, z.PctGrazing,
                      z.GRBarnNRate, z.Prec, z.DaysMonth, z.AWMSGrPct, z.GrAWMSCoeffN, z.RunContPct, z.RunConCoeffN,
                      z.n41b, z.n85h, z.NGPctManApp, z.AWMSNgPct, z.NGBarnNRate, z.NgAWMSCoeffN, z.n41d, z.n85j, z.n41f,
                      z.n85l, z.PctStreams, z.n42, z.n45, z.n69, z.n43, z.n64),
            N7b.N7b(z.NYrs, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN, z.NGAppNRate,
                    z.NGPctSoilIncRate, z.GRAppNRate, z.GRPctSoilIncRate, z.GrazingNRate, z.GRPctManApp, z.PctGrazing,
                    z.GRBarnNRate, z.Prec, z.DaysMonth, z.AWMSGrPct, z.GrAWMSCoeffN, z.RunContPct, z.RunConCoeffN,
                    z.n41b, z.n85h, z.NGPctManApp, z.AWMSNgPct, z.NGBarnNRate, z.NgAWMSCoeffN, z.n41d, z.n85j, z.n41f,
                    z.n85l, z.PctStreams, z.n42, z.n45, z.n69, z.n43, z.n64), decimal=7)
