import numpy as np
from Timer import time_function
from Memoization import memoize
from Water import Water
from AdjUrbanQTotal_1 import AdjUrbanQTotal_1
from NLU import NLU
from WashImperv import WashImperv
from WashPerv import WashPerv
from LU_1 import LU_1
from UrbLoadRed import UrbLoadRed


@memoize
def SurfaceLoad(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0,
                     Imper, ISRR, ISRA, Qretention, PctAreaInfil, Nqual, LoadRateImp, SweepFrac, UrbSweepFrac, LoadRatePerv, Storm, UrbBMPRed):
    result = np.zeros((NYrs, 12, 31, 16, Nqual))
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    adjurbanqtotal_1 = AdjUrbanQTotal_1(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0,
                     Imper, ISRR, ISRA, Qretention, PctAreaInfil)
    nlu = NLU(NRur, NUrb)
    washimperv = WashImperv(NYrs, DaysMonth, InitSnow_0, Temp, Prec, CNI_0, AntMoist_0, Grow, NRur, NUrb)
    washperv = WashPerv(NYrs, DaysMonth, InitSnow_0, Temp, Prec, CNP_0, AntMoist_0, Grow, NRur, NUrb)
    lu_1 = LU_1(NRur, NUrb)
    urbloadred = UrbLoadRed(NYrs, DaysMonth, InitSnow_0, Temp, Prec,  NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0,
                     Imper, ISRR, ISRA, Qretention, PctAreaInfil, Nqual, Storm, UrbBMPRed)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    if adjurbanqtotal_1[Y][i][j] > 0.001:
                        for l in range(NRur, nlu):
                            for q in range(Nqual):
                                if Area[l] > 0:
                                    result[Y][i][j][l][q] = (((LoadRateImp[l][q] * washimperv[Y][i][j][l] * (
                                            (Imper[l] * (1 - ISRR[lu_1[l]]) * (1 - ISRA[lu_1[l]]))
                                            # * (SweepFrac[i] + (
                                            # (1 - SweepFrac[i]) * ((1 - UrbSweepFrac) * Area[l]) / Area[l]))
                                                        * 1 ) # TODO For some reason, this commented out code always needs to evaluate to 1 in order for the separation to occur
                                                       + LoadRatePerv[l][q] * washperv[Y][i][j][l] * (
                                                               1 - (Imper[l] * (1 - ISRR[lu_1[l]]) * (
                                                                   1 - ISRA[lu_1[l]]))))
                                                      * Area[l]) - urbloadred[Y][i][j][l][q])
                                else:
                                    result[Y][i][j][l][q] = 0

                                if result[Y][i][j][l][q] < 0:
                                    result[Y][i][j][l][q] = 0
                                else:
                                    pass
                    else:
                        pass
                else:
                    pass
    return result


def SurfaceLoad_2():
    pass
