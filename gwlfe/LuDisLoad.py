import numpy as np
# from Timer import time_function
from Memoization import memoize
from Water import Water
from NLU import NLU
from AdjUrbanQTotal import AdjUrbanQTotal
from DisSurfLoad import DisSurfLoad
from DisSurfLoad import DisSurfLoad_2


@memoize
def LuDisLoad(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
              Grow_0, CNP_0, Imper, ISRR, ISRA, Qretention, PctAreaInfil, Nqual, LoadRateImp,
              LoadRatePerv, Storm, UrbBMPRed, DisFract, FilterWidth, PctStrmBuf):
    result = np.zeros((NYrs, 16, 3))
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    nlu = NLU(NRur, NUrb)
    adjurbanqtotal = AdjUrbanQTotal(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                                        Grow_0, CNP_0, Imper, ISRR, ISRA, Qretention, PctAreaInfil)
    dissurfaceload = DisSurfLoad(NYrs, DaysMonth, InitSnow_0, Temp, Prec, Nqual, NRur, NUrb, Area, CNI_0, AntMoist_0,
                                 Grow_0, CNP_0, Imper, ISRR, ISRA, Qretention, PctAreaInfil, LoadRateImp, LoadRatePerv,
                                 Storm, UrbBMPRed, DisFract, FilterWidth, PctStrmBuf)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    if adjurbanqtotal[Y][i][j] > 0.001:
                        for l in range(NRur, nlu):
                            for q in range(Nqual):
                                result[Y][l][q] += dissurfaceload[Y][i][j][l][q]
                    else:
                        pass
                else:
                    pass
    return result


@memoize
def LuDisLoad_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec, Nqual, NRur, NUrb, Area, CNI_0, AntMoist_0,
                Grow_0, CNP_0, Imper, ISRR, ISRA, Qretention, PctAreaInfil, LoadRateImp, LoadRatePerv,
                Storm, UrbBMPRed, DisFract, FilterWidth, PctStrmBuf):
    return np.sum(DisSurfLoad_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec, Nqual, NRur, NUrb, Area, CNI_0, AntMoist_0,
                                Grow_0, CNP_0, Imper, ISRR, ISRA, Qretention, PctAreaInfil, LoadRateImp, LoadRatePerv,
                                Storm, UrbBMPRed, DisFract, FilterWidth, PctStrmBuf), axis=(1, 2))
