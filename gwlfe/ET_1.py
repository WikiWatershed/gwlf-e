from numpy import zeros
from numpy import array

from Infiltration import Infiltration_f
from Memoization import memoize
from MultiUse_Fxns.ET import DailyET
from MultiUse_Fxns.ET import DailyET_f
from Timer import time_function

try:
    from UnsatStor_inner_compiled import UnsatStor_inner
except ImportError:
    print("Unable to import compiled UnsatStor_inner, using slower version")
    from UnsatStor_inner import UnsatStor_inner


# @memoize
def ET_1(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
         ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, ETFlag):
    result = zeros((NYrs, 12, 31))
    infiltration = Infiltration_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                                  CNP_0, Imper, ISRR, ISRA, CN)
    unsatstor_carryover = UnsatStor_0
    et = DailyET(NYrs, DaysMonth, Temp, DayHrs, KV, PcntET, ETFlag)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                result[Y][i][j] = unsatstor_carryover
                result[Y][i][j] = result[Y][i][j] + infiltration[Y][i][j]
                if et[Y][i][j] >= result[Y][i][j]:
                    et[Y][i][j] = result[Y][i][j]
                    result[Y][i][j] = 0
                else:
                    result[Y][i][j] = result[Y][i][j] - et[Y][i][j]
                if result[Y][i][j] > MaxWaterCap:
                    result[Y][i][j] = MaxWaterCap
                else:
                    pass
                unsatstor_carryover = result[Y][i][j]
    return et

# @memoize
def ET_1_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
           ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap):
    infiltration = Infiltration_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                                  CNP_0, Imper, ISRR, ISRA, CN)
    daily_et = DailyET_f(Temp, KV, PcntET, DayHrs)
    return UnsatStor_inner(NYrs, DaysMonth, MaxWaterCap, UnsatStor_0, infiltration, daily_et)[1]
