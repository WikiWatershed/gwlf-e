import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.AFOS.GrazingAnimals.Losses import AvGRLostBarnNSum


class TestAvGRLostBarnNSum(VariableUnitTest):

    def test_AvGRLostBarnNSum(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            AvGRLostBarnNSum.AvGRLostBarnNSum_f(z.NYrs, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN,
                                                z.GRPctManApp, z.PctGrazing, z.GRBarnNRate,
                                                z.Prec, z.DaysMonth, z.AWMSGrPct, z.GrAWMSCoeffN, z.RunContPct,
                                                z.RunConCoeffN),
            AvGRLostBarnNSum.AvGRLostBarnNSum(z.NYrs, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN,
                                              z.GRPctManApp, z.PctGrazing, z.GRBarnNRate,
                                              z.Prec, z.DaysMonth, z.AWMSGrPct, z.GrAWMSCoeffN, z.RunContPct,
                                              z.RunConCoeffN), decimal=7)
