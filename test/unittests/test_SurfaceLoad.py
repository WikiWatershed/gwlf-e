import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import SurfaceLoad


class TestSurfaceLoad(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_SurfaceLoad(self):
        z = self.z
        # for i,j in zip(np.ravel(temp1),np.ravel(temp2)):
        #     print(i,j,i==j)
        np.testing.assert_array_almost_equal(
            SurfaceLoad.SurfaceLoad_2(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.NUrb, z.Area,
                                      z.CNI_0,
                                      z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention,
                                      z.PctAreaInfil, z.Nqual, z.LoadRateImp, z.LoadRatePerv, z.Storm, z.UrbBMPRed),
            SurfaceLoad.SurfaceLoad(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                                    z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention,
                                    z.PctAreaInfil, z.Nqual, z.LoadRateImp, z.LoadRatePerv, z.Storm, z.UrbBMPRed)[:, :,
            :, z.NRur:],
            decimal=7)
