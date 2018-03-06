import unittest
import numpy as np
from numpy import array
import json
from gwlfe import Parser
from gwlfe import GrazingAnimalWorksheet
import os


class TestGrazingAnimalWorksheet(unittest.TestCase):
    def setUp(self):
        print(os.path.dirname(os.path.realpath(__file__)))
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

        # use these variables in tests that depend on them so that their tests do not depend on the results of other functions
        self.mock_LossFactAdj = np.load("LossFactAdj.npy")
        self.mock_GRAppManN = np.load("GRAppManN.npy")
        self.mock_GrazingN = np.load("GrazingN.npy")
        self.mock_GRInitBarnN = np.load("GRInitBarnN.npy")

    def test_GrAppManN(self):
        z = self.z
        np.testing.assert_array_almost_equal(GrazingAnimalWorksheet.GRAppManN(z.GRPctManApp, z.InitGrN),
                                             GrazingAnimalWorksheet.GRAppManN_2(), decimal=7)

    def test_GrazingN(self):
        z = self.z
        np.testing.assert_array_almost_equal(GrazingAnimalWorksheet.GrazingN(z.PctGrazing, z.InitGrN),
                                             GrazingAnimalWorksheet.GrazingN_2(), decimal=7)

    def test_GRAccManAppN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GrazingAnimalWorksheet.GRAccManAppN(z.InitGrN, z.GRPctManApp, self.mock_GrazingN),
            GrazingAnimalWorksheet.GRAccManAppN_2(), decimal=7)

    def test_GRInitBarnN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GrazingAnimalWorksheet.GRInitBarnN(self.mock_GRAppManN, z.InitGrN, z.GRPctManApp, self.mock_GrazingN),
            GrazingAnimalWorksheet.GRInitBarnN_2(), decimal=7)

    def test_LossFactAdj(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GrazingAnimalWorksheet.LossFactAdj(z.NYrs, z.Precipitation, z.DaysMonth),
            GrazingAnimalWorksheet.LossFactAdj_2(), decimal=7)

    def test_NGLostBarnN(self):
        z = self.z
        mock_LossFactAdj = 10
        np.testing.assert_array_almost_equal(
            GrazingAnimalWorksheet.NGLostBarnN(z.NYrs, z.NGInitBarnN, z.NGBarnNRate, self.mock_LossFactAdj, z.AWMSNgPct,
                                               z.NgAWMSCoeffN, z.RunContPct, z.RunConCoeffN),
            GrazingAnimalWorksheet.NGLostBarnN_2(), decimal=7)

    def test_NGLostManN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GrazingAnimalWorksheet.NGLostManN(z.NYrs, z.NGAppManN, z.NGAppNRate, self.mock_LossFactAdj,
                                              z.NGPctSoilIncRate),
            GrazingAnimalWorksheet.NGLostManN_2(), decimal=7)

    def test_GRLostManN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GrazingAnimalWorksheet.GRLostManN(z.NYrs, self.mock_GRAppManN, z.GRAppNRate, self.mock_LossFactAdj,
                                              z.GRPctSoilIncRate),
            GrazingAnimalWorksheet.GRLostManN_2(), decimal=7)

    def test_GRLostBarnN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GrazingAnimalWorksheet.GRLostBarnN(z.NYrs, self.mock_GRInitBarnN, z.GRBarnNRate, self.mock_LossFactAdj,
                                               z.AWMSNgPct,
                                               z.GrAWMSCoeffN, z.RunContPct, z.RunConCoeffN),
            GrazingAnimalWorksheet.GRLostBarnN_2(), decimal=7)

    def test_GRLossN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GrazingAnimalWorksheet.GRLossN(z.NYrs, self.mock_GrazingN, z.GRStreamN, z.GrazingNRate,
                                           self.mock_LossFactAdj),
            GrazingAnimalWorksheet.GRLossN_2(), decimal=7)
