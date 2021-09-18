from unittest import skip

import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.AFOS.GrazingAnimals.Losses import GRLBN_2


class TestGRLBN_2(VariableUnitTest):
    @skip('Not Ready Yet.')
    def test_GRLBN_2(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            GRLBN_2.GRLBN_2_f(),
            GRLBN_2.GRLBN_2(), decimal=7)
