import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import Melt_1


class TestMelt_1(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    @skip("not ready")
    def test_Melt_1(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            Melt_1.Melt_1_2(),
            Melt_1.Melt_1(), decimal=7)