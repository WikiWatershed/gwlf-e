import numpy as np
from Timer import time_function
from DailyArrayConverter import get_value_for_yesterday
from MeltPest import MeltPest
from NewCN import NewCN
from AMC5 import AMC5
from GrowFactor import GrowFactor
from Water import Water
from Melt import Melt


def CNum(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, CN, NRur, NUrb, Grow):
    result = np.zeros((NYrs, 12, 31, 10))
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    melt = Melt(NYrs, DaysMonth, Temp, InitSnow_0, Prec)
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


def CNum_2():
    pass
