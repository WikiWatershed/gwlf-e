import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import GroundWatLE_2


class TestGroundWatLE_2(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    def test_GroundWatLE_2_ground_truth(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            np.load("unittests/GroundWatLE_2.npy"),
            GroundWatLE_2.GroundWatLE_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
                  z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0, z.RecessionCoef, z.SeepCoef,
                  z.Landuse, z.TileDrainDensity), decimal=7)


    @skip('Not Ready Yet.')
    def test_GroundWatLE_2(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GroundWatLE_2.GroundWatLE_2_2(),
            GroundWatLE_2.GroundWatLE_2(), decimal=7)