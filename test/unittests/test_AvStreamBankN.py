# import unittest
# from unittest import skip
# from mock import patch
# import numpy as np
# from gwlfe import Parser
# from gwlfe import AvStreamBankN
#
#
# class TestAvStreamBankN(VariableUnitTest):
#     def setUp(self):
#         input_file = open('unittests/input_4.gms', 'r')
#         self.z = Parser.GmsReader(input_file).read()
#
#
#     @skip("not ready")
#     def test_AvStreamBankN(self):
#         z = self.z
#         np.testing.assert_array_almost_equal(
#             AvStreamBankN.AvStreamBankN_f(),
#             AvStreamBankN.AvStreamBankN(), decimal=7)
