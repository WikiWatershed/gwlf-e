import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import StreamBankN_1


class TestStreamBankN_1(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    @skip("not ready")
    def test_StreamBankN_1(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            StreamBankN_1.StreamBankN_1_2(),
            StreamBankN_1.StreamBankN_1(), decimal=7)