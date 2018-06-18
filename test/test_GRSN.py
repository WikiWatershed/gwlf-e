import unittest
from unittest import skip
import numpy as np
from gwlfe import Parser
from gwlfe.AFOS.GrazingAnimals.Losses import GRSN


class TestGRSN(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    @skip("not ready")
    def test_GRSN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GRSN.GRSN_f(),
            GRSN.GRSN(), decimal=7)
