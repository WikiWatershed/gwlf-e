import numpy as np

from VariableUnittest import VariableUnitTest
from gwlfe.Input.LandUse.Urb import PcntUrbanArea


class TestPcntUrbanArea(VariableUnitTest):

    def test_PcntUrbanArea(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            PcntUrbanArea.PcntUrbanArea_f(z.NRur, z.NUrb, z.Area),
            PcntUrbanArea.PcntUrbanArea(z.NRur, z.NUrb, z.Area), decimal=7)
