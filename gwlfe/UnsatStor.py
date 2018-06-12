import numpy as np
from Timer import time_function
from Infiltration import Infiltration
from Infiltration import Infiltration_2
from MultiUse_Fxns.ET import DailyET_2
from Memoization import memoize

try:
    from UnsatStor_inner_compiled import UnsatStor_inner
except ImportError:
    print("Unable to import compiled UnsatStor_inner, using slower version")
    from UnsatStor_inner import UnsatStor_inner


@memoize
def UnsatStor(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
              ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap):
    result = np.zeros((NYrs, 12, 31))
    infiltration = Infiltration(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                                CNP_0, Imper,
                                ISRR, ISRA, CN)
    unsatstor_carryover = UnsatStor_0
    et = DailyET_2(Temp, KV, PcntET, DayHrs)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                result[Y][i][j] = unsatstor_carryover
                result[Y][i][j] = result[Y][i][j] + infiltration[Y][i][j]
                if et[Y][i][j] >= result[Y][i][j]:
                    result[Y][i][j] = 0
                else:
                    result[Y][i][j] = result[Y][i][j] - et[Y][i][j]
                if result[Y][i][j] > MaxWaterCap:
                    result[Y][i][j] = MaxWaterCap
                else:
                    pass
                unsatstor_carryover = result[Y][i][j]
    return result


# NYrs = arg(0, name=NYrs)  :: int64
#   DaysMonth = arg(1, name=DaysMonth)  :: array(int32, 2d, C)
#   MaxWaterCap = arg(2, name=MaxWaterCap)  :: float64
#   UnsatStor_0 = arg(3, name=UnsatStor_0)  :: float64
#   infiltration = arg(4, name=infiltration)  :: array(float64, 3d, C)
#   et = arg(5, name=et)  :: array(float64, 3d, C)

# @jit(cache=True, nopython=True)
# @compiled


@memoize
def UnsatStor_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap):
    infiltration = Infiltration_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                                  CNP_0, Imper, ISRR, ISRA, CN)
    et = DailyET_2(Temp, KV, PcntET, DayHrs)
    return UnsatStor_inner(NYrs, DaysMonth, MaxWaterCap, UnsatStor_0, infiltration, et)[0]
