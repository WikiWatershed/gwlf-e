import numpy as np
from Timer import time_function
from Memoization import memoize
from SedTrans import SedTrans


def BSed(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
         ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN):
    result = np.zeros((NYrs, 12))  # These used to be (NYrs,16) but it looks like a mistake
    sedtrans = SedTrans(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0,
                        Imper,
                        ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN)
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = 0
            for m in range(i, 12):
                result[Y][i] = result[Y][i] + sedtrans[Y][m]
    return result


def BSed_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
           ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN):
    sedtrans = SedTrans(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0,
                        Imper, ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN)
    return np.flip(np.cumsum(np.flip(sedtrans, axis=1), axis=1), axis=1)
