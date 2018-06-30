from numpy import sum
from numpy import where
from numpy import zeros

from gwlfe.Input.LandUse.NLU import NLU
from gwlfe.Input.WaterBudget.Water import Water
from gwlfe.Input.WaterBudget.Water import Water_f
from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.Discharge.AdjUrbanQTotal import AdjUrbanQTotal
from gwlfe.MultiUse_Fxns.Discharge.AdjUrbanQTotal import AdjUrbanQTotal_f
from gwlfe.Output.Loading.DisSurfLoad import DisSurfLoad
from gwlfe.Output.Loading.DisSurfLoad import DisSurfLoad_f
from gwlfe.Output.Loading.SurfaceLoad_1 import SurfaceLoad_1
from gwlfe.Output.Loading.SurfaceLoad_1 import SurfaceLoad_1_f


@memoize
def NetSolidLoad(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                 Grow_0, CNP_0, Imper, ISRR, ISRA, Qretention, PctAreaInfil, Nqual, LoadRateImp,
                 LoadRatePerv, Storm, UrbBMPRed, DisFract, FilterWidth, PctStrmBuf):
    result = zeros((NYrs, 12, 31, Nqual))
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    nlu = NLU(NRur, NUrb)
    adjurbanqtotal = AdjUrbanQTotal(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                                    Grow_0, CNP_0, Imper, ISRR, ISRA, Qretention, PctAreaInfil)
    dissurfaceload = DisSurfLoad(NYrs, DaysMonth, InitSnow_0, Temp, Prec, Nqual, NRur, NUrb, Area, CNI_0, AntMoist_0,
                                 Grow_0, CNP_0, Imper, ISRR, ISRA, Qretention, PctAreaInfil, LoadRateImp, LoadRatePerv,
                                 Storm, UrbBMPRed, DisFract, FilterWidth, PctStrmBuf)
    surfaceload_1 = SurfaceLoad_1(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                                  CNP_0, Imper, ISRR, ISRA, Qretention, PctAreaInfil, Nqual, LoadRateImp, LoadRatePerv,
                                  Storm, UrbBMPRed, FilterWidth, PctStrmBuf)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    if adjurbanqtotal[Y][i][j] > 0.001:
                        for l in range(NRur, nlu):
                            for q in range(Nqual):
                                result[Y][i][j][q] += surfaceload_1[Y][i][j][l][q] - dissurfaceload[Y][i][j][l][q]
                    else:
                        pass
                else:
                    pass
    return result


def NetSolidLoad_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                   Grow_0, CNP_0, Imper, ISRR, ISRA, Qretention, PctAreaInfil, Nqual, LoadRateImp,
                   LoadRatePerv, Storm, UrbBMPRed, DisFract, FilterWidth, PctStrmBuf):
    nlu = NLU(NRur, NUrb)
    result = zeros((NYrs, 12, 31, nlu - NRur, Nqual))
    water = Water_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    adjurbanqtotal = AdjUrbanQTotal_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                                      Grow_0, CNP_0, Imper, ISRR, ISRA, Qretention, PctAreaInfil)
    dissurfaceload = DisSurfLoad_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec, Nqual, NRur, NUrb, Area, CNI_0, AntMoist_0,
                                   Grow_0, CNP_0, Imper, ISRR, ISRA, Qretention, PctAreaInfil, LoadRateImp,
                                   LoadRatePerv, Storm, UrbBMPRed, DisFract, FilterWidth, PctStrmBuf)
    surfaceload_1 = SurfaceLoad_1_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                                    Grow_0,
                                    CNP_0, Imper, ISRR, ISRA, Qretention, PctAreaInfil, Nqual, LoadRateImp,
                                    LoadRatePerv,
                                    Storm, UrbBMPRed, FilterWidth, PctStrmBuf)
    nonzero = where((Temp > 0) & (water > 0.01) & (adjurbanqtotal > 0.001))
    result[nonzero] = surfaceload_1[nonzero] - dissurfaceload[nonzero]
    return sum(result, axis=3)
