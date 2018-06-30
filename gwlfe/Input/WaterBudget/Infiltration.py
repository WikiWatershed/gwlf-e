from numpy import where
from numpy import zeros

from gwlfe.Input.WaterBudget.Water import Water
from gwlfe.Input.WaterBudget.Water import Water_f
from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.Discharge.QTotal import QTotal
from gwlfe.MultiUse_Fxns.Discharge.QTotal import QTotal_f


@memoize
def Infiltration(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                 ISRR, ISRA, CN):
    result = zeros((NYrs, 12, 31))
    qtotal = QTotal(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                    ISRR, ISRA, CN)
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if qtotal[Y][i][j] <= water[Y][i][j]:
                    result[Y][i][j] = water[Y][i][j] - qtotal[Y][i][j]
    return result


@memoize
def Infiltration_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                   ISRR, ISRA, CN):
    result = zeros((NYrs, 12, 31))
    qtotal = QTotal_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                      Imper,
                      ISRR, ISRA, CN)
    water = Water_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    result[where(qtotal < water)] = water[where(qtotal < water)] - qtotal[where(qtotal < water)]
    return result
