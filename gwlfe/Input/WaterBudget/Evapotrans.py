from numpy import sum
from numpy import zeros

from gwlfe.Input.WaterBudget.ET_1 import ET_1
from gwlfe.Input.WaterBudget.ET_1 import ET_1_f
from gwlfe.Memoization import memoize


def Evapotrans(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
               ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, ETFlag):
    result = zeros((NYrs, 12))
    et_f = ET_1(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0,
                AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET,
                DayHrs, MaxWaterCap, ETFlag)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                result[Y][i] = result[Y][i] + et_f[Y][i][j]
    return result


@memoize
def Evapotrans_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                 ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap):
    et_f = ET_1_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0,
                  AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET,
                  DayHrs, MaxWaterCap)
    return sum(et_f, axis=2)
