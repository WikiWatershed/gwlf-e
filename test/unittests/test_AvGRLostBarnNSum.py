import unittest

import numpy as np

from gwlfe import Parser
from gwlfe.AFOS.GrazingAnimals.Losses import AvGRLostBarnNSum


class TestAvGRLostBarnNSum(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_AvGRLostBarnNSum(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            AvGRLostBarnNSum.AvGRLostBarnNSum_2(z.NYrs, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN,
                                                z.GRPctManApp, z.PctGrazing, z.GRBarnNRate,
                                                z.Prec, z.DaysMonth, z.AWMSGrPct, z.GrAWMSCoeffN, z.RunContPct, z.RunConCoeffN),
            AvGRLostBarnNSum.AvGRLostBarnNSum(z.NYrs, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN, z.GRPctManApp,
                                              z.PctGrazing, z.GRBarnNRate,
                                              z.Prec, z.DaysMonth, z.AWMSGrPct, z.GrAWMSCoeffN, z.RunContPct, z.RunConCoeffN),
            decimal=7)
