import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import ErosWashoff


class TestErosWashoff(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    @skip('Not Ready Yet.')
    def test_ErosWashoff(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            ErosWashoff.ErosWashoff_2(),
            ErosWashoff.ErosWashoff(), decimal=7)