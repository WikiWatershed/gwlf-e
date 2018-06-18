# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

import sys
import importlib
import unittest
import json
import numpy as np
from unittest import skip
from mock import patch
import threading
from test_output import TestOutput

from StringIO import StringIO


class test3_TestOutput(TestOutput):
    """
    Tests model generated output versus known
    static output.
    """
    __test__ = True
    def setUp(self):
        super(test3_TestOutput, self).setUp('test3.gms','test3_output.json')