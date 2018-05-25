import unittest
from unittest import skip
import numpy as np
from gwlfe import Parser
from gwlfe import ET


class TestET(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    @skip("not ready")
    def test_DailyETPart1(self):
        z = self.z
        # np.testing.assert_array_almost_equal(ET.DailyET_2(z.Temp, z.KV, z.PcntET, z.DayHrs),
        #                                      ET.DailyET(z.NYrs, z.DaysMonth, z.Temp, z.DayHrs, z.KV, z.PcntET,
        #                                                 z.ETFlag), decimal=7)

    @skip("not ready")
    def test_AvEvapoTrans(self):
        z = self.z
        np.testing.assert_array_almost_equal(ET.AvEvapoTrans_2(z.Precipitation),
                                             ET.AvEvapoTrans(z.NYrs, z.Precipitation), decimal=7)
