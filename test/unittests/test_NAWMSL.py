import unittest
from unittest import skip
import numpy as np
from gwlfe import Parser
from gwlfe.BMPs.AgAnimal import NAWMSL


class TestNAWMSL(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_NAWMSL(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            NAWMSL.NAWMSL_2(z.NYrs, z.GrazingAnimal, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN, z.GRPctManApp, z.PctGrazing, z.GRBarnNRate,
           z.Prec, z.DaysMonth, z.AWMSGrPct, z.GrAWMSCoeffN, z.RunContPct, z.RunConCoeffN, z.n41b, z.n85h),
            NAWMSL.NAWMSL(z.NYrs, z.GrazingAnimal, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN, z.GRPctManApp, z.PctGrazing, z.GRBarnNRate,
           z.Prec, z.DaysMonth, z.AWMSGrPct, z.GrAWMSCoeffN, z.RunContPct, z.RunConCoeffN, z.n41b, z.n85h), decimal=7)