import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import Load


class TestLoad(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    @skip('Not Ready Yet.')
    def test_Load(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            Load.Load_2(),
            Load.Load(), decimal=7)