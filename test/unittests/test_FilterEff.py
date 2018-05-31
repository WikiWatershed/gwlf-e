import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import FilterEff


class TestFilterEff(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    def test_FilterEff(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            FilterEff.FilterEff_2(z.FilterWidth),
            FilterEff.FilterEff(z.FilterWidth), decimal=7)