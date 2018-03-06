import unittest
import numpy as np
from gwlfe import Parser
from gwlfe import GrazingAnimalWorksheet


class TestVariable(unittest.TestCase):
   def setUp(self):
       input_file = open('input_4.gms', 'r')
       self.z = Parser.GmsReader(input_file).read()

   def test_GrAppManN(self):
       z = self.z
       np.testing.assert_array_almost_equal(GrazingAnimalWorksheet.GrAppManN(z.GRPctManApp,z.InitGrN),
                                            GrazingAnimalWorksheet.GrAppManN_2(z.GRPctManApp, z.InitGrN), decimal=7)