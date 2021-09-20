# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json
from calendar import monthrange
from decimal import Decimal

from numpy import zeros
from numpy import ndarray

class DataModel(object):
    def __init__(self, data=None):
        self.__dict__.update(self.defaults())
        self.__dict__.update(data or {})
        self.__dict__.update(self.date_guides())

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

            'Landuse': zeros(NLU, dtype=object),
            'Area': zeros(NLU),
            'CN': zeros(NLU),
            'KF': zeros(NLU),
            'LS': zeros(NLU),
            'C': zeros(NLU),
            'P': zeros(NLU),

            'NumNormalSys': zeros(12, dtype=int),
            'NumPondSys': zeros(12),
            'NumShortSys': zeros(12),
            'NumDischargeSys': zeros(12),
            'NumSewerSys': zeros(12),

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
            'CSNDevType': 'None'
        }

    def date_guides(self):
        model = self.__dict__
        output = {}
        if 'WxYrBeg' in model and 'WxYrEnd' in model:
            begyear = model['WxYrBeg']
            endyear = model['WxYrEnd']
            year_range = endyear - begyear + 1
            month_abbr = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

            if 'DaysMonth' not in model:
                output['DaysMonth'] = zeros((year_range, 12),
                                            dtype=int)
                for y in range(year_range):
                    year = begyear + y
                    for m in range(12):
                        output['DaysMonth'][y][m] = monthrange(year, m + 1)[1]

            if 'WxMonth' not in model:
                output['WxMonth'] = [month_abbr
                                     for y in range(year_range)]

            if 'WxYear' not in model:
                output['WxYear'] = [[begyear + y] * 12
                                    for y in range(year_range)]
        return output

    def __str__(self):
        return '<GWLF-E DataModel>'

    def tojson(self):
        return json.dumps(self.__dict__, cls=NumpyAwareJSONEncoder)


class NumpyAwareJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ndarray):
            return obj.tolist()
        elif isinstance(obj, Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)
