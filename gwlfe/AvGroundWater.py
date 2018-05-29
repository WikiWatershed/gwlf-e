import numpy as np
from Timer import time_function
from Memoization import memoize
from GroundWatLE_2 import GroundWatLE
from GroundWatLE_2 import GroundWatLE_2


def AvGroundWater(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0,
                  AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap,
                  SatStor_0, RecessionCoef, SeepCoef):
    result = np.zeros(12)
    ground_wat_le = GroundWatLE(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0,
                                AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs,
                                MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef)
    for Y in range(NYrs):
        for i in range(12):
            result[i] += ground_wat_le[Y][i] / NYrs
    return result


def AvGroundWater_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0,
                    AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap,
                    SatStor_0, RecessionCoef, SeepCoef, Landuse, TileDrainDensity):
    return np.sum(GroundWatLE_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0,
                                AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs,
                                MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef, Landuse, TileDrainDensity),
                  axis=0) / NYrs
