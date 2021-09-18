# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .test_output import TestOutput


class gms9_TestOutput(TestOutput):
    """
    Tests model generated output versus known
    static output.
    """
    __test__ = True

    @classmethod
    def setUpClass(self):
        super(gms9_TestOutput, self).setUpClass('GMS9.gms', 'GMS9_output.json')
