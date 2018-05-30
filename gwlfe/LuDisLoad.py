import numpy as np
from Timer import time_function
from Memoization import memoize
from Water import Water
from NLU import NLU
from AdjUrbanQTotal_1 import AdjUrbanQTotal_1
from DisSurfLoad import DisSurfLoad


@memoize
def LuDisLoad(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                        Grow_0, CNP_0, Imper, ISRR, ISRA, Qretention, PctAreaInfil, Nqual, LoadRateImp,
                        SweepFrac, UrbSweepFrac, LoadRatePerv, Storm, UrbBMPRed, DisFract, FilterWidth, PctStrmBuf):
    result = np.zeros((NYrs, 16, 3))
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    nlu = NLU(NRur, NUrb)
    adjurbanqtotal_1 = AdjUrbanQTotal_1(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                                        Grow_0, CNP_0, Imper, ISRR, ISRA, Qretention, PctAreaInfil)
    dissurfaceload = DisSurfLoad(NYrs, DaysMonth, InitSnow_0, Temp, Prec, Nqual, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                     Imper, ISRR, ISRA, Qretention, PctAreaInfil, LoadRateImp, SweepFrac, UrbSweepFrac, LoadRatePerv, Storm, UrbBMPRed, DisFract, FilterWidth, PctStrmBuf)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    if adjurbanqtotal_1[Y][i][j] > 0.001:
                        for l in range(NRur, nlu):
                            for q in range(Nqual):
                                result[Y][l][q] += dissurfaceload[Y][i][j][l][q]
                    else:
                        pass
                else:
                    pass
    return result


def LuDisLoad_2():
    pass
