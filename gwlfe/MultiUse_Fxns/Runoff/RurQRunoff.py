from numpy import repeat
from numpy import reshape
from numpy import sum
from numpy import where
from numpy import zeros

from gwlfe.Input.LandUse.NLU import NLU
from gwlfe.Input.WaterBudget.Water import Water
from gwlfe.Input.WaterBudget.Water import Water_f
from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.Runoff.Qrun import Qrun
from gwlfe.MultiUse_Fxns.Runoff.Qrun import Qrun_f
from gwlfe.MultiUse_Fxns.Runoff.Retention import Retention
from gwlfe.MultiUse_Fxns.Runoff.Retention import Retention_f


@memoize
def RurQRunoff(NYrs, DaysMonth, InitSnow_0, Temp, Prec, AntMoist_0, NRur, NUrb, CN, Grow_0):
    result = zeros((NYrs, 16, 12))
    nlu = NLU(NRur, NUrb)
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    retention = Retention(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, NRur, NUrb, CN, Grow_0)
    qrun = Qrun(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, CN, AntMoist_0, Grow_0)
    for Y in range(NYrs):
        for i in range(12):
            for l in range(nlu):
                result[Y, l, i] = 0.0
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    for l in range(NRur):
                        if CN[l] > 0:
                            if water[Y][i][j] >= 0.2 * retention[Y][i][j][l]:
                                result[Y][l][i] += qrun[Y][i][j][l]
                            else:
                                pass
                        else:
                            pass
                else:
                    pass

    return result


@memoize
def RurQRunoff_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec, AntMoist_0, NRur, NUrb, CN, Grow_0):
    water = reshape(repeat(Water_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec), repeats=NRur, axis=2),
                    (NYrs, 12, 31, NRur))
    retention = Retention_f(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0, NRur, NUrb, CN, Grow_0)[:, :, :, :NRur]
    qrun = Qrun_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, CN, AntMoist_0, Grow_0)[:, :, :, :NRur]
    return sum(where((water >= 0.2 * retention) & (CN[:NRur] > 0), qrun, 0), axis=2)
