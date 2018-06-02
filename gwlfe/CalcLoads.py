# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

"""
Imported from CalcLoads.bas
"""

import logging

import numpy as np

log = logging.getLogger(__name__)

from Memoization import memoize
from AreaTotal import AreaTotal_2
from GroundWatLE_2 import GroundWatLE_2
from TileDrain import TileDrain_2
from TotAreaMeters import TotAreaMeters
from SedDelivRatio import SedDelivRatio
from Erosion_1 import Erosion_1_2
from SedYield import SedYield_2
from RurQRunoff import RurQRunoff_2
from ErosWashoff import ErosWashoff_2
from ErosWashoff import ErosWashoff
from UrbQRunoff import UrbQRunoff_2
from UrbQRunoff import UrbQRunoff
from LuLoad import LuLoad_2
from LuLoad import LuLoad
from LuDisLoad import LuDisLoad_2
from LuDisLoad import LuDisLoad
from LuErosion import LuErosion_2
from nRunoff import nRunoff
from pRunoff import pRunoff


def CalculateLoads(z, Y):
    # PrecipitationTotal = 0
    # RunoffTotal = 0
    GroundWatLETotal = np.zeros(z.WxYrs)
    # EvapotransTotal = 0
    # PtSrcFlowTotal = 0
    # WithdrawalTotal = 0
    # StreamFlowTotal = 0
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

    # CALCULATE THE MONTHLY WATER BALANCE FOR STREAM Flow FOR EACH YEAR OF THE ANALYSIS
    # for i in range(12):
    # z.StreamFlow[Y][i] = (z.Runoff[Y][i]
    #                       + z.GroundWatLE_2[Y][i]
    #                       + z.PtSrcFlow[Y][i]
    #                       + z.TileDrain[Y][i]
    #                       - z.Withdrawal[Y][i])
    #
    # print("StreamFlow orig = ", z.StreamFlow[Y][i], "StreamFlow new = ", z.StreamFlow_temp[Y][i])
    # print(z.StreamFlow[Y][i] == z.StreamFlow_temp[Y][i])

    # z.StreamFlowLE[Y][i] = z.StreamFlow[Y][i]
    # if z.StreamFlowLE[Y][i] < 0:
    #     z.StreamFlowLE[Y][i] = 0

    # ANNUAL WATER BALANCE CALCULATIONS
    for i in range(12):
        # Calculate landuse runoff for rural areas
        # for l in range(z.NRur):
        #     z.LuRunoff[Y][l] += \
        #         RurQRunoff_2(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.AntMoist_0, z.NRur, z.NUrb, z.CN,
        #                    z.Grow_0)[Y][l][i]
        # print("RurQRunoff old = ", z.RurQRunoff[l][i], "RurQRunoff new = ", z.RurQRunoff_temp[Y][l][i])
        # print(z.RurQRunoff[l][i] == z.RurQRunoff_temp[Y][l][i])

        # # Calculate landuse runoff for urban areas
        # for l in range(z.NRur, z.NLU):
        #     z.LuRunoff[Y][l] += \
        #         UrbQRunoff_2(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.NUrb, z.CNI_0, z.CNP_0,
        #                    z.AntMoist_0, z.Grow_0, z.Imper, z.ISRR, z.ISRA)[Y][l][i]

        # PrecipitationTotal += z.Precipitation[Y][i]
        # RunoffTotal += z.Runoff[Y][i]
        GroundWatLETotal += \
            GroundWatLE_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                          z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
                          z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap,
                          z.SatStor_0, z.RecessionCoef, z.SeepCoef,
                          z.Landuse, z.TileDrainDensity)[Y][i]
        # EvapotransTotal += z.Evapotrans[Y][i]
        # PtSrcFlowTotal += z.PtSrcFlow[Y][i]
        # WithdrawalTotal += z.Withdrawal[Y][i]
        # StreamFlowTotal += z.StreamFlow[Y][i]

    # CALCULATE ANNUAL NITROGEN  LOADS FROM NORMAL SEPTIC SYSTEMS
    AnNormNitr = 0
    for i in range(12):
        AnNormNitr += z.MonthNormNitr[i] * z.NumNormalSys[i]

    z.CalendarYr = z.WxYrBeg + (Y - 1)

    # print("AdjQTotal = ", np.sum(z.AdjQTotal[Y][i]))
    # print("SedTrans orig = ", z.SedTrans[Y][i], "SedTrans new = ", z.SedTrans_temp[Y][i])
    # print(z.SedTrans[Y][i] == z.SedTrans_temp[Y][i])

    # SEDIMENT YIELD AND TILE DRAINAGE
    for i in range(12):
        # z.BSed[i] = 0
        # for m in range(i, 12):
        #     z.BSed[i] += z.SedTrans[Y][m]
        # for m in range(i + 1):
        #     if z.BSed[Y][m] > 0:
        #         z.SedYield[Y][i] += z.Erosion[Y][m] / z.BSed[Y][m]
        #
        # z.SedYield[Y][i] = z.SedDelivRatio * z.SedTrans[Y][i] * z.SedYield[Y][i]

        SedYieldTotal += \
            SedYield_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.Acoef, z.NRur, z.KF, z.LS, z.C, z.P,
                       z.Area, z.NUrb, z.CNI_0, z.AntMoist_0, z.Grow_0, z.ISRR, z.ISRA, z.Qretention, z.PctAreaInfil,
                       z.n25b, z.CN, z.CNP_0, z.Imper, z.SedDelivRatio_0)[Y][i]
        ErosionTotal += \
            Erosion_1_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
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
            # z.LuErosion[Y][l] += \
            #     ErosWashoff_2(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.Acoef, z.KF, z.LS,
            #                   z.C, z.P, z.Area)[Y][l][i]
            z.LuSedYield[Y][l] = \
                LuErosion_2(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.Acoef, z.KF, z.LS,
                            z.C, z.P, z.Area)[Y][l] * SedDelivRatio(z.SedDelivRatio_0)
            # print("ErosWashoff old = ", z.ErosWashoff[l][i], "ErosWashoff new = ", z.ErosWashoff_temp[Y][l][i])
            # print(z.ErosWashoff[l][i] == z.ErosWashoff_temp[Y][l][i])

            # # Add in the urban calucation for sediment
            # for l in range(z.NRur, z.NLU):
            #     z.UrbSedLoad[l][i] += \
            #         LuLoad_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
            #                  z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention, z.PctAreaInfil,
            #                  z.Nqual, z.LoadRateImp, z.LoadRatePerv, z.Storm, z.UrbBMPRed,
            #                  z.FilterWidth, z.PctStrmBuf)[Y][l][2]

            # NUTRIENT FLUXES
            # for i in range(12):
            #     for l in range(z.NRur):
            #         # RURAL DISSOLVED NUTRIENTS
            #         # z.NConc = z.NitrConc[l]
            #         z.PConc = z.PhosConc[l]
            #
            #         # MANURE SPREADING DAYS FOR FIRST SPREADING PERIOD
            #         if l < z.ManuredAreas and i >= z.FirstManureMonth and i <= z.LastManureMonth:
            #             # z.NConc = z.ManNitr[l]
            #             z.PConc = z.ManPhos[l]
            #
            #         # MANURE SPREADING DAYS FOR SECOND SPREADING PERIOD
            #         if l < z.ManuredAreas and i >= z.FirstManureMonth2 and i <= z.LastManureMonth2:
            #             # z.NConc = z.ManNitr[l]
            #             z.PConc = z.ManPhos[l]

            # nRunoff = 0.1 * z.NConc * \
            #           RurQRunoff_2(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.AntMoist_0, z.NRur, z.NUrb,
            #                        z.CN,
            #                        z.Grow_0)[Y][l][i] * z.Area[l]
            # pRunoff = 0.1 * z.PConc * \
            #           RurQRunoff_2(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.AntMoist_0, z.NRur, z.NUrb,
            #                        z.CN,
            #                        z.Grow_0)[Y][l][i] * z.Area[l]

            z.DisNitr[Y][i] += \
                nRunoff(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.AntMoist_0, z.NRur, z.NUrb, z.CN, z.Grow_0,
                        z.Area, z.NitrConc, z.ManNitr, z.ManuredAreas, z.FirstManureMonth, z.LastManureMonth,
                        z.FirstManureMonth2, z.LastManureMonth2)[Y][i]
            z.DisPhos[Y][i] += \
                pRunoff(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.AntMoist_0, z.NRur, z.NUrb, z.CN, z.Grow_0,
                        z.Area, z.PhosConc, z.ManuredAreas, z.FirstManureMonth, z.LastManureMonth, z.ManPhos,
                        z.FirstManureMonth2, z.LastManureMonth2)[Y][i]
            # z.LuTotNitr[Y][l] += \
            #     nRunoff(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.AntMoist_0, z.NRur, z.NUrb, z.CN, z.Grow_0,
            #             z.Area, z.NitrConc, z.ManNitr, z.ManuredAreas, z.FirstManureMonth, z.LastManureMonth,
            #             z.FirstManureMonth2, z.LastManureMonth2)[Y][i]
            # z.LuTotPhos[Y][l] += \
            #     pRunoff(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.AntMoist_0, z.NRur, z.NUrb, z.CN, z.Grow_0,
            #             z.Area, z.PhosConc, z.ManuredAreas, z.FirstManureMonth, z.LastManureMonth, z.ManPhos,
            #             z.FirstManureMonth2, z.LastManureMonth2)[Y][i]
            z.LuDisNitr[Y][l] += \
                nRunoff(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.AntMoist_0, z.NRur, z.NUrb, z.CN, z.Grow_0,
                        z.Area, z.NitrConc, z.ManNitr, z.ManuredAreas, z.FirstManureMonth, z.LastManureMonth,
                        z.FirstManureMonth2, z.LastManureMonth2)[Y][i]
            z.LuDisPhos[Y][l] += \
                pRunoff(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.AntMoist_0, z.NRur, z.NUrb, z.CN, z.Grow_0,
                        z.Area, z.PhosConc, z.ManuredAreas, z.FirstManureMonth, z.LastManureMonth, z.ManPhos,
                        z.FirstManureMonth2, z.LastManureMonth2)[Y][i]

            # ADD SOLID RURAL NUTRIENTS
            # z.LuTotNitr[Y][l] += 0.001 * SedDelivRatio(z.SedDelivRatio_0) * \
            #                      ErosWashoff(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.NUrb, z.Acoef,
            #                                  z.KF, z.LS,
            #                                  z.C, z.P, z.Area)[Y][l][i] * z.SedNitr
            # z.LuTotPhos[Y][l] += 0.001 * SedDelivRatio(z.SedDelivRatio_0) * \
            #                      ErosWashoff(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.NUrb,z.Acoef,
            #                                  z.KF, z.LS,
            #                                  z.C, z.P, z.Area)[Y][l][i] * z.SedPhos

        z.TotNitr[Y][i] = z.DisNitr[Y][i] + 0.001 * z.SedNitr * \
                          SedYield_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.Acoef, z.NRur, z.KF, z.LS,
                                     z.C, z.P,
                                     z.Area, z.NUrb, z.CNI_0, z.AntMoist_0, z.Grow_0, z.ISRR, z.ISRA, z.Qretention,
                                     z.PctAreaInfil,
                                     z.n25b, z.CN, z.CNP_0, z.Imper, z.SedDelivRatio_0)[Y][i]
        z.TotPhos[Y][i] = z.DisPhos[Y][i] + 0.001 * z.SedPhos * \
                          SedYield_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.Acoef, z.NRur, z.KF, z.LS,
                                     z.C, z.P,
                                     z.Area, z.NUrb, z.CNI_0, z.AntMoist_0, z.Grow_0, z.ISRR, z.ISRA, z.Qretention,
                                     z.PctAreaInfil,
                                     z.n25b, z.CN, z.CNP_0, z.Imper, z.SedDelivRatio_0)[Y][i]

        # SUM TILE DRAIN N, P, AND SEDIMENT
        z.TileDrainN[Y][i] += ((((TileDrain_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
                                              z.CNI_0,
                                              z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
                                              z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs,
                                              z.MaxWaterCap, z.SatStor_0,
                                              z.RecessionCoef, z.SeepCoef, z.Landuse,
                                              z.TileDrainDensity)[Y][i] / 100) * TotAreaMeters(z.NRur, z.NUrb,
                                                                                               z.Area)) * 1000) * z.TileNconc) / 1000000
        z.TileDrainP[Y][i] += ((((TileDrain_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
                                              z.CNI_0,
                                              z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
                                              z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs,
                                              z.MaxWaterCap, z.SatStor_0,
                                              z.RecessionCoef, z.SeepCoef, z.Landuse,
                                              z.TileDrainDensity)[Y][i] / 100) * TotAreaMeters(z.NRur, z.NUrb,
                                                                                               z.Area)) * 1000) * z.TilePConc) / 1000000
        z.TileDrainSed[Y][i] += ((((TileDrain_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb,
                                                z.Area, z.CNI_0,
                                                z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
                                                z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs,
                                                z.MaxWaterCap, z.SatStor_0,
                                                z.RecessionCoef, z.SeepCoef, z.Landuse,
                                                z.TileDrainDensity)[Y][i] / 100) * TotAreaMeters(z.NRur, z.NUrb,
                                                                                                 z.Area)) * 1000) * z.TileSedConc) / 1000000

        # ADD URBAN NUTRIENTS
        # for l in range(z.NRur, z.NLU):
        # z.LuTotNitr[Y][l] += \
        #     LuLoad(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0,
        #            z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention, z.PctAreaInfil, z.Nqual, z.LoadRateImp,
        #            z.LoadRatePerv, z.Storm, z.UrbBMPRed,
        #            z.FilterWidth, z.PctStrmBuf)[Y][l][0] / z.NYrs / 2
        # z.LuTotPhos[Y][l] += \
        #     LuLoad(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0,
        #            z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention, z.PctAreaInfil, z.Nqual, z.LoadRateImp,
        #            z.LoadRatePerv, z.Storm, z.UrbBMPRed,
        #            z.FilterWidth, z.PctStrmBuf)[Y][l][1] / z.NYrs / 2
        z.LuDisNitr[:, z.NRur:] += \
            LuDisLoad_2(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.Nqual, z.NRur, z.NUrb, z.Area, z.CNI_0,
                        z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention, z.PctAreaInfil,
                        z.LoadRateImp, z.LoadRatePerv, z.Storm, z.UrbBMPRed, z.DisFract, z.FilterWidth, z.PctStrmBuf)[:,
            :, 0] / z.NYrs / 2
        z.LuDisPhos[:, z.NRur:] += \
            LuDisLoad_2(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.Nqual, z.NRur, z.NUrb, z.Area, z.CNI_0,
                        z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention, z.PctAreaInfil,
                        z.LoadRateImp, z.LoadRatePerv, z.Storm, z.UrbBMPRed, z.DisFract, z.FilterWidth, z.PctStrmBuf)[:, :, 1] / z.NYrs / 2
        z.LuSedYield[:, z.NRur:] += (LuLoad_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
                                              z.CNI_0, z.AntMoist_0,
                                              z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention, z.PctAreaInfil,
                                              z.Nqual, z.LoadRateImp,
                                              z.LoadRatePerv, z.Storm, z.UrbBMPRed,
                                              z.FilterWidth, z.PctStrmBuf)[:, :, 2] / z.NYrs) / 1000 / 2

        z.DisNitr[Y][i] += z.DisLoad[Y][i][0]
        z.DisPhos[Y][i] += z.DisLoad[Y][i][1]
        z.TotNitr[Y][i] += z.Load[Y][i][0]
        z.TotPhos[Y][i] += z.Load[Y][i][1]

        # ADD UPLAND N and P LOADS
        z.UplandN[Y][i] = z.TotNitr[Y][i]
        z.UplandP[Y][i] = z.TotPhos[Y][i]

        # ADD GROUNDWATER, POINT SOURCES,
        z.GroundNitr[Y][i] = 0.1 * z.GrNitrConc * \
                             GroundWatLE_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
                                           z.CNI_0,
                                           z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
                                           z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap,
                                           z.SatStor_0, z.RecessionCoef, z.SeepCoef,
                                           z.Landuse, z.TileDrainDensity)[Y][i] * AreaTotal_2(z.Area)
        z.GroundPhos[Y][i] = 0.1 * z.GrPhosConc * \
                             GroundWatLE_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
                                           z.CNI_0,
                                           z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
                                           z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap,
                                           z.SatStor_0, z.RecessionCoef, z.SeepCoef,
                                           z.Landuse, z.TileDrainDensity)[Y][i] * AreaTotal_2(z.Area)
        z.DisNitr[Y][i] += z.GroundNitr[Y][i] + z.PointNitr[i]
        z.DisPhos[Y][i] += z.GroundPhos[Y][i] + z.PointPhos[i]
        z.TotNitr[Y][i] += z.GroundNitr[Y][i] + z.PointNitr[i]
        z.TotPhos[Y][i] += z.GroundPhos[Y][i] + z.PointPhos[i]

        # ADD SEPTIC SYSTEM SOURCES TO MONTHLY DISSOLVED NUTRIENT TOTALS
        if GroundWatLETotal[Y] <= 0:
            GroundWatLETotal[Y] = 0.0001

        z.MonthNormNitr[i] = AnNormNitr * \
                             GroundWatLE_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
                                           z.CNI_0,
                                           z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
                                           z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap,
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

        # CALCULATE THE VOLUMETRIC STREAM Flow
        # z.StreamFlowVol[Y][i] = ((z.StreamFlowLE[Y][i] / 100) * z.TotAreaMeters) / (86400 * z.DaysMonth[Y][i])
