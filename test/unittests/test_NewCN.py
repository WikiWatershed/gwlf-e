import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import NewCN


class TestNewCN(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_NewCN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            NewCN.NewCN_2(z.NRur, z.NUrb, z.CN),
            NewCN.NewCN(z.NRur, z.NUrb, z.CN), decimal=7)
