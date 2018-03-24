import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import AvAnimalN


class TestAvAnimalN(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    @skip("not ready yet")
    def test_AvAnimalN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            AvAnimalN.AvAnimalN_2(),
            AvAnimalN.AvAnimalN(), decimal=7)