import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import LU


class Testlu(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    # @skip("not ready")
    def test_lu(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            LU.lu_2(z.NRur, z.NUrb),
            LU.LU(z.NRur, z.NUrb), decimal=7)