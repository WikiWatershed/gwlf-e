import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import ErosionSedYield


class TestErosionSedYield(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    @skip('Not Ready Yet.')
    def test_ErosionSedYield(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            ErosionSedYield.ErosionSedYield_2(),
            ErosionSedYield.ErosionSedYield(), decimal=7)