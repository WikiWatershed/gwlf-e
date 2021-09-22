import unittest
from unittest import skip

import numpy as np

from gwlfe import Parser
from gwlfe.Input.WaterBudget import AntMoist
from .VariableUnitTest import VariableUnitTest

class TestAntMoist(VariableUnitTest):
    @skip("not ready")
    def test_AntMoist(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            AntMoist.AntMoist_2(),
            AntMoist.AntMoist(), decimal=7)
