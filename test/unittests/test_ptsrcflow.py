import unittest
import numpy as np
from gwlfe import Parser
from gwlfe import PtSrcFlow


class TestPrecipitation(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_PtSrcFlow(self):
        z = self.z
        np.testing.assert_array_almost_equal(PtSrcFlow.PtSrcFlow_2(z.NYrs, z.PointFlow),
                                             PtSrcFlow.PtSrcFlow(z.NYrs, z.PointFlow), decimal=7)

    def test_AvPtSrcFlow(self):
        z = self.z
        z.PtSrcFlow = PtSrcFlow.PtSrcFlow_2(z.NYrs, z.PointFlow)
        np.testing.assert_array_almost_equal(PtSrcFlow.AvPtSrcFlow_2(z.PointFlow),
                                             PtSrcFlow.AvPtSrcFlow(z.NYrs, z.PtSrcFlow), decimal=7)
