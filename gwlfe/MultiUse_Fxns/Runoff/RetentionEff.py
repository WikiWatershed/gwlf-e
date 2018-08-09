from numpy import where
from numpy import zeros

from gwlfe.Input.WaterBudget.Water import Water
from gwlfe.Input.WaterBudget.Water import Water_f
from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.Discharge.UrbanQTotal import UrbanQTotal
from gwlfe.MultiUse_Fxns.Discharge.UrbanQTotal import UrbanQTotal_f


# Precipitation.Precipitation(z.NYrs, z.DaysMonth, z.Prec)ize
def RetentionEff(NYrs, DaysMonth, InitSnow_0, Temp, Prec, Qretention, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                 CNP_0,
                 Imper, ISRR, ISRA, PctAreaInfil):
    # result = 0
    result = zeros((NYrs, 12, 31))
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    urbanqtotal = UrbanQTotal(NYrs, DaysMonth, NRur, NUrb, Temp, InitSnow_0, Prec, Area, CNI_0, AntMoist_0, Grow_0,
                              CNP_0,
                              Imper, ISRR,
                              ISRA)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    if water[Y][i][j] < 0.05:
                        pass
                    else:
                        if Qretention > 0:
                            if urbanqtotal[Y][i][j] > 0:
                                if urbanqtotal[Y][i][j] <= Qretention * PctAreaInfil:
                                    result[Y][i][j] = 1
                                else:
                                    result[Y][i][j] = Qretention * PctAreaInfil / urbanqtotal[Y][i][j]
                else:
                    pass
    return result


@memoize
def RetentionEff_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec, Qretention, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                   CNP_0, Imper, ISRR, ISRA, PctAreaInfil):
    result = zeros((NYrs, 12, 31))
    water = Water_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    urbanqtotal = UrbanQTotal_f(NYrs, DaysMonth, NRur, NUrb, Temp, InitSnow_0, Prec, Area, CNI_0, AntMoist_0, Grow_0,
                                CNP_0,
                                Imper, ISRR, ISRA)
    result[where((Temp > 0) & (water > 0.05) & (Qretention > 0) & (urbanqtotal > 0) & (
            urbanqtotal <= Qretention * PctAreaInfil))] = 1
    result[where((Temp > 0) & (water > 0.05) & (Qretention > 0) & (urbanqtotal > 0) & (
            urbanqtotal > Qretention * PctAreaInfil))] = \
        Qretention * PctAreaInfil / urbanqtotal[where(
            (Temp > 0) & (water > 0.05) & (Qretention > 0) & (urbanqtotal > 0) & (
                    urbanqtotal > Qretention * PctAreaInfil))]

    return result
