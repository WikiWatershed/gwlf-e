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
from gwlfe import gwlfe,Parser




class TestOutput(unittest.TestCase):
    """
    Tests model generated output versus known
    static output.
    """
    __test__ = False
    def setUp(self, input_file_name, output_file_name):
        input_file = open('integrationtests/'+input_file_name, 'r')
        self.z = Parser.GmsReader(input_file).read()
        self.generated_output,_ = gwlfe.run(self.z)
        self.static_output = json.load(open('integrationtests/'+output_file_name, 'r'))

    def test_constants(self):
        constant_keys = ["MeanFlow", "MeanFlowPerSecond", "AreaTotal"]
        for key in constant_keys:
            try:
                self.assertIn(key, self.generated_output)
                np.testing.assert_allclose(self.generated_output[key], self.static_output[key], rtol=1e-7,
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
                    np.testing.assert_allclose(self.generated_output["monthly"][i][key],
                                                   self.static_output["monthly"][i][key],
                                                   rtol=1e-7,
                                                   verbose=True)
                except AssertionError as e:
                    print("AssertionError on %s (month %i)" % (key, i))
                    raise e

    def test_meta(self):
        for key in self.static_output["meta"].keys():
            try:
                self.assertIn(key, self.generated_output["meta"])
                np.testing.assert_allclose(self.generated_output["meta"][key], self.static_output["meta"][key],
                                               rtol=1e-7,
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
                    try:
                        np.testing.assert_allclose(self.generated_output["SummaryLoads"][i][key],
                                                       self.static_output["SummaryLoads"][i][key],
                                                       rtol=1e-7,
                                                       verbose=True)
                    except TypeError:
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
                    try:
                        np.testing.assert_allclose(self.generated_output["Loads"][i][key],
                                                       self.static_output["Loads"][i][key],
                                                       rtol=1e-7,
                                                       verbose=True)
                    except TypeError:
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
