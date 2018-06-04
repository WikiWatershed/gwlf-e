# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

"""
Imported from AnnualMeans.bas
"""

import logging
from Precipitation import AvPrecipitation_2
from AvEvapoTrans import AvEvapoTrans_2
from PtSrcFlow import AvPtSrcFlow_2
from AvStreamBankEros import AvStreamBankEros_2
from StreamBankN_1 import StreamBankN_1_2
from AvTileDrain import AvTileDrain_2
from AvWithdrawal import AvWithdrawal_2
from AvGroundWater import AvGroundWater_2
from AvRunoff import AvRunoff_2
from AvErosion import AvErosion_2
from AvSedYield import AvSedYield_2
import numpy as np
from LuRunoff import LuRunoff_2
from LuTotPhos import LuTotPhos

log = logging.getLogger(__name__)


def CalculateAnnualMeanLoads(z, Y):
    # UPDATE SEPTIC SYSTEM AVERAGES
    z.AvSeptNitr += z.SepticNitr[Y] / z.NYrs
    z.AvSeptPhos += z.SepticPhos[Y] / z.NYrs

    # Add the Stream Bank Erosion to sediment yield
    # for i in range(12):
    #     z.SedYield[Y][i] += z.StreamBankEros_2[Y][i] / 1000

    z.CalendarYr = z.WxYrBeg + (Y - 1)

    # CALCULATE ANNUAL MEANS FOR STREAM BANK AND TILE DRAINAGE VALUES
    # z.AvPtSrcFlow = AvPtSrcFlow(z.NYrs,z.PtSrcFlow)
    z.AvPtSrcFlow = AvPtSrcFlow_2(z.PointFlow)
    for i in range(12):
        z.AvStreamBankP[i] += z.StreamBankP[Y][i] / z.NYrs
        z.AvTileDrainN[i] += z.TileDrainN[Y][i] / z.NYrs
        z.AvTileDrainP[i] += z.TileDrainP[Y][i] / z.NYrs
        z.AvTileDrainSed[i] += z.TileDrainSed[Y][i] / z.NYrs

    # COMPUTE ANNUAL MEANS
    z.AvPrecipitation = AvPrecipitation_2(z.Prec)
    for i in range(12):
        z.AvDisNitr[i] += z.DisNitr[Y][i] / z.NYrs
        z.AvTotNitr[i] += z.TotNitr[Y][i] / z.NYrs
        z.AvDisPhos[i] += z.DisPhos[Y][i] / z.NYrs
        z.AvTotPhos[i] += z.TotPhos[Y][i] / z.NYrs
        z.AvGroundNitr[i] += z.GroundNitr[Y][i] / z.NYrs
        z.AvGroundPhos[i] += z.GroundPhos[Y][i] / z.NYrs
        # z.AvAnimalN[i] += z.AnimalN[Y][i] / z.NYrs
        z.AvAnimalP[i] += z.AnimalP[Y][i] / z.NYrs

        # z.AvGRLostBarnN[i] += z.GRLostBarnN[Y][i] / z.NYrs
        z.AvGRLostBarnP[i] += z.GRLostBarnP[Y][i] / z.NYrs
        z.AvGRLostBarnFC[i] += z.GRLostBarnFC[Y][i] / z.NYrs

        # z.AvNGLostBarnN[i] += z.NGLostBarnN[Y][i] / z.NYrs
        z.AvNGLostBarnP[i] += z.NGLostBarnP[Y][i] / z.NYrs
        z.AvNGLostBarnFC[i] += z.NGLostBarnFC[Y][i] / z.NYrs

        z.AvNGLostManP[i] += z.NGLostManP[Y][i] / z.NYrs

        # Average pathogen totals
        z.AvAnimalFC[i] += z.AnimalFC[Y][i] / z.NYrs
        z.AvWWOrgs[i] += z.WWOrgs[Y][i] / z.NYrs
        z.AvSSOrgs[i] += z.SSOrgs[Y][i] / z.NYrs
        z.AvUrbOrgs[i] += z.UrbOrgs[Y][i] / z.NYrs
        z.AvWildOrgs[i] += z.WildOrgs[Y][i] / z.NYrs
        z.AvTotalOrgs[i] += z.TotalOrgs[Y][i] / z.NYrs

    # Average loads for each landuse
    for l in range(z.NRur):
        z.AvLuRunoff[l] += \
            LuRunoff_2(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.NUrb, z.CNI_0, z.CNP_0,
                       z.AntMoist_0, z.Grow_0, z.Imper, z.ISRR, z.ISRA, z.CN)[Y][l] / z.NYrs
        z.AvLuErosion[l] += \
            LuRunoff_2(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.NUrb, z.CNI_0, z.CNP_0,
                       z.AntMoist_0, z.Grow_0, z.Imper, z.ISRR, z.ISRA, z.CN)[Y][l] / z.NYrs
        z.AvLuSedYield[l] += z.LuSedYield[Y][l] / z.NYrs
        z.AvLuDisNitr[l] += z.LuDisNitr[Y][l] / z.NYrs
        z.AvLuTotNitr[l] += z.LuTotNitr[Y][l] / z.NYrs
        z.AvLuDisPhos[l] += z.LuDisPhos[Y][l] / z.NYrs
        z.AvLuTotPhos[l] += z.LuTotPhos[Y][l] / z.NYrs

    for l in range(z.NRur, z.NLU):
        z.AvLuRunoff[l] += \
            LuRunoff_2(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.NUrb, z.CNI_0, z.CNP_0,
                       z.AntMoist_0, z.Grow_0, z.Imper, z.ISRR, z.ISRA, z.CN)[Y][l] / z.NYrs
        z.AvLuTotNitr[l] += z.LuTotNitr[Y][l] / z.NYrs
        z.AvLuTotPhos[l] += z.LuTotPhos[Y][l] / z.NYrs
        z.AvLuDisNitr[l] += z.LuDisNitr[Y][l] / z.NYrs
        z.AvLuDisPhos[l] += z.LuDisPhos[Y][l] / z.NYrs
        z.AvLuSedYield[l] += z.LuSedYield[Y][l] / z.NYrs

    z.AvStreamBankErosSum = sum(
        AvStreamBankEros_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                           z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV,
                           z.PcntET,
                           z.DayHrs, z.MaxWaterCap, z.SatStor_0, z.RecessionCoef, z.SeepCoef, z.Qretention,
                           z.PctAreaInfil, z.n25b, z.Landuse, z.TileDrainDensity, z.PointFlow, z.StreamWithdrawal,
                           z.GroundWithdrawal, z.NumAnimals, z.AvgAnimalWt, z.StreamFlowVolAdj, z.SedAFactor_0, z.AvKF,
                           z.AvSlope, z.SedAAdjust, z.StreamLength, z.n42b, z.n46c, z.n85d, z.AgLength, z.n42, z.n45,
                           z.n85, z.UrbBankStab))
    # z.AvStreamBankNSum = sum(z.AvStreamBankN)
    z.AvStreamBankPSum = sum(z.AvStreamBankP)
    z.AvPtSrcFlowSum = sum(z.AvPtSrcFlow)
    z.AvTileDrainSum = sum(AvTileDrain_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
                                         z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
                                         z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap,
                                         z.SatStor_0, z.RecessionCoef, z.SeepCoef,
                                         z.Landuse, z.TileDrainDensity))
    z.AvWithdrawalSum = sum(AvWithdrawal_2(z.NYrs, z.StreamWithdrawal, z.GroundWithdrawal))
    z.AvTileDrainNSum = sum(z.AvTileDrainN)
    z.AvTileDrainPSum = sum(z.AvTileDrainP)
    z.AvTileDrainSedSum = sum(z.AvTileDrainSed)
    # z.AvPrecipitationSum = sum(z.AvPrecipitation)
    z.AvEvapoTransSum = sum(
        AvEvapoTrans_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0,
                       z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs,
                       z.MaxWaterCap))
    z.AvGroundWaterSum = sum(
        AvGroundWater_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                        z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET,
                        z.DayHrs, z.MaxWaterCap,
                        z.SatStor_0, z.RecessionCoef, z.SeepCoef, z.Landuse, z.TileDrainDensity))
    z.AvRunoffSum = sum(AvRunoff_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                                   z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention,
                                   z.PctAreaInfil,
                                   z.n25b, z.CN, z.Landuse, z.TileDrainDensity))
    z.AvErosionSum = sum(
        AvErosion_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0,
                                  z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap,
                                  z.SatStor_0, z.RecessionCoef, z.SeepCoef, z.Qretention, z.PctAreaInfil, z.n25b, z.Landuse, z.TileDrainDensity, z.PointFlow,
                                  z.StreamWithdrawal, z.GroundWithdrawal, z.NumAnimals, z.AvgAnimalWt, z.StreamFlowVolAdj, z.SedAFactor_0,
                                  z.AvKF, z.AvSlope, z.SedAAdjust, z.StreamLength, z.n42b, z.n46c, z.n85d, z.AgLength, z.n42, z.n45, z.n85, z.UrbBankStab,
                                  z.SedDelivRatio_0, z.Acoef, z.KF, z.LS, z.C, z.P))
    z.AvSedYieldSum = sum(
        AvSedYield_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                     z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV,
                     z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0, z.RecessionCoef, z.SeepCoef,
                     z.Qretention, z.PctAreaInfil, z.n25b, z.Landuse, z.TileDrainDensity, z.PointFlow,
                     z.StreamWithdrawal, z.GroundWithdrawal, z.NumAnimals, z.AvgAnimalWt,
                     z.StreamFlowVolAdj, z.SedAFactor_0, z.AvKF, z.AvSlope, z.SedAAdjust, z.StreamLength,
                     z.n42b, z.n46c, z.n85d, z.AgLength, z.n42, z.n45, z.n85, z.UrbBankStab, z.Acoef, z.KF,
                     z.LS, z.C, z.P, z.SedDelivRatio_0))
    z.AvDisNitrSum = sum(z.AvDisNitr)
    z.AvTotNitrSum = sum(z.AvTotNitr)
    z.AvDisPhosSum = sum(z.AvDisPhos)
    z.AvTotPhosSum = sum(z.AvTotPhos)
    z.AvGroundNitrSum = sum(z.AvGroundNitr)
    z.AvGroundPhosSum = sum(z.AvGroundPhos)
    # z.AvAnimalNSum = sum(z.AvAnimalN)
    z.AvAnimalPSum = sum(z.AvAnimalP)
    # z.AvGRLostBarnNSum = sum(z.AvGRLostBarnN)
    z.AvGRLostBarnPSum = sum(z.AvGRLostBarnP)
    z.AvGRLostBarnFCSum = sum(z.AvGRLostBarnFC)
    # z.AvNGLostBarnNSum = sum(z.AvNGLostBarnN)
    z.AvNGLostBarnPSum = sum(z.AvNGLostBarnP)
    z.AvNGLostBarnFCSum = sum(z.AvNGLostBarnFC)
    z.AvNGLostManPSum = sum(z.AvNGLostManP)
    z.AvAnimalFCSum = sum(z.AvAnimalFC)
    z.AvWWOrgsSum = sum(z.AvWWOrgs)
    z.AvSSOrgsSum = sum(z.AvSSOrgs)
    z.AvUrbOrgsSum = sum(z.AvUrbOrgs)
    z.AvWildOrgsSum = sum(z.AvWildOrgs)
    z.AvTotalOrgsSum = sum(z.AvTotalOrgs)
    z.AvLuRunoffSum = sum(z.AvLuRunoff)
    z.AvLuErosionSum = sum(z.AvLuErosion)
    z.AvLuSedYieldSum = sum(z.AvLuSedYield)
    z.AvLuDisNitrSum = sum(z.AvLuDisNitr)
    z.AvLuTotNitrSum = sum(z.AvLuTotNitr)
    z.AvLuDisPhosSum = sum(z.AvLuDisPhos)
    z.AvLuTotPhosSum = sum(z.AvLuTotPhos)
