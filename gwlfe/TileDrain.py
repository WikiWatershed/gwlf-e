from numpy import zeros

from Memoization import memoize
# from Timer import time_function
from TileDrainGW import TileDrainGW
from TileDrainGW import TileDrainGW_2
from TileDrainRO import TileDrainRO
from TileDrainRO import TileDrainRO_2


# @memoize
def TileDrain(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
              ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef, Landuse,
              TileDrainDensity):
    result = zeros((NYrs, 12))
    tiledrainro = TileDrainRO(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, CN, AntMoist_0, NUrb, Grow_0, Landuse, Area,
                              TileDrainDensity)
    tiledraingw = TileDrainGW(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                              Imper,
                              ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef,
                              SeepCoef, Landuse, TileDrainDensity)
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = (result[Y][i] + tiledrainro[Y][i] + tiledraingw[Y][i])
    return result

@memoize
def TileDrain_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef,
                Landuse, TileDrainDensity):
    tiledrainro = TileDrainRO_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, CN, AntMoist_0, NUrb, Grow_0, Landuse,
                                Area,
                                TileDrainDensity)
    tiledraingw = TileDrainGW_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                                CNP_0,
                                Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                                RecessionCoef, SeepCoef, Landuse, TileDrainDensity)
    return tiledrainro + tiledraingw
