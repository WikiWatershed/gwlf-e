# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

import unittest
import json
import numpy as np

from StringIO import StringIO

from gwlfe import gwlfe, Parser


class TestOutput(unittest.TestCase):
    """
    Tests model generated output versus known
    static output.
    """

    def test_constants(self):
        constant_keys = ["MeanFlow", "MeanFlowPerSecond", "AreaTotal"]
        input_file = open('input_4.gms', 'r')
        z = Parser.GmsReader(input_file).read()
        generated_output = gwlfe.run(z)

        static_output = json.load(open('input_4.output', 'r'))

        for key in constant_keys:
            self.assertIn(key, generated_output)
            np.testing.assert_almost_equal(generated_output[key], static_output[key], decimal=7, err_msg='',
                                           verbose=True)

    def test_check_monthly(self):
        input_file = open('input_4.gms', 'r')
        z = Parser.GmsReader(input_file).read()
        generated_output = gwlfe.run(z)

        static_output = json.load(open('input_4.output', 'r'))
        self.assertEqual(len(generated_output["monthly"]), len(static_output["monthly"]))
        for i, month in enumerate(generated_output["monthly"]):
            self.assertItemsEqual(generated_output["monthly"][i], static_output["monthly"][i])
            for (key, val) in month.iteritems():
                np.testing.assert_almost_equal(generated_output["monthly"][i][key], static_output["monthly"][i][key],
                                               decimal=7, err_msg='',
                                               verbose=True)

    def test_meta(self):
        input_file = open('input_4.gms', 'r')
        z = Parser.GmsReader(input_file).read()
        generated_output = gwlfe.run(z)

        static_output = json.load(open('input_4.output', 'r'))

        for key in static_output["meta"].keys():
            self.assertIn(key, generated_output["meta"])
            np.testing.assert_almost_equal(generated_output["meta"][key], static_output["meta"][key], decimal=7,
                                           err_msg='',
                                           verbose=True)

    def test_summary_loads(self):
        input_file = open('input_4.gms', 'r')
        z = Parser.GmsReader(input_file).read()
        generated_output = gwlfe.run(z)

        static_output = json.load(open('input_4.output', 'r'))
        self.assertEqual(len(generated_output["SummaryLoads"]), len(static_output["SummaryLoads"]))
        for i, month in enumerate(generated_output["SummaryLoads"]):
            self.assertItemsEqual(generated_output["SummaryLoads"][i], static_output["SummaryLoads"][i])
            for (key, val) in month.iteritems():
                if (type(key) == float):
                    np.testing.assert_almost_equal(generated_output["SummaryLoads"][i][key],
                                                   static_output["SummaryLoads"][i][key],
                                                   decimal=7, err_msg='',
                                                   verbose=True)
                else:
                    self.assertEqual(generated_output["SummaryLoads"][i][key], static_output["SummaryLoads"][i][key])

    def test_loads(self):
        input_file = open('input_4.gms', 'r')
        z = Parser.GmsReader(input_file).read()
        generated_output = gwlfe.run(z)

        static_output = json.load(open('input_4.output', 'r'))
        self.assertEqual(len(generated_output["Loads"]), len(static_output["Loads"]))
        for i, month in enumerate(generated_output["Loads"]):
            self.assertItemsEqual(generated_output["Loads"][i], static_output["Loads"][i])
            for (key, val) in month.iteritems():
                if (type(key) == float):
                    np.testing.assert_almost_equal(generated_output["Loads"][i][key],
                                                   static_output["Loads"][i][key],
                                                   decimal=7, err_msg='',
                                                   verbose=True)
                else:
                    self.assertEqual(generated_output["Loads"][i][key], static_output["Loads"][i][key])

    # def test_generated_output_matches_static_output(self):
    #     """
    #     Test generated output using the sample GMS, input_4.gms
    #     versus static output generated using the same file.
    #     """
    #     input_file = open('input_4.gms', 'r')
    #     z = parser.GmsReader(input_file).read()
    #     generated_output = gwlfe.run(z)
    #
    #     static_output = json.load(open('input_4.output', 'r'))
    #
    #     self.assertEqual(generated_output, static_output)

    def test_gms_writer(self):
        """
        Test that GmsWriter is able to replicate the sample GMS created
        from MapShed.
        """
        input_file = open('input_4.gms', 'r')
        z = Parser.GmsReader(input_file).read()

        output = StringIO()
        writer = Parser.GmsWriter(output)
        writer.write(z)

        input_file.seek(0)
        output.seek(0)

        self.assertGmsEqual(input_file, output)

    def assertGmsEqual(self, gms1, gms2):
        """
        Assert that 2 GMS files match.
        """
        left = Parser.iterate_csv_values(gms1)
        right = Parser.iterate_csv_values(gms2)

        done = False

        while not done:
            try:
                a, y1, x1 = left.next()
            except StopIteration:
                done = True

            try:
                b, y2, x2 = right.next()
            except StopIteration:
                if done:
                    # The first file must have ended.
                    continue
                else:
                    self.fail('GMS files did not end at the same time')

            if done:
                # The first file must have ended, but the second file didn't.
                self.fail('GMS files did not end at the same time')

            self.assertEqual(y1, y2)
            self.assertEqual(x1, x2)
            self.assertEqualFuzzy(a, b)

    def assertEqualFuzzy(self, a, b):
        """
        Assert that 2 values match. The purpose of doing a fuzzy comparison
        is to ignore slight formatting differences between VB and Python.
        """
        # Test that floats like ".06" match "0.06".
        try:
            f1 = float(a)
            f2 = float(b)
            self.assertEqual(f1, f2)
            return
        except ValueError:
            pass
        self.assertEqual(a, b)
