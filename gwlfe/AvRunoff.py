import numpy as np
# from Timer import time_function
from Memoization import memoize
from Runoff import Runoff
from Runoff import Runoff_2

def AvRunoff(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
             Imper, ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN, Landuse, TileDrainDensity):
    result = np.zeros(12)
    runoff = Runoff(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                    Imper, ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN, Landuse, TileDrainDensity)
    for Y in range(NYrs):
        for i in range(12):
            result[i] += runoff[Y][i] / NYrs
    return result

def AvRunoff_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
               Imper, ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN, Landuse, TileDrainDensity):
    return np.sum(Runoff_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                         Imper, ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN, Landuse, TileDrainDensity),
                  axis=0) / NYrs
