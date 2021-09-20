import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.BMPs.AgAnimal import NAWMSL


class TestNAWMSL(VariableUnitTest):

    def test_NAWMSL(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            NAWMSL.NAWMSL_f(z.NYrs, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN, z.GRPctManApp,
                            z.PctGrazing, z.GRBarnNRate,
                            z.Prec, z.DaysMonth, z.AWMSGrPct, z.GrAWMSCoeffN, z.RunContPct, z.RunConCoeffN, z.n41b,
                            z.n85h),
            NAWMSL.NAWMSL(z.NYrs, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN, z.GRPctManApp,
                          z.PctGrazing, z.GRBarnNRate,
                          z.Prec, z.DaysMonth, z.AWMSGrPct, z.GrAWMSCoeffN, z.RunContPct, z.RunConCoeffN, z.n41b,
                          z.n85h), decimal=7)
