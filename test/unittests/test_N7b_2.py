from unittest import skip

import numpy as np

from .VariableUnitTest import VariableUnitTest
from gwlfe.Output.AvAnimalNSum import N7b_2


class TestN7b_2(VariableUnitTest):
    def test_N7b_2_groundtruth(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            [39960.96326247645, 37071.76743004616, 33868.16593622824, 29561.315455296623, 25534.846999520218,
             21807.54439157898, 17796.283775647138, 13613.865844324624, 9482.969059018225, 6904.1067500478,
             4398.941229775999,
             1071.1450121011485, -1482.58458171158, -5405.017772409345, -9204.368759850697],
            N7b_2.N7b_2(z.NYrs, z.NGPctManApp, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN,
                        z.NGAppNRate, z.Prec, z.DaysMonth,
                        z.NGPctSoilIncRate, z.GRPctManApp, z.GRAppNRate, z.GRPctSoilIncRate, z.NGBarnNRate, z.AWMSNgPct,
                        z.NgAWMSCoeffN,
                        z.RunContPct, z.RunConCoeffN, z.PctGrazing, z.GRBarnNRate, z.AWMSGrPct, z.GrAWMSCoeffN,
                        z.PctStreams, z.GrazingNRate, z.n41b,
                        z.n85h, z.n41d, z.n85j, z.n41f, z.n85l, z.n42, z.n45, z.n69, z.n43, z.n64), decimal=7)

    @skip('Not Ready Yet.')
    def test_N7b_2(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            N7b_2.N7b_2_f(),
            N7b_2.N7b_2(), decimal=7)
