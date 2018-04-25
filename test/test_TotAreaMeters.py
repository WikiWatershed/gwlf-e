import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import TotAreaMeters


class TestTotAreaMeters(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    @skip('Not Ready Yet.')
    def test_TotAreaMeters(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            TotAreaMeters.TotAreaMeters_2(),
            TotAreaMeters.TotAreaMeters(), decimal=7)