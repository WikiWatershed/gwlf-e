import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import TotAEU


class TestTotAEU(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    # @skip("not ready")
    def test_TotAEU(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            TotAEU.TotAEU_2(z.NumAnimals, z.AvgAnimalWt),
            TotAEU.TotAEU(z.NumAnimals, z.AvgAnimalWt), decimal=7)