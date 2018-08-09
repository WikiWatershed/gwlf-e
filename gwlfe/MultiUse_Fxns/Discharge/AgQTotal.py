from numpy import array
from numpy import sum
from numpy import zeros

from gwlfe.Input.LandUse.Ag.AgAreaTotal import AgAreaTotal
# from Timer import time_function
from gwlfe.Input.WaterBudget.Water import Water
from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.Runoff.Qrun import Qrun, Qrun_f
from gwlfe.MultiUse_Fxns.Runoff.Retention import Retention
from gwlfe.enums import LandUse


@memoize
def AgQTotal(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, CN, AntMoist_0, NUrb, Grow_0, Landuse, Area):
    result = zeros((NYrs, 12, 31))
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    retention = Retention(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, NRur, NUrb, CN, Grow_0)
    q_run = Qrun(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, CN, AntMoist_0, Grow_0)
    ag_area_total = AgAreaTotal(NRur, Landuse, Area)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                result[Y][i][j] = 0

                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    for l in range(NRur):
                        if CN[l] > 0:
                            if water[Y][i][j] >= 0.2 * retention[Y][i][j][l]:
                                if Landuse[l] is LandUse.CROPLAND:
                                    # (Maybe used for STREAMPLAN?)
                                    result[Y][i][j] += q_run[Y][i][j][l] * Area[l]
                                    # z.AgQRunoff[l][i] += z.Qrun[Y][i][j][l]
                                elif Landuse[l] is LandUse.HAY_PAST:
                                    result[Y][i][j] += q_run[Y][i][j][l] * Area[l]
                                    # z.AgQRunoff[l][i] += z.Qrun[Y][i][j][l]
                                elif Landuse[l] is LandUse.TURFGRASS:
                                    result[Y][i][j] += q_run[Y][i][j][l] * Area[l]
                                    # z.AgQRunoff[l][i] += z.Qrun[Y][i][j][l]
                    if ag_area_total > 0:
                        result[Y][i][j] = result[Y][i][j] / ag_area_total
                    else:
                        result[Y][i][j] = 0
    return result


@memoize
def AgQTotal_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, CN, AntMoist_0, NUrb, Grow_0, Landuse, Area):
    result = zeros((NYrs, 12, 31))
    q_run = Qrun_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, CN, AntMoist_0, Grow_0)
    ag_area_total = AgAreaTotal(NRur, Landuse, Area)
    ag_used = array([1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    ag_area = Area * ag_used
    qrun_agarea = q_run * ag_area
    if ag_area_total > 0:
        result = sum(qrun_agarea, axis=3) / ag_area_total
    return result
