import unittest
from unittest import skip
import numpy as np
from gwlfe import Parser
from gwlfe.AFOS.GrazingAnimals.Loads import InitGrN


class TestInitGrN(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    @skip("not ready")
    def test_InitGrN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            InitGrN.InitGrN_2(),
            InitGrN.InitGrN(), decimal=7)