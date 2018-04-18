import numpy as np
from Timer import time_function
from Water import Water
from Qrun import Qrun
from RurAreaTotal import RurAreaTotal
from Retention import Retention
from AreaTotal import AreaTotal


def RuralQTotal(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, CN, NUrb, AntMoist_0, Grow, Area):
    result = np.zeros((NYrs, 12, 31))
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    q_run = Qrun(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, CN, AntMoist_0, Grow)
    rur_area_total = RurAreaTotal(NRur, Area)
    retention = Retention(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, NRur, NUrb, CN, Grow)
    area_total = AreaTotal(NRur, NUrb, Area)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                result[Y][i][j] = 0  # this does not need to be calculated daily
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    for l in range(NRur):
                        if CN[l] > 0:  # TODO: CN in set to all zeros in datamodel:42
                            if water[Y][i][j] >= 0.2 * retention[Y][i][j][l]:
                                result[Y][i][j] += q_run[Y][i][j][l] * Area[l] / rur_area_total
                    if result[Y][i][j] > 0:
                        result[Y][i][j] *= rur_area_total / area_total
                    else:
                        result[Y][i][j] = 0  # TODO: this seems redundant
                else:
                    pass
    return result


def RuralQTotal_2():
    pass
