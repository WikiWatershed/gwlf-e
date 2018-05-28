import numpy as np
from Timer import time_function
from Water import Water
from AgQTotal import AgQTotal
from Memoization import memoize
from Water import Water_2
from AgQTotal import AgQTotal_2


# @time_function
@memoize
def AgRunoff(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, CN, AntMoist_0, NUrb, Grow_0, Landuse, Area):
    result = np.zeros((NYrs, 12))
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    ag_q_total = AgQTotal(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, CN, AntMoist_0, NUrb, Grow_0, Landuse, Area)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    result[Y][i] += ag_q_total[Y][i][j]
    return result

# @time_function
@memoize
def AgRunoff_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, CN, AntMoist_0, NUrb, Grow_0, Landuse, Area):
    result = np.zeros((NYrs, 12, 31))
    water = Water_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    ag_q_total = AgQTotal_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, CN, AntMoist_0, NUrb, Grow_0, Landuse, Area)
    result[np.where((Temp>0) & (water > 0.01))] = ag_q_total[np.where((Temp>0) & (water > 0.01))]
    return np.sum(result, axis = 2)