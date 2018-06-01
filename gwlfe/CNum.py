import numpy as np
from Timer import time_function
from DailyArrayConverter import get_value_for_yesterday
from MeltPest import MeltPest
from NewCN import NewCN, NewCN_2
from AMC5 import AMC5, AMC5_1, AMC5_yesterday
from GrowFactor import GrowFactor
from GrowFactor import GrowFactor_2
from Water import Water, Water_2
from Melt import Melt
from Melt_1 import Melt_1_2
from numba import jit
from Memoization import memoize
from numba.pycc import CC

try:
    from CNum_inner_compiled import CNum_inner
except ImportError:
    print("Unable to import compiled CNum_inner, using slower version")
    from CNum_inner import CNum_inner


@memoize
# @time_function
def CNum(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, CN, NRur, NUrb, Grow_0):
    result = np.zeros((NYrs, 12, 31, 10))
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    melt = Melt(NYrs, DaysMonth, Temp, InitSnow_0, Prec)  # I think this should be Melt_1
    grow_factor = GrowFactor(Grow_0)
    amc5 = AMC5(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0)
    new_cn = NewCN(NRur, NUrb, CN)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                # result[Y][i][j][l] = 0
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    for l in range(NRur):
                        if CN[l] > 0:
                            if melt[Y][i][j] <= 0:
                                if grow_factor[i] > 0:
                                    # growing season
                                    if get_value_for_yesterday(amc5, 0, Y, i, j, NYrs, DaysMonth) >= 5.33:
                                        result[Y][i][j][l] = new_cn[2][l]
                                    elif get_value_for_yesterday(amc5, 0, Y, i, j, NYrs, DaysMonth) < 3.56:
                                        result[Y][i][j][l] = new_cn[0][l] + (
                                                CN[l] - new_cn[0][l]) * get_value_for_yesterday(amc5, 0, Y,
                                                                                                i, j,
                                                                                                NYrs,
                                                                                                DaysMonth) / 3.56
                                    else:
                                        result[Y][i][j][l] = CN[l] + (new_cn[2][l] - CN[l]) * (
                                                get_value_for_yesterday(amc5, 0, Y, i, j, NYrs,
                                                                        DaysMonth) - 3.56) / 1.77
                                else:
                                    # dormant season
                                    if get_value_for_yesterday(amc5, 0, Y, i, j, NYrs, DaysMonth) >= 2.79:
                                        result[Y][i][j][l] = new_cn[2][l]
                                    elif get_value_for_yesterday(amc5, 0, Y, i, j, NYrs, DaysMonth) < 1.27:
                                        result[Y][i][j][l] = new_cn[0][l] + (
                                                CN[l] - new_cn[0][l]) * get_value_for_yesterday(amc5, 0, Y,
                                                                                                i, j,
                                                                                                NYrs,
                                                                                                DaysMonth) / 1.27
                                    else:
                                        result[Y][i][j][l] = CN[l] + (new_cn[2][l] - CN[l]) * (
                                                get_value_for_yesterday(amc5, 0, Y, i, j, NYrs,
                                                                        DaysMonth) - 1.27) / 1.52
                            else:
                                result[Y][i][j][l] = new_cn[2][l]
                        # result[Y][i][j][l] = CNum
    return result


# @time_function
def CNum_1(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, CN, NRur, NUrb, Grow_0):
    melt_pest = np.repeat(Melt_1_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec)[:, :, :, None], NRur, axis=3)
    newcn = NewCN_2(NRur, NUrb, CN)
    amc5 = np.repeat(AMC5_yesterday(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0)[:, :, :, None], NRur, axis=3)
    # g = GrowFactor(Grow_0)
    grow_factor = np.tile(GrowFactor(Grow_0)[None, :, None, None], (NYrs, 1, 31, NRur))
    water = np.repeat(Water_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec)[:, :, :, None], NRur, axis=3)
    Temp = np.repeat(Temp[:, :, :, None], NRur, axis=3)
    CN_0 = np.tile(CN[:10][None, None, None, :], (NYrs, 12, 31, 1))
    newcn_0 = np.tile(newcn[0, :10][None, None, None, :], (NYrs, 12, 31, 1))
    newcn_2 = np.tile(newcn[2, :10][None, None, None, :], (NYrs, 12, 31, 1))
    result_0 = np.zeros((NYrs, 12, 31, NRur))
    result_1 = np.zeros((NYrs, 12, 31, NRur))
    result = np.zeros((NYrs, 12, 31, NRur))  # TODO: should we just generalize to NLU?
    # result[np.where((Temp > 0) & (water > 0.01) & (melt_pest <= 0) & (grow_factor>0))]
    result_0[np.where((Temp > 0) & (water > 0.01) & (CN_0 > 0))] = 1
    result_1[np.where((result_0 == 1) & (melt_pest <= 0) & (grow_factor > 0))] = 1
    result_1[np.where((result_0 == 1) & (melt_pest <= 0) & (grow_factor <= 0))] = 2
    result_1[np.where((result_0 == 1) & (melt_pest > 0))] = 3
    A = CN_0 + (newcn_2 - CN_0) * (amc5 - 3.56) / 1.77
    result[np.where((result_1 == 1))] = A[np.where((result_1 == 1))]
    result[np.where((result_1 == 1) & (amc5 >= 5.33))] = newcn_2[np.where((result_1 == 1) & (amc5 >= 5.33))]
    A = (newcn_0 + (CN_0 - newcn_0) * amc5 / 3.56)
    result[np.where((result_1 == 1) & (amc5 < 3.56))] = A[np.where((result_1 == 1) & (amc5 < 3.56))]
    A = CN_0 + (newcn_2 - CN_0) * (amc5 - 1.27) / 1.52
    result[np.where(result_1 == 2)] = A[np.where(result_1 == 2)]
    result[np.where((result_1 == 2) & (amc5 >= 2.79))] = newcn_2[np.where((result_1 == 2) & (amc5 >= 2.79))]
    A = newcn_0 + (CN_0 - newcn_0) * amc5 / 1.27
    result[np.where((result_1 == 2) & (amc5 < 1.27))] = A[np.where((result_1 == 2) & (amc5 < 1.27))]
    result[result_1 == 3] = newcn_2[result_1 == 3]
    return result


# CNUM_2 is faster than CNUM_1. CNUM_1 is
# @time_function
@memoize
def CNum_2(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, CN, NRur, NUrb, Grow_0):
    melt_pest = Melt_1_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    newcn = NewCN_2(NRur, NUrb, CN)
    amc5 = AMC5_yesterday(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0)
    grow_factor = GrowFactor_2(Grow_0)
    water = Water_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    return CNum_inner(NYrs, DaysMonth, Temp, CN, NRur, melt_pest, newcn, amc5, grow_factor, water)
