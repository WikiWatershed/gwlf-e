import os
import json
from gwlfe import Parser
from StringIO import StringIO
from test_gms_writer import TestGMSWriter


class TestPrerunGMS(TestGMSWriter):
    @classmethod
    def setUpClass(self):
        mapshed_data = json.load(open(os.path.abspath(os.path.join(__file__, '../', "mapshed_data.json.txt")),"r"))
        pre_z = Parser.DataModel(mapshed_data)
        output = StringIO()
        writer = Parser.GmsWriter(output)
        writer.write(pre_z)

        output.seek(0)

        super(TestPrerunGMS, self).setUpClass(
            output,
            open(os.path.abspath(os.path.join(__file__, '../', "mapshed_data.gms")), 'r'))
