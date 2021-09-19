import csv
import os
import unittest
from io import StringIO
import json

import numpy as np

from gwlfe import Parser
from gwlfe import gwlfe



class TestGMSOutput(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.input_file = open(os.path.abspath(os.path.join(__file__, '../', 'input_4.gms')), 'r')
        self.output_file = open(os.path.abspath(os.path.join(__file__, '../', 'input_4.gmsout')), 'r')

    def test_gms_output(self):
        """
        Test that GmsWriter is able to replicate the sample GMS created
        from MapShed.
        """
        z = Parser.GmsReader(self.input_file).read()

        output = StringIO()
        _, output_z = gwlfe.run(z)
        output_writer = Parser.GmsWriter(output)
        output_writer.writeOutput(output_z)

        ground_truth = csv.reader(self.output_file, delimiter=",")
        output.seek(0)
        output_parsed = csv.reader(output, delimiter=",")
        error = False
        for i, row in enumerate(zip(ground_truth, output_parsed)):
            for j, column in enumerate(zip(row[0], row[1])):
                ground_truth_val = column[0]
                output_val = column[1]
                try:
                    try:
                        np.testing.assert_allclose(float(ground_truth_val), float(output_val), rtol=1e-07)
                    except ValueError:  # catch all non float values
                        self.assertEqual(ground_truth_val, output_val)
                except AssertionError as e:
                    print("Error on line %i, column %i" % (i + 1, j))
                    print(e)
                    error = True
        if (error == True):
            raise AssertionError("Not all variables within margin of error")
