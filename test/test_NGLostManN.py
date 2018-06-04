import unittest

import numpy as np

from gwlfe import Parser
from gwlfe.AFOS.nonGrazingAnimals.Losses import NGLostManN


class TestNGLostManN(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_NGLostManN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            NGLostManN.NGLostManN(z.NYrs, z.NGPctManApp, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN,
                                  z.NGAppNRate, z.Prec, z.DaysMonth, z.NGPctSoilIncRate),
            NGLostManN.NGLostManN_2(z.NYrs, z.NGPctManApp, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt,
                                    z.AnimalDailyN, z.NGAppNRate, z.Prec, z.DaysMonth,
                                    z.NGPctSoilIncRate), decimal=7)
