# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

"""
Imported from PrelimCalculations.bas
"""

import math
import logging

from .enums import LandUse


log = logging.getLogger(__name__)


def InitialCalculations(z):
    log.debug('InitialCalculations')

    # OBTAIN THE LENGTH OF STREAMS IN AGRICULTURAL AREAS
    z.AGSTRM = z.AgLength / z.StreamLength

    # Obtain areas in Ha for Urban, Agricultural and Forested landuse
    for l in range(z.NRur):
        if z.Landuse[l] is LandUse.FOREST:
            z.ForestAreaTotal += z.Area[l]
        elif z.Landuse[l] is LandUse.CROPLAND:
            z.AgAreaTotal += z.Area[l]
        elif z.Landuse[l] is LandUse.HAY_PAST:
            z.AgAreaTotal += z.Area[l]
        elif z.Landuse[l] is LandUse.TURFGRASS:
            z.AgAreaTotal += z.Area[l]

        z.NewCN[0][l] = z.CN[l] / (2.334 - 0.01334 * z.CN[l])
        z.NewCN[2][l] = z.CN[l] / (0.4036 + 0.0059 * z.CN[l])
        if z.NewCN[2][l] > 100:
            z.NewCN[2][l] = 100

    for l in range(z.NRur, z.NLU):
        z.CNI[0][l] = z.CNI[1][l] / (2.334 - 0.01334 * z.CNI[1][1])
        z.CNI[2][l] = z.CNI[1][l] / (0.4036 + 0.0059 * z.CNI[1][l])
        z.CNP[0][l] = z.CNP[1][l] / (2.334 - 0.01334 * z.CNP[1][1])
        z.CNP[2][l] = z.CNP[1][l] / (0.4036 + 0.0059 * z.CNP[1][l])

    if z.FilterWidth <= 30:
        z.FilterEff = z.FilterWidth / 30
    else:
        z.FilterEff = 1

    if z.BasinArea > 0:
        z.BasinVol = z.BasinDeadStorage
        z.Difference = z.Capacity - z.BasinDeadStorage
        z.OutletCoef = 0

        while z.Difference > 0:
            z.OutletCoef += 0.001
            z.Volume = z.Capacity - z.BasinDeadStorage
            for k in range(z.DaysToDrain):
                z.Head = z.Volume / z.BasinArea
                if z.Volume > 0:
                    z.Flow = 382700 * z.OutletCoef * math.sqrt(z.Head)
                else:
                    z.Flow = 0
                z.Volume -= z.Flow
            z.Difference = z.Volume

        z.OutletCoef -= 0.001
        z.Difference = z.Capacity - z.BasinDeadStorage

        while z.Difference > 0:
            z.OutletCoef += 0.0001
            z.Volume = z.Capacity - z.BasinDeadStorage
            for k in range(z.DaysToDrain):
                z.Head = z.Volume / z.BasinArea
                z.Flow = 382700 * z.OutletCoef * math.sqrt(z.Head)
                z.Volume -= z.Flow
            z.Difference = z.Volume

    # ANTECEDANT MOISTURE OUT TO 5 DAYS
    z.AMC5 = 0
    for k in range(5):
        z.AMC5 += z.AntMoist[k]
