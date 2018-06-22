import unittest
from unittest import skip
import numpy as np
from gwlfe import Parser
from gwlfe.AFOS.GrazingAnimals.Losses import GRLBN
from VariableUnittest import VariableUnitTest

class TestGRLBN(VariableUnitTest):
    @skip("not ready")
    def test_GRLBN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GRLBN.GRLBN_2(),
            GRLBN.GRLBN(), decimal=7)