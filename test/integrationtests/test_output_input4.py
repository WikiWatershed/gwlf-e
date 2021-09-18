# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .test_output import TestOutput


# from mock import patch
# from gwlfe.Memoization import memoize_with_args
# patch('gwlfe.Memoization.memoize', memoize_with_args).start()


class input_4_TestOutput(TestOutput):
    """
    Tests model generated output versus known
    static output.
    """
    __test__ = True
    @classmethod
    def setUpClass(self):
        super(input_4_TestOutput, self).setUpClass('input_4.gms', 'input_4_output.json')
