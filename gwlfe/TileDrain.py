import numpy as np
from Timer import time_function
from TileDrainGW import TileDrainGW
from TileDrainRO import TileDrainRO
from Memoization import memoize


@memoize
def TileDrain(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
              ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef, Landuse,
              TileDrainDensity):
    result = np.zeros((NYrs, 12))
    tiledrainro = TileDrainRO(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, CN, AntMoist_0, NUrb, Grow, Landuse, Area,
                              TileDrainDensity)
    tiledraingw = TileDrainGW(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0,
                              Imper,
                              ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef,
                              SeepCoef, Landuse, TileDrainDensity)
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = (result[Y][i] + tiledrainro[Y][i] + tiledraingw[Y][i])
    return result


def TileDrain_2():
    pass
