import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe.enums import YesOrNo
from gwlfe import Parser
from gwlfe import GrazingAnimal
from VariableUnittest import VariableUnitTest

class TestGrazingAnimal(VariableUnitTest):
    def test_GrazingAnimal(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GrazingAnimal.GrazingAnimal_2(z.GrazingAnimal_0),
            GrazingAnimal.GrazingAnimal(z.GrazingAnimal_0)==YesOrNo.YES, decimal=7)
