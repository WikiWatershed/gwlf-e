from numpy import zeros

from gwlfe.Input.LandUse.NLU import NLU
from gwlfe.Input.WaterBudget.Water import Water
from gwlfe.Input.WaterBudget.Water import Water_f
from gwlfe.MultiUse_Fxns.Discharge.AdjUrbanQTotal import AdjUrbanQTotal
from gwlfe.MultiUse_Fxns.Discharge.AdjUrbanQTotal import AdjUrbanQTotal_f

try:
    from .UrbLoadRed_inner_compiled import UrbLoadRed_inner
except ImportError:
    print("Unable to import compiled UrbLoadRed_inner, using slower version")
    from gwlfe.BMPs.Stream.UrbLoadRed_inner import UrbLoadRed_inner


def UrbLoadRed(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
               Imper, ISRR, ISRA, Qretention, PctAreaInfil, Nqual, Storm, UrbBMPRed):
    result = zeros((NYrs, 12, 31, 16, Nqual))
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    adjurbanqtotal = AdjUrbanQTotal(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                                    Grow_0, CNP_0, Imper, ISRR, ISRA, Qretention, PctAreaInfil)
    nlu = NLU(NRur, NUrb)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    if adjurbanqtotal[Y][i][j] > 0.001:
                        for l in range(NRur, nlu):
                            for q in range(Nqual):
                                if Storm > 0:
                                    result[Y][i][j][l][q] = (water[Y][i][j] / Storm) * UrbBMPRed[l][q]
                                else:
                                    result[Y][i][j][l][q] = 0
                                if water[Y][i][j] > Storm:
                                    result[Y][i][j][l][q] = UrbBMPRed[l][q]
                else:
                    pass
    return result


# UrbLoadRed_f is faster than UrbLoadRed_1
def UrbLoadRed_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                 Imper, ISRR, ISRA, Qretention, PctAreaInfil, Nqual, Storm, UrbBMPRed):
    if (Storm > 0):
        water = Water_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
        adjurbanqtotal = AdjUrbanQTotal_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                                          Grow_0, CNP_0,
                                          Imper, ISRR, ISRA, Qretention, PctAreaInfil)
        nlu = NLU(NRur, NUrb)
        return UrbLoadRed_inner(NYrs, DaysMonth, Temp, NRur, Nqual, Storm, UrbBMPRed, water, adjurbanqtotal, nlu)
    else:
        return zeros((NYrs, 12, 31, 16, Nqual))
