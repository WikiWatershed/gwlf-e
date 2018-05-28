import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import StreamBankEros_2


class TestStreamBankEros_2(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    @skip('Not Ready Yet.')
    def test_StreamBankEros_2(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            StreamBankEros_2.StreamBankEros_2_2(),
            StreamBankEros_2.StreamBankEros_2(), decimal=7)