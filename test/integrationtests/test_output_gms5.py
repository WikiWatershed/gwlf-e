# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .test_output import TestOutput


class gms5_TestOutput(TestOutput):
    """
    Tests model generated output versus known
    static output.
    """
    __test__ = True

    @classmethod
    def setUpClass(self):
        super(gms5_TestOutput, self).setUpClass('GMS5.gms', 'GMS5_output.json')
