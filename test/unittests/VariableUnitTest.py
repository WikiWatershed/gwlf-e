import os
import unittest

from gwlfe import Parser


class VariableUnitTest(unittest.TestCase):
    def setUp(self):
        self.basepath = os.path.abspath(os.path.join(__file__, '../'))
        testgms = os.path.join(self.basepath, 'input_4.gms')
        input_file = open(testgms, 'r')
        self.z = Parser.GmsReader(input_file).read()
