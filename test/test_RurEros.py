import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import RurEros


class TestRurEros(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    @skip('Not Ready Yet.')
    def test_RurEros(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            RurEros.RurEros_2(),
            RurEros.RurEros(), decimal=7)