import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.MultiUse_Fxns.Erosion import SedAFactor


class TestSedAFactor(VariableUnitTest):
    def test_SedAFactor(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            SedAFactor.SedAFactor_f(z.NumAnimals, z.AvgAnimalWt, z.NRur, z.NUrb, z.CNI_0, z.CNP_0, z.CN, z.Imper,
                                    z.Area, z.SedAFactor_0, z.AvKF, z.AvSlope, z.SedAAdjust),
            SedAFactor.SedAFactor(z.NumAnimals, z.AvgAnimalWt, z.NRur, z.NUrb, z.CNI_0, z.CNP_0, z.CN, z.Imper, z.Area,
                                  z.SedAFactor_0, z.AvKF, z.AvSlope, z.SedAAdjust), decimal=7)
        pass
