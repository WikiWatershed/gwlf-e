# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

"""
Imported from AnnualMeans.bas
"""

import logging
from .Input.WaterBudget import Precipitation
from .Input.WaterBudget.AvEvapoTrans import AvEvapoTrans_f
from .MultiUse_Fxns.PtSrcFlow import AvPtSrcFlow_f
from .MultiUse_Fxns.Erosion.AvStreamBankEros import AvStreamBankEros_f
from .Input.LandUse.Ag.AvTileDrain import AvTileDrain_f
from .Input.WaterBudget.AvWithdrawal import AvWithdrawal_f
from .Input.WaterBudget.AvGroundWater import AvGroundWater_f
from .MultiUse_Fxns.Runoff.AvRunoff import AvRunoff_f
from .MultiUse_Fxns.Erosion.AvErosion import AvErosion_f
from .MultiUse_Fxns.Erosion.AvSedYield import AvSedYield_f
from .MultiUse_Fxns.Runoff.LuRunoff import LuRunoff_f
from .Output.Loading.LuTotPhos import LuTotPhos_f
from .Output.Loading.LuTotNitr import LuTotNitr_f

log = logging.getLogger(__name__)


def CalculateAnnualMeanLoads(z, Y):
    # UPDATE SEPTIC SYSTEM AVERAGES
    z.AvSeptNitr += z.SepticNitr[Y] / z.NYrs
    z.AvSeptPhos += z.SepticPhos[Y] / z.NYrs

    z.CalendarYr = z.WxYrBeg + (Y - 1)

    # CALCULATE ANNUAL MEANS FOR STREAM BANK AND TILE DRAINAGE VALUES
    z.AvPtSrcFlow = AvPtSrcFlow_f(z.PointFlow)
    for i in range(12):
        z.AvStreamBankP[i] += z.StreamBankP[Y][i] / z.NYrs
        z.AvTileDrainN[i] += z.TileDrainN[Y][i] / z.NYrs
        z.AvTileDrainP[i] += z.TileDrainP[Y][i] / z.NYrs
        z.AvTileDrainSed[i] += z.TileDrainSed[Y][i] / z.NYrs

    # COMPUTE ANNUAL MEANS
    z.AvPrecipitation = Precipitation.AvPrecipitation_f(Precipitation.Precipitation_f(z.Prec))
    for i in range(12):
        z.AvDisNitr[i] += z.DisNitr[Y][i] / z.NYrs
        z.AvTotNitr[i] += z.TotNitr[Y][i] / z.NYrs
        z.AvDisPhos[i] += z.DisPhos[Y][i] / z.NYrs
        z.AvTotPhos[i] += z.TotPhos[Y][i] / z.NYrs
        z.AvGroundNitr[i] += z.GroundNitr[Y][i] / z.NYrs
        z.AvGroundPhos[i] += z.GroundPhos[Y][i] / z.NYrs
        z.AvAnimalP[i] += z.AnimalP[Y][i] / z.NYrs

        z.AvGRLostBarnP[i] += z.GRLostBarnP[Y][i] / z.NYrs
        z.AvGRLostBarnFC[i] += z.GRLostBarnFC[Y][i] / z.NYrs

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
            LuRunoff_f(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.NUrb, z.CNI_0, z.CNP_0,
                       z.AntMoist_0, z.Grow_0, z.Imper, z.ISRR, z.ISRA, z.CN)[Y][l] / z.NYrs
        z.AvLuErosion[l] += \
            LuRunoff_f(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.NUrb, z.CNI_0, z.CNP_0,
                       z.AntMoist_0, z.Grow_0, z.Imper, z.ISRR, z.ISRA, z.CN)[Y][l] / z.NYrs
        z.AvLuSedYield[l] += z.LuSedYield[Y][l] / z.NYrs
        z.AvLuDisNitr[l] += z.LuDisNitr[Y][l] / z.NYrs
        z.AvLuTotNitr[l] += \
        LuTotNitr_f(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.AntMoist_0, z.NRur, z.NUrb, z.CN, z.Grow_0,
                    z.Area, z.NitrConc, z.ManNitr, z.ManuredAreas, z.FirstManureMonth, z.LastManureMonth,
                    z.FirstManureMonth2, z.LastManureMonth2, z.SedDelivRatio_0, z.KF, z.LS, z.C, z.P, z.SedNitr,
                    z.CNP_0, z.Imper, z.ISRR, z.ISRA,
                    z.Qretention, z.PctAreaInfil, z.LoadRateImp, z.LoadRatePerv, z.Storm, z.UrbBMPRed, z.FilterWidth,
                    z.PctStrmBuf, z.Acoef,
                    z.CNI_0, z.Nqual)[Y][l] / z.NYrs
        z.AvLuDisPhos[l] += z.LuDisPhos[Y][l] / z.NYrs
        z.AvLuTotPhos[l] += \
        LuTotPhos_f(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.AntMoist_0, z.NRur, z.NUrb, z.CN,
                    z.Grow_0, z.Area, z.PhosConc, z.ManPhos, z.ManuredAreas, z.FirstManureMonth,
                    z.LastManureMonth, z.FirstManureMonth2, z.LastManureMonth2, z.SedDelivRatio_0, z.KF,
                    z.LS, z.C, z.P, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention, z.PctAreaInfil, z.Nqual,
                    z.LoadRateImp, z.LoadRatePerv, z.Storm, z.UrbBMPRed, z.FilterWidth, z.PctStrmBuf,
                    z.Acoef, z.SedPhos, z.CNI_0)[Y][l] / z.NYrs

    for l in range(z.NRur, z.NLU):
        z.AvLuRunoff[l] += \
            LuRunoff_f(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.NUrb, z.CNI_0, z.CNP_0,
                       z.AntMoist_0, z.Grow_0, z.Imper, z.ISRR, z.ISRA, z.CN)[Y][l] / z.NYrs
        z.AvLuTotNitr[l] += \
        LuTotNitr_f(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.AntMoist_0, z.NRur, z.NUrb, z.CN, z.Grow_0,
                    z.Area, z.NitrConc, z.ManNitr, z.ManuredAreas, z.FirstManureMonth, z.LastManureMonth,
                    z.FirstManureMonth2, z.LastManureMonth2, z.SedDelivRatio_0, z.KF, z.LS, z.C, z.P, z.SedNitr,
                    z.CNP_0, z.Imper, z.ISRR, z.ISRA,
                    z.Qretention, z.PctAreaInfil, z.LoadRateImp, z.LoadRatePerv, z.Storm, z.UrbBMPRed, z.FilterWidth,
                    z.PctStrmBuf, z.Acoef,
                    z.CNI_0, z.Nqual)[Y][l] / z.NYrs
        z.AvLuTotPhos[l] += \
        LuTotPhos_f(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.AntMoist_0, z.NRur, z.NUrb, z.CN,
                    z.Grow_0, z.Area, z.PhosConc, z.ManPhos, z.ManuredAreas, z.FirstManureMonth,
                    z.LastManureMonth, z.FirstManureMonth2, z.LastManureMonth2, z.SedDelivRatio_0, z.KF,
                    z.LS, z.C, z.P, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention, z.PctAreaInfil, z.Nqual,
                    z.LoadRateImp, z.LoadRatePerv, z.Storm, z.UrbBMPRed, z.FilterWidth, z.PctStrmBuf,
                    z.Acoef, z.SedPhos, z.CNI_0)[Y][l] / z.NYrs
        z.AvLuDisNitr[l] += z.LuDisNitr[Y][l] / z.NYrs
        z.AvLuDisPhos[l] += z.LuDisPhos[Y][l] / z.NYrs
        z.AvLuSedYield[l] += z.LuSedYield[Y][l] / z.NYrs

    z.AvStreamBankErosSum = sum(
        AvStreamBankEros_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                           z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV,
                           z.PcntET,
                           z.DayHrs, z.MaxWaterCap, z.SatStor_0, z.RecessionCoef, z.SeepCoef, z.Qretention,
                           z.PctAreaInfil, z.n25b, z.Landuse, z.TileDrainDensity, z.PointFlow, z.StreamWithdrawal,
                           z.GroundWithdrawal, z.NumAnimals, z.AvgAnimalWt, z.StreamFlowVolAdj, z.SedAFactor_0, z.AvKF,
                           z.AvSlope, z.SedAAdjust, z.StreamLength, z.n42b, z.n46c, z.n85d, z.AgLength, z.n42, z.n45,
                           z.n85, z.UrbBankStab))
    z.AvStreamBankPSum = sum(z.AvStreamBankP)
    z.AvPtSrcFlowSum = sum(z.AvPtSrcFlow)
    z.AvTileDrainSum = sum(AvTileDrain_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
                                         z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
                                         z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap,
                                         z.SatStor_0, z.RecessionCoef, z.SeepCoef,
                                         z.Landuse, z.TileDrainDensity))
    z.AvWithdrawalSum = sum(AvWithdrawal_f(z.NYrs, z.StreamWithdrawal, z.GroundWithdrawal))
    z.AvTileDrainNSum = sum(z.AvTileDrainN)
    z.AvTileDrainPSum = sum(z.AvTileDrainP)
    z.AvTileDrainSedSum = sum(z.AvTileDrainSed)
    z.AvEvapoTransSum = sum(
        AvEvapoTrans_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0,
                       z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs,
                       z.MaxWaterCap))
    z.AvGroundWaterSum = sum(
        AvGroundWater_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                        z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET,
                        z.DayHrs, z.MaxWaterCap,
                        z.SatStor_0, z.RecessionCoef, z.SeepCoef, z.Landuse, z.TileDrainDensity))
    z.AvRunoffSum = sum(AvRunoff_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                                   z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention,
                                   z.PctAreaInfil,
                                   z.n25b, z.CN, z.Landuse, z.TileDrainDensity))
    z.AvErosionSum = sum(
        AvErosion_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0,
                    z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs,
                    z.MaxWaterCap,
                    z.SatStor_0, z.RecessionCoef, z.SeepCoef, z.Qretention, z.PctAreaInfil, z.n25b, z.Landuse,
                    z.TileDrainDensity, z.PointFlow,
                    z.StreamWithdrawal, z.GroundWithdrawal, z.NumAnimals, z.AvgAnimalWt, z.StreamFlowVolAdj,
                    z.SedAFactor_0,
                    z.AvKF, z.AvSlope, z.SedAAdjust, z.StreamLength, z.n42b, z.n46c, z.n85d, z.AgLength, z.n42, z.n45,
                    z.n85, z.UrbBankStab,
                    z.SedDelivRatio_0, z.Acoef, z.KF, z.LS, z.C, z.P))
    z.AvSedYieldSum = sum(
        AvSedYield_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
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
    z.AvAnimalPSum = sum(z.AvAnimalP)
    z.AvGRLostBarnPSum = sum(z.AvGRLostBarnP)
    z.AvGRLostBarnFCSum = sum(z.AvGRLostBarnFC)
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
