import numpy as np
from Timer import time_function
from Water import Water
from Qrun import Qrun, Qrun_2
from RurAreaTotal import RurAreaTotal
from Retention import Retention
from AreaTotal import AreaTotal
from Memoization import memoize

# @time_function
@memoize
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

# @time_function
@memoize
def RuralQTotal_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, CN, NUrb, AntMoist_0, Grow, Area):
    result = np.zeros((NYrs, 12, 31))
    q_run = Qrun_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, CN, AntMoist_0, Grow)
    area_total = AreaTotal(NRur, NUrb, Area)
    qrun_area = q_run * Area
    result = np.sum(qrun_area, axis=3)/area_total
    return result