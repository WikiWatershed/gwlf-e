#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

import logging

from .parser import GmsReader


if __name__ == '__main__':
    import sys
    import json

    ch = logging.StreamHandler()
    log.addHandler(ch)

    gms_filename = sys.argv[1]

    fp = open(gms_filename, 'r')
    gms = GmsReader(fp).read()

    print(json.dumps(gms))
