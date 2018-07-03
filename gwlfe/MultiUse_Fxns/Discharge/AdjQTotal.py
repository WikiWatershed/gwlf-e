from numpy import where
from numpy import zeros

from gwlfe.Input.WaterBudget.Water import Water
from gwlfe.Input.WaterBudget.Water import Water_f
from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.Discharge.AdjUrbanQTotal_1 import AdjUrbanQTotal_1
from gwlfe.MultiUse_Fxns.Discharge.AdjUrbanQTotal_1 import AdjUrbanQTotal_1_f
from gwlfe.MultiUse_Fxns.Discharge.RuralQTotal import RuralQTotal
from gwlfe.MultiUse_Fxns.Discharge.RuralQTotal import RuralQTotal_f


@memoize
def AdjQTotal(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
              ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN):
    result = zeros((NYrs, 12, 31))
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    adj_urban_q_total = AdjUrbanQTotal_1(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                                         Grow_0, CNP_0, Imper,
                                         ISRR, ISRA, Qretention, PctAreaInfil)
    rural_q_total = RuralQTotal(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, CN, NUrb, AntMoist_0, Grow_0, Area)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    # Assume 20% reduction of runoff with urban wetlands
                    result[Y][i][j] = (adj_urban_q_total[Y][i][j] * (1 - (n25b * 0.2))) + rural_q_total[Y][i][j]
    return result


@memoize
def AdjQTotal_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN):
    result = zeros((NYrs, 12, 31))
    water = Water_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    adj_urban_q_total = AdjUrbanQTotal_1_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                                           Grow_0, CNP_0, Imper, ISRR, ISRA, Qretention, PctAreaInfil)
    rural_q_total = RuralQTotal_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, CN, NUrb, AntMoist_0, Grow_0, Area)
    result[where((Temp > 0) & (water > 0.01))] = (adj_urban_q_total[where((Temp > 0) & (water > 0.01))] * (
                1 - (n25b * 0.2))) + rural_q_total[where((Temp > 0) & (water > 0.01))]
    return result
