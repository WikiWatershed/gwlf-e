import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import SedAFactor


class TestSedAFactor(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_SedAFactor(self):
        pass
        # z = self.z
        # np.testing.assert_array_almost_equal(
        #     SedAFactor.SedAFactor_f(z.NumAnimals, z.AvgAnimalWt, z.NRur, z.NUrb, z.CNI_0, z.CNP_0, z.CN, z.Imper,
        #                             z.Area, z.SedAFactor_0, z.AvKF, z.AvSlope, z.SedAAdjust),
        #     SedAFactor.SedAFactor(z.NumAnimals, z.AvgAnimalWt, z.NRur, z.NUrb, z.CNI_0, z.CNP_0, z.CN, z.Imper,
        #                             z.Area, z.SedAFactor_0, z.AvKF, z.AvSlope, z.SedAAdjust), decimal=7)
