import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import UrbAreaTotal


class TestUrbAreaTotal(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    # @skip("not ready")
    def test_UrbAreaTotal(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            UrbAreaTotal.UrbAreaTotal_2(z.NRur,z.NUrb,z.Area),
            UrbAreaTotal.UrbAreaTotal(z.NRur,z.NUrb,z.Area), decimal=7)