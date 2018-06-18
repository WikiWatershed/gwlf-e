import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe.enums import YesOrNo
from gwlfe import Parser
from gwlfe import GrazingAnimal


class TestGrazingAnimal(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_GrazingAnimal(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GrazingAnimal.GrazingAnimal_f(z.GrazingAnimal_0),
            GrazingAnimal.GrazingAnimal(z.GrazingAnimal_0)==YesOrNo.YES, decimal=7)
