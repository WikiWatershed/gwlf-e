from numpy import sum
from numpy import where
from numpy import zeros

from gwlfe.Input.LandUse.Ag.TileDrainRO import TileDrainRO
from gwlfe.Input.LandUse.Ag.TileDrainRO import TileDrainRO_f
from gwlfe.Input.WaterBudget.Water import Water
from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.Discharge.AdjQTotal import AdjQTotal
from gwlfe.MultiUse_Fxns.Discharge.AdjQTotal import AdjQTotal_f
from gwlfe.MultiUse_Fxns.Discharge.QTotal import QTotal
from gwlfe.MultiUse_Fxns.Discharge.QTotal import QTotal_f


def Runoff(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
           ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN, Landuse, TileDrainDensity):
    result = zeros((NYrs, 12))
    adj_q_total = AdjQTotal(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                            Imper,
                            ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN)
    q_total = QTotal(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                     ISRR, ISRA, CN)
    tile_drain_ro = TileDrainRO(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, CN, AntMoist_0, NUrb, Grow_0, Landuse,
                                Area,
                                TileDrainDensity)
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    if adj_q_total[Y][i][j] > 0:
                        result[Y][i] += adj_q_total[Y][i][j]
                    else:
                        result[Y][i] += q_total[Y][i][j]
                    # ADJUST THE SURFACE RUNOFF
            result[Y][i] = result[Y][i] - tile_drain_ro[Y][i]
            if result[Y][i] < 0:
                result[Y][i] = 0
    return result


@memoize
def Runoff_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
             ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN, Landuse, TileDrainDensity):
    adj_q_total = AdjQTotal_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                              CNP_0,
                              Imper,
                              ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN)
    q_total = QTotal_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                       Imper,
                       ISRR, ISRA, CN)
    tile_drain_ro = TileDrainRO_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, CN, AntMoist_0, NUrb, Grow_0, Landuse,
                                  Area,
                                  TileDrainDensity)
    result = where(adj_q_total > 0, adj_q_total, q_total)
    result = sum(result, axis=2) - tile_drain_ro
    result[result < 0] = 0
    return result
