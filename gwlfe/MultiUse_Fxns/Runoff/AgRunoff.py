from numpy import sum
from numpy import where
from numpy import zeros

from gwlfe.Input.WaterBudget.Water import Water
from gwlfe.Input.WaterBudget.Water import Water_f
from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.Discharge.AgQTotal import AgQTotal
from gwlfe.MultiUse_Fxns.Discharge.AgQTotal import AgQTotal_f


@memoize
def AgRunoff(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, CN, AntMoist_0, NUrb, Grow_0, Landuse, Area):
    result = zeros((NYrs, 12))
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    ag_q_total = AgQTotal(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, CN, AntMoist_0, NUrb, Grow_0, Landuse, Area)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    result[Y][i] += ag_q_total[Y][i][j]
    return result


@memoize
def AgRunoff_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, CN, AntMoist_0, NUrb, Grow_0, Landuse, Area):
    result = zeros((NYrs, 12, 31))
    water = Water_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    ag_q_total = AgQTotal_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, CN, AntMoist_0, NUrb, Grow_0, Landuse, Area)
    result[where((Temp > 0) & (water > 0.01))] = ag_q_total[where((Temp > 0) & (water > 0.01))]
    return sum(result, axis=2)
