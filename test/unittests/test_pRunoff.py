import numpy as np

from VariableUnittest import VariableUnitTest
from gwlfe import Parser
from gwlfe import pRunoff


class TestpRunoff(VariableUnitTest):
    def setUp(self):
        input_file = open('integrationtests/test1.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_pRunoff(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            pRunoff.pRunoff_f(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.AntMoist_0, z.NRur, z.NUrb, z.CN,
                              z.Grow_0, z.Area, z.PhosConc, z.ManuredAreas, z.FirstManureMonth, z.LastManureMonth,
                              z.ManPhos, z.FirstManureMonth2, z.LastManureMonth2),
            pRunoff.pRunoff(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.AntMoist_0, z.NRur, z.NUrb, z.CN,
                            z.Grow_0, z.Area, z.PhosConc, z.ManuredAreas, z.FirstManureMonth, z.LastManureMonth,
                            z.ManPhos, z.FirstManureMonth2, z.LastManureMonth2), decimal=7)
