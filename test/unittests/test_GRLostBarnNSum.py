import unittest
from unittest import skip
import numpy as np
from gwlfe import Parser
from gwlfe.AFOS.GrazingAnimals.Losses import GRLostBarnNSum
from VariableUnittest import VariableUnitTest

class TestGRLostBarnNSum(VariableUnitTest):
    def test_GRLostBarnNSum(self):
        pass
        # z = self.z
        # np.testing.assert_array_almost_equal(
        #     GRLostBarnNSum.GRLostBarnNSum_2(),
        #     GRLostBarnNSum.GRLostBarnNSum(), decimal=7)