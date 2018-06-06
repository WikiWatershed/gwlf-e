import numpy as np
from Timer import time_function
from Water import Water
from AdjUrbanQTotal_1 import AdjUrbanQTotal_1
from RuralQTotal import RuralQTotal
from Memoization import memoize
from Water import Water_2
from AdjUrbanQTotal_1 import AdjUrbanQTotal_1_2
from RuralQTotal import RuralQTotal_2


# @time_function
@memoize
def AdjQTotal(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
              ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN):
    result = np.zeros((NYrs, 12, 31))
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    adj_urban_q_total = AdjUrbanQTotal_1(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                                       Grow_0, CNP_0, Imper,
                                       ISRR, ISRA, Qretention, PctAreaInfil)
    rural_q_total = RuralQTotal(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, CN, NUrb, AntMoist_0, Grow_0, Area)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    # Assume 20% reduction of runoff with urban wetlands
                    result[Y][i][j] = (adj_urban_q_total[Y][i][j] * (1 - (n25b * 0.2))) + rural_q_total[Y][i][j]
    return result

# @time_function
@memoize
def AdjQTotal_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
              ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN):
    result = np.zeros((NYrs, 12, 31))
    water = Water_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    adj_urban_q_total = AdjUrbanQTotal_1_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                                       Grow_0, CNP_0, Imper,ISRR, ISRA, Qretention, PctAreaInfil)
    rural_q_total = RuralQTotal_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, CN, NUrb, AntMoist_0, Grow_0, Area)
    result[np.where((Temp>0) & (water>0.01))] = (adj_urban_q_total[np.where((Temp>0) & (water>0.01))]* (1 - (n25b * 0.2))) + rural_q_total[np.where((Temp>0) & (water>0.01))]
    return result
