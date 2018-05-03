import numpy as np
from Timer import time_function
from Water import Water
from UrbAreaTotal import UrbAreaTotal
from AreaTotal import AreaTotal
from UrbanQTotal import UrbanQTotal, UrbanQTotal_2


def UrbanQTotal_1(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
                  ISRR, ISRA):
    result = np.zeros((NYrs, 12, 31))
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    urban_area_total = UrbAreaTotal(NRur, NUrb, Area)
    area_total = AreaTotal(NRur, NUrb, Area)
    urban_q_total = UrbanQTotal(NYrs, DaysMonth, NRur, NUrb, Temp, InitSnow_0, Prec, Area, CNI_0, AntMoist_0, Grow,
                                CNP_0, Imper, ISRR, ISRA)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    if urban_area_total > 0:
                        result[Y][i][j] = urban_q_total[Y][i][j] * urban_area_total / area_total
                    else:
                        result[Y][i][j] = 0
    return result


def UrbanQTotal_1_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
                  ISRR, ISRA):
    result = np.zeros((NYrs, 12, 31))
    urban_area_total = UrbAreaTotal(NRur, NUrb, Area)
    area_total = AreaTotal(NRur, NUrb, Area)
    urban_q_total = UrbanQTotal_2(NYrs, DaysMonth, NRur, NUrb, Temp, InitSnow_0, Prec, Area, CNI_0, AntMoist_0, Grow,
                                CNP_0, Imper, ISRR, ISRA)
    result = urban_q_total * urban_area_total / area_total
    return result