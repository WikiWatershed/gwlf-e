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
        NLU = 16
        NAnimals = 9

        return {
            'BasinId': 0,
            'AgSlope3to8': 0,
            'NumUAs': 0,
            'UABasinArea': 0,

            # Variables that are passed to PRedICT and are no longer used.
            'InName': '',
            'OutName': '',
            'UnitsFileFlag': 1,
            'AssessDate': '',
            'VersionNo': '',
            'ProjName': '',

            'NLU': NLU,
            'NAnimals': NAnimals,

            'Landuse': np.zeros(NLU, dtype=object),
            'Area': np.zeros(NLU),
            'CN': np.zeros(NLU),
            'KF': np.zeros(NLU),
            'LS': np.zeros(NLU),
            'C': np.zeros(NLU),
            'P': np.zeros(NLU),

            'NumNormalSys': np.zeros(12, dtype=int),
            'NumPondSys': np.zeros(12),
            'NumShortSys': np.zeros(12),
            'NumDischargeSys': np.zeros(12),
            'NumSewerSys': np.zeros(12),

            'SEDFEN': 0,
            'NFEN': 0,
            'PFEN': 0,

            'n86': 0,
            'n87': 0,
            'n88': 0,
            'n89': 0,
            'n90': 0,
            'n91': 0,
            'n92': 0,
            'n93': 0,
            'n94': 0,
            'n95': 0,
            'n95b': 0,
            'n95c': 0,
            'n95d': 0,
            'n95e': 0,

            'n96': 0,
            'n97': 0,
            'n98': 0,
            'n99': 0,
            'n99b': 0,
            'n99c': 0,
            'n99d': 0,
            'n99e': 0,
            'n100': 0,
            'n101': 0,
            'n101b': 0,
            'n101c': 0,
            'n101d': 0,
            'n101e': 0,
            'n102': 0,
            'n103a': 0,
            'n103b': 0,
            'n103c': 0,
            'n103d': 0,

            'n104': 0,
            'n105': 0,
            'n106': 0,
            'n106b': 0,
            'n106c': 0,
            'n106d': 0,
            'n107': 0,
            'n107b': 0,
            'n107c': 0,
            'n107d': 0,
            'n107e': 0,

            'Storm': 0,
            'CSNAreaSim': 0,
            'CSNDevType': 'None',
        }

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
