import os


variable_name = raw_input("Enter the name of the variable:")

#write variable file
var_filename = "%s.py"%(variable_name)
if os.path.exists("gwlfe/"+var_filename):
    raise IOError("File already exists")
else:
    with open("gwlfe/"+var_filename,"w") as file:
        file.write("from numpy import zeros\n"
                    "from Memoization import memoize\n\n\n"
                    "def %s():\n"
                    "    pass\n"
                    "\n\n"
                    "def %s_f():\n"
                    "    pass\n"%(variable_name,variable_name)
                   )

#write test file
test_filename = "test_%s.py"%(variable_name)
if os.path.exists("test/"+test_filename):
    raise IOError("File already exists")
else:
    with open("test/"+test_filename,"w") as file:
        file.write("import numpy as np\n"
                    "from .VariableUnitTest import VariableUnitTest\n"
                    "from unittest import skip\n"
                    "from gwlfe import {variable}\n"
                    "\n\n"
                    "class Test{variable}(VariableUnitTest):\n"
                    "    @skip('Not Ready Yet.')\n"
                    "    def test_{variable}(self):\n"
                    "        z = self.z\n"
                    "        np.testing.assert_array_almost_equal(\n"
                    "            {variable}.{variable}_f(),\n"
                    "            {variable}.{variable}(), decimal=7)".format(variable=variable_name))