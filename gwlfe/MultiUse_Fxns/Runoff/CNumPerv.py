from numpy import zeros

from gwlfe.DailyArrayConverter import get_value_for_yesterday
from gwlfe.Input.LandUse.NLU import NLU
from gwlfe.Input.WaterBudget.AMC5 import AMC5, AMC5_yesterday
from gwlfe.Input.WaterBudget.GrowFactor import GrowFactor
from gwlfe.Input.WaterBudget.Melt import Melt
from gwlfe.Input.WaterBudget.Melt_1 import Melt_1_f
from gwlfe.Input.WaterBudget.Water import Water, Water_f
from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.Runoff.CNP import CNP, CNP_f

try:
    from .CNumPerv_inner_compiled import CNumPerv_inner
except ImportError:
    print("Unable to import compiled CNumPerv_f_inner, using slower version")
    from gwlfe.MultiUse_Fxns.Runoff.CNumPerv_inner import CNumPerv_inner


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
                                                                 get_value_for_yesterday(amc5, 0, Y, i, j,
                                                                                         DaysMonth) / 3.56
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
                                                                 get_value_for_yesterday(amc5, 0, Y, i, j,
                                                                                         DaysMonth) / 1.27
                                        else:
                                            result[Y][i][j][l] = cnp[1][l] + (cnp[2][l] - cnp[1][l]) * (
                                                    get_value_for_yesterday(amc5, 0, Y, i, j, DaysMonth) - 1.27) / 1.52
                                else:
                                    result[Y][i][j][l] = cnp[2][l]
    return result


def CNumPerv_f(NYrs, DaysMonth, Temp, NRur, NUrb, CNP_0, InitSnow_0, Prec, Grow_0, AntMoist_0):
    nlu = NLU(NRur, NUrb)
    cnp = CNP_f(NRur, NUrb, CNP_0)
    water = Water_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    melt = Melt_1_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    grow_factor = GrowFactor(Grow_0)  # TODO: some bug in cnumperv_inner causes an error if this is switched to _f
    amc5 = AMC5_yesterday(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0)
    return CNumPerv_inner(NYrs, DaysMonth, Temp, NRur, nlu, cnp, water, melt, grow_factor, amc5)
