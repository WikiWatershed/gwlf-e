import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import RetentionEff


class TestRetentionEff(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    # @skip('Not Ready Yet.')
    def test_RetentionEff(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            RetentionEff.RetentionEff_2(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.Qretention, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.PctAreaInfil),
            RetentionEff.RetentionEff(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.Qretention, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.PctAreaInfil), decimal=7)