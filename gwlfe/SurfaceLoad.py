from numpy import maximum
from numpy import repeat
from numpy import reshape
from numpy import where
from numpy import zeros

from AdjUrbanQTotal import AdjUrbanQTotal
from AdjUrbanQTotal import AdjUrbanQTotal_f
from LU_1 import LU_1
# from Timer import time_function
from Memoization import memoize
from NLU import NLU
from UrbLoadRed import UrbLoadRed
from UrbLoadRed import UrbLoadRed_f
from WashImperv import WashImperv
from WashImperv import WashImperv_f
from WashPerv import WashPerv
from WashPerv import WashPerv_f
from Water import Water
from Water import Water_f


@memoize
def SurfaceLoad(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                Imper, ISRR, ISRA, Qretention, PctAreaInfil, Nqual, LoadRateImp, LoadRatePerv, Storm, UrbBMPRed):
    result = zeros((NYrs, 12, 31, 16, Nqual))
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    adjurbanqtotal = AdjUrbanQTotal(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                                        Grow_0, CNP_0,
                                        Imper, ISRR, ISRA, Qretention, PctAreaInfil)
    nlu = NLU(NRur, NUrb)
    washimperv = WashImperv(NYrs, DaysMonth, InitSnow_0, Temp, Prec, CNI_0, AntMoist_0, Grow_0, NRur, NUrb)
    washperv = WashPerv(NYrs, DaysMonth, InitSnow_0, Temp, Prec, CNP_0, AntMoist_0, Grow_0, NRur, NUrb)
    lu_1 = LU_1(NRur, NUrb)
    urbloadred = UrbLoadRed(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                            Imper, ISRR, ISRA, Qretention, PctAreaInfil, Nqual, Storm, UrbBMPRed)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    if adjurbanqtotal[Y][i][j] > 0.001:
                        for l in range(NRur, nlu):
                            for q in range(Nqual):
                                if Area[l] > 0:
                                    result[Y][i][j][l][q] = (((LoadRateImp[l][q] * washimperv[Y][i][j][l] * (
                                            (Imper[l] * (1 - ISRR[lu_1[l]]) * (1 - ISRA[lu_1[l]]))
                                            # * (SweepFrac[i] + (
                                            # (1 - SweepFrac[i]) * ((1 - UrbSweepFrac) * Area[l]) / Area[l]))
                                            * 1)  # TODO For some reason, this commented out code always needs to evaluate to 1 in order for the separation to occur
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

@memoize
def SurfaceLoad_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                  Imper, ISRR, ISRA, Qretention, PctAreaInfil, Nqual, LoadRateImp,
                  LoadRatePerv, Storm, UrbBMPRed):
    nlu = NLU(NRur, NUrb)
    result = zeros((NYrs, 12, 31, nlu - NRur, Nqual))
    water = Water_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    adjurbanqtotal = AdjUrbanQTotal_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                                          Grow_0, CNP_0, Imper, ISRR, ISRA, Qretention, PctAreaInfil)
    # print(np.where((Temp > 0) & (water > 0.01) & (adjurbanqtotal_1 > 0.001)).shape)
    nonzeroday = where((Temp > 0) & (water > 0.01) & (adjurbanqtotal > 0.001))
    washimperv = reshape(
        repeat(
            WashImperv_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec, CNI_0, AntMoist_0, Grow_0, NRur, NUrb)[:, :, :,
            NRur:],
            repeats=Nqual,
            axis=3), (NYrs, 12, 31, nlu - NRur, Nqual))
    washperv = reshape(
        repeat(
            WashPerv_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec, CNP_0, AntMoist_0, Grow_0, NRur, NUrb)[:, :, :, NRur:],
            repeats=Nqual,
            axis=3), (NYrs, 12, 31, nlu - NRur, Nqual))
    urbloadred = UrbLoadRed_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                              CNP_0,
                              Imper, ISRR, ISRA, Qretention, PctAreaInfil, Nqual, Storm, UrbBMPRed)[:, :, :, NRur:]

    # area = np.reshape(np.repeat(Area, repeats=NYrs * 12 * 31), (NYrs, 12, 31, nlu))[NRur:]
    temp = reshape(repeat(Imper[NRur:] * (1 - ISRR) * (1 - ISRA), repeats=Nqual, axis=0), (-1, Nqual))
    # print((washimperv * LoadRateImp).shape)
    # making an assumption that Area cannot be negative. Therefor where area = 0 result will be <= 0 and will be set to zero before returned (eliminating an if)
    result[nonzeroday] = (washimperv[nonzeroday] * LoadRateImp[NRur:] * temp +
                          washperv[nonzeroday] * LoadRatePerv[NRur:] * (1 - temp)) * reshape(
        repeat(Area[NRur:], repeats=Nqual, axis=0), (nlu - NRur, Nqual)) - urbloadred[nonzeroday]
    return maximum(result, 0)
