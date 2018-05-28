import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import Erosion_2


class TestErosion_2(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    @skip('Not Ready Yet.')
    def test_Erosion_2(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            Erosion_2.Erosion_2_2(),
            Erosion_2.Erosion_2(), decimal=7)