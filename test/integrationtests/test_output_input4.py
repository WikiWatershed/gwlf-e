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
from ddt import ddt, data
from test_output import TestOutput
# from mock import patch
# from gwlfe.Memoization import memoize_with_args
# patch('gwlfe.Memoization.memoize', memoize_with_args).start()

from StringIO import StringIO

class input_4_TestOutput(TestOutput):
    """
    Tests model generated output versus known
    static output.
    """
    __test__ = True
    def setUp(self):
        super(input_4_TestOutput, self).setUp('input_4.gms','input_4_output.json')


