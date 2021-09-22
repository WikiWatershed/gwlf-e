import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.AFOS.GrazingAnimals.Losses import GRLostManN


class TestGRLostManN(VariableUnitTest):

    def test_GRLostManN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GRLostManN.GRLostManN(z.NYrs, z.GRPctManApp, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN,
                                  z.GRAppNRate, z.Prec, z.DaysMonth, z.GRPctSoilIncRate),
            GRLostManN.GRLostManN_f(z.NYrs, z.GRPctManApp, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt,
                                    z.AnimalDailyN, z.GRAppNRate, z.Prec, z.DaysMonth, z.GRPctSoilIncRate), decimal=7)
