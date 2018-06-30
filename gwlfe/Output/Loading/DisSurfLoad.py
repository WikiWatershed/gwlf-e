from numpy import repeat
from numpy import where
from numpy import zeros

from gwlfe.BMPs.Stream.FilterEff import FilterEff
from gwlfe.BMPs.Stream.FilterEff import FilterEff_f
from gwlfe.Input.LandUse.NLU import NLU
from gwlfe.Input.WaterBudget.Water import Water
from gwlfe.Input.WaterBudget.Water import Water_f
from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.Discharge.AdjUrbanQTotal import AdjUrbanQTotal
from gwlfe.MultiUse_Fxns.Discharge.AdjUrbanQTotal import AdjUrbanQTotal_f
from gwlfe.MultiUse_Fxns.Runoff.RetentionEff import RetentionEff
from gwlfe.MultiUse_Fxns.Runoff.RetentionEff import RetentionEff_f
from gwlfe.Output.Loading.SurfaceLoad import SurfaceLoad
from gwlfe.Output.Loading.SurfaceLoad import SurfaceLoad_f


@memoize
def DisSurfLoad(NYrs, DaysMonth, InitSnow_0, Temp, Prec, Nqual, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                Imper, ISRR, ISRA, Qretention, PctAreaInfil, LoadRateImp, LoadRatePerv, Storm,
                UrbBMPRed, DisFract, FilterWidth, PctStrmBuf):
    result = zeros((NYrs, 12, 31, 16, Nqual))
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    nlu = NLU(NRur, NUrb)
    adjurbanqtotal = AdjUrbanQTotal(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                                    Grow_0, CNP_0,
                                    Imper, ISRR, ISRA, Qretention, PctAreaInfil)
    surfaceload = SurfaceLoad(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                              CNP_0, Imper, ISRR, ISRA, Qretention, PctAreaInfil, Nqual, LoadRateImp, LoadRatePerv,
                              Storm, UrbBMPRed)
    retentioneff = RetentionEff(NYrs, DaysMonth, InitSnow_0, Temp, Prec, Qretention, NRur, NUrb, Area, CNI_0,
                                AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, PctAreaInfil)
    filtereff = FilterEff(FilterWidth)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    if adjurbanqtotal[Y][i][j] > 0.001:
                        for l in range(NRur, nlu):
                            for q in range(Nqual):
                                result[Y][i][j][l][q] = DisFract[l][q] * surfaceload[Y][i][j][l][q]
                                result[Y][i][j][l][q] *= (1 - retentioneff[Y][i][j]) * (1 - (filtereff * PctStrmBuf))
                    else:
                        pass
                else:
                    pass
    return result


@memoize
def DisSurfLoad_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec, Nqual, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                  Imper, ISRR, ISRA, Qretention, PctAreaInfil, LoadRateImp, LoadRatePerv,
                  Storm, UrbBMPRed, DisFract, FilterWidth, PctStrmBuf):
    nlu = NLU(NRur, NUrb)
    result = zeros((NYrs, 12, 31, nlu - NRur, Nqual))
    water = Water_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    adjurbanqtotal = AdjUrbanQTotal_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                                      Grow_0, CNP_0,
                                      Imper, ISRR, ISRA, Qretention, PctAreaInfil)
    surfaceload = SurfaceLoad_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                                CNP_0,
                                Imper, ISRR, ISRA, Qretention, PctAreaInfil, Nqual, LoadRateImp, LoadRatePerv, Storm,
                                UrbBMPRed)
    retentioneff = RetentionEff_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec, Qretention, NRur, NUrb, Area, CNI_0,
                                  AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, PctAreaInfil)[:, :, :, None, None]
    retentioneff = repeat(repeat(retentioneff, nlu - NRur, axis=3), Nqual, axis=4)
    filtereff = FilterEff_f(FilterWidth)
    nonzero = where((Temp > 0) & (water > 0.01) & (adjurbanqtotal > 0.001))
    result[nonzero] = surfaceload[nonzero] * DisFract[NRur:] * (1 - retentioneff[nonzero]) * (
                1 - (filtereff * PctStrmBuf))
    return result
