# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .test_output import TestOutput


class gms6_TestOutput(TestOutput):
    """
    Tests model generated output versus known
    static output.
    """
    __test__ = True

    @classmethod
    def setUpClass(self):
        super(gms6_TestOutput, self).setUpClass('GMS6.gms', 'GMS6_output.json')
