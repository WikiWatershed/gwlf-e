from numpy import repeat
from numpy import where
from numpy import zeros

from gwlfe.Input.WaterBudget.Water import Water
from gwlfe.Input.WaterBudget.Water import Water_f
from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.Erosion.Erosiv import Erosiv
from gwlfe.MultiUse_Fxns.Erosion.Erosiv import Erosiv_f


@memoize
def RurEros(NYrs, DaysMonth, Temp, InitSnow_0, Prec, Acoef, NRur, KF, LS, C, P, Area):
    result = zeros((NYrs, 12, 31, NRur))
    erosiv = Erosiv(NYrs, DaysMonth, Temp, InitSnow_0, Prec, Acoef)
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    for l in range(NRur):
                        result[Y][i][j][l] = 1.32 * erosiv[Y][i][j] * KF[l] * LS[l] * C[l] * P[l] * Area[l]
    return result


@memoize
def RurEros_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, Acoef, NRur, KF, LS, C, P, Area):
    erosiv = repeat(Erosiv_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, Acoef)[:, :, :, None], NRur, axis=3)
    water = Water_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    water = water[:, :, :, None]
    resized_temp = repeat(Temp[:, :, :, None], NRur, axis=3)
    water_r = repeat(water, NRur, axis=3)
    temp = KF * LS * C * P * Area
    return where((resized_temp > 0) & (water_r > 0.01), 1.32 * erosiv * temp[:NRur], 0.)
