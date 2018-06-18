import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import Runoff


class TestRunoff(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    # @skip("not ready")
    def test_Runoff(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            Runoff.Runoff_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
           z.ISRR, z.ISRA, z.Qretention, z.PctAreaInfil, z.n25b, z.CN, z.Landuse, z.TileDrainDensity),
            Runoff.Runoff(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
           z.ISRR, z.ISRA, z.Qretention, z.PctAreaInfil, z.n25b, z.CN, z.Landuse, z.TileDrainDensity), decimal=7)