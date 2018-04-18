import numpy as np
from Timer import time_function
from UrbanQTotal_1 import UrbanQTotal_1


def QTotal(NYrs, DaysMonth, Temp, Water, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
           ISRR, ISRA):
    result = np.zeros((NYrs, 12, 31))
    urban_q_total_1 = UrbanQTotal_1(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow,
                                    CNP_0, Imper, ISRR, ISRA)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp > 0 and Water[Y][i][j] > 0.01:
                    result[Y][i][j] = urban_q_total_1[Y][i][j] + z.RuralQTotal
    return result


def QTotal_2():
    pass
