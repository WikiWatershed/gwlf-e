# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

"""
Imported from CalcLoads.bas
"""

from numpy import zeros

from .Input.LandUse.AreaTotal import AreaTotal_f
from .Input.WaterBudget.GroundWatLE_1 import GroundWatLE_1_f
from .Input.LandUse.Ag.TileDrain import TileDrain_f
from .Input.LandUse.TotAreaMeters import TotAreaMeters
from .MultiUse_Fxns.Erosion.SedDelivRatio import SedDelivRatio
from .MultiUse_Fxns.Erosion.Erosion_1 import Erosion_1_f
from .Output.Loading.SedYield import SedYield_f
from .Output.Loading.LuLoad import LuLoad_f
from .Output.Loading.LuDisLoad import LuDisLoad_f
from .MultiUse_Fxns.Erosion.LuErosion import LuErosion_f
from .MultiUse_Fxns.Runoff.nRunoff import nRunoff_f
from .MultiUse_Fxns.Runoff.pRunoff import pRunoff_f
from .Output.Loading.DisLoad import DisLoad_f
from .Output.Loading.Load import Load_f


def CalculateLoads(z, Y):
    GroundWatLETotal = zeros(z.WxYrs)
    SedYieldTotal = 0
    ErosionTotal = 0
    DisNitrTotal = 0
    DisPhosTotal = 0
    TotNitrTotal = 0
    TotPhosTotal = 0
    AnimalFCTotal = 0
    WWOrgsTotal = 0
    SSOrgsTotal = 0
    UrbOrgsTotal = 0
    WildOrgsTotal = 0
    TotalOrgsTotal = 0
    CMStreamTotal = 0
    OrgConcTotal = 0

    # ANNUAL WATER BALANCE CALCULATIONS
    for i in range(12):
        # Calculate landuse runoff for rural areas
        GroundWatLETotal += \
            GroundWatLE_1_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                            z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
                            z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap,
                            z.SatStor_0, z.RecessionCoef, z.SeepCoef,
                            z.Landuse, z.TileDrainDensity)[Y][i]

    # CALCULATE ANNUAL NITROGEN  LOADS FROM NORMAL SEPTIC SYSTEMS
    AnNormNitr = 0
    for i in range(12):
        AnNormNitr += z.MonthNormNitr[i] * z.NumNormalSys[i]

    z.CalendarYr = z.WxYrBeg + (Y - 1)

    # SEDIMENT YIELD AND TILE DRAINAGE
    for i in range(12):
        SedYieldTotal += \
            SedYield_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.Acoef, z.NRur, z.KF, z.LS, z.C, z.P,
                       z.Area, z.NUrb, z.CNI_0, z.AntMoist_0, z.Grow_0, z.ISRR, z.ISRA, z.Qretention, z.PctAreaInfil,
                       z.n25b, z.CN, z.CNP_0, z.Imper, z.SedDelivRatio_0)[Y][i]
        ErosionTotal += \
            Erosion_1_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                        z.AntMoist_0,
                        z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs,
                        z.MaxWaterCap, z.SatStor_0,
                        z.RecessionCoef, z.SeepCoef, z.Qretention, z.PctAreaInfil, z.n25b, z.Landuse,
                        z.TileDrainDensity, z.PointFlow,
                        z.StreamWithdrawal, z.GroundWithdrawal, z.NumAnimals, z.AvgAnimalWt, z.StreamFlowVolAdj,
                        z.SedAFactor_0,
                        z.AvKF, z.AvSlope, z.SedAAdjust, z.StreamLength, z.n42b, z.n46c, z.n85d, z.AgLength, z.n42,
                        z.n45, z.n85, z.UrbBankStab,
                        z.SedDelivRatio_0, z.Acoef, z.KF, z.LS, z.C, z.P)[Y][i]

        # CALCULATION OF THE LANDUSE EROSION AND SEDIMENT YIELDS
        for l in range(z.NRur):
            z.LuSedYield[Y][l] = \
                LuErosion_f(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.Acoef, z.KF, z.LS,
                            z.C, z.P, z.Area)[Y][l] * SedDelivRatio(z.SedDelivRatio_0)
            z.DisNitr[Y][i] += \
                nRunoff_f(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.AntMoist_0, z.NRur, z.NUrb, z.CN,
                          z.Grow_0,
                          z.Area, z.NitrConc, z.ManNitr, z.ManuredAreas, z.FirstManureMonth, z.LastManureMonth,
                          z.FirstManureMonth2, z.LastManureMonth2)[Y][i][l]
            z.DisPhos[Y][i] += \
                pRunoff_f(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.AntMoist_0, z.NRur, z.NUrb, z.CN,
                          z.Grow_0,
                          z.Area, z.PhosConc, z.ManuredAreas, z.FirstManureMonth, z.LastManureMonth, z.ManPhos,
                          z.FirstManureMonth2, z.LastManureMonth2)[Y][i][l]
            z.LuDisNitr[Y][l] += \
                nRunoff_f(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.AntMoist_0, z.NRur, z.NUrb, z.CN,
                          z.Grow_0,
                          z.Area, z.NitrConc, z.ManNitr, z.ManuredAreas, z.FirstManureMonth, z.LastManureMonth,
                          z.FirstManureMonth2, z.LastManureMonth2)[Y][i][l]
            z.LuDisPhos[Y][l] += \
                pRunoff_f(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.AntMoist_0, z.NRur, z.NUrb, z.CN,
                          z.Grow_0,
                          z.Area, z.PhosConc, z.ManuredAreas, z.FirstManureMonth, z.LastManureMonth, z.ManPhos,
                          z.FirstManureMonth2, z.LastManureMonth2)[Y][i][l]

        z.TotNitr[Y][i] = z.DisNitr[Y][i] + 0.001 * z.SedNitr * \
                          SedYield_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.Acoef, z.NRur, z.KF, z.LS,
                                     z.C, z.P,
                                     z.Area, z.NUrb, z.CNI_0, z.AntMoist_0, z.Grow_0, z.ISRR, z.ISRA, z.Qretention,
                                     z.PctAreaInfil,
                                     z.n25b, z.CN, z.CNP_0, z.Imper, z.SedDelivRatio_0)[Y][i]
        z.TotPhos[Y][i] = z.DisPhos[Y][i] + 0.001 * z.SedPhos * \
                          SedYield_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.Acoef, z.NRur, z.KF, z.LS,
                                     z.C, z.P,
                                     z.Area, z.NUrb, z.CNI_0, z.AntMoist_0, z.Grow_0, z.ISRR, z.ISRA, z.Qretention,
                                     z.PctAreaInfil,
                                     z.n25b, z.CN, z.CNP_0, z.Imper, z.SedDelivRatio_0)[Y][i]

        # SUM TILE DRAIN N, P, AND SEDIMENT
        z.TileDrainN[Y][i] += ((((TileDrain_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
                                              z.CNI_0,
                                              z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
                                              z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs,
                                              z.MaxWaterCap, z.SatStor_0,
                                              z.RecessionCoef, z.SeepCoef, z.Landuse,
                                              z.TileDrainDensity)[Y][i] / 100) * TotAreaMeters(z.NRur, z.NUrb,
                                                                                               z.Area)) * 1000) * z.TileNconc) / 1000000
        z.TileDrainP[Y][i] += ((((TileDrain_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
                                              z.CNI_0,
                                              z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
                                              z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs,
                                              z.MaxWaterCap, z.SatStor_0,
                                              z.RecessionCoef, z.SeepCoef, z.Landuse,
                                              z.TileDrainDensity)[Y][i] / 100) * TotAreaMeters(z.NRur, z.NUrb,
                                                                                               z.Area)) * 1000) * z.TilePConc) / 1000000
        z.TileDrainSed[Y][i] += ((((TileDrain_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb,
                                                z.Area, z.CNI_0,
                                                z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
                                                z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs,
                                                z.MaxWaterCap, z.SatStor_0,
                                                z.RecessionCoef, z.SeepCoef, z.Landuse,
                                                z.TileDrainDensity)[Y][i] / 100) * TotAreaMeters(z.NRur, z.NUrb,

                                                                                                 z.Area)) * 1000) * z.TileSedConc) / 1000000
        z.LuDisNitr[Y, z.NRur:] += \
            LuDisLoad_f(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.Nqual, z.NRur, z.NUrb, z.Area, z.CNI_0,
                        z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention, z.PctAreaInfil,
                        z.LoadRateImp, z.LoadRatePerv, z.Storm, z.UrbBMPRed, z.DisFract,
                        z.FilterWidth, z.PctStrmBuf)[Y, :, 0] / z.NYrs / 2
        z.LuDisPhos[Y, z.NRur:] += \
            LuDisLoad_f(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.Nqual, z.NRur, z.NUrb, z.Area, z.CNI_0,
                        z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention, z.PctAreaInfil,
                        z.LoadRateImp, z.LoadRatePerv, z.Storm, z.UrbBMPRed, z.DisFract,
                        z.FilterWidth, z.PctStrmBuf)[Y, :, 1] / z.NYrs / 2
        z.LuSedYield[Y, z.NRur:] += (LuLoad_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
                                              z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA,
                                              z.Qretention, z.PctAreaInfil, z.Nqual, z.LoadRateImp, z.LoadRatePerv,
                                              z.Storm, z.UrbBMPRed,
                                              z.FilterWidth, z.PctStrmBuf)[Y, :, 2] / z.NYrs) / 1000 / 2

        z.DisNitr[Y][i] += \
        DisLoad_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0,
                  z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention, z.PctAreaInfil, z.Nqual, z.LoadRateImp,
                  z.LoadRatePerv, z.Storm, z.UrbBMPRed, z.DisFract, z.FilterWidth, z.PctStrmBuf)[Y][i][0]
        z.DisPhos[Y][i] += \
        DisLoad_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0,
                  z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention, z.PctAreaInfil, z.Nqual, z.LoadRateImp,
                  z.LoadRatePerv, z.Storm, z.UrbBMPRed, z.DisFract, z.FilterWidth, z.PctStrmBuf)[Y][i][1]
        z.TotNitr[Y][i] += \
        Load_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0,
               z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention, z.PctAreaInfil, z.Nqual, z.LoadRateImp,
               z.LoadRatePerv, z.Storm, z.UrbBMPRed, z.DisFract, z.FilterWidth, z.PctStrmBuf)[Y][i][0]
        z.TotPhos[Y][i] += \
        Load_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0,
               z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention, z.PctAreaInfil, z.Nqual, z.LoadRateImp,
               z.LoadRatePerv, z.Storm, z.UrbBMPRed, z.DisFract, z.FilterWidth, z.PctStrmBuf)[Y][i][1]

        # ADD UPLAND N and P LOADS
        z.UplandN[Y][i] = z.TotNitr[Y][i]
        z.UplandP[Y][i] = z.TotPhos[Y][i]

        # ADD GROUNDWATER, POINT SOURCES,
        z.GroundNitr[Y][i] = 0.1 * z.GrNitrConc * \
                             GroundWatLE_1_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
                                             z.CNI_0,
                                             z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
                                             z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs,
                                             z.MaxWaterCap,
                                             z.SatStor_0, z.RecessionCoef, z.SeepCoef,
                                             z.Landuse, z.TileDrainDensity)[Y][i] * AreaTotal_f(z.Area)
        z.GroundPhos[Y][i] = 0.1 * z.GrPhosConc * \
                             GroundWatLE_1_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
                                             z.CNI_0,
                                             z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
                                             z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs,
                                             z.MaxWaterCap,
                                             z.SatStor_0, z.RecessionCoef, z.SeepCoef,
                                             z.Landuse, z.TileDrainDensity)[Y][i] * AreaTotal_f(z.Area)
        z.DisNitr[Y][i] += z.GroundNitr[Y][i] + z.PointNitr[i]
        z.DisPhos[Y][i] += z.GroundPhos[Y][i] + z.PointPhos[i]
        z.TotNitr[Y][i] += z.GroundNitr[Y][i] + z.PointNitr[i]
        z.TotPhos[Y][i] += z.GroundPhos[Y][i] + z.PointPhos[i]

        # ADD SEPTIC SYSTEM SOURCES TO MONTHLY DISSOLVED NUTRIENT TOTALS
        if GroundWatLETotal[Y] <= 0:
            GroundWatLETotal[Y] = 0.0001

        z.MonthNormNitr[i] = AnNormNitr * \
                             GroundWatLE_1_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
                                             z.CNI_0,
                                             z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
                                             z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs,
                                             z.MaxWaterCap,
                                             z.SatStor_0, z.RecessionCoef, z.SeepCoef,
                                             z.Landuse, z.TileDrainDensity)[Y][i] / GroundWatLETotal[Y]

        z.DisSeptNitr = (z.MonthNormNitr[i]
                         + z.MonthPondNitr[i]
                         + z.MonthShortNitr[i] * z.NumShortSys[i]
                         + z.MonthDischargeNitr[i] * z.NumDischargeSys[i])

        z.DisSeptPhos = (z.MonthPondPhos[i]
                         + z.MonthShortPhos[i] * z.NumShortSys[i]
                         + z.MonthDischargePhos[i] * z.NumDischargeSys[i])

        # 0.59 IS ATTENUATION FACTOR FOR SOIL LOSS
        # 0.66 IS ATTENUATION FACTOR FOR SUBSURFACE FLOW LOSS
        z.DisSeptNitr = z.DisSeptNitr / 1000 * 0.59 * 0.66
        z.DisSeptPhos = z.DisSeptPhos / 1000

        z.DisNitr[Y][i] += z.DisSeptNitr
        z.DisPhos[Y][i] += z.DisSeptPhos
        z.TotNitr[Y][i] += z.DisSeptNitr
        z.TotPhos[Y][i] += z.DisSeptPhos
        z.SepticN[Y][i] += z.DisSeptNitr
        z.SepticP[Y][i] += z.DisSeptPhos

        # ANNUAL TOTALS
        DisNitrTotal += z.DisNitr[Y][i]
        DisPhosTotal += z.DisPhos[Y][i]
        TotNitrTotal += z.TotNitr[Y][i]
        TotPhosTotal += z.TotPhos[Y][i]

        # UPDATE ANNUAL SEPTIC SYSTEM LOADS
        z.SepticNitr[Y] += z.DisSeptNitr
        z.SepticPhos[Y] += z.DisSeptPhos

        # Annual pathogen totals
        AnimalFCTotal += z.AnimalFC[Y][i]
        WWOrgsTotal += z.WWOrgs[Y][i]
        SSOrgsTotal += z.SSOrgs[Y][i]
        UrbOrgsTotal += z.UrbOrgs[Y][i]
        WildOrgsTotal += z.WildOrgs[Y][i]
        TotalOrgsTotal += z.TotalOrgs[Y][i]
        CMStreamTotal += z.CMStream[Y][i]
        OrgConcTotal += z.OrgConc[Y][i]
