# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

import unittest
import json

from gwlfe import gwlfe, parser


class TestOutput(unittest.TestCase):
    """
    Tests model generated output versus known
    static output.
    """
    def test_generated_output_matches_static_output(self):
        """
        Test generated output using the sample GMS, input_4.gms
        versus static output generated using the same file.
        """
        input_file = open('test/input_4.gms', 'r')
        z = parser.GmsReader(input_file).read()
        generated_output = gwlfe.run(z)

        static_output = json.load(open('test/input_4.output', 'r'))

        self.assertEqual(generated_output, static_output)
