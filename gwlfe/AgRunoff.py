import numpy as np
from Timer import time_function
from Water import Water
from AgQTotal import AgQTotal


def AgRunoff(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, CN, AntMoist_0, NUrb, Grow, Landuse, Area):
    result = np.zeros((NYrs, 12))
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    ag_q_total = AgQTotal(NYrs,DaysMonth,InitSnow_0, Temp, Prec,NRur,CN, AntMoist_0,NUrb,Grow,Landuse,Area)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    result[Y][i] += ag_q_total[Y][i][j]
    return result


def AgRunoff_2():
    pass
