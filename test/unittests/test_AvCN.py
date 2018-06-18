import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import AvCN


class TestAvCN(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    def test_AvCN(self):
        pass
        # z = self.z
        # np.testing.assert_array_almost_equal(
        #     AvCN.AvCN_f(z.NRur, z.NUrb, z.CNI_0, z.CNP_0, z.CN, z.Imper, z.Area),
        #     AvCN.AvCN(z.NRur, z.NUrb, z.CNI_0, z.CNP_0, z.CN, z.Imper, z.Area), decimal=7)