from numpy import hstack
from numpy import sum
from numpy import zeros

from gwlfe.Input.LandUse.NLU import NLU
from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.Erosion.ErosWashoff import ErosWashoff
from gwlfe.MultiUse_Fxns.Erosion.ErosWashoff import ErosWashoff_f
from gwlfe.MultiUse_Fxns.Erosion.SedDelivRatio import SedDelivRatio
from gwlfe.MultiUse_Fxns.Runoff.pRunoff import pRunoff
from gwlfe.MultiUse_Fxns.Runoff.pRunoff import pRunoff_f
from gwlfe.Output.Loading.LuLoad import LuLoad
from gwlfe.Output.Loading.LuLoad import LuLoad_f


@memoize
def LuTotPhos(NYrs, DaysMonth, InitSnow_0, Temp, Prec, AntMoist_0, NRur, NUrb, CN, Grow_0, Area, PhosConc, ManPhos,
              ManuredAreas, FirstManureMonth, LastManureMonth, FirstManureMonth2, LastManureMonth2, SedDelivRatio_0, KF,
              LS, C, P, CNP_0, Imper, ISRR, ISRA, Qretention, PctAreaInfil, Nqual, LoadRateImp, LoadRatePerv, Storm,
              UrbBMPRed, FilterWidth, PctStrmBuf, Acoef, SedPhos, CNI_0):
    result = zeros((NYrs, 16))
    p_runoff = pRunoff(NYrs, DaysMonth, InitSnow_0, Temp, Prec, AntMoist_0, NRur, NUrb, CN, Grow_0, Area, PhosConc,
                       ManuredAreas, FirstManureMonth, LastManureMonth, ManPhos, FirstManureMonth2,
                       LastManureMonth2)
    sed_deliv_ratio = SedDelivRatio(SedDelivRatio_0)
    eros_washoff = ErosWashoff(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, Acoef,
                               KF, LS, C, P, Area)
    lu_load = LuLoad(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0,
                     AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, Qretention, PctAreaInfil, Nqual,
                     LoadRateImp, LoadRatePerv, Storm, UrbBMPRed, FilterWidth, PctStrmBuf)
    nlu = NLU(NRur, NUrb)
    for Y in range(NYrs):
        for i in range(12):
            # Add in the urban calucation for sediment
            for l in range(NRur):
                result[Y][l] += p_runoff[Y][i][l]
                result[Y][l] += 0.001 * sed_deliv_ratio * eros_washoff[Y][l][i] * SedPhos

            for l in range(NRur, nlu):
                result[Y][l] += lu_load[Y][l][1] / NYrs / 2
    return result


@memoize
def LuTotPhos_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec, AntMoist_0, NRur, NUrb, CN, Grow_0, Area, PhosConc, ManPhos,
                ManuredAreas, FirstManureMonth, LastManureMonth, FirstManureMonth2, LastManureMonth2, SedDelivRatio_0,
                KF,
                LS, C, P, CNP_0, Imper, ISRR, ISRA, Qretention, PctAreaInfil, Nqual, LoadRateImp, LoadRatePerv, Storm,
                UrbBMPRed, FilterWidth, PctStrmBuf, Acoef, SedPhos, CNI_0):
    p_runoff = sum(
        pRunoff_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec, AntMoist_0, NRur, NUrb, CN, Grow_0, Area, PhosConc,
                  ManuredAreas, FirstManureMonth, LastManureMonth, ManPhos, FirstManureMonth2,
                  LastManureMonth2), axis=1)
    sed_deliv_ratio = SedDelivRatio(SedDelivRatio_0)

    eros_washoff = sum(ErosWashoff_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, Acoef,
                                     KF, LS, C, P, Area), axis=1)

    lu_load = LuLoad_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                       Grow_0, CNP_0, Imper, ISRR, ISRA, Qretention, PctAreaInfil, Nqual, LoadRateImp,
                       LoadRatePerv, Storm, UrbBMPRed, FilterWidth, PctStrmBuf)[:, :, 1]
    # luLoad is not needed because it is only defined for NUrb land use, and the others are only defined for NRur
    return hstack(
        (p_runoff + 0.001 * sed_deliv_ratio * eros_washoff * SedPhos, 12. * lu_load / NYrs / 2))  # + lu_load / NYrs / 2
