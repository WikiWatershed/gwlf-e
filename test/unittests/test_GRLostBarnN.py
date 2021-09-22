import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.AFOS.GrazingAnimals.Losses.GRLostBarnN import GRLostBarnN
from gwlfe.AFOS.GrazingAnimals.Losses.GRLostBarnN import GRLostBarnN_f


class TestGRLostBarnN(VariableUnitTest):

    def test_GRLostBarnN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GRLostBarnN(z.NYrs, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN,
                        z.GRPctManApp, z.PctGrazing, z.GRBarnNRate, z.Prec,
                        z.DaysMonth, z.AWMSGrPct, z.GrAWMSCoeffN, z.RunContPct, z.RunConCoeffN),
            GRLostBarnN_f(z.NYrs, z.Prec, z.DaysMonth, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN,
                          z.GRPctManApp, z.PctGrazing, z.GRBarnNRate, z.AWMSGrPct, z.GrAWMSCoeffN, z.RunContPct,
                          z.RunConCoeffN), decimal=7)
