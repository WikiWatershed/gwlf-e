# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

import importlib

import sys
import unittest
import json
import numpy as np
from unittest import skip
from types import ModuleType
from mock import patch
from test_output import TestOutput

from StringIO import StringIO


class elm_fork_TestOutput(TestOutput):
    """
    Tests model generated output versus known
    static output.
    """
    __test__ = True
    def setUp(self):
        super(elm_fork_TestOutput, self).setUp('underflow_exception_elm_fork_red.gms','underflow_exception_elm_fork_red_output.json')