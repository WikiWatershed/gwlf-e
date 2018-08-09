from numpy import sum
from numpy import zeros

from gwlfe.Input.LandUse.AreaTotal import AreaTotal
from gwlfe.Input.LandUse.RurAreaTotal import RurAreaTotal
# from Timer import time_function
from gwlfe.Input.WaterBudget.Water import Water
from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.Runoff.Qrun import Qrun, Qrun_f
from gwlfe.MultiUse_Fxns.Runoff.Retention import Retention


# @time_function
@memoize
def RuralQTotal(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, CN, NUrb, AntMoist_0, Grow_0, Area):
    result = zeros((NYrs, 12, 31))
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    q_run = Qrun(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, CN, AntMoist_0, Grow_0)
    rur_area_total = RurAreaTotal(NRur, Area)
    retention = Retention(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, NRur, NUrb, CN, Grow_0)
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


@memoize
def RuralQTotal_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, CN, NUrb, AntMoist_0, Grow_0, Area):
    result = zeros((NYrs, 12, 31))
    q_run = Qrun_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, CN, AntMoist_0, Grow_0)
    area_total = AreaTotal(NRur, NUrb, Area)
    qrun_area = q_run * Area
    result = sum(qrun_area, axis=3) / area_total
    return result
