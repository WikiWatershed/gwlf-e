from numpy import zeros

from gwlfe.Input.LandUse.Urb.UrbAreaTotal import UrbAreaTotal
from gwlfe.Input.LandUse.Urb.UrbAreaTotal import UrbAreaTotal_f
from gwlfe.Input.WaterBudget.Water import Water
from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.Runoff.UrbanRunoff import UrbanRunoff
from gwlfe.MultiUse_Fxns.Runoff.UrbanRunoff import UrbanRunoff_f


@memoize
def UrbRunoffLiter(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                   ISRR, ISRA):
    result = zeros((NYrs, 12))
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    urbareatotal = UrbAreaTotal(NRur, NUrb, Area)
    urbanrunoff = UrbanRunoff(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                              CNP_0, Imper,
                              ISRR, ISRA)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    result[Y][i] = (urbanrunoff[Y][i] / 100) * urbareatotal * 10000 * 1000
                else:
                    pass
    return result


@memoize
def UrbRunoffLiter_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                     CNP_0, Imper, ISRR, ISRA):
    urbareatotal = UrbAreaTotal_f(NRur, NUrb, Area)
    urbanrunoff = UrbanRunoff_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                                CNP_0, Imper, ISRR, ISRA)
    return urbanrunoff / 100 * urbareatotal * 10000 * 1000
