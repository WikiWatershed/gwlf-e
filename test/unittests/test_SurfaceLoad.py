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


    @skip('Not Ready Yet.')
    def test_SurfaceLoad(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            SurfaceLoad.SurfaceLoad_2(),
            SurfaceLoad.SurfaceLoad(), decimal=7)