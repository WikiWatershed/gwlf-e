import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import AEU


class TestAEU(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    # @skip("Not Ready Yet.")
    def test_AEU(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            AEU.AEU_2(z.NumAnimals, z.AvgAnimalWt, z.NRur, z.NUrb, z.Area),
            AEU.AEU(z.NumAnimals, z.AvgAnimalWt, z.NRur, z.NUrb, z.Area), decimal=7)