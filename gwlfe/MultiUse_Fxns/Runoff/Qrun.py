from numpy import repeat
from numpy import tile
from numpy import where
from numpy import zeros

from gwlfe.Input.LandUse.NLU import NLU
from gwlfe.Input.WaterBudget.Water import Water, Water_f
from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.Runoff.Retention import Retention, Retention_f


@memoize
def Qrun(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, CN, AntMoist_0, Grow_0):
    nlu = NLU(NRur, NUrb)
    result = zeros((NYrs, 12, 31, nlu))
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    retention = Retention(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, NRur, NUrb, CN, Grow_0)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    for l in range(NRur):
                        result[Y][i][j][l] = 0
                        if CN[l] > 0:
                            if water[Y][i][j] >= 0.2 * retention[Y][i][j][l]:
                                result[Y][i][j][l] = (water[Y][i][j] - 0.2 * retention[Y][i][j][l]) ** 2 / (
                                        water[Y][i][j] + 0.8 * retention[Y][i][j][l])
    return result


@memoize
def Qrun_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, CN, AntMoist_0, Grow_0):
    nlu = NLU(NRur, NUrb)
    result = zeros((NYrs, 12, 31, nlu))
    water = repeat(Water_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec)[:, :, :, None], nlu, axis=3)
    TempE = repeat(Temp[:, :, :, None], nlu, axis=3)
    cnrur = tile(CN[None, None, None, :], (NYrs, 12, 31, 1))
    retention = Retention_f(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, NRur, NUrb, CN, Grow_0)
    retention02 = 0.2 * retention
    nonzero = where((TempE > 0) & (water > 0.01) & (water >= retention02) & (cnrur > 0))
    result[nonzero] = (water[nonzero] - retention02[nonzero]) ** 2 / (water[nonzero] + 0.8 * retention[nonzero])
    return result
