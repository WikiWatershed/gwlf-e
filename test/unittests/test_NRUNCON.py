import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.BMPs.AgAnimal import NRUNCON


class TestNRUNCON(VariableUnitTest):

    def test_NRUNCON(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            NRUNCON.NRUNCON_f(z.NYrs, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN, z.GRPctManApp,
                              z.PctGrazing, z.GRBarnNRate, z.Prec, z.DaysMonth, z.AWMSGrPct, z.GrAWMSCoeffN,
                              z.RunContPct,
                              z.RunConCoeffN, z.NGPctManApp, z.NGBarnNRate, z.AWMSNgPct, z.NgAWMSCoeffN, z.n41f,
                              z.n85l),
            NRUNCON.NRUNCON(z.NYrs, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN, z.GRPctManApp,
                            z.PctGrazing,
                            z.GRBarnNRate, z.Prec, z.DaysMonth, z.AWMSGrPct, z.GrAWMSCoeffN, z.RunContPct,
                            z.RunConCoeffN,
                            z.NGPctManApp, z.NGBarnNRate, z.AWMSNgPct, z.NgAWMSCoeffN, z.n41f, z.n85l), decimal=7)
