import os

from test_gms_writer import TestGMSWriter


class TestInput4GMS(TestGMSWriter):
    @classmethod
    def setUpClass(self):
        super(TestInput4GMS, self).setUpClass(
            open(os.path.abspath(os.path.join(__file__, '../', 'input_4.gms')), 'r'),
            open(os.path.abspath(os.path.join(__file__, '../', 'input_4.gmsout')), 'r'))
