import unittest

import numpy as np

from gwlfe import Parser
from gwlfe.Outputs.AvAnimalNSum import AvAnimalN


class TestAvAnimalN(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_AvAnimalN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            AvAnimalN.AvAnimalN_2(z.NYrs, z.NGPctManApp, z.Grazinganimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN,
                                  z.NGAppNRate, z.Prec, z.DaysMonth,
                                  z.NGPctSoilIncRate, z.GRPctManApp, z.GRAppNRate, z.GRPctSoilIncRate, z.NGBarnNRate,
                                  z.AWMSNgPct, z.NgAWMSCoeffN,
                                  z.RunContPct, z.RunConCoeffN, z.PctGrazing, z.GRBarnNRate, z.AWMSGrPct, z.GrAWMSCoeffN,
                                  z.PctStreams, z.GrazingNRate),
            AvAnimalN.AvAnimalN(z.NYrs, z.NGPctManApp, z.Grazinganimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN,
                                z.NGAppNRate, z.Prec, z.DaysMonth,
                                z.NGPctSoilIncRate, z.GRPctManApp, z.GRAppNRate, z.GRPctSoilIncRate, z.NGBarnNRate,
                                z.AWMSNgPct, z.NgAWMSCoeffN,
                                z.RunContPct, z.RunConCoeffN, z.PctGrazing, z.GRBarnNRate, z.AWMSGrPct, z.GrAWMSCoeffN,
                                z.PctStreams, z.GrazingNRate), decimal=7)
