from numpy import where
from numpy import zeros

from gwlfe.Input.WaterBudget.Water import Water
from gwlfe.Input.WaterBudget.Water import Water_f
from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.Discharge.AdjQTotal import AdjQTotal
from gwlfe.MultiUse_Fxns.Discharge.AdjQTotal import AdjQTotal_f
from gwlfe.MultiUse_Fxns.Discharge.QTotal import QTotal
from gwlfe.MultiUse_Fxns.Discharge.QTotal import QTotal_f


@memoize
def DayRunoff(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
              Imper, ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN):
    result = zeros((NYrs, 12, 31))
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    adj_q_total = AdjQTotal(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                            Imper, ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN)
    q_total = QTotal(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                     ISRR, ISRA, CN)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    if adj_q_total[Y][i][j] > 0:
                        result[Y][i][j] = adj_q_total[Y][i][j]
                    elif q_total[Y][i][j] > 0:
                        result[Y][i][j] = q_total[Y][i][j]
                    else:
                        result[Y][i][j] = 0
                else:
                    pass
    return result


@memoize
def DayRunoff_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                Imper, ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN):
    result = zeros((NYrs, 12, 31))
    water = Water_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    adj_q_total = AdjQTotal_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                              CNP_0,
                              Imper, ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN)
    q_total = QTotal_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                       Imper,
                       ISRR, ISRA, CN)
    result[where((Temp > 0) & (water > 0.01) & (adj_q_total > 0))] = adj_q_total[
        where((Temp > 0) & (water > 0) & (adj_q_total > 0))]
    result[where((Temp > 0) & (water > 0.01) & (q_total > 0))] = q_total[
        where((Temp > 0) & (water > 0) & (q_total > 0))]
    return result
