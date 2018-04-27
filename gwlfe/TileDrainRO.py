import numpy as np
from Timer import time_function
from AgRunoff import AgRunoff
from Memoization import memoize


@memoize
def TileDrainRO(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, CN, AntMoist_0, NUrb, Grow, Landuse, Area,
                TileDrainDensity):
    result = np.zeros((NYrs, 12))
    ag_runoff = AgRunoff(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, CN, AntMoist_0, NUrb, Grow, Landuse, Area)
    for Y in range(NYrs):
        for i in range(12):
            # CALCULATE THE SURFACE RUNOFF PORTION OF TILE DRAINAGE
            result[Y][i] = ag_runoff[Y][i] * TileDrainDensity
    return result


def TileDrainRO_2():
    pass
