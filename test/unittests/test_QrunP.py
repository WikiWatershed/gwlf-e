import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import QrunP


class TestQrunP(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    # @skip("not ready")
    def test_QrunP(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            QrunP.QrunP_2(z.NYrs, z.DaysMonth, z.NRur, z.NUrb, z.Temp, z.InitSnow_0, z.Prec, z.CNP_0, z.AntMoist_0, z.Grow_0),
            QrunP.QrunP(z.NYrs, z.DaysMonth, z.NRur, z.NUrb, z.Temp, z.InitSnow_0, z.Prec, z.CNP_0, z.AntMoist_0, z.Grow_0), decimal=7)