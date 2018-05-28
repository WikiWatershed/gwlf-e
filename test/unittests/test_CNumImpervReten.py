import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import CNumImpervReten


class TestCNumImpervReten(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    @skip("not ready")
    def test_CNumImpervReten(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            CNumImpervReten.CNumImpervReten_2(z.NYrs, z.DaysMonth, z.Temp, z.Prec, z.InitSnow_0, z.AntMoist_0, z.NRur, z.NUrb, z.CNI_0, z.Grow_0),
            CNumImpervReten.CNumImpervReten(z.NYrs, z.DaysMonth, z.Temp, z.Prec, z.InitSnow_0, z.AntMoist_0, z.NRur, z.NUrb, z.CNI_0, z.Grow_0), decimal=7)