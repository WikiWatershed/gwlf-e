import csv
import os
import unittest
from StringIO import StringIO
from itertools import izip

import numpy as np

from gwlfe import Parser
from gwlfe import gwlfe


class TestGMSWriter(unittest.TestCase):
    def test_gms_writer(self):
        """
        Test that GmsWriter is able to replicate the sample GMS created
        from MapShed.
        """
        input_file = open(os.path.abspath(os.path.join(__file__, '../', 'input_4.gms')), 'r')
        z = Parser.GmsReader(input_file).read()

        output = StringIO()
        _, output_z = gwlfe.run(z)
        output_writer = Parser.GmsWriter(output)
        output_writer.write(output_z)

        ground_truth = csv.reader(open(os.path.abspath(os.path.join(__file__, '../', 'input_4.gmsout')), 'r'), delimiter=",")
        output.seek(0)
        output_parsed = csv.reader(output, delimiter=",")
        error = False
        for i, row in enumerate(izip(ground_truth, output_parsed)):
            for j, column in enumerate(izip(row[0], row[1])):
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
