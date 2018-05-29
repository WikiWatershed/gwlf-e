import numpy as np
from Timer import time_function
from TileDrainGW import TileDrainGW
from TileDrainGW import TileDrainGW_2
from GroundWatLE import GroundWatLE
from GroundWatLE import GroundWatLE_2 as GroundWatLE_2_actual
from Memoization import memoize


@memoize
def GroundWatLE_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                  ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef,
                  Landuse, TileDrainDensity):
    result = np.zeros((NYrs, 12))
    tiledraingw = TileDrainGW_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                              Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef,
                              SeepCoef, Landuse, TileDrainDensity)
    grounwatle_1 = GroundWatLE_2_actual(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                               CNP_0, Imper,
                               ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef,
                               SeepCoef)
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = grounwatle_1[Y][i] - tiledraingw[Y][i]
        if result[Y][i] < 0:
            result[Y][i] = 0
    return result


def GroundWatLE_2_2():
    pass
