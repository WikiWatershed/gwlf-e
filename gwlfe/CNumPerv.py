import numpy as np
from Timer import time_function
from DailyArrayConverter import get_value_for_yesterday
from NLU import NLU
from Water import Water, Water_2
from CNP import CNP, CNP_2
from Melt import Melt, Melt_2
from Melt_1 import Melt_1_2
from GrowFactor import GrowFactor
from AMC5 import AMC5, AMC5_yesterday
from numba import jit
from Memoization import memoize
from numba.pycc import CC
from CompiledFunction import compiled


cc = CC('gwlfe_compiled')
@memoize
def CNumPerv(NYrs, DaysMonth, Temp, NRur, NUrb, CNP_0, InitSnow_0, Prec, Grow, AntMoist_0):
    nlu = NLU(NRur, NUrb)
    result = np.zeros((NYrs, 12, 31, nlu))
    cnp = CNP(NRur, NUrb, CNP_0)
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    melt = Melt(NYrs, DaysMonth, Temp, InitSnow_0, Prec)
    grow_factor = GrowFactor(Grow)
    amc5 = AMC5(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0)

    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    if water[Y][i][j] < 0.05:
                        pass
                    else:
                        for l in range(NRur, nlu):
                            if cnp[1][l] > 0:
                                if melt[Y][i][j] <= 0:
                                    if grow_factor[i] > 0:
                                        # Growing season
                                        if get_value_for_yesterday(amc5, 0, Y, i, j, NYrs, DaysMonth) >= 5.33:
                                            result[Y][i][j][l] = cnp[2][l]
                                        elif get_value_for_yesterday(amc5, 0, Y, i, j, NYrs, DaysMonth) < 3.56:
                                            result[Y][i][j][l] = cnp[0][l] + (
                                                    cnp[1][l] - cnp[0][l]) * \
                                                                 get_value_for_yesterday(amc5, 0, Y, i, j, NYrs,
                                                                                         DaysMonth) / 3.56
                                        else:
                                            result[Y][i][j][l] = cnp[1][l] + (cnp[2][l] - cnp[1][l]) * (
                                                    get_value_for_yesterday(amc5, 0, Y, i, j, NYrs,
                                                                            DaysMonth) - 3.56) / 1.77
                                    else:
                                        # Dormant season
                                        if get_value_for_yesterday(amc5, 0, Y, i, j, NYrs, DaysMonth) >= 2.79:
                                            result[Y][i][j][l] = cnp[2][l]
                                        elif get_value_for_yesterday(amc5, 0, Y, i, j, NYrs, DaysMonth) < 1.27:
                                            result[Y][i][j][l] = cnp[0][l] + (
                                                    cnp[1][l] - cnp[0][l]) * \
                                                                 get_value_for_yesterday(amc5, 0, Y, i, j, NYrs,
                                                                                         DaysMonth) / 1.27
                                        else:
                                            result[Y][i][j][l] = cnp[1][l] + (cnp[2][l] - cnp[1][l]) * (
                                                    get_value_for_yesterday(amc5, 0, Y, i, j, NYrs,
                                                                            DaysMonth) - 1.27) / 1.52
                                else:
                                    result[Y][i][j][l] = cnp[2][l]
    return result


# --- LINE 69 ---
#   NYrs = arg(0, name=NYrs)  :: int64
#   DaysMonth = arg(1, name=DaysMonth)  :: array(int64, 2d, C)
#   Temp = arg(2, name=Temp)  :: array(float64, 3d, C)
#   NRur = arg(3, name=NRur)  :: int64
#   nlu = arg(4, name=nlu)  :: int64
#   cnp = arg(5, name=cnp)  :: array(float64, 2d, C)
#   water = arg(6, name=water)  :: array(float64, 3d, C)
#   melt = arg(7, name=melt)  :: array(float64, 3d, C)
#   grow_factor = arg(8, name=grow_factor)  :: array(float64, 1d, C)
#   amc5 = arg(9, name=amc5)  :: array(float64, 3d, C)
#   $0.1 = global(np: <module 'numpy' from '/Users/bs643/anaconda3/envs/gwlfeEnv/lib/python2.7/site-packages/numpy/__init__.pyc'>)  :: Module(<module 'numpy' from '/Users/bs643/anaconda3/envs/gwlfeEnv/lib/python2.7/site-packages/numpy/__init__.pyc'>)
#   $0.2 = getattr(attr=zeros, value=$0.1)  :: Function(<built-in function zeros>)
#   $const0.4 = const(int, 12)  :: int64
#   $const0.5 = const(int, 31)  :: int64
#   $0.7 = build_tuple(items=[Var(NYrs, /Users/bs643/Documents/ANS/gwlfe_develop/gwlf-e/gwlfe/CNumPerv.py (69)), Var($const0.4, /Users/bs643/Documents/ANS/gwlfe_develop/gwlf-e/gwlfe/CNumPerv.py (69)), Var($const0.5, /Users/bs643/Documents/ANS/gwlfe_develop/gwlf-e/gwlfe/CNumPerv.py (69)), Var(nlu, /Users/bs643/Documents/ANS/gwlfe_develop/gwlf-e/gwlfe/CNumPerv.py (69))])  :: (int64 x 4)
#   $0.8 = call $0.2($0.7, kws=[], args=[Var($0.7, /Users/bs643/Documents/ANS/gwlfe_develop/gwlf-e/gwlfe/CNumPerv.py (69))], func=$0.2, vararg=None)  :: ((int64 x 4),) -> array(float64, 4d, C)
#   result = $0.8  :: array(float64, 4d, C)

# @time_function
# @jit(cache = True, nopython = True)
@compiled
@cc.export('CNumImperv_2_inner', '(int64, int64[:,::1], float64[:,:,::1], int64, int64, float64[:,::1], float64[:,:,::1], float64[:,:,::1], float64[::1], float64[:,:,::1])')
def CNumPerv_2_inner(NYrs, DaysMonth, Temp, NRur, nlu, cnp, water, melt, grow_factor, amc5):
    result = np.zeros((NYrs, 12, 31, nlu))
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    if water[Y][i][j] < 0.05:
                        pass
                    else:
                        for l in range(NRur, nlu):
                            if cnp[1][l] > 0:
                                if melt[Y][i][j] <= 0:
                                    if grow_factor[i] > 0:
                                        # Growing season
                                        if amc5[Y][i][j] >= 5.33:
                                            result[Y][i][j][l] = cnp[2][l]
                                        elif amc5[Y][i][j] < 3.56:
                                            result[Y][i][j][l] = cnp[0][l] + (
                                                    cnp[1][l] - cnp[0][l]) * amc5[Y][i][j] / 3.56
                                        else:
                                            result[Y][i][j][l] = cnp[1][l] + (cnp[2][l] - cnp[1][l]) * (
                                                    amc5[Y][i][j] - 3.56) / 1.77
                                    else:
                                        # Dormant season
                                        if amc5[Y][i][j] >= 2.79:
                                            result[Y][i][j][l] = cnp[2][l]
                                        elif amc5[Y][i][j] < 1.27:
                                            result[Y][i][j][l] = cnp[0][l] + (
                                                    cnp[1][l] - cnp[0][l]) * amc5[Y][i][j] / 1.27
                                        else:
                                            result[Y][i][j][l] = cnp[1][l] + (cnp[2][l] - cnp[1][l]) * (
                                                    amc5[Y][i][j] - 1.27) / 1.52
                                else:
                                    result[Y][i][j][l] = cnp[2][l]
    return result


def CNumPerv_2(NYrs, DaysMonth, Temp, NRur, NUrb, CNP_0, InitSnow_0, Prec, Grow, AntMoist_0):
    # cc.compile()
    nlu = NLU(NRur, NUrb)
    cnp = CNP_2(NRur, NUrb, CNP_0)
    water = Water_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    melt = Melt_1_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    grow_factor = GrowFactor(Grow)
    amc5 = AMC5_yesterday(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0)
    # print(CNumPerv_2_inner.inspect_types())
    return CNumPerv_2_inner(NYrs, DaysMonth, Temp, NRur, nlu, cnp, water, melt, grow_factor, amc5)


# def CNumPerv_3(NYrs, DaysMonth, Temp, NRur, NUrb, CNP_0, InitSnow_0, Prec, Grow, AntMoist_0):
#     nlu = NLU(NRur, NUrb)
#     result = np.zeros((NYrs, 12, 31, 16))
#     landuse = np.zeros((16,))
#     cnp = CNP_2(NRur, NUrb, CNP_0)
#     water = Water_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
#     melt = Melt_1_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
#     grow_factor = GrowFactor(Grow)
#     amc5 = AMC5_yesterday(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0)
#
#     non_zero = result[(Temp > 0) & (water > 0.05)]
#
#     if amc5[Y][i][j] >= 5.33:
#         landuse[cnp[1] > 0] = cnp[2][l]
#     elif amc5[Y][i][j] < 3.56:
#         landuse[cnp[1] > 0] = cnp[0][l] + (
#                 cnp[1][l] - cnp[0][l]) * amc5[Y][i][j] / 3.56
#     else:
#         result[Y][i][j][l] = cnp[1][l] + (cnp[2][l] - cnp[1][l]) * (
#                 amc5[Y][i][j] - 3.56) / 1.77
#
#     # =
#     print(non_zero.shape)
#
#     temp = np.where(melt <= 0, 2, cnp[2])
