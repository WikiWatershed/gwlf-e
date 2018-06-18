import numpy as np

from VariableUnittest import VariableUnitTest
from gwlfe import Parser
from gwlfe.MultiUse_Fxns.Runoff import RurQRunoff


class TestRurQRunoff(VariableUnitTest):
    def setUp(self):
        input_file = open('integrationtests/test1.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_RurQRunoff(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            RurQRunoff.RurQRunoff_f(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.AntMoist_0, z.NRur, z.NUrb,
                                    z.CN, z.Grow_0),
            np.swapaxes(
                RurQRunoff.RurQRunoff(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.AntMoist_0, z.NRur, z.NUrb,
                                      z.CN, z.Grow_0), 1, 2)[:, :, :z.NRur], decimal=7)
