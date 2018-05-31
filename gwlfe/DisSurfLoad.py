import numpy as np
from Timer import time_function
from Memoization import memoize
from Water import Water
from NLU import NLU
from AdjUrbanQTotal_1 import AdjUrbanQTotal_1
from SurfaceLoad import SurfaceLoad
from RetentionEff import RetentionEff
from FilterEff import FilterEff
from Water import Water
from AdjUrbanQTotal_1 import AdjUrbanQTotal_1
from SurfaceLoad import SurfaceLoad
from RetentionEff import RetentionEff


@memoize
def DisSurfLoad(NYrs, DaysMonth, InitSnow_0, Temp, Prec, Nqual, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0,
                     Imper, ISRR, ISRA, Qretention, PctAreaInfil, LoadRateImp, SweepFrac, UrbSweepFrac, LoadRatePerv, Storm, UrbBMPRed, DisFract, FilterWidth, PctStrmBuf):
    result = np.zeros((NYrs, 12, 31, 16, Nqual))
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    nlu = NLU(NRur, NUrb)
    adjurbanqtotal_1 = AdjUrbanQTotal_1(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0,
                     Imper, ISRR, ISRA, Qretention, PctAreaInfil)
    surfaceload = SurfaceLoad(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0,
                     Imper, ISRR, ISRA, Qretention, PctAreaInfil, Nqual, LoadRateImp, SweepFrac, UrbSweepFrac, LoadRatePerv, Storm, UrbBMPRed)
    retentioneff = RetentionEff(NYrs, DaysMonth, InitSnow_0, Temp, Prec, Qretention, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper, ISRR, ISRA, PctAreaInfil)
    filtereff = FilterEff(FilterWidth)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    if adjurbanqtotal_1[Y][i][j] > 0.001:
                        for l in range(NRur, nlu):
                            for q in range(Nqual):
                                result[Y][i][j][l][q] = DisFract[l][q] * surfaceload[Y][i][j][l][q]
                                result[Y][i][j][l][q] *= (1 - retentioneff) * (1 - (filtereff * PctStrmBuf))
                    else:
                        pass
                else:
                    pass
    return result


def DisSurfLoad_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec, Nqual, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0,
                     Imper, ISRR, ISRA, Qretention, PctAreaInfil, LoadRateImp, SweepFrac, UrbSweepFrac, LoadRatePerv,
                  Storm, UrbBMPRed, DisFract, FilterWidth, PctStrmBuf):

