import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.BMPs.AgAnimal import NAWMSP


class TestNAWMSP(VariableUnitTest):

    def test_NAWMSP(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            NAWMSP.NAWMSP_f(z.NYrs, z.NGPctManApp, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN,
                            z.NGBarnNRate,
                            z.Prec, z.DaysMonth, z.AWMSNgPct, z.NgAWMSCoeffN, z.RunContPct, z.RunConCoeffN, z.n41d,
                            z.n85j),
            NAWMSP.NAWMSP(z.NYrs, z.NGPctManApp, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN,
                          z.NGBarnNRate,
                          z.Prec, z.DaysMonth, z.AWMSNgPct, z.NgAWMSCoeffN, z.RunContPct, z.RunConCoeffN, z.n41d,
                          z.n85j), decimal=7)
