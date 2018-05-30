import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import StreamBankNSum


class TestStreamBankNSum(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    @skip("not ready")
    def test_StreamBankNSum(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            StreamBankNSum.StreamBankNSum_2(),
            StreamBankNSum.StreamBankNSum(), decimal=7)