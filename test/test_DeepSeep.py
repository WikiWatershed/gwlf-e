import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import DeepSeep


class TestDeepSeep(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    @skip('Not Ready Yet.')
    def test_DeepSeep(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            DeepSeep.DeepSeep_2(),
            DeepSeep.DeepSeep(), decimal=7)