import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import AvEvapoTrans


class TestAvEvapoTrans(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_AvEvapoTrans(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            AvEvapoTrans.AvEvapoTrans_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
                                        z.CNI_0, z.AntMoist_0, z.Grow, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN,
                                        z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap),
            AvEvapoTrans.AvEvapoTrans(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
                                        z.CNI_0, z.AntMoist_0, z.Grow, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN,
                                        z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap), decimal=7)
