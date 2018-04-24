import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import ET_2


class TestET_2(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    @skip('Not Ready Yet.')
    def test_ET_2(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            ET_2.ET_2_2(),
            ET_2.ET_2(), decimal=7)