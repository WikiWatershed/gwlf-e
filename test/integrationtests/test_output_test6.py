# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from test_output import TestOutput


class test6_TestOutput(TestOutput):
    """
    Tests model generated output versus known
    static output.
    """
    __test__ = True

    def setUp(self):
        super(test6_TestOutput, self).setUp('test6.gms', 'test6_output.json')
