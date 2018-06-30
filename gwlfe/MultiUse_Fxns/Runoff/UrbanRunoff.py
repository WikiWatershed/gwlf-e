from numpy import sum
from numpy import zeros

from gwlfe.Input.WaterBudget.Water import Water
from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.Discharge.UrbanQTotal_1 import UrbanQTotal_1
from gwlfe.MultiUse_Fxns.Discharge.UrbanQTotal_1 import UrbanQTotal_1_f


@memoize
def UrbanRunoff(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                ISRR, ISRA):
    result = zeros((NYrs, 12))
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    urbanqtotal_1 = UrbanQTotal_1(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                                  CNP_0, Imper,
                                  ISRR, ISRA)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    result[Y][i] += urbanqtotal_1[Y][i][j]
                else:
                    pass
    return result


def UrbanRunoff_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                  CNP_0, Imper, ISRR, ISRA):
    return sum(UrbanQTotal_1_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                               CNP_0, Imper, ISRR, ISRA), axis=2)
