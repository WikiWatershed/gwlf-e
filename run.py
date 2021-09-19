#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json
import logging
import sys
import time
import argparse
from gwlfe import gwlfe, Parser


def main():
    log = logging.getLogger('gwlfe')
    log.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    log.addHandler(ch)

    parser = argparse.ArgumentParser(description='Run the GWLF-E model for a specified gms file.')
    parser.add_argument('input', type=str, nargs="+", help='Input GMS file')
    parser.add_argument('--output', type=str, nargs="?", help='Optional output file to write result of model run')
    parser.add_argument('--json', type=str, nargs="?", help='Optional output file to write JSON result of model run')

    args = parser.parse_args()

    gms_filenames = args.input

    for gms_filename in gms_filenames:
        fp = open(gms_filename, 'r')
        z = Parser.GmsReader(fp).read()

        result, z = gwlfe.run(z)
        if (args.output != None):  # gms out filename is sepcified so write
            gmsout_filename = args.output
            log.debug("Writing GMS output file (%s)" % (gmsout_filename))
            with open(gmsout_filename, "w") as file:
                test = Parser.GmsWriter(file)
                test.write(z)

        if (args.json != None):
            with open(args.json, "w") as file:
                json.dump(result, file, indent=2, sort_keys=True)


if __name__ == '__main__':
    main()
