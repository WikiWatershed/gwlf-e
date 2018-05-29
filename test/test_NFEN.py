import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import NFEN


class TestNFEN(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    @skip("not ready")
    def test_NFEN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            NFEN.NFEN_2(),
            NFEN.NFEN(), decimal=7)