from numpy import cumsum
from numpy import where
from numpy import zeros

from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.Erosion.BSed import BSed
from gwlfe.MultiUse_Fxns.Erosion.BSed import BSed_f
from gwlfe.MultiUse_Fxns.Erosion.Erosion import Erosion
from gwlfe.MultiUse_Fxns.Erosion.Erosion import Erosion_f
from gwlfe.MultiUse_Fxns.Erosion.SedDelivRatio import SedDelivRatio
from gwlfe.MultiUse_Fxns.Erosion.SedTrans import SedTrans
from gwlfe.MultiUse_Fxns.Erosion.SedTrans import SedTrans_f


def SedYield(NYrs, DaysMonth, Temp, InitSnow_0, Prec, Acoef, NRur, KF, LS, C, P, Area, NUrb, CNI_0, AntMoist_0, Grow_0,
             ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN, CNP_0, Imper, SedDelivRatio_0):
    result = zeros((NYrs, 12))
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
            result[Y][i] = seddelivratio * sedtrans[Y][i] * result[Y][i]
    return result


@memoize
def SedYield_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, Acoef, NRur, KF, LS, C, P, Area, NUrb, CNI_0, AntMoist_0,
               Grow_0,
               ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN, CNP_0, Imper, SedDelivRatio_0):
    erosion = Erosion_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, Acoef, NRur, KF, LS, C, P, Area)
    bsed = BSed_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                  ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN)
    seddelivratio = SedDelivRatio(SedDelivRatio_0)
    sedtrans = SedTrans_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                          Imper, ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN)
    nonzero = where(bsed > 0)
    temp = zeros((NYrs, 12))
    temp[nonzero] = erosion[nonzero] / bsed[nonzero]
    return seddelivratio * sedtrans * cumsum(temp, axis=1)
