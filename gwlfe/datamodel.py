# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

from decimal import Decimal
import json

import numpy as np


class DataModel(object):
    def __init__(self, data=None):
        self.__dict__.update(self.defaults())
        self.__dict__.update(data or {})

    def defaults(self):
        return {}

    def __str__(self):
        return '<GWLF-E DataModel>'

    def tojson(self):
        return json.dumps(self.__dict__, cls=NumpyAwareJSONEncoder)


class NumpyAwareJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)
