import unittest
from unittest import skip

import numpy as np

from gwlfe import Parser
from gwlfe.Input.WaterBudget import SatStorCarryOver


class TestSatStorCarryOver(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    @skip("not ready")
    def test_SatStorCarryOver(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            SatStorCarryOver.SatStorCarryOver_2(),
            SatStorCarryOver.SatStorCarryOver(), decimal=7)
