import unittest
from unittest import skip
import numpy as np
from gwlfe import Parser
from gwlfe.AFOS.nonGrazingAnimals.Loads import InitNgN
from VariableUnittest import VariableUnitTest

class TestInitNgN(VariableUnitTest):
    def test_InitNgN(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            InitNgN.InitNgN_f(z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN),
            InitNgN.InitNgN(z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN), decimal=7)