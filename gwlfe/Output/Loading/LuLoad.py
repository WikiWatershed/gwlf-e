from numpy import sum
from numpy import zeros

from gwlfe.Input.LandUse.NLU import NLU
from gwlfe.Input.WaterBudget.Water import Water
from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.Discharge.AdjUrbanQTotal import AdjUrbanQTotal
from gwlfe.Output.Loading.SurfaceLoad_1 import SurfaceLoad_1
from gwlfe.Output.Loading.SurfaceLoad_1 import SurfaceLoad_1_f


@memoize
def LuLoad(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
           Grow_0, CNP_0, Imper, ISRR, ISRA, Qretention, PctAreaInfil, Nqual, LoadRateImp,
           LoadRatePerv, Storm, UrbBMPRed, FilterWidth, PctStrmBuf):
    result = zeros((NYrs, 16, 3))
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    nlu = NLU(NRur, NUrb)
    adjurbanqtotal = AdjUrbanQTotal(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                                    Grow_0, CNP_0, Imper, ISRR, ISRA, Qretention, PctAreaInfil)
    surfaceload_1 = SurfaceLoad_1(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                                  CNP_0,
                                  Imper, ISRR, ISRA, Qretention, PctAreaInfil, Nqual, LoadRateImp, LoadRatePerv, Storm,
                                  UrbBMPRed, FilterWidth, PctStrmBuf)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    if adjurbanqtotal[Y][i][j] > 0.001:
                        for l in range(NRur, nlu):
                            for q in range(Nqual):
                                result[Y][l][q] += surfaceload_1[Y][i][j][l][q]
                    else:
                        pass
                else:
                    pass
    return result


@memoize
def LuLoad_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
             Grow_0, CNP_0, Imper, ISRR, ISRA, Qretention, PctAreaInfil, Nqual, LoadRateImp,
             LoadRatePerv, Storm, UrbBMPRed, FilterWidth, PctStrmBuf):
    return sum(SurfaceLoad_1_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                               CNP_0, Imper, ISRR, ISRA, Qretention, PctAreaInfil, Nqual, LoadRateImp, LoadRatePerv,
                               Storm, UrbBMPRed, FilterWidth, PctStrmBuf), axis=(1, 2))
