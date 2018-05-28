import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import MeltPest


class TestMeltPest(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    @skip("not ready")
    def test_MeltPest(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            MeltPest.MeltPest_2(),
            MeltPest.MeltPest(), decimal=7)