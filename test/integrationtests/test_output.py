# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json
import os
import unittest

import numpy as np

from gwlfe import gwlfe, Parser
from gwlfe.Memoization import resetMemoization


class TestOutput(unittest.TestCase):
    """
    Tests model generated output versus known
    static output.
    """
    __test__ = False

    @classmethod
    def setUpClass(self, input_file_name, output_file_name):
        self.basepath = os.path.abspath(os.path.join(__file__, '../'))
        
        inputfile = os.path.join(self.basepath,input_file_name)
        with open(inputfile, 'r') as input_file:
            self.z = Parser.GmsReader(input_file).read()
            self.generated_output, _ = gwlfe.run(self.z)    
        
        outputfile = os.path.join(self.basepath,output_file_name)
        with open(outputfile, 'r') as output_file:
            self.static_output = json.load(output_file)    

    def test_constants(self):
        constant_keys = ["MeanFlow", "MeanFlowPerSecond", "AreaTotal"]
        error = False
        for key in constant_keys:
            try:
                self.assertIn(key, self.generated_output)
                np.testing.assert_allclose(self.generated_output[key], self.static_output[key], rtol=1e-7,
                                           verbose=True)
            except AssertionError as e:
                print("AssertionError on %s" % (key))
                print(e)
                error = True
        if (error == True):
            raise AssertionError("Not all values within margin of error")

    def test_check_monthly(self):
        self.assertEqual(len(self.generated_output["monthly"]), len(self.static_output["monthly"]))
        error = False
        for i, month in enumerate(self.generated_output["monthly"]):
            self.assertCountEqual(self.generated_output["monthly"][i], self.static_output["monthly"][i])
            for (key, val) in month.items():
                try:
                    np.testing.assert_allclose(self.generated_output["monthly"][i][key],
                                               self.static_output["monthly"][i][key],
                                               rtol=1e-7,
                                               verbose=True)
                except AssertionError as e:
                    print("AssertionError on %s (month %i)" % (key, i))
                    print(e)
                    error = True
        if (error == True):
            raise AssertionError("Not all values within margin of error")

    def test_meta(self):
        error = False
        for key in self.static_output["meta"].keys():
            try:
                self.assertIn(key, self.generated_output["meta"])
                np.testing.assert_allclose(self.generated_output["meta"][key], self.static_output["meta"][key],
                                           rtol=1e-7,
                                           verbose=True)
            except AssertionError as e:
                print("AssertionError on %s" % (key))
                print(e)
                error = True
        if (error == True):
            raise AssertionError("Not all values within margin of error")

    def test_summary_loads(self):
        self.assertEqual(len(self.generated_output["SummaryLoads"]), len(self.static_output["SummaryLoads"]))
        error = False
        for i, month in enumerate(self.generated_output["SummaryLoads"]):
            self.assertCountEqual(self.generated_output["SummaryLoads"][i], self.static_output["SummaryLoads"][i])
            for (key, val) in month.items():
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
                    print(e)
                    error = True
        if (error == True):
            raise AssertionError("Not all values within margin of error")

    def test_loads(self):
        self.assertEqual(len(self.generated_output["Loads"]), len(self.static_output["Loads"]))
        error = False
        for i, month in enumerate(self.generated_output["Loads"]):
            self.assertCountEqual(self.generated_output["Loads"][i], self.static_output["Loads"][i])
            for (key, val) in month.items():
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
                    print(e)
                    error = True
        if (error == True):
            raise AssertionError("Not all values within margin of error")

    def tearDown(self):
        resetMemoization()
