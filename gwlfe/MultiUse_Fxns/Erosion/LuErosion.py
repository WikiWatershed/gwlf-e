from numpy import sum
from numpy import zeros

from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.Erosion.ErosWashoff import ErosWashoff
from gwlfe.MultiUse_Fxns.Erosion.ErosWashoff import ErosWashoff_f


def LuErosion(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, Acoef, KF, LS,
              C, P, Area):
    result = zeros((NYrs, 10))
    eros_washoff = ErosWashoff(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, Acoef, KF, LS,
                               C, P, Area)
    for Y in range(NYrs):
        for i in range(12):
            for l in range(NRur):
                result[Y][l] += eros_washoff[Y][l][i]
    return result


@memoize
def LuErosion_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, Acoef, KF, LS,
                C, P, Area):
    return sum(ErosWashoff_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, Acoef, KF, LS,
                             C, P, Area), axis=1)
