import numpy as np
from Timer import time_function
from Memoization import memoize
from NLU import NLU
from FilterEff import FilterEff
from FilterEff import FilterEff_2
from Water import Water
from Water import Water_2
from AdjUrbanQTotal import AdjUrbanQTotal
from AdjUrbanQTotal import AdjUrbanQTotal_2
from SurfaceLoad import SurfaceLoad
from SurfaceLoad import SurfaceLoad_2
from RetentionEff import RetentionEff
from RetentionEff import RetentionEff_2


@memoize
def DisSurfLoad(NYrs, DaysMonth, InitSnow_0, Temp, Prec, Nqual, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                Imper, ISRR, ISRA, Qretention, PctAreaInfil, LoadRateImp, LoadRatePerv, Storm,
                UrbBMPRed, DisFract, FilterWidth, PctStrmBuf):
    result = np.zeros((NYrs, 12, 31, 16, Nqual))
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    nlu = NLU(NRur, NUrb)
    adjurbanqtotal = AdjUrbanQTotal(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                                        Grow_0, CNP_0,
                                        Imper, ISRR, ISRA, Qretention, PctAreaInfil)
    surfaceload = SurfaceLoad(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                              CNP_0, Imper, ISRR, ISRA, Qretention, PctAreaInfil, Nqual, LoadRateImp, LoadRatePerv,
                              Storm, UrbBMPRed)
    retentioneff = RetentionEff(NYrs, DaysMonth, InitSnow_0, Temp, Prec, Qretention, NRur, NUrb, Area, CNI_0,
                                AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, PctAreaInfil)
    filtereff = FilterEff(FilterWidth)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    if adjurbanqtotal[Y][i][j] > 0.001:
                        for l in range(NRur, nlu):
                            for q in range(Nqual):
                                result[Y][i][j][l][q] = DisFract[l][q] * surfaceload[Y][i][j][l][q]
                                result[Y][i][j][l][q] *= (1 - retentioneff) * (1 - (filtereff * PctStrmBuf))
                    else:
                        pass
                else:
                    pass
    return result


def DisSurfLoad_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec, Nqual, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                  Imper, ISRR, ISRA, Qretention, PctAreaInfil, LoadRateImp, LoadRatePerv,
                  Storm, UrbBMPRed, DisFract, FilterWidth, PctStrmBuf):
    nlu = NLU(NRur, NUrb)
    result = np.zeros((NYrs, 12, 31, nlu - NRur, Nqual))
    water = Water_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    adjurbanqtotal = AdjUrbanQTotal_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                                          Grow_0, CNP_0,
                                          Imper, ISRR, ISRA, Qretention, PctAreaInfil)
    surfaceload = SurfaceLoad_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                                CNP_0,
                                Imper, ISRR, ISRA, Qretention, PctAreaInfil, Nqual, LoadRateImp, LoadRatePerv, Storm,
                                UrbBMPRed)
    retentioneff = RetentionEff_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec, Qretention, NRur, NUrb, Area, CNI_0,
                                  AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, PctAreaInfil)
    filtereff = FilterEff_2(FilterWidth)
    nonzero = np.where((Temp > 0) & (water > 0.01) & (adjurbanqtotal > 0.001))
    result[nonzero] = surfaceload[nonzero] * DisFract[NRur:] * (1 - retentioneff) * (1 - (filtereff * PctStrmBuf))
    return result
