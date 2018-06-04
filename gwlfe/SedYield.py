import numpy as np
from Timer import time_function
from Memoization import memoize
from Erosion import Erosion
from Erosion import Erosion_2
from BSed import BSed
from BSed import BSed_2
from SedDelivRatio import SedDelivRatio
from SedTrans import SedTrans
from SedTrans import SedTrans_2


# @memoize
def SedYield(NYrs, DaysMonth, Temp, InitSnow_0, Prec, Acoef, NRur, KF, LS, C, P, Area, NUrb, CNI_0, AntMoist_0, Grow_0,
             ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN, CNP_0, Imper, SedDelivRatio_0):
    result = np.zeros((NYrs, 12))
    erosion = Erosion(NYrs, DaysMonth, Temp, InitSnow_0, Prec, Acoef, NRur, KF, LS, C, P, Area)
    bsed = BSed(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN)
    seddelivratio = SedDelivRatio(SedDelivRatio_0)
    sedtrans = SedTrans(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                        Imper, ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN)
    for Y in range(NYrs):
        for i in range(12):
            for m in range(i + 1):
                if bsed[Y][m] > 0:
                    result[Y][i] = result[Y][i] + erosion[Y][m] / bsed[Y][m]
        # for i in range(12):
            result[Y][i] = seddelivratio * sedtrans[Y][i] * result[Y][i]
    return result

@memoize
def SedYield_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, Acoef, NRur, KF, LS, C, P, Area, NUrb, CNI_0, AntMoist_0, Grow_0,
               ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN, CNP_0, Imper, SedDelivRatio_0):
    erosion = Erosion_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, Acoef, NRur, KF, LS, C, P, Area)
    bsed = BSed_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                  ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN)
    seddelivratio = SedDelivRatio(SedDelivRatio_0)
    sedtrans = SedTrans_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                          Imper, ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN)

    return seddelivratio * sedtrans * np.cumsum(np.where(bsed > 0., erosion / bsed, 0.), axis=1)
