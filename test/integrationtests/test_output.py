# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

from types import ModuleType
import sys
import importlib
import unittest
import json
import numpy as np
from unittest import skip
from mock import patch
# from gwlfe.Memoization import memoize_with_args
# patch('gwlfe.Memoization.memoize.memodict.__call__', lambda x:x).start()
from gwlfe import gwlfe,Parser
# from mock import patch

# patch('gwlfe.Memoization.memoize', memoize_with_args).start()

from StringIO import StringIO


class TestOutput(unittest.TestCase):
    """
    Tests model generated output versus known
    static output.
    """
    __test__ = False
    def setUp(self, input_file_name, output_file_name):
        input_file = open('integrationtests/'+input_file_name, 'r')
        self.z = Parser.GmsReader(input_file).read()
        self.generated_output = gwlfe.run(self.z)
        self.static_output = json.load(open('integrationtests/'+output_file_name, 'r'))

    def test_constants(self):
        constant_keys = ["MeanFlow", "MeanFlowPerSecond", "AreaTotal"]
        for key in constant_keys:
            try:
                self.assertIn(key, self.generated_output)
                np.testing.assert_almost_equal(self.generated_output[key], self.static_output[key], decimal=7,
                                               verbose=True)
            except AssertionError as e:
                print("AssertionError on %s" % (key))
                raise e

    def test_check_monthly(self):
        self.assertEqual(len(self.generated_output["monthly"]), len(self.static_output["monthly"]))
        for i, month in enumerate(self.generated_output["monthly"]):
            self.assertItemsEqual(self.generated_output["monthly"][i], self.static_output["monthly"][i])
            for (key, val) in month.iteritems():
                try:
                    np.testing.assert_almost_equal(self.generated_output["monthly"][i][key],
                                                   self.static_output["monthly"][i][key],
                                                   decimal=7,
                                                   verbose=True)
                except AssertionError as e:
                    print("AssertionError on %s (month %i)" % (key, i))
                    raise e

    def test_meta(self):
        for key in self.static_output["meta"].keys():
            try:
                self.assertIn(key, self.generated_output["meta"])
                np.testing.assert_almost_equal(self.generated_output["meta"][key], self.static_output["meta"][key],
                                               decimal=7,
                                               verbose=True)
            except AssertionError as e:
                print("AssertionError on %s" % (key))
                raise e

    def test_summary_loads(self):
        self.assertEqual(len(self.generated_output["SummaryLoads"]), len(self.static_output["SummaryLoads"]))
        for i, month in enumerate(self.generated_output["SummaryLoads"]):
            self.assertItemsEqual(self.generated_output["SummaryLoads"][i], self.static_output["SummaryLoads"][i])
            for (key, val) in month.iteritems():
                try:
                    if (type(key) == float):
                        np.testing.assert_almost_equal(self.generated_output["SummaryLoads"][i][key],
                                                       self.static_output["SummaryLoads"][i][key],
                                                       decimal=7, err_msg='',
                                                       verbose=True)
                    else:
                        self.assertEqual(self.generated_output["SummaryLoads"][i][key],
                                         self.static_output["SummaryLoads"][i][key])
                except Exception as e:
                    print("AssertionError on %s (%s)" % (key, self.generated_output["SummaryLoads"][i]["Source"]))
                    raise e

    def test_loads(self):
        self.assertEqual(len(self.generated_output["Loads"]), len(self.static_output["Loads"]))
        for i, month in enumerate(self.generated_output["Loads"]):
            self.assertItemsEqual(self.generated_output["Loads"][i], self.static_output["Loads"][i])
            for (key, val) in month.iteritems():
                try:
                    if (type(key) == float):
                        np.testing.assert_almost_equal(self.generated_output["Loads"][i][key],
                                                       self.static_output["Loads"][i][key],
                                                       decimal=7, err_msg='',
                                                       verbose=True)
                    else:
                        self.assertEqual(self.generated_output["Loads"][i][key], self.static_output["Loads"][i][key])
                except AssertionError as e:
                    print("AssertionError on %s (%s)" % (key, self.static_output["Loads"][i]["Source"]))
                    raise e

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
    @skip("we broke it")
    def test_gms_writer(self):
        """
        Test that GmsWriter is able to replicate the sample GMS created
        from MapShed.
        """
        input_file = open('unittests/input_4.gms', 'r')
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

    # def tearDown(self):
    # if globals().has_key('init_modules'):
    #     for m in [x for x in sys.modules.keys() if x not in init_modules]:
    #         del (sys.modules[m])
    # else:
    #     init_modules = sys.modules.keys()
    # def tearDown(self):
    #     patch('gwlfe.Memoization.memoize', lambda x: x).stop()
