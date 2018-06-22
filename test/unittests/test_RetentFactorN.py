import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import RetentFactorN
from VariableUnittest import VariableUnitTest

class TestRetentFactorN(VariableUnitTest):
    pass
    # @skip("not ready")
    # def test_RetentFactorN(self):
    #     z = self.z
    #     np.testing.assert_array_almost_equal(
    #         RetentFactorN.RetentFactorN_2(),
    #         RetentFactorN.RetentFactorN(), decimal=7)
