import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import AvCNUrb


class TestAvCNUrb(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    def test_AvCNUrb(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            AvCNUrb.AvCNUrb_2(z.NRur, z.NUrb, z.CNI_0, z.CNP_0, z.Imper, z.Area),
            AvCNUrb.AvCNUrb(z.NRur, z.NUrb, z.CNI_0, z.CNP_0, z.Imper, z.Area), decimal=7)