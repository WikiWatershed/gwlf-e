from numpy import sum
from numpy import zeros

from gwlfe.Input.LandUse.NLU import NLU
from gwlfe.Input.WaterBudget.Water import Water
from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.Erosion.RurEros import RurEros
from gwlfe.MultiUse_Fxns.Erosion.RurEros import RurEros_f


@memoize
def ErosWashoff(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, Acoef, KF, LS, C, P, Area):
    result = zeros((NYrs, 16, 12))
    nlu = NLU(NRur, NUrb)
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    rureros = RurEros(NYrs, DaysMonth, Temp, InitSnow_0, Prec, Acoef, NRur, KF, LS, C, P, Area)
    for Y in range(NYrs):
        for i in range(12):
            for l in range(nlu):
                result[Y, l, i] = 0
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    for l in range(NRur):
                        result[Y][l][i] = result[Y][l][i] + rureros[Y][i][j][l]
                else:
                    pass
    return result


@memoize
def ErosWashoff_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, Acoef, KF, LS, C, P, Area):
    return sum(RurEros_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, Acoef, NRur, KF, LS, C, P, Area), axis=2)
