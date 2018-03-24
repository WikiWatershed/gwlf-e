import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import NAWMSL


class TestNAWMSL(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    @skip("test")
    def test_NAWMSL(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            NAWMSL.NAWMSL_2(),
            NAWMSL.NAWMSL(), decimal=7)