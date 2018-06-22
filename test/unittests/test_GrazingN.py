import unittest
from unittest import skip
import numpy as np
from gwlfe import Parser
from gwlfe.AFOS.GrazingAnimals.Loads import GrazingN
from VariableUnittest import VariableUnitTest

class TestGrazingN(VariableUnitTest):
    def test_GrazingN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GrazingN.GrazingN(z.PctGrazing, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN)[None,:],
            GrazingN.GrazingN_f(z.PctGrazing, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN),
            decimal=7)
