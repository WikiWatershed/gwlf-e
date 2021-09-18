# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

"""
Imported from PrelimCalculations.bas
"""

import logging
from .enums import LandUse

log = logging.getLogger(__name__)


def InitialCalculations(z):
    # Obtain areas in Ha for Urban, Agricultural and Forested landuse
    for l in range(z.NRur):
        if z.Landuse[l] is LandUse.FOREST:
            z.ForestAreaTotal += z.Area[l]

    # ANTECEDANT MOISTURE OUT TO 5 DAYS
    z.AMC5_f = 0
    for k in range(5):
        z.AMC5_f += z.AntMoist[k]
