import csv
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
        input_file = open('unittests/input_4.gms', 'r')
        z = Parser.GmsReader(input_file).read()


        output = StringIO()
        _,output_z = gwlfe.run(z)
        output_writer = Parser.GmsWriter(output)
        output_writer.write(output_z)
        variable_names = csv.reader(open('gms_variables.csv', 'r'), delimiter=",")

        ground_truth = csv.reader(open('input_4.gmsout', 'r'), delimiter=",")
        output.seek(0)
        output_parsed = csv.reader(output, delimiter=",")
        for i, row in enumerate(izip(ground_truth, output_parsed, variable_names)):
            for j, column in enumerate(izip(row[0],row[1], row[2])):
                ground_truth_val = column[0]
                output_val = column[1]
                variable_name = column[2]
                try:
                    try:
                        np.testing.assert_allclose(float(ground_truth_val), float(output_val), rtol=1e-07)
                    except ValueError:#catch all non float values
                        self.assertEqual(ground_truth_val,output_val)
                except AssertionError as e:
                    print("Error on line %i, column %i (%s)" % (i+1,j,variable_name))
                    raise e
