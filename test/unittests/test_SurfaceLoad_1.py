import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import SurfaceLoad_1


class TestSurfaceLoad_1(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    @skip('Not Ready Yet.')
    def test_SurfaceLoad_1(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            SurfaceLoad_1.SurfaceLoad_1_2(),
            SurfaceLoad_1.SurfaceLoad_1(), decimal=7)