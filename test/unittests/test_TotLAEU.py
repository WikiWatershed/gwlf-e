import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import TotLAEU


class TestTotLAEU(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    def test_TotLAEU(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            TotLAEU.TotLAEU_f(z.NumAnimals, z.AvgAnimalWt),
            TotLAEU.TotLAEU(z.NumAnimals, z.AvgAnimalWt), decimal=7)