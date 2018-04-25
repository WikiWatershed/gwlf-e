import numpy as np
from Timer import time_function
from GwAgLE import GwAgLE


def TileDrainGW(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
           ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef, Landuse, TileDrainDensity):
    result = np.zeros((NYrs, 12))
    gwagle = GwAgLE(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
           ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef, Landuse)
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = (result[Y][i] + [gwagle[Y][i] * TileDrainDensity])
    return result


def TileDrainGW_2():
    pass
