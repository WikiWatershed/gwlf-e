import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import PcntUrbanArea


class TestPcntUrbanArea(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_PcntUrbanArea(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            PcntUrbanArea.PcntUrbanArea_f(z.NRur, z.NUrb, z.Area),
            PcntUrbanArea.PcntUrbanArea(z.NRur, z.NUrb, z.Area), decimal=7)
