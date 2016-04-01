#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

import sys
import logging

from gwlfe import gwlfe, parser
from gwlfe.model import DataModel


def main():
    ch = logging.StreamHandler()
    parser.log.addHandler(ch)

    gms_filename = sys.argv[1]

    fp = open(gms_filename, 'r')
    gms = parser.GmsReader(fp).read()

    z = DataModel(gms)
    gwlfe.run(z)


if __name__ == '__main__':
    main()
