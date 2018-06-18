import numpy as np

from VariableUnittest import VariableUnitTest
from gwlfe import PConc
from gwlfe import Parser


class TestPConc(VariableUnitTest):
    def setUp(self):
        input_file = open('integrationtests/test1.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_PConc(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            PConc.PConc_f(z.NRur, z.NUrb, z.PhosConc, z.ManPhos, z.ManuredAreas, z.FirstManureMonth, z.LastManureMonth,
                          z.FirstManureMonth2,
                          z.LastManureMonth2),
            PConc.PConc(z.NRur, z.NUrb, z.PhosConc, z.ManPhos, z.ManuredAreas, z.FirstManureMonth, z.LastManureMonth,
                        z.FirstManureMonth2,
                        z.LastManureMonth2), decimal=7)
