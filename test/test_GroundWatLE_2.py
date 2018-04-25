import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import GroundWatLE_2


class TestGroundWatLE_2(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    @skip('Not Ready Yet.')
    def test_GroundWatLE_2(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GroundWatLE_2.GroundWatLE_2_2(),
            GroundWatLE_2.GroundWatLE_2(), decimal=7)