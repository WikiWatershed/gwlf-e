import unittest
from unittest import skip

import numpy as np

from gwlfe import Parser
from gwlfe.AFOS.nonGrazingAnimals.Losses import NGLostBarnN


class TestNGLostBarnN(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_NGLostBarnN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            NGLostBarnN.NGLostBarnN(z.NYrs, z.NGPctManApp, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt,
                                    z.AnimalDailyN, z.NGBarnNRate, z.Prec, z.DaysMonth, z.AWMSNgPct, z.NgAWMSCoeffN,
                                    z.RunContPct, z.RunConCoeffN),
            NGLostBarnN.NGLostBarnN_2(z.NYrs, z.NGPctManApp, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt,
                                      z.AnimalDailyN, z.NGBarnNRate, z.Prec, z.DaysMonth, z.AWMSNgPct, z.NgAWMSCoeffN,
                                      z.RunContPct, z.RunConCoeffN),
            decimal=7)

    def test_AvNGLostBarnN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            NGLostBarnN.AvNGLostBarnN_2(z.NYrs, z.NGPctManApp, z.GrazingAnimal, z.NumAnimals, z.AvgAnimalWt,
                                        z.AnimalDailyN, z.NGBarnNRate, z.Prec, z.DaysMonth, z.AWMSNgPct, z.NgAWMSCoeffN,
                                        z.RunContPct, z.RunConCoeffN),
            NGLostBarnN.AvNGLostBarnN(z.NYrs, z.NGPctManApp, z.GrazingAnimal, z.NumAnimals, z.AvgAnimalWt,
                                      z.AnimalDailyN, z.NGBarnNRate, z.Prec, z.DaysMonth, z.AWMSNgPct, z.NgAWMSCoeffN,
                                      z.RunContPct, z.RunConCoeffN), decimal=7)

    def test_AvNGLostBarnNSum(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            NGLostBarnN.AvNGLostBarnNSum_2(z.NYrs, z.NGPctManApp, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt,
                                           z.AnimalDailyN, z.NGBarnNRate, z.Prec, z.DaysMonth, z.AWMSNgPct,
                                           z.NgAWMSCoeffN, z.RunContPct, z.RunConCoeffN),
            NGLostBarnN.AvNGLostBarnNSum(z.NYrs, z.NGPctManApp, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt,
                                         z.AnimalDailyN, z.NGBarnNRate, z.Prec, z.DaysMonth, z.AWMSNgPct,
                                         z.NgAWMSCoeffN, z.RunContPct, z.RunConCoeffN), decimal=7)

    @skip("not ready")
    def test_NGLostBarnNSum(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            NGLostBarnN.NGLostBarnNSum_2(),
            NGLostBarnN.NGLostBarnNSum(), decimal=7)
