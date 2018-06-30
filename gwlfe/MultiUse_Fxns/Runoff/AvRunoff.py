from numpy import sum
from numpy import zeros

from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.Runoff.Runoff import Runoff
from gwlfe.MultiUse_Fxns.Runoff.Runoff import Runoff_f


def AvRunoff(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
             Imper, ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN, Landuse, TileDrainDensity):
    result = zeros(12)
    runoff = Runoff(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                    Imper, ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN, Landuse, TileDrainDensity)
    for Y in range(NYrs):
        for i in range(12):
            result[i] += runoff[Y][i] / NYrs
    return result


@memoize
def AvRunoff_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
               Imper, ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN, Landuse, TileDrainDensity):
    return sum(Runoff_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                        Imper, ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN, Landuse, TileDrainDensity),
               axis=0) / NYrs
