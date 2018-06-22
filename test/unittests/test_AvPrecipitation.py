import unittest
from unittest import skip
import numpy as np
from gwlfe import Parser
from gwlfe.Input.WaterBudget import AvPrecipitation
from VariableUnittest import VariableUnitTest

class TestAvPrecipitation(VariableUnitTest):
    @skip("test")
    def test_AvPrecipitation(self):
        z = self.z
        np.testing.assert_array_almost_equal(AvPrecipitation.AvPrecipitation_2(z.Prec),
                                             AvPrecipitation.AvPrecipitation(z.NYrs, z.Prec), decimal=7)
