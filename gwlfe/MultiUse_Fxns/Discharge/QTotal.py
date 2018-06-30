from numpy import where
from numpy import zeros

from gwlfe.Input.WaterBudget.Water import Water
from gwlfe.Input.WaterBudget.Water import Water_f
from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.Discharge.RuralQTotal import RuralQTotal
from gwlfe.MultiUse_Fxns.Discharge.RuralQTotal import RuralQTotal_f
# from Timer import time_function
from gwlfe.MultiUse_Fxns.Discharge.UrbanQTotal_1 import UrbanQTotal_1
from gwlfe.MultiUse_Fxns.Discharge.UrbanQTotal_1 import UrbanQTotal_1_f


@memoize
def QTotal(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
           ISRR, ISRA, CN):
    result = zeros((NYrs, 12, 31))
    urban_q_total_1 = UrbanQTotal_1(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                                    Grow_0, CNP_0, Imper, ISRR, ISRA)
    rural_q_total = RuralQTotal(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, CN, NUrb, AntMoist_0, Grow_0, Area)
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                # z.QTotal = 0
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    result[Y][i][j] = urban_q_total_1[Y][i][j] + rural_q_total[Y][i][j]
    return result


@memoize
def QTotal_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
             ISRR, ISRA, CN):
    result = zeros((NYrs, 12, 31))
    urban_q_total_1 = UrbanQTotal_1_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                                      Grow_0, CNP_0, Imper, ISRR, ISRA)
    rural_q_total = RuralQTotal_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, CN, NUrb, AntMoist_0, Grow_0, Area)
    water = Water_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    result[where((Temp > 0) & (water > 0))] = urban_q_total_1[where((Temp > 0) & (water > 0))] + rural_q_total[
        where((Temp > 0) & (water > 0))]

    return result
