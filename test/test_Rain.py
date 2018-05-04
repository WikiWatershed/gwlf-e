import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import Rain


class TestRain(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    # @skip("not ready")
    def test_Rain(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            Rain.Rain_2(z.Temp, z.Prec),
            Rain.Rain(z.NYrs, z.DaysMonth, z.Temp, z.Prec), decimal=7)