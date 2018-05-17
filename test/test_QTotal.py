import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import QTotal


class TestQTotal(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    # @skip("not ready")
    def test_QTotal(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            QTotal.QTotal(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0,
                            z.Grow, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN),
            QTotal.QTotal_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0,
                            z.Grow, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN), decimal=7)