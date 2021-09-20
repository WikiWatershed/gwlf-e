# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .test_output import TestOutput


class elm_fork_TestOutput(TestOutput):
    """
    Tests model generated output versus known
    static output.
    """
    __test__ = True

    @classmethod
    def setUpClass(self):
        super(elm_fork_TestOutput, self).setUpClass('underflow_exception_elm_fork_red.gms',
                                               'underflow_exception_elm_fork_red_output.json')
