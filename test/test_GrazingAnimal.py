import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import GrazingAnimal


class TestGrazingAnimal(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    @skip('Not Ready Yet.')
    def test_GrazingAnimal(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GrazingAnimal.GrazingAnimal_2(),
            GrazingAnimal.GrazingAnimal(), decimal=7)