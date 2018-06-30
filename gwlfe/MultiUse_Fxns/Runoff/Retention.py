from numpy import repeat
from numpy import tile
from numpy import where
from numpy import zeros

from gwlfe.Input.LandUse.NLU import NLU
from gwlfe.Input.WaterBudget.Water import Water, Water_f
from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.Runoff.CNum import CNum, CNum_f


@memoize
def Retention(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, NRur, NUrb, CN, Grow_0):
    nlu = NLU(NRur, NUrb)
    result = zeros((NYrs, 12, 31, nlu))  # Why nlu ?
    c_num = CNum(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, CN, NRur, NUrb, Grow_0)
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    for l in range(NRur):
                        if CN[l] > 0:  # TODO:CN is set to zero in datamodel
                            result[Y][i][j][l] = 2540 / c_num[Y][i][j][l] - 25.4
                            if result[Y][i][j][l] < 0:
                                result[Y][i][j][l] = 0
    return result


@memoize
def Retention_f(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, NRur, NUrb, CN, Grow_0):
    nlu = NLU(NRur, NUrb)
    result = zeros((NYrs, 12, 31, nlu))
    c_num = CNum_f(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, CN, NRur, NUrb, Grow_0)
    cnrur = tile(CN[:NRur][None, None, None, :], (NYrs, 12, 31, 1))
    water = repeat(Water_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec)[:, :, :, None], NRur, axis=3)
    TempE = repeat(Temp[:, :, :, None], NRur, axis=3)
    result[where((TempE > 0) & (water > 0.01) & (cnrur > 0))] = 2540 / c_num[
        where((TempE > 0) & (water > 0.01) & (cnrur > 0))] - 25.4
    result[where(result < 0)] = 0
    return result
