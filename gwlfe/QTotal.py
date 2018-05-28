import numpy as np
from Timer import time_function
from UrbanQTotal_1 import UrbanQTotal_1
from RuralQTotal import RuralQTotal
from Water import Water
from Memoization import memoize
from UrbanQTotal_1 import UrbanQTotal_1_2
from RuralQTotal import RuralQTotal_2
from Water import Water_2

# @time_function
@memoize
def QTotal(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
           ISRR, ISRA, CN):
    result = np.zeros((NYrs, 12, 31))
    urban_q_total_1 = UrbanQTotal_1(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                                    CNP_0, Imper, ISRR, ISRA)
    rural_q_total = RuralQTotal(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, CN, NUrb, AntMoist_0, Grow_0, Area)
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                # z.QTotal = 0
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    result[Y][i][j] = urban_q_total_1[Y][i][j] + rural_q_total[Y][i][j]
    return result

@memoize
# @time_function
def QTotal_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
           ISRR, ISRA, CN):
    result = np.zeros((NYrs, 12, 31))
    urban_q_total_1 = UrbanQTotal_1(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                                    CNP_0, Imper, ISRR, ISRA)
    rural_q_total = RuralQTotal_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, CN, NUrb, AntMoist_0, Grow_0, Area)
    water = Water_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    result[np.where((Temp>0) & (water>0))] = urban_q_total_1[np.where((Temp>0) & (water>0))] + rural_q_total[np.where((Temp>0) & (water>0))]

    return result