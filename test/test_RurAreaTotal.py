import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import RurAreaTotal


class TestRurAreaTotal(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()



    def test_RurAreaTotal(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            RurAreaTotal.RurAreaTotal_2(z.NRur, z.Area),
            RurAreaTotal.RurAreaTotal(z.NRur, z.Area), decimal=7)