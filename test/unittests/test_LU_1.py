import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import LU_1


class TestLU_1(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    @skip("not ready")
    def test_LU_1(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            LU_1.LU_1_2(),
            LU_1.LU_1(), decimal=7)