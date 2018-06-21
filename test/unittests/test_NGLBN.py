import unittest
from unittest import skip
import numpy as np
from gwlfe import Parser
from gwlfe.AFOS.nonGrazingAnimals.Losses import NGLBN


class TestNGLBN(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    @skip("not ready")
    def test_NGLBN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            NGLBN.NGLBN_2(),
            NGLBN.NGLBN(), decimal=7)