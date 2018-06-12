from numpy import zeros

# from Timer import time_function
from Infiltration import Infiltration
from Infiltration import Infiltration_2
from Memoization import memoize
from MultiUse_Fxns.ET import DailyET_2

try:
    from Percolation_inner_compiled import Percolation_inner
except ImportError:
    print("Unable to import compiled Percolation_inner, using slower version")
    from Percolation_inner import Percolation_inner


@memoize
def Percolation(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap):
    result = zeros((NYrs, 12, 31))
    percolation = zeros((NYrs, 12, 31))
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
                    percolation[Y][i][j] = result[Y][i][j] - MaxWaterCap
                    result[Y][i][j] = MaxWaterCap
                else:
                    pass
                unsatstor_carryover = result[Y][i][j]
    return percolation


def Percolation_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                  ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap):
    infiltration = Infiltration_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                                  CNP_0, Imper, ISRR, ISRA, CN)

    et = DailyET_2(Temp, KV, PcntET, DayHrs)
    return Percolation_inner(NYrs, UnsatStor_0, DaysMonth, MaxWaterCap, infiltration, et)

    #   NYrs = arg(0, name=NYrs)  :: int64
    #   UnsatStor_0 = arg(1, name=UnsatStor_0)  :: float64
    #   DaysMonth = arg(2, name=DaysMonth)  :: array(int64, 2d, C)
    #   MaxWaterCap = arg(3, name=MaxWaterCap)  :: float64
    #   infiltration = arg(4, name=infiltration)  :: array(float64, 3d, C)
    #   et = arg(5, name=et)  :: array(float64, 3d, C)
