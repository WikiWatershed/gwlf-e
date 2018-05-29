import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import StreamBankN


class TestStreamBankN(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    @skip("not ready")
    def test_StreamBankN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            StreamBankN.StreamBankN_2(),
            StreamBankN.StreamBankN(), decimal=7)