import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import QrunI


class TestQRunI(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    # @skip("not ready")
    def test_QRunI(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            QrunI.QrunI_2(z.NYrs, z.DaysMonth, z.NRur, z.NUrb, z.Temp, z.InitSnow_0, z.Prec, z.CNI_0, z.AntMoist_0, z.Grow),
            QrunI.QrunI(z.NYrs, z.DaysMonth, z.NRur, z.NUrb, z.Temp, z.InitSnow_0, z.Prec, z.CNI_0, z.AntMoist_0, z.Grow), decimal=7)