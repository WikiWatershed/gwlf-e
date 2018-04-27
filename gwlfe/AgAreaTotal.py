import numpy as np
from Timer import time_function
from enums import LandUse

from Memoization import memoize


@memoize
def AgAreaTotal(NRur, Landuse, Area):
    result = 0
    for l in range(NRur):
        if Landuse[l] is LandUse.FOREST:
            pass
        elif Landuse[l] is LandUse.CROPLAND:
            result += Area[l]
        elif Landuse[l] is LandUse.HAY_PAST:
            result += Area[l]
        elif Landuse[l] is LandUse.TURFGRASS:
            result += Area[l]
    return result


def AgAreaTotal_2():
    pass
