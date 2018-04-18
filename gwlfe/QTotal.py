import numpy as np
from Timer import time_function
from UrbanQTotal_1 import UrbanQTotal_1
from RuralQTotal import RuralQTotal
from Water import Water


def QTotal(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
           ISRR, ISRA, CN):
    result = np.zeros((NYrs, 12, 31))
    urban_q_total_1 = UrbanQTotal_1(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow,
                                    CNP_0, Imper, ISRR, ISRA)
    rural_q_total = RuralQTotal(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, CN, NUrb, AntMoist_0, Grow, Area)
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                # z.QTotal = 0
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    result[Y][i][j] = urban_q_total_1[Y][i][j] + rural_q_total[Y][i][j]
    return result


def QTotal_2():
    pass
