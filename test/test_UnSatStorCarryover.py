import unittest
from unittest import skip
import numpy as np
from gwlfe import Parser
from gwlfe.Input.WaterBudget import UnSatStorCarryover


class TestUnSatStorCarryover(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    @skip("not ready")
    def test_UnSatStorCarryover(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            UnSatStorCarryover.UnSatStorCarryover_2(),
            UnSatStorCarryover.UnSatStorCarryover(), decimal=7)