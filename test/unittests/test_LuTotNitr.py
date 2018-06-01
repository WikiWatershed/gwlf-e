import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import LuTotNitr


class TestLuTotNitr(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    @skip("not ready")
    def test_LuTotNitr(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            LuTotNitr.LuTotNitr_2(),
            LuTotNitr.LuTotNitr(), decimal=7)
