import csv
import os
import unittest
from StringIO import StringIO
from itertools import izip
import json

import numpy as np

from gwlfe import Parser
from gwlfe import gwlfe



class TestGMSWriter(unittest.TestCase):
    __test__ = False

    @classmethod
    def setUpClass(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
    #
    # def test_prez_gms_writer(self):
    #     mapshed_data = json.load(self.input_file)
    #     pre_z = Parser.DataModel(mapshed_data)
    #     output = StringIO()
    #     writer = Parser.GmsWriter(output)
    #     writer.write(pre_z)
    #
    #     output.seek(0)
    #
    #     print(output.readlines())

    def test_gms_writer(self):
        """
        Test that GmsWriter is able to replicate the sample GMS created
        from MapShed.
        """
        z = Parser.GmsReader(self.input_file).read()

        output = StringIO()
        _, output_z = gwlfe.run(z)
        output_writer = Parser.GmsWriter(output)
        output_writer.write(output_z)

        ground_truth = csv.reader(self.output_file, delimiter=",")
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
