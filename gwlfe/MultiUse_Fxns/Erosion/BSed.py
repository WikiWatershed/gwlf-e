from numpy import cumsum
from numpy import flip
from numpy import zeros

from gwlfe.MultiUse_Fxns.Erosion.SedTrans import SedTrans
from gwlfe.MultiUse_Fxns.Erosion.SedTrans import SedTrans_f


def BSed(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
         ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN):
    result = zeros((NYrs, 12))  # These used to be (NYrs,16) but it looks like a mistake
    sedtrans = SedTrans(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                        Imper,
                        ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN)
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = 0
            for m in range(i, 12):
                result[Y][i] = result[Y][i] + sedtrans[Y][m]
    return result


def BSed_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
           ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN):
    sedtrans = SedTrans_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                          Imper, ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN)
    return flip(cumsum(flip(sedtrans, axis=1), axis=1), axis=1)
