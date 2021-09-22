import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.AFOS.nonGrazingAnimals.Losses import NGLostManN


class TestNGLostManN(VariableUnitTest):

    def test_NGLostManN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            NGLostManN.NGLostManN(z.NYrs, z.NGPctManApp, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN,
                                  z.NGAppNRate, z.Prec, z.DaysMonth, z.NGPctSoilIncRate),
            NGLostManN.NGLostManN_f(z.NYrs, z.NGPctManApp, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt,
                                    z.AnimalDailyN, z.NGAppNRate, z.Prec, z.DaysMonth,
                                    z.NGPctSoilIncRate), decimal=7)
