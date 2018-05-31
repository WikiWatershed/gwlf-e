import numpy as np
from Timer import time_function
from Memoization import memoize
from Water import Water
from AdjUrbanQTotal_1 import AdjUrbanQTotal_1
from NLU import NLU
from Water import Water_2
from AdjUrbanQTotal_1 import AdjUrbanQTotal_1_2
from UrbLoadRed_inner import UrbLoadRed_inner
# @memoize
@time_function
def UrbLoadRed(NYrs, DaysMonth, InitSnow_0, Temp, Prec,  NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0,
                     Imper, ISRR, ISRA, Qretention, PctAreaInfil, Nqual, Storm, UrbBMPRed):
    result = np.zeros((NYrs, 12, 31, 16, Nqual))
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    adjurbanqtotal = AdjUrbanQTotal_1(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0,
                     Imper, ISRR, ISRA, Qretention, PctAreaInfil)
    nlu = NLU(NRur, NUrb)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    # result[Y][i][j][l][q] = 0
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
    
@time_function
def UrbLoadRed_1(NYrs, DaysMonth, InitSnow_0, Temp, Prec,  NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0,
                     Imper, ISRR, ISRA, Qretention, PctAreaInfil, Nqual, Storm, UrbBMPRed):
    result = np.zeros((NYrs, 12, 31, 16, Nqual))
    water = Water_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    adjurbanqtotal = AdjUrbanQTotal_1_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0,
                     Imper, ISRR, ISRA, Qretention, PctAreaInfil)
    nlu = NLU(NRur, NUrb)
    np.repeat(Temp[:, :, :, None, None], NRur, axis=3)
    Temp = np.tile(Temp[:, :, :, None, None], (1,1,1,16, Nqual))
    water = np.tile(water[:, :, :, None, None], (1,1,1,16, Nqual))
    adjurbanqtotal =  np.tile(adjurbanqtotal[:, :, :, None, None], (1,1,1,16, Nqual))
    Storm = np.tile(np.array([Storm]), (1,1,1,16, Nqual))
    UrbBMPRed = np.tile(UrbBMPRed, (NYrs, 12,31,1,1))
    temp = (water/Storm) * UrbBMPRed
    result[np.where((Temp>0) & (water>0.01) & (adjurbanqtotal > 0.001) & (Storm > 0 ))] = temp[np.where((Temp>0) & (water>0.01) & (adjurbanqtotal > 0.001) & (Storm > 0 ))]
    result[np.where((Temp>0) & (water>0.01) & (adjurbanqtotal > 0.001) & (water>Storm))] = UrbBMPRed[np.where((Temp>0) & (water>0.01) & (adjurbanqtotal > 0.001) & (water>Storm))]
    result[:,:,:,0:NRur] = 0
    return result


 #UrbLoadRed_2 is faster than UrbLoadRed_1
@time_function
def UrbLoadRed_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec,  NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0,
                     Imper, ISRR, ISRA, Qretention, PctAreaInfil, Nqual, Storm, UrbBMPRed):
    water = Water_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    adjurbanqtotal = AdjUrbanQTotal_1_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                                        Grow, CNP_0,
                                        Imper, ISRR, ISRA, Qretention, PctAreaInfil)
    nlu = NLU(NRur, NUrb)
    return UrbLoadRed_inner(NYrs, DaysMonth, Temp,  NRur, Nqual, Storm, UrbBMPRed, water, adjurbanqtotal, nlu)