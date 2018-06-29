#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

import sys
import json
import logging
import time

from gwlfe import gwlfe, Parser

def main():
    log = logging.getLogger('gwlfe')
    log.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    log.addHandler(ch)

    gms_filename = sys.argv[1]

    fp = open(gms_filename, 'r')
    z = Parser.GmsReader(fp).read()
    start = time.time()
    result,z = gwlfe.run(z)
    print(time.time()-start)
    print(json.dumps(result, indent=4))
    if(len(sys.argv) == 3):#gms out filename is sepcified so write
        gmsout_filename = sys.argv[2]
        log.debug("Writing GMS output file (%s)"%(gmsout_filename))
        with open(gmsout_filename,"w") as file:
            test = Parser.GmsWriter(file)
            test.write(z)

if __name__ == '__main__':
    main()
