import unittest
import numpy as np
from gwlfe import Parser
from gwlfe import GrazingAnimalWorksheet


class TestGrazingAnimalWorksheet(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

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
        np.testing.assert_array_almost_equal(GrazingAnimalWorksheet.GRAccManAppN(z.InitGrN, z.GRPctManApp, z.GrazingN),
                                             GrazingAnimalWorksheet.GRAccManAppN_2(), decimal=7)

    def test_GRInitBarnN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GrazingAnimalWorksheet.GRInitBarnN(z.GRAppManN, z.InitGrN, z.GRPctManApp, z.GrazingN),
            GrazingAnimalWorksheet.GRInitBarnN_2(), decimal=7)

    def test_LossFactAdj(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GrazingAnimalWorksheet.LossFactAdj(),
            GrazingAnimalWorksheet.LossFactAdj_2(), decimal=7)
