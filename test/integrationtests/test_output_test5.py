# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from test_output import TestOutput


class test5_TestOutput(TestOutput):
    """
    Tests model generated output versus known
    static output.
    """
    __test__ = True

    def setUp(self):
        super(test5_TestOutput, self).setUp('test5.gms', 'test5_output.json')
