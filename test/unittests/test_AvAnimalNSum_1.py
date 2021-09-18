import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.Output.AvAnimalNSum import AvAnimalNSum_1


class TestAvAnimalNSum_1(VariableUnitTest):

    def test_AvAnimalNSum_1(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            AvAnimalNSum_1.AvAnimalNSum_1_f(z.NYrs, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN,
                                            z.NGAppNRate, z.NGPctSoilIncRate, z.GRAppNRate,
                                            z.GRPctSoilIncRate, z.GrazingNRate, z.GRPctManApp, z.PctGrazing,
                                            z.GRBarnNRate,
                                            z.Prec, z.DaysMonth, z.AWMSGrPct, z.GrAWMSCoeffN, z.RunContPct,
                                            z.RunConCoeffN, z.n41b, z.n85h, z.NGPctManApp,
                                            z.AWMSNgPct, z.NGBarnNRate, z.NgAWMSCoeffN, z.n41d, z.n85j, z.n41f, z.n85l,
                                            z.PctStreams, z.n42, z.n45, z.n69, z.n43, z.n64),
            AvAnimalNSum_1.AvAnimalNSum_1(z.NYrs, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN,
                                          z.NGAppNRate, z.NGPctSoilIncRate, z.GRAppNRate,
                                          z.GRPctSoilIncRate, z.GrazingNRate, z.GRPctManApp, z.PctGrazing,
                                          z.GRBarnNRate,
                                          z.Prec, z.DaysMonth, z.AWMSGrPct, z.GrAWMSCoeffN, z.RunContPct,
                                          z.RunConCoeffN, z.n41b, z.n85h, z.NGPctManApp,
                                          z.AWMSNgPct, z.NGBarnNRate, z.NgAWMSCoeffN, z.n41d, z.n85j, z.n41f, z.n85l,
                                          z.PctStreams, z.n42, z.n45, z.n69, z.n43, z.n64), decimal=7)
