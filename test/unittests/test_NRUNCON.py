import unittest
from unittest import skip
import numpy as np
from gwlfe import Parser
from gwlfe.BMPs.AgAnimal import NRUNCON


class TestNRUNCON(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_NRUNCON(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            NRUNCON.NRUNCON_2(z.NYrs, z.GrazingAnimal, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN, z.GRPctManApp, z.PctGrazing, z.GRBarnNRate,
              z.Prec, z.DaysMonth, z.AWMSGrPct, z.GrAWMSCoeffN, z.RunContPct, z.RunConCoeffN, z.NGPctManApp, z.NGBarnNRate, z.AWMSNgPct,
              z.NgAWMSCoeffN, z.n41f, z.n85l),
            NRUNCON.NRUNCON(z.NYrs, z.GrazingAnimal, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN, z.GRPctManApp, z.PctGrazing, z.GRBarnNRate,
              z.Prec, z.DaysMonth, z.AWMSGrPct, z.GrAWMSCoeffN, z.RunContPct, z.RunConCoeffN, z.NGPctManApp, z.NGBarnNRate, z.AWMSNgPct,
              z.NgAWMSCoeffN, z.n41f, z.n85l), decimal=7)