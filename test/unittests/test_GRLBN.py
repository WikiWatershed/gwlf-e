import unittest
from unittest import skip
import numpy as np
from gwlfe import Parser
from gwlfe.AFOS.GrazingAnimals.Losses import GRLBN


class TestGRLBN(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    @skip("not ready")
    def test_GRLBN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GRLBN.GRLBN_2(),
            GRLBN.GRLBN(), decimal=7)