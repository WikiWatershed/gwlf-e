import numpy as np
from Timer import time_function
from Memoization import memoize
from Evapotrans import Evapotrans


def AvEvapoTrans(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
               ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap):
    result = np.zeros(12)
    evapotrans = Evapotrans(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
               ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap)
    for Y in range(NYrs):
        for i in range(12):
            result[i] += evapotrans[Y][i] / NYrs
    return result


@memoize
def AvEvapoTrans_2(Evapotrans):
    return np.average(Evapotrans, axis=0)
