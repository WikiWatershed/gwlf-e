import numpy as np
from Timer import time_function
from Memoization import memoize
from Water import Water
from AdjUrbanQTotal_1 import AdjUrbanQTotal_1
from NLU import NLU


@memoize
def UrbLoadRed(NYrs, DaysMonth, InitSnow_0, Temp, Prec,  NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0,
                     Imper, ISRR, ISRA, Qretention, PctAreaInfil, Nqual, Storm, UrbBMPRed):
    result = np.zeros(1)
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    adjurbanqtotal = AdjUrbanQTotal_1(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0,
                     Imper, ISRR, ISRA, Qretention, PctAreaInfil)
    nlu = NLU(NRur, NUrb)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    result = 0
                    if adjurbanqtotal[Y][i][j] > 0.001:
                        for l in range(NRur, nlu):
                            for q in range(Nqual):
                                if Storm > 0:
                                    result = (water[Y][i][j] / Storm) * UrbBMPRed[l][q]
                                else:
                                    result = 0
                                if water[Y][i][j] > Storm:
                                    result = UrbBMPRed[l][q]
                else:
                    pass
    return result
    

def UrbLoadRed_2():
    pass
