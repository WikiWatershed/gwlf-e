import numpy as np
from Timer import time_function
from GroundWatLE import GroundWatLE
from GroundWatLE import GroundWatLE_2
from AreaTotal import AreaTotal
from AreaTotal import AreaTotal_2
from AgAreaTotal import AgAreaTotal
from Memoization import memoize


def GwAgLE(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
           ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef, Landuse):
    result = np.zeros((NYrs, 12))
    areatotal = AreaTotal(NRur, NUrb, Area)
    agareatotal = AgAreaTotal(NRur, Landuse, Area)
    groundwatle = GroundWatLE(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                              Imper,
                              ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef,
                              SeepCoef)
    for Y in range(NYrs):
        for i in range(12):
            if areatotal > 0:
                result[Y][i] = (result[Y][i] + (groundwatle[Y][i] * (agareatotal / areatotal)))
    return result


def GwAgLE_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
             ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef, Landuse):
    areatotal = AreaTotal_2(Area)
    agareatotal = AgAreaTotal(NRur, Landuse, Area)
    groundwatle = GroundWatLE_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                                CNP_0,
                                Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                                RecessionCoef, SeepCoef)
    if (areatotal > 0):
        return groundwatle * agareatotal / areatotal
    else:
        return np.zeros((NYrs, 12))
