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
from ddt import ddt, data
from mock import patch
import threading
from test_output import TestOutput

from StringIO import StringIO


class gms9_TestOutput(TestOutput):
    """
    Tests model generated output versus known
    static output.
    """
    __test__ = True
    def setUp(self):
        super(gms9_TestOutput, self).setUp('GMS9.gms','GMS9_output.json')