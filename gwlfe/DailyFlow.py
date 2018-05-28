import numpy as np
from Timer import time_function
from Memoization import memoize
from DayRunoff import DayRunoff
from GrFlow import GrFlow


@memoize
def DailyFlow(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
              ISRR, ISRA, CN, Qretention, PctAreaInfil, n25b, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
              RecessionCoef, SeepCoef):
    result = np.zeros((NYrs, 12, 31))
    day_runoff = DayRunoff(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0,
                           AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN)
    grflow = GrFlow(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                    ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                result[Y][i][j] = day_runoff[Y][i][j] + grflow[Y][i][j]
    return result


def DailyFlow_2():
    pass
