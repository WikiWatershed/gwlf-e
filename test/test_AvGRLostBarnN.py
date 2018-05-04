import unittest
from unittest import skip
import numpy as np
from gwlfe import Parser
from gwlfe.AFOS.GrazingAnimals.Losses import AvGRLostBarnN


class TestAvGRLostBarnN(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    @skip('Not Ready Yet.')
    def test_AvGRLostBarnN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            AvGRLostBarnN.AvGRLostBarnN_2(),
            AvGRLostBarnN.AvGRLostBarnN(), decimal=7)