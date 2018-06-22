from numpy import zeros

from gwlfe.Input.WaterBudget.AMC5 import AMC5, AMC5_yesterday
# from Timer import time_function
from gwlfe.DailyArrayConverter import get_value_for_yesterday
from gwlfe.Input.WaterBudget.GrowFactor import GrowFactor
from gwlfe.Input.WaterBudget.GrowFactor import GrowFactor_f
from gwlfe.Input.WaterBudget.Melt import Melt
from gwlfe.Input.WaterBudget.Melt_1 import Melt_1_f
from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.Runoff.NewCN import NewCN, NewCN_f
from gwlfe.Input.WaterBudget.Water import Water, Water_f

try:
    from CNum_inner_xcompiled import CNum_inner
except ImportError:
    print("Unable to import compiled CNum_inner, using slower version")
    from gwlfe.MultiUse_Fxns.Runoff.CNum_inner import CNum_inner


@memoize
# @time_function
def CNum(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, CN, NRur, NUrb, Grow_0):
    result = zeros((NYrs, 12, 31, 10))
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
                                    if get_value_for_yesterday(amc5, 0, Y, i, j, DaysMonth) >= 5.33:
                                        result[Y][i][j][l] = new_cn[2][l]
                                    elif get_value_for_yesterday(amc5, 0, Y, i, j, DaysMonth) < 3.56:
                                        result[Y][i][j][l] = new_cn[0][l] + (
                                                CN[l] - new_cn[0][l]) * get_value_for_yesterday(amc5, 0, Y, i, j,
                                                                                                DaysMonth) / 3.56
                                    else:
                                        result[Y][i][j][l] = CN[l] + (new_cn[2][l] - CN[l]) * (
                                                get_value_for_yesterday(amc5, 0, Y, i, j, DaysMonth) - 3.56) / 1.77
                                else:
                                    # dormant season
                                    if get_value_for_yesterday(amc5, 0, Y, i, j, DaysMonth) >= 2.79:
                                        result[Y][i][j][l] = new_cn[2][l]
                                    elif get_value_for_yesterday(amc5, 0, Y, i, j, DaysMonth) < 1.27:
                                        result[Y][i][j][l] = new_cn[0][l] + (
                                                CN[l] - new_cn[0][l]) * get_value_for_yesterday(amc5, 0, Y, i, j,
                                                                                                DaysMonth) / 1.27
                                    else:
                                        result[Y][i][j][l] = CN[l] + (new_cn[2][l] - CN[l]) * (
                                                get_value_for_yesterday(amc5, 0, Y, i, j, DaysMonth) - 1.27) / 1.52
                            else:
                                result[Y][i][j][l] = new_cn[2][l]
                        # result[Y][i][j][l] = CNum
    return result




# CNUM_f is faster than CNUM_1. CNUM_1 is
# @time_function
@memoize
def CNum_f(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, CN, NRur, NUrb, Grow_0):
    melt_pest = Melt_1_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    newcn = NewCN_f(NRur, NUrb, CN)
    amc5 = AMC5_yesterday(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0)
    grow_factor = GrowFactor_f(Grow_0)
    water = Water_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    return CNum_inner(NYrs, DaysMonth, Temp, CN, NRur, melt_pest, newcn, amc5, grow_factor, water)

# # @time_function
# def CNum_1(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, CN, NRur, NUrb, Grow_0):
#     melt_pest = repeat(Melt_1_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec)[:, :, :, None], NRur, axis=3)
#     newcn = NewCN_f(NRur, NUrb, CN)
#     amc5 = repeat(AMC5_yesterday(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0)[:, :, :, None], NRur, axis=3)
#     # g = GrowFactor(Grow_0)
#     grow_factor = tile(GrowFactor(Grow_0)[None, :, None, None], (NYrs, 1, 31, NRur))
#     water = repeat(Water_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec)[:, :, :, None], NRur, axis=3)
#     Temp = repeat(Temp[:, :, :, None], NRur, axis=3)
#     CN_0 = tile(CN[:10][None, None, None, :], (NYrs, 12, 31, 1))
#     newcn_0 = tile(newcn[0, :10][None, None, None, :], (NYrs, 12, 31, 1))
#     newcn_f = tile(newcn[2, :10][None, None, None, :], (NYrs, 12, 31, 1))
#     result_0 = zeros((NYrs, 12, 31, NRur))
#     result_1 = zeros((NYrs, 12, 31, NRur))
#     result = zeros((NYrs, 12, 31, NRur))  # TODO: should we just generalize to NLU?
#     # result[np.where((Temp > 0) & (water > 0.01) & (melt_pest <= 0) & (grow_factor>0))]
#     result_0[where((Temp > 0) & (water > 0.01) & (CN_0 > 0))] = 1
#     result_1[where((result_0 == 1) & (melt_pest <= 0) & (grow_factor > 0))] = 1
#     result_1[where((result_0 == 1) & (melt_pest <= 0) & (grow_factor <= 0))] = 2
#     result_1[where((result_0 == 1) & (melt_pest > 0))] = 3
#     A = CN_0 + (newcn_f - CN_0) * (amc5 - 3.56) / 1.77
#     result[where((result_1 == 1))] = A[where((result_1 == 1))]
#     result[where((result_1 == 1) & (amc5 >= 5.33))] = newcn_f[where((result_1 == 1) & (amc5 >= 5.33))]
#     A = (newcn_0 + (CN_0 - newcn_0) * amc5 / 3.56)
#     result[where((result_1 == 1) & (amc5 < 3.56))] = A[where((result_1 == 1) & (amc5 < 3.56))]
#     A = CN_0 + (newcn_f - CN_0) * (amc5 - 1.27) / 1.52
#     result[where(result_1 == 2)] = A[where(result_1 == 2)]
#     result[where((result_1 == 2) & (amc5 >= 2.79))] = newcn_f[where((result_1 == 2) & (amc5 >= 2.79))]
#     A = newcn_0 + (CN_0 - newcn_0) * amc5 / 1.27
#     result[where((result_1 == 2) & (amc5 < 1.27))] = A[where((result_1 == 2) & (amc5 < 1.27))]
#     result[result_1 == 3] = newcn_f[result_1 == 3]
#     return result
