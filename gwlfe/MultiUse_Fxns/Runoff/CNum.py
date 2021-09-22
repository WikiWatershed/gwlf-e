from numpy import zeros

from gwlfe.DailyArrayConverter import get_value_for_yesterday
from gwlfe.Input.WaterBudget.AMC5 import AMC5, AMC5_yesterday
from gwlfe.Input.WaterBudget.GrowFactor import GrowFactor
from gwlfe.Input.WaterBudget.GrowFactor import GrowFactor_f
from gwlfe.Input.WaterBudget.Melt import Melt
from gwlfe.Input.WaterBudget.Melt_1 import Melt_1_f
from gwlfe.Input.WaterBudget.Water import Water, Water_f
from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.Runoff.NewCN import NewCN, NewCN_f

try:
    from .CNum_inner_compiled import CNum_inner
except ImportError:
    print("Unable to import compiled CNum_inner, using slower version")
    from gwlfe.MultiUse_Fxns.Runoff.CNum_inner import CNum_inner


@memoize
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
    return result


# CNUM_f is faster than CNUM_1. CNUM_1 is
@memoize
def CNum_f(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, CN, NRur, NUrb, Grow_0):
    melt_pest = Melt_1_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    newcn = NewCN_f(NRur, NUrb, CN)
    amc5 = AMC5_yesterday(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0)
    grow_factor = GrowFactor_f(Grow_0)
    water = Water_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    return CNum_inner(NYrs, DaysMonth, Temp, CN, NRur, melt_pest, newcn, amc5, grow_factor, water)
