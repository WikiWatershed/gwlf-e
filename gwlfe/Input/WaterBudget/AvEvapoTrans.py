from numpy import average
from numpy import zeros

from gwlfe.Input.WaterBudget.Evapotrans import Evapotrans
from gwlfe.Input.WaterBudget.Evapotrans import Evapotrans_f
from gwlfe.Memoization import memoize


@memoize
def AvEvapoTrans(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                 ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, ETFlag):
    result = zeros(12)
    evapotrans = Evapotrans(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                            Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, ETFlag)
    for Y in range(NYrs):
        for i in range(12):
            result[i] += evapotrans[Y][i] / NYrs
    return result


@memoize
def AvEvapoTrans_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                   Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap):
    evapotrans = Evapotrans_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                              CNP_0, Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap)
    return average(evapotrans, axis=0)
