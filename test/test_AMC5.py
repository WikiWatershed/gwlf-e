import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import AMC5


class TestAMC5(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    @skip("not ready")
    def test_AMC5(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            AMC5.AMC5_2(),
            AMC5.AMC5(), decimal=7)