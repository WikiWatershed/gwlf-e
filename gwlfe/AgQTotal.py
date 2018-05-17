import numpy as np
from Timer import time_function
from Water import Water
from Retention import Retention
from enums import LandUse
from Qrun import Qrun, Qrun_2
from AgAreaTotal import AgAreaTotal
from Memoization import memoize


@memoize
def AgQTotal(NYrs,DaysMonth,InitSnow_0, Temp, Prec,NRur,CN, AntMoist_0,NUrb,Grow,Landuse,Area):
    result = np.zeros((NYrs,12,31))
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    retention = Retention(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, NRur, NUrb, CN, Grow)
    q_run = Qrun(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, CN, AntMoist_0, Grow)
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

# @time_function
@memoize
def AgQTotal_2(NYrs,DaysMonth,InitSnow_0, Temp, Prec,NRur,CN, AntMoist_0,NUrb,Grow,Landuse,Area):
    result = np.zeros((NYrs, 12, 31))
    q_run = Qrun_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, CN, AntMoist_0, Grow)
    ag_area_total = AgAreaTotal(NRur, Landuse, Area)
    ag_used = np.array([1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0])
    ag_area = Area * ag_used
    qrun_agarea = q_run * ag_area
    result = np.sum(qrun_agarea, axis=3) / ag_area_total
    return result