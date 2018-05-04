import unittest
from unittest import skip
import numpy as np
from gwlfe import Parser
from gwlfe.AFOS.nonGrazingAnimals.Loads import NGAppManN


class TestNGAppManN(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    @skip("not ready yet")
    def test_NGAppManN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            NGAppManN.NGAppManN_2(),
            NGAppManN.NGAppManN(), decimal=7)
