import math

from numpy import exp
from numpy import zeros

from gwlfe.Input.LandUse.NLU import NLU
from gwlfe.Input.WaterBudget.Water import Water
from gwlfe.Input.WaterBudget.Water import Water_f
from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.Runoff.QrunI import QrunI
from gwlfe.MultiUse_Fxns.Runoff.QrunI import QrunI_f

try:
    from .WashImperv_inner_compiled import WashImperv_inner
except ImportError:
    print("Unable to import compiled WashPerv_inner, using slower version")
    from gwlfe.MultiUse_Fxns.Runoff.WashImperv_inner import WashImperv_inner


@memoize
def WashImperv(NYrs, DaysMonth, InitSnow_0, Temp, Prec, CNI_0, AntMoist_0, Grow_0, NRur, NUrb):
    result = zeros((NYrs, 12, 31, 16))
    impervaccum = zeros(16)
    carryover = zeros(16)
    nlu = NLU(NRur, NUrb)
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    qruni = QrunI(NYrs, DaysMonth, NRur, NUrb, Temp, InitSnow_0, Prec, CNI_0, AntMoist_0, Grow_0)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                for l in range(nlu):
                    impervaccum[l] = carryover[l]
                    impervaccum[l] = (impervaccum[l] * exp(-0.12) + (1 / 0.12) * (1 - exp(-0.12)))
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    if water[Y][i][j] < 0.05:
                        pass
                    else:
                        for l in range(NRur, nlu):
                            result[Y][i][j][l] = (1 - math.exp(-1.81 * qruni[Y][i][j][l])) * impervaccum[l]
                            impervaccum[l] -= result[Y][i][j][l]
                else:
                    pass
                for l in range(nlu):
                    carryover[l] = impervaccum[l]
    return result


@memoize
def WashImperv_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec, CNI_0, AntMoist_0, Grow_0, NRur, NUrb):
    nlu = NLU(NRur, NUrb)
    water = Water_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    qruni = QrunI_f(NYrs, DaysMonth, NRur, NUrb, Temp, InitSnow_0, Prec, CNI_0, AntMoist_0, Grow_0)
    return WashImperv_inner(NYrs, DaysMonth, Temp, NRur, nlu, water, qruni)
