from numpy import zeros

from gwlfe.Input.WaterBudget.GrFlow import GrFlow
from gwlfe.Input.WaterBudget.GrFlow import GrFlow_f
# from Timer import time_function
from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.Runoff.DayRunoff import DayRunoff
from gwlfe.MultiUse_Fxns.Runoff.DayRunoff import DayRunoff_f


@memoize
def DailyFlow(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
              ISRR, ISRA, CN, Qretention, PctAreaInfil, n25b, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
              RecessionCoef, SeepCoef):
    result = zeros((NYrs, 12, 31))
    day_runoff = DayRunoff(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0,
                           AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN)
    grflow = GrFlow(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                    ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                result[Y][i][j] = day_runoff[Y][i][j] + grflow[Y][i][j]
    return result


@memoize
def DailyFlow_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                ISRR, ISRA, CN, Qretention, PctAreaInfil, n25b, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                RecessionCoef, SeepCoef):
    day_runoff = DayRunoff_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0,
                             AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN)
    grflow = GrFlow_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                      Imper,
                      ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef)
    return day_runoff + grflow
