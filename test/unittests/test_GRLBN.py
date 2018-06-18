import numpy as np

from VariableUnittest import VariableUnitTest
from gwlfe.AFOS.GrazingAnimals.Losses import GRLBN


class TestGRLBN(VariableUnitTest):

    def test_GRLBN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GRLBN.GRLBN_f(z.NYrs, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN, z.GRPctManApp,
                          z.PctGrazing, z.GRBarnNRate,
                          z.Prec, z.DaysMonth, z.AWMSGrPct, z.GrAWMSCoeffN, z.RunContPct, z.RunConCoeffN),
            GRLBN.GRLBN(z.NYrs, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN, z.GRPctManApp,
                        z.PctGrazing, z.GRBarnNRate,
                        z.Prec, z.DaysMonth, z.AWMSGrPct, z.GrAWMSCoeffN, z.RunContPct, z.RunConCoeffN), decimal=7)
