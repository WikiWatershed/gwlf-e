import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import Grow
from gwlfe import enums


class TestGrow(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_Grow(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            Grow.Grow_f(z.Grow_0),
            Grow.Grow(z.Grow_0)==enums.GROWING_SEASON, decimal=7)
