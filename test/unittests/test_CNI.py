import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import CNI


class TestCNI(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    @skip("not ready")
    def test_CNI(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            CNI.CNI_2(z.NRur, z.NUrb, z.CNI_0),
            CNI.CNI(z.NRur, z.NUrb, z.CNI_0), decimal=7)