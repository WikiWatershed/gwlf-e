import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import NSTAB


class TestNSTAB(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    @skip("not ready")
    def test_NSTAB(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            NSTAB.NSTAB_2(),
            NSTAB.NSTAB(), decimal=7)