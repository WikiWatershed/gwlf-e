# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .test_output import TestOutput


class test10_TestOutput(TestOutput):
    """
    Tests model generated output versus known
    static output.
    """
    __test__ = True

    @classmethod
    def setUpClass(self):
        super(test10_TestOutput, self).setUpClass('test10.gms', 'test10_output.json')
