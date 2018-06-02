import numpy as np
from Timer import time_function
from Memoization import memoize
from SedDelivRatio import SedDelivRatio
from pRunoff import pRunoff
from pRunoff import pRunoff_2
from ErosWashoff import ErosWashoff
from ErosWashoff import ErosWashoff_2
from LuLoad import LuLoad


@memoize
def LuTotPhos(NYrs, DaysMonth, InitSnow_0, Temp, Prec, AntMoist_0, NRur, NUrb, CN, Grow_0, Area, PhosConc, ManPhos,
              ManuredAreas, FirstManureMonth, LastManureMonth, FirstManureMonth2, LastManureMonth2, SedDelivRatio_0, KF,
              LS, C, P, CNP_0, Imper, ISRR, ISRA, Qretention, PctAreaInfil, Nqual, LoadRateImp, LoadRatePerv, Storm,
              UrbBMPRed, FilterWidth, PctStrmBuf, Acoef, SedPhos, CNI_0):
    result = np.zeros((NYrs, 16))
    p_runoff = pRunoff(NYrs, DaysMonth, InitSnow_0, Temp, Prec, AntMoist_0, NRur, NUrb, CN, Grow_0, Area, PhosConc,
                       ManuredAreas, FirstManureMonth, LastManureMonth, ManPhos, FirstManureMonth2,
                       LastManureMonth2)
    sed_deliv_ratio = SedDelivRatio(SedDelivRatio_0)
    eros_washoff = ErosWashoff(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, Acoef,
                               KF, LS, C, P, Area)
    lu_load = LuLoad(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0,
                     AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, Qretention, PctAreaInfil, Nqual,
                     LoadRateImp, LoadRatePerv, Storm, UrbBMPRed, FilterWidth, PctStrmBuf)
    for Y in range(NYrs):
        for i in range(12):
            # Add in the urban calucation for sediment
            for l in range(NRur):
                result[Y][l] += p_runoff[Y][i]
                result[Y][l] += 0.001 * sed_deliv_ratio * eros_washoff[Y][l][i] * SedPhos
                result[Y][l] += lu_load[Y][l][1] / NYrs / 2
    return result

def LuTotPhos_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec, AntMoist_0, NRur, NUrb, CN, Grow_0, Area, PhosConc, ManPhos,
                ManuredAreas, FirstManureMonth, LastManureMonth, FirstManureMonth2, LastManureMonth2, SedDelivRatio_0,
                KF, LS, C, P, Acoef, SedPhos):
    p_runoff = np.reshape(
        np.repeat(np.sum(
            pRunoff_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec, AntMoist_0, NRur, NUrb, CN, Grow_0, Area, PhosConc,
                      ManuredAreas,
                      FirstManureMonth, LastManureMonth, ManPhos, FirstManureMonth2, LastManureMonth2), axis=1),
            repeats=10), (NYrs, 10))
    sed_deliv_ratio = SedDelivRatio(SedDelivRatio_0)
    eros_washoff = np.sum(ErosWashoff_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, Acoef,
                                        KF, LS, C, P, Area), axis=1)
    # luLoad is not needed because it is only defined for NUrb land use, and the others are only defined for NRur
    return p_runoff + 0.001 * sed_deliv_ratio * eros_washoff * SedPhos  # + lu_load / NYrs / 2
