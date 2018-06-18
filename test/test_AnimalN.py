import unittest
from unittest import skip
import numpy as np
from gwlfe import Parser
from gwlfe.Outputs.AvAnimalNSum import AnimalN


class TestAnimalN(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_AnimalN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            AnimalN.AnimalN_f(z.NYrs, z.NGPctManApp, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN, z.NGAppNRate, z.Prec, z.DaysMonth,
              z.NGPctSoilIncRate, z.GRPctManApp, z.GRAppNRate, z.GRPctSoilIncRate, z.NGBarnNRate, z.AWMSNgPct, z.NgAWMSCoeffN,
              z.RunContPct, z.RunConCoeffN, z.PctGrazing, z.GRBarnNRate, z.AWMSGrPct, z.GrAWMSCoeffN, z.PctStreams, z.GrazingNRate),
            AnimalN.AnimalN(z.NYrs, z.NGPctManApp, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN, z.NGAppNRate, z.Prec, z.DaysMonth,
            z.NGPctSoilIncRate, z.GRPctManApp, z.GRAppNRate, z.GRPctSoilIncRate, z.NGBarnNRate, z.AWMSNgPct, z.NgAWMSCoeffN,
            z.RunContPct, z.RunConCoeffN, z.PctGrazing, z.GRBarnNRate, z.AWMSGrPct, z.GrAWMSCoeffN, z.PctStreams, z.GrazingNRate), decimal=7)