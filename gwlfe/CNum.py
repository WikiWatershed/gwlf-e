import numpy as np
from Timer import time_function
from DailyArrayConverter import get_value_for_yesterday
from MeltPest import MeltPest
from NewCN import NewCN, NewCN_2
from AMC5 import AMC5, AMC5_1, AMC5_3
from GrowFactor import GrowFactor
from Water import Water, Water_2
from Melt import  Melt
from Melt_1 import Melt_1_2
from numba import jit

# @time_function
def CNum(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, CN, NRur, NUrb, Grow):
    result = np.zeros((NYrs, 12, 31, 10))
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    melt = Melt(NYrs, DaysMonth, Temp, InitSnow_0, Prec) # I think this should be Melt_1
    grow_factor = GrowFactor(Grow)
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

def signfunc( array, i, j, k, x, y, z):
    a = 0.5 * (x+z)
    b = 0.5 * (y-x)
    c = 0.5 * (z-y)
    return a * np.sign(array - i) + b * np.sign(array - j) + c * np.sign(array - k)

# @time_function
def CNum_2(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, CN, NRur, NUrb, Grow):
    melt_pest = np.repeat(Melt_1_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec)[:,:,:,None],NRur, axis=3 )
    newcn = NewCN_2(NRur, NUrb, CN)
    amc5 = np.repeat(AMC5_3(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0)[:,:,:,None], NRur,axis=3)
    g = GrowFactor(Grow)
    grow_factor = np.tile(GrowFactor(Grow)[None,:,None,None], (NYrs , 1, 31, NRur))
    water = np.repeat(Water_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec)[:,:,:,None],NRur, axis=3 )
    Temp = np.repeat(Temp[:,:,:, None], NRur, axis=3)
    CN_0 = np.tile(CN[:10][None,None,None,:], (NYrs , 12, 31, 1))
    newcn_0 = np.tile(newcn[0, :10][None,None,None,:], (NYrs , 12, 31, 1))
    newcn_2 = np.tile(newcn[2, :10][None,None,None,:], (NYrs , 12, 31, 1))
    result_0 = np.zeros((NYrs, 12, 31, NRur))
    result_1 = np.zeros((NYrs, 12, 31, NRur))

    # result_2 = np.zeros((NYrs, 12, 31, NRur))
    # result_3 = np.zeros((NYrs, 12, 31, NRur))
    result = np.zeros((NYrs, 12, 31, NRur))  # TODO: should we just generalize to NLU?
    # result[np.where((Temp > 0) & (water > 0.01) & (melt_pest <= 0) & (grow_factor>0))]
    result_0[np.where((Temp > 0) & (water> 0.01) & (CN_0>0 ))] = 1
    result_1[np.where((result_0 == 1) & (melt_pest <= 0) & (grow_factor > 0 )) ] = 1
    result_1[np.where((result_0 == 1) & (melt_pest <= 0) & (grow_factor <= 0))] = 2
    result_1[np.where((result_0 == 1) & (melt_pest > 0))] = 3
    # temp = signfunc(amc5, 0, 3.56-10e-8, 5.33-10e-8, newcn_0 + (CN_0 -newcn_0) * amc5/3.56 ,
    #                                                 CN_0 + (newcn_2 - CN_0) * (amc5 - 3.56) / 1.77,
    #                                                 newcn_2)

    # result =  np.where(result_1 ==1 , 1, 0) * temp
    # temp = signfunc(amc5, 0, 1.27 - 10e-8, 2.79 - 10e-8,newcn_0 + (CN_0 - newcn_0) * amc5 / 1.27 ,
    #                                                     CN_0 + (newcn_2 - CN_0) * (amc5 - 1.27) / 1.52,
    #                                                     newcn_2)
    # result = np.where(result_1 ==2, 1, 0) * temp
    # result[np.where(result_1 == 3)] = newcn_2[np.where(result_1 == 3)]
    A = CN_0 + (newcn_2 - CN_0) * (amc5 - 3.56) / 1.77
    result[np.where((result_1 == 1))] = A[np.where((result_1 == 1))]
    result[np.where((result_1 == 1) & (amc5 >= 5.33))] = newcn_2[np.where((result_1 == 1) & (amc5 >= 5.33))]
    A = (newcn_0 + (CN_0 - newcn_0) * amc5 / 3.56)
    result[np.where((result_1 == 1) & (amc5 < 3.56))] = A[np.where((result_1 == 1) & (amc5 < 3.56))]
    A = CN_0+ (newcn_2 - CN_0) * (amc5 - 1.27) / 1.52
    result[np.where(result_1 == 2)] = A[np.where(result_1 == 2)]
    result[np.where((result_1 == 2) & (amc5 >= 2.79))] = newcn_2[np.where((result_1 == 2) & (amc5 >= 2.79))]
    A = newcn_0 + (CN_0 - newcn_0) * amc5 / 1.27
    result[np.where((result_1 == 2) & (amc5 < 1.27))] = A[np.where((result_1 == 2) & (amc5 < 1.27))]
    result[result_1==3] = newcn_2[result_1==3]
    return result


# @time_function
@jit(cache = True, nopython = True)

def CNum_1(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, CN, NRur, NUrb, Grow):
    melt_pest = Melt_1_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    newcn = NewCN_2(NRur, NUrb, CN)
    amc5 = AMC5_3(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0)
    grow_factor = GrowFactor(Grow)
    water = Water_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    result = np.zeros((NYrs, 12, 31, NRur))  # TODO: should we just generalize to NLU?

    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:  # forgot this
                    for l in range(NRur):
                        if CN[l] > 0:
                            if melt_pest[Y][i][j] <= 0:
                                if grow_factor[i] > 0:
                                    # growing season
                                    if amc5[Y][i][j] >= 5.33:  # forgot "get value from yesterday"
                                        result[Y][i][j][l] = newcn[2][l]
                                    elif amc5[Y][i][j] < 3.56:
                                        result[Y][i][j][l] = newcn[0][l] + (
                                                    CN[l] - newcn[0][l]) * amc5[Y][i][j] / 3.56
                                    else:
                                        result[Y][i][j][l] = CN[l] + (newcn[2][l] - CN[l]) * (
                                                amc5[Y][i][j] - 3.56) / 1.77
                                else:
                                    # dormant season
                                    if amc5[Y][i][j] >= 2.79:
                                        result[Y][i][j][l] = newcn[2][l]
                                    elif amc5[Y][i][j] < 1.27:
                                        result[Y][i][j][l] = newcn[0][l] + (
                                                    CN[l] - newcn[0][l]) * amc5[Y][i][j] / 1.27
                                    else:
                                        result[Y][i][j][l] = CN[l] + (newcn[2][l] - CN[l]) * (
                                                amc5[Y][i][j] - 1.27) / 1.52
                            else:
                                result[Y][i][j][l] = newcn[2][l]
    return result
