from numpy import zeros

from AMC5 import AMC5, AMC5_yesterday
from CNI import CNI, CNI_f
from DailyArrayConverter import get_value_for_yesterday
from GrowFactor import GrowFactor
from Melt import Melt
from Melt_1 import Melt_1_f
from Memoization import memoize
# from Timer import time_function
from NLU import NLU
from Water import Water, Water_f

try:
    from CNumImperv_inner_compiled import CNumImperv_inner
except ImportError:
    print("Unable to import compiled CNumImper_f_inner, using slower version")
    from CNumImperv_inner import CNumImperv_inner


@memoize
def CNumImperv(NYrs, NRur, NUrb, DaysMonth, InitSnow_0, Temp, Prec, CNI_0, Grow_0, AntMoist_0):
    nlu = NLU(NRur, NUrb)
    result = zeros((NYrs, 12, 31, nlu))
    cni = CNI(NRur, NUrb, CNI_0)
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
                            if cni[1][l] > 0:
                                if melt[Y][i][j] <= 0:
                                    if grow_factor[i] > 0:
                                        # Growing season
                                        if get_value_for_yesterday(amc5, 0, Y, i, j, NYrs, DaysMonth) >= 5.33:
                                            result[Y][i][j][l] = cni[2][l]
                                        elif get_value_for_yesterday(amc5, 0, Y, i, j, NYrs, DaysMonth) < 3.56:
                                            result[Y][i][j][l] = cni[0][l] + (
                                                    cni[1][l] - cni[0][l]) * get_value_for_yesterday(amc5, 0, Y, i, j,
                                                                                                     NYrs, DaysMonth) / 3.56
                                        else:
                                            result[Y][i][j][l] = cni[1][l] + (cni[2][l] - cni[1][l]) * (
                                                    get_value_for_yesterday(amc5, 0, Y, i, j, NYrs, DaysMonth) - 3.56) / 1.77
                                    else:
                                        # Dormant season
                                        if get_value_for_yesterday(amc5, 0, Y, i, j, NYrs, DaysMonth) >= 2.79:
                                            result[Y][i][j][l] = cni[2][l]
                                        elif get_value_for_yesterday(amc5, 0, Y, i, j, NYrs, DaysMonth) < 1.27:
                                            result[Y][i][j][l] = cni[0][l] + (
                                                    cni[1][l] - cni[0][l]) * get_value_for_yesterday(amc5, 0, Y, i, j,
                                                                                                     NYrs, DaysMonth) / 1.27
                                        else:
                                            result[Y][i][j][l] = cni[1][l] + (cni[2][l] - cni[1][l]) * (
                                                    get_value_for_yesterday(amc5, 0, Y, i, j, NYrs, DaysMonth) - 1.27) / 1.52
                                else:
                                    result[Y][i][j][l] = cni[2][l]
    return result


def CNumImperv_f(NYrs, NRur, NUrb, DaysMonth, InitSnow_0, Temp, Prec, CNI_0, Grow_0, AntMoist_0):
    nlu = NLU(NRur, NUrb)
    cni = CNI_f(NRur, NUrb, CNI_0)
    water = Water_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    melt = Melt_1_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    grow_factor = GrowFactor(Grow_0)
    amc5 = AMC5_yesterday(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0)
    return CNumImperv_inner(NYrs, NRur, DaysMonth, Temp, nlu, cni, water, melt, grow_factor, amc5)
