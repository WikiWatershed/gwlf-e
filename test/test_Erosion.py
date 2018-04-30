import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import Erosion


class TestErosion(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    @skip('Not Ready Yet.')
    def test_Erosion(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            Erosion.Erosion_2(),
            Erosion.Erosion(), decimal=7)