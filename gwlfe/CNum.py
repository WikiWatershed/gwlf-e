import numpy as np
from Timer import time_function
from DailyArrayConverter import get_value_for_yesterday
from MeltPest import MeltPest
from NewCN import NewCN
from AMC5 import AMC5
from GrowFactor import GrowFactor
from Water import Water


def CNum(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, CN, NRur, NUrb, Grow):
    melt_pest = MeltPest(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    newcn = NewCN(NRur, NUrb, CN)
    amc5 = AMC5(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0)
    grow_factor = GrowFactor(Grow)
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
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
                                    if get_value_for_yesterday(amc5, 0, Y, i, j, NYrs,
                                                               DaysMonth) >= 5.33:  # forgot "get value from yesterday"
                                        result[Y][i][j][l] = newcn[2][l]
                                    elif get_value_for_yesterday(amc5, 0, Y, i, j, NYrs, DaysMonth) < 3.56:
                                        result[Y][i][j][l] = newcn[0][l] + (
                                                    CN[l] - newcn[0][l]) * get_value_for_yesterday(amc5, 0, Y, i, j,
                                                                                                   NYrs,
                                                                                                   DaysMonth) / 3.56
                                    else:
                                        result[Y][i][j][l] = CN[l] + (newcn[2][l] - CN[l]) * (
                                                    get_value_for_yesterday(amc5, 0, Y, i, j, NYrs,
                                                                            DaysMonth) - 3.56) / 1.77
                                else:
                                    # dormant season
                                    if get_value_for_yesterday(amc5, 0, Y, i, j, NYrs, DaysMonth) >= 2.79:
                                        result[Y][i][j][l] = newcn[2][l]
                                    elif get_value_for_yesterday(amc5, 0, Y, i, j, NYrs, DaysMonth) < 1.27:
                                        result[Y][i][j][l] = newcn[0][l] + (
                                                    CN[l] - newcn[0][l]) * get_value_for_yesterday(amc5, 0, Y, i, j,
                                                                                                   NYrs,
                                                                                                   DaysMonth) / 1.27
                                    else:
                                        result[Y][i][j][l] = CN[l] + (newcn[2][l] - CN[l]) * (
                                                    get_value_for_yesterday(amc5, 0, Y, i, j, NYrs,
                                                                            DaysMonth) - 1.27) / 1.52
                            else:
                                result[Y][i][j][l] = newcn[2][l]
    return result


def CNum_2():
    pass
