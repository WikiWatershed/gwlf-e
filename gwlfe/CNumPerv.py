from numpy import zeros

from AMC5 import AMC5, AMC5_yesterday
from CNP import CNP, CNP_2
# from Timer import time_function
from DailyArrayConverter import get_value_for_yesterday
from GrowFactor import GrowFactor
from Melt import Melt
from Melt_1 import Melt_1_2
from Memoization import memoize
from NLU import NLU
from Water import Water, Water_2

try:
    from CNumPerv_2_inner_compiled import CNumPerv_2_inner
except ImportError:
    print("Unable to import compiled CNumPerv_2_inner, using slower version")
    from CNumPerv_2_inner import CNumPerv_2_inner


@memoize
def CNumPerv(NYrs, DaysMonth, Temp, NRur, NUrb, CNP_0, InitSnow_0, Prec, Grow_0, AntMoist_0):
    nlu = NLU(NRur, NUrb)
    result = zeros((NYrs, 12, 31, nlu))
    cnp = CNP(NRur, NUrb, CNP_0)
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    melt = Melt(NYrs, DaysMonth, Temp, InitSnow_0, Prec)
    grow_factor = GrowFactor(Grow_0)
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
                                        if get_value_for_yesterday(amc5, 0, Y, i, j, DaysMonth) >= 5.33:
                                            result[Y][i][j][l] = cnp[2][l]
                                        elif get_value_for_yesterday(amc5, 0, Y, i, j, DaysMonth) < 3.56:
                                            result[Y][i][j][l] = cnp[0][l] + (
                                                    cnp[1][l] - cnp[0][l]) * \
                                                                 get_value_for_yesterday(amc5, 0, Y, i, j, DaysMonth) / 3.56
                                        else:
                                            result[Y][i][j][l] = cnp[1][l] + (cnp[2][l] - cnp[1][l]) * (
                                                    get_value_for_yesterday(amc5, 0, Y, i, j, DaysMonth) - 3.56) / 1.77
                                    else:
                                        # Dormant season
                                        if get_value_for_yesterday(amc5, 0, Y, i, j, DaysMonth) >= 2.79:
                                            result[Y][i][j][l] = cnp[2][l]
                                        elif get_value_for_yesterday(amc5, 0, Y, i, j, DaysMonth) < 1.27:
                                            result[Y][i][j][l] = cnp[0][l] + (
                                                    cnp[1][l] - cnp[0][l]) * \
                                                                 get_value_for_yesterday(amc5, 0, Y, i, j, DaysMonth) / 1.27
                                        else:
                                            result[Y][i][j][l] = cnp[1][l] + (cnp[2][l] - cnp[1][l]) * (
                                                    get_value_for_yesterday(amc5, 0, Y, i, j, DaysMonth) - 1.27) / 1.52
                                else:
                                    result[Y][i][j][l] = cnp[2][l]
    return result


def CNumPerv_2(NYrs, DaysMonth, Temp, NRur, NUrb, CNP_0, InitSnow_0, Prec, Grow_0, AntMoist_0):
    nlu = NLU(NRur, NUrb)
    cnp = CNP_2(NRur, NUrb, CNP_0)
    water = Water_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    melt = Melt_1_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    grow_factor = GrowFactor(Grow_0)
    amc5 = AMC5_yesterday(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0)
    return CNumPerv_2_inner(NYrs, DaysMonth, Temp, NRur, nlu, cnp, water, melt, grow_factor, amc5)

# def CNumPerv_3(NYrs, DaysMonth, Temp, NRur, NUrb, CNP_0, InitSnow_0, Prec, Grow_0, AntMoist_0):
#     nlu = NLU(NRur, NUrb)
#     result = np.zeros((NYrs, 12, 31, 16))
#     landuse = np.zeros((16,))
#     cnp = CNP_2(NRur, NUrb, CNP_0)
#     water = Water_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
#     melt = Melt_1_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
#     grow_factor = GrowFactor(Grow_0)
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
