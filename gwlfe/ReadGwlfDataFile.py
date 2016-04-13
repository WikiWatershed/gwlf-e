# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

"""
Initialize variables and perfom some preliminary calculations.

Imported from ReadAllDataFiles.bas
"""

import re
import logging

import numpy as np

from .enums import SweepType, YesOrNo
from . import PrelimQualCalculations


log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


def ReadAllData(z):
    z.NLU = z.NRur + z.NUrb

    z.NYrs = z.WxYrs
    z.DimYrs = z.WxYrs

    z.Load = np.zeros((z.DimYrs, 12, 3))
    z.DisLoad = np.zeros((z.DimYrs, 12, 3))
    z.UplandN = np.zeros((z.DimYrs, 12))
    z.UplandP = np.zeros((z.DimYrs, 12))
    z.UrbRunoffCm = np.zeros((z.DimYrs, 12))
    z.UrbRunoffLiter = np.zeros((z.DimYrs, 12))
    z.DailyFlow = np.zeros((z.DimYrs, 12, 31))
    z.DailyFlowMGD = np.zeros((z.DimYrs, 12, 31))
    z.DailyFlowGPM = np.zeros((z.DimYrs, 12, 31))
    z.DailyPtSrcFlow = np.zeros((z.DimYrs, 12, 31))

    # Declare the daily values as ReDimensional arrays in
    # to Pesticide components
    z.DailyUplandSed = np.zeros((z.DimYrs, 12, 31))
    z.DailyUplandN = np.zeros((z.DimYrs, 12, 31))
    z.DailyUplandP = np.zeros((z.DimYrs, 12, 31))
    z.DailyTileDrainN = np.zeros((z.DimYrs, 12, 31))
    z.DailyTileDrainP = np.zeros((z.DimYrs, 12, 31))
    z.DailyStrmSed = np.zeros((z.DimYrs, 12, 31))
    z.DailySepticN = np.zeros((z.DimYrs, 12, 31))
    z.DailySepticP = np.zeros((z.DimYrs, 12, 31))
    z.DailyStrmN = np.zeros((z.DimYrs, 12, 31))
    z.DailyStrmP = np.zeros((z.DimYrs, 12, 31))
    z.DailyGroundN = np.zeros((z.DimYrs, 12, 31))
    z.DailyGroundP = np.zeros((z.DimYrs, 12, 31))
    z.DayGroundNitr = np.zeros((z.DimYrs, 12, 31))
    z.DayGroundPhos = np.zeros((z.DimYrs, 12, 31))
    z.DayDisPhos = np.zeros((z.DimYrs, 12, 31))
    z.DayDisNitr = np.zeros((z.DimYrs, 12, 31))
    z.DayTotNitr = np.zeros((z.DimYrs, 12, 31))
    z.DailyPointN = np.zeros((z.DimYrs, 12, 31))
    z.DailyPointP = np.zeros((z.DimYrs, 12, 31))
    z.DayTotPhos = np.zeros((z.DimYrs, 12, 31))
    z.DayLuTotN = np.zeros((16, z.DimYrs, 12, 31))
    z.DayLuTotP = np.zeros((16, z.DimYrs, 12, 31))
    z.DayLuDisN = np.zeros((16, z.DimYrs, 12, 31))
    z.DayLuDisP = np.zeros((16, z.DimYrs, 12, 31))
    z.DayErWashoff = np.zeros((16, z.DimYrs, 12, 31))
    z.Perc = np.zeros((z.DimYrs, 12, 31))
    z.DeepFlow = np.zeros((z.DimYrs, 12, 31))
    z.DayQRunoff = np.zeros((z.DimYrs, 12, 31))
    z.SdYld = np.zeros((z.DimYrs, 12, 31))
    z.Erosn = np.zeros((z.DimYrs, 12, 31))
    z.DayErosion = np.zeros((z.DimYrs, 12, 31))
    z.DayLuErosion = np.zeros((16, z.DimYrs, 12, 31))
    z.DaySed = np.zeros((z.DimYrs, 12, 31))
    z.DayLuSed = np.zeros((16, z.DimYrs, 12, 31))
    z.DayRunoff = np.zeros((z.DimYrs, 12, 31))
    z.DayLuRunoff = np.zeros((16, z.DimYrs, 12, 31))
    z.MeltPest = np.zeros((z.DimYrs, 12, 31))
    z.PrecPest = np.zeros((z.DimYrs, 12, 31))
    z.DailyGrFlow = np.zeros((z.DimYrs, 12, 31))
    z.DailyETCm = np.zeros((z.DimYrs, 12, 31))
    z.DailyETShal = np.zeros((z.DimYrs, 12, 31))
    z.PercCm = np.zeros((z.DimYrs, 12, 31))
    z.PercShal = np.zeros((z.DimYrs, 12, 31))
    z.DailyUnsatStorCm = np.zeros((z.DimYrs, 12, 31))
    z.DailyUnsatStorShal = np.zeros((z.DimYrs, 12, 31))
    z.DailyET = np.zeros((z.DimYrs, 12, 31))
    z.DailyRetent = np.zeros((z.DimYrs, 12, 31))
    z.SatStorPest = np.zeros((z.DimYrs, 12, 31))
    z.UrbanRunoff = np.zeros((z.DimYrs, 12))
    z.RuralRunoff = np.zeros((z.DimYrs, 12))
    z.DailyInfilt = np.zeros((z.DimYrs, 12, 31))
    z.StreamFlowVol = np.zeros((z.DimYrs, 12))
    z.DailyCN = np.zeros((z.DimYrs, 12, 31))
    z.DailyWater = np.zeros((z.DimYrs, 12, 31))
    z.LE = np.zeros((z.DimYrs, 12))
    z.StreamBankEros = np.zeros((z.DimYrs, 12))
    z.StreamBankN = np.zeros((z.DimYrs, 12))
    z.StreamBankP = np.zeros((z.DimYrs, 12))
    z.DailyAMC5 = np.zeros((z.DimYrs, 12, 31))
    z.MonthFlow = np.zeros((z.DimYrs, 12))
    z.LuGrFlow = np.zeros((16, z.DimYrs, 12, 31))
    z.LuDeepSeep = np.zeros((16, z.DimYrs, 12, 31))
    z.LuInfiltration = np.zeros((16, z.DimYrs, 12, 31))
    z.PestTemp = np.zeros((z.DimYrs, 12, 31))
    z.PestPrec = np.zeros((z.DimYrs, 12, 31))

    # Tile Drainage and Flow Variables
    z.TileDrainN = np.zeros((z.DimYrs, 12))
    z.TileDrainP = np.zeros((z.DimYrs, 12))
    z.TileDrainSed = np.zeros((z.DimYrs, 12))
    z.TileDrain = np.zeros((z.DimYrs, 12))
    z.TileDrainRO = np.zeros((z.DimYrs, 12))
    z.TileDrainGW = np.zeros((z.DimYrs, 12))
    z.GwAgLE = np.zeros((z.DimYrs, 12))
    z.Withdrawal = np.zeros((z.DimYrs, 12))
    z.PtSrcFlow = np.zeros((z.DimYrs, 12))
    z.StreamFlow = np.zeros((z.DimYrs, 12))
    z.StreamFlowLE = np.zeros((z.DimYrs, 12))
    z.Precipitation = np.zeros((z.DimYrs, 12))
    z.Evapotrans = np.zeros((z.DimYrs, 12))
    z.GroundWatLE = np.zeros((z.DimYrs, 12))
    z.AgRunoff = np.zeros((z.DimYrs, 12))
    z.Runoff = np.zeros((z.DimYrs, 12))
    z.Erosion = np.zeros((z.DimYrs, 12))
    z.SedYield = np.zeros((z.DimYrs, 12))
    # XXX: This is initialized correctly in the parser
    # and should not be reinitialized
    # z.DaysMonth = np.zeros((z.DimYrs, 12), dtype=int)
    z.WxMonth = np.zeros((z.DimYrs, 12))
    z.WxYear = np.zeros((z.DimYrs, 12))
    z.GroundNitr = np.zeros((z.DimYrs, 12))
    z.GroundPhos = np.zeros((z.DimYrs, 12))
    z.DisNitr = np.zeros((z.DimYrs, 12))
    z.SepticN = np.zeros((z.DimYrs, 12))
    z.SepticP = np.zeros((z.DimYrs, 12))
    z.TotNitr = np.zeros((z.DimYrs, 12))
    z.DisPhos = np.zeros((z.DimYrs, 12))
    z.TotPhos = np.zeros((z.DimYrs, 12))
    z.LuRunoff = np.zeros((z.DimYrs, 16))
    z.LuErosion = np.zeros((z.DimYrs, 16))
    z.LuSedYield = np.zeros((z.DimYrs, 16))
    z.LuDisNitr = np.zeros((z.DimYrs, 16))
    z.LuTotNitr = np.zeros((z.DimYrs, 16))
    z.LuDisPhos = np.zeros((z.DimYrs, 16))
    z.LuTotPhos = np.zeros((z.DimYrs, 16))
    z.SedTrans = np.zeros((z.DimYrs, 16))
    z.SepticNitr = np.zeros(z.DimYrs)
    z.SepticPhos = np.zeros(z.DimYrs)

    # ANIMAL FEEDING OPERATIONS VARIABLES
    z.DailyAnimalN = np.zeros((z.DimYrs, 12, 31))
    z.DailyAnimalP = np.zeros((z.DimYrs, 12, 31))

    # Calculated Values for Animal Feeding Operations
    z.NGLostManN = np.zeros((z.DimYrs, 12))
    z.NGLostBarnN = np.zeros((z.DimYrs, 12))
    z.NGLostManP = np.zeros((z.DimYrs, 12))
    z.NGLostBarnP = np.zeros((z.DimYrs, 12))
    z.NGLostManFC = np.zeros((z.DimYrs, 12))
    z.NGLostBarnFC = np.zeros((z.DimYrs, 12))

    z.GRLostManN = np.zeros((z.DimYrs, 12))
    z.GRLostBarnN = np.zeros((z.DimYrs, 12))
    z.GRLossN = np.zeros((z.DimYrs, 12))
    z.GRLostManP = np.zeros((z.DimYrs, 12))
    z.GRLostBarnP = np.zeros((z.DimYrs, 12))
    z.GRLossP = np.zeros((z.DimYrs, 12))
    z.GRLostManFC = np.zeros((z.DimYrs, 12))
    z.GRLostBarnFC = np.zeros((z.DimYrs, 12))
    z.GRLossFC = np.zeros((z.DimYrs, 12))
    z.LossFactAdj = np.zeros((z.DimYrs, 12))
    z.AnimalN = np.zeros((z.DimYrs, 12))
    z.AnimalP = np.zeros((z.DimYrs, 12))
    z.AnimalFC = np.zeros((z.DimYrs, 12))
    z.WWOrgs = np.zeros((z.DimYrs, 12))
    z.SSOrgs = np.zeros((z.DimYrs, 12))
    z.UrbOrgs = np.zeros((z.DimYrs, 12))
    z.WildOrgs = np.zeros((z.DimYrs, 12))
    z.TotalOrgs = np.zeros((z.DimYrs, 12))
    z.CMStream = np.zeros((z.DimYrs, 12))
    z.OrgConc = np.zeros((z.DimYrs, 12))

    # If RunQual output is requested, then redim RunQual values
    PrelimQualCalculations.ReDimRunQualVars(z)

    # Set the Total AEU to the value from the Animal Density layer
    if not VersionMatch(z.TranVersionNo, '1.[0-9].[0-9]'):
        raise Exception('Input data file is not in the correct format or is no longer supported')

    for i in range(12):
        z.AnnDayHrs += z.DayHrs[i]

    for l in range(z.NRur):
        z.AreaTotal += z.Area[l]
        z.RurAreaTotal += z.Area[l]

    for l in range(z.NUrb):
        z.AreaTotal += z.Area[l + z.NRur]
        z.UrbAreaTotal += z.Area[l + z.NRur]

    z.TotAreaMeters = z.AreaTotal * 10000

    # Get the area weighted average CN for rural areas
    z.AvCNRur = 0
    for l in range(z.NRur):
        # Calculate average area weighted CN and KF
        z.AvCNRur += z.CN[l] * z.Area[l] / z.RurAreaTotal

    # Get the area weighted average CN for urban areas
    z.AvCNUrb = 0

    for l in range(z.NUrb):
        # Calculate average area-weighted CN for urban areas
        if z.UrbAreaTotal > 0:
            z.AvCNUrb += ((z.Imper[l] * z.CNI[2, l]
                          + (1 - z.Imper[l]) * z.CNP[2, l])
                          * z.Area[l + z.NRur] / z.UrbAreaTotal)

    # Calculate the average CN and percent urban area
    z.AvCN = ((z.AvCNRur * z.RurAreaTotal / z.AreaTotal) +
              (z.AvCNUrb * z.UrbAreaTotal / z.AreaTotal))

    z.PcntUrbanArea = z.UrbAreaTotal / z.AreaTotal

    if z.SepticFlag is YesOrNo.YES:
        for i in range(12):
            z.SepticsDay[i] = (z.NumNormalSys[i] + z.NumPondSys[i] +
                               z.NumShortSys[i] + z.NumDischargeSys[i])

    if VersionMatch(z.TranVersionNo, '1.[0-2].[0-9]'):
        z.Storm = 0
        z.CSNAreaSim = 0
        z.CSNDevType = "None"

    if VersionMatch(z.TranVersionNo, '1.[0-1].[0-9]'):
        for i in range(6):
            z.ISRR[i] = 0
            z.ISRA[i] = 0
        z.SweepType = 1
        z.UrbSweepFrac = 1
    elif VersionMatch(z.TranVersionNo, '1.[2-3].[0-9]'):
        z.SweepType = 1
        z.UrbSweepFrac = 1

    for i in range(12):
        if z.SweepType is SweepType.VACUUM:
            if z.StreetSweepNo[i] == 0:
                z.SweepFrac[i] = 1
            if z.StreetSweepNo[i] == 1:
                z.SweepFrac[i] = 0.94
            if z.StreetSweepNo[i] == 2:
                z.SweepFrac[i] = 0.89
            if z.StreetSweepNo[i] == 3:
                z.SweepFrac[i] = 0.84
            if z.StreetSweepNo[i] >= 4:
                z.SweepFrac[i] = 0.79
        elif z.SweepType is SweepType.MECHANICAL:
            if z.StreetSweepNo[i] == 0:
                z.SweepFrac[i] = 1
            if z.StreetSweepNo[i] == 1:
                z.SweepFrac[i] = 0.99
            if z.StreetSweepNo[i] == 2:
                z.SweepFrac[i] = 0.98
            if z.StreetSweepNo[i] == 3:
                z.SweepFrac[i] = 0.97
            if z.StreetSweepNo[i] >= 4:
                z.SweepFrac[i] = 0.96
        else:
            raise ValueError('Invalid value for SweepType')

    # Get the Animal values
    z.InitGrN = 0
    z.InitGrP = 0
    z.InitGrFC = 0
    z.InitNgN = 0
    z.InitNgP = 0
    z.InitNgFC = 0

    for a in range(9):
        if z.GrazingAnimal[a] is YesOrNo.NO:
            z.NGLoadN[a] = (z.NumAnimals[a] * z.AvgAnimalWt[a] / 1000) * z.AnimalDailyN[a] * 365
            z.NGLoadP[a] = (z.NumAnimals[a] * z.AvgAnimalWt[a] / 1000) * z.AnimalDailyP[a] * 365
            z.NGLoadFC[a] = (z.NumAnimals[a] * z.AvgAnimalWt[a] / 1000) * z.FCOrgsPerDay[a] * 365
            z.InitNgN += z.NGLoadN[a]
            z.InitNgP += z.NGLoadP[a]
            z.InitNgFC += z.NGLoadFC[a]
        elif z.GrazingAnimal[a] is YesOrNo.YES:
            z.GRLoadN[a] = (z.NumAnimals[a] * z.AvgAnimalWt[a] / 1000) * z.AnimalDailyN[a] * 365
            z.GRLoadP[a] = (z.NumAnimals[a] * z.AvgAnimalWt[a] / 1000) * z.AnimalDailyP[a] * 365
            z.GRLoadFC[a] = (z.NumAnimals[a] * z.AvgAnimalWt[a] / 1000) * z.FCOrgsPerDay[a] * 365
            z.InitGrN += z.GRLoadN[a]
            z.InitGrP += z.GRLoadP[a]
            z.InitGrFC += z.GRLoadFC[a]
        else:
            raise ValueError('Unexpected value for GrazingAnimal')

    # Obtain AEU for each farm animal
    z.AEU1 = ((z.NumAnimals[3] / 2) * (z.AvgAnimalWt[3]) / 1000) + ((z.NumAnimals[4] / 2) * (z.AvgAnimalWt[4]) / 1000)
    z.AEU2 = (z.NumAnimals[8] * z.AvgAnimalWt[8]) / 1000
    z.AEU3 = (z.NumAnimals[6] * z.AvgAnimalWt[6]) / 1000
    z.AEU4 = (z.NumAnimals[5] * z.AvgAnimalWt[5]) / 1000
    z.AEU5 = (z.NumAnimals[7] * z.AvgAnimalWt[7]) / 1000
    z.AEU6 = (z.NumAnimals[1] * z.AvgAnimalWt[1]) / 1000
    z.AEU7 = (z.NumAnimals[2] * z.AvgAnimalWt[2]) / 1000

    # Get the total AEU, Total livestock and poultry AEU
    z.TotAEU = z.AEU1 + z.AEU2 + z.AEU3 + z.AEU4 + z.AEU5 + z.AEU6 + z.AEU7
    z.TotLAEU = z.AEU3 + z.AEU4 + z.AEU5 + z.AEU6 + z.AEU7
    z.TotPAEU = z.AEU1 + z.AEU2

    # Get the Non-Grazing Animal Worksheet values
    for i in range(12):
        # For Non-Grazing
        z.NGAccManAppN[i] += (z.InitNgN / 12) - (z.NGPctManApp[i] * z.InitNgN)

        if z.NGAccManAppN[i] < 0:
            z.NGAccManAppN[i] = 0

        z.NGAccManAppP[i] += (z.InitNgP / 12) - (z.NGPctManApp[i] * z.InitNgP)

        if z.NGAccManAppP[i] < 0:
            z.NGAccManAppP[i] = 0

        z.NGAccManAppFC[i] += (z.InitNgFC / 12) - (z.NGPctManApp[i] * z.InitNgFC)

        if z.NGAccManAppFC[i] < 0:
            z.NGAccManAppFC[i] = 0

        z.NGAppManN[i] = z.NGPctManApp[i] * z.InitNgN
        z.NGInitBarnN[i] = z.NGAccManAppN[i] - z.NGAppManN[i]

        if z.NGInitBarnN[i] < 0:
            z.NGInitBarnN[i] = 0

        z.NGAppManP[i] = z.NGPctManApp[i] * z.InitNgP
        z.NGInitBarnP[i] = z.NGAccManAppP[i] - z.NGAppManP[i]

        if z.NGInitBarnP[i] < 0:
            z.NGInitBarnP[i] = 0

        z.NGAppManFC[i] = z.NGPctManApp[i] * z.InitNgFC
        z.NGInitBarnFC[i] = z.NGAccManAppFC[i] - z.NGAppManFC[i]

        if z.NGInitBarnFC[i] < 0:
            z.NGInitBarnFC[i] = 0

    # Read the Grazing Animal Worksheet values
    for i in range(12):
        z.GrazingN[i] = z.PctGrazing[i] * (z.InitGrN / 12)
        z.GrazingP[i] = z.PctGrazing[i] * (z.InitGrP / 12)
        z.GrazingFC[i] = z.PctGrazing[i] * (z.InitGrFC / 12)

        z.GRStreamN[i] = z.PctStreams[i] * z.GrazingN[i]
        z.GRStreamP[i] = z.PctStreams[i] * z.GrazingP[i]
        z.GRStreamFC[i] = z.PctStreams[i] * z.GrazingFC[i]

        # Get the annual sum for FC
        z.AvGRStreamFC += z.GRStreamFC[i]
        z.AvGRStreamN += z.GRStreamN[i]
        z.AvGRStreamP += z.GRStreamP[i]

        z.GRAccManAppN[i] = (z.GRAccManAppN[i] + (z.InitGrN / 12)
                             - (z.GRPctManApp[i] * z.InitGrN) - z.GrazingN[i])
        if z.GRAccManAppN[i] < 0:
            z.GRAccManAppN[i] = 0

        z.GRAccManAppP[i] = (z.GRAccManAppP[i] + (z.InitGrP / 12)
                             - (z.GRPctManApp[i] * z.InitGrP) - z.GrazingP[i])
        if z.GRAccManAppP[i] < 0:
            z.GRAccManAppP[i] = 0

        z.GRAccManAppFC[i] = (z.GRAccManAppFC[i] + (z.InitGrFC / 12)
                              - (z.GRPctManApp[i] * z.InitGrFC) - z.GrazingFC[i])
        if z.GRAccManAppFC[i] < 0:
            z.GRAccManAppFC[i] = 0

        z.GRAppManN[i] = z.GRPctManApp[i] * z.InitGrN
        z.GRInitBarnN[i] = z.GRAccManAppN[i] - z.GRAppManN[i]
        if z.GRInitBarnN[i] < 0:
            z.GRInitBarnN[i] = 0

        z.GRAppManP[i] = z.GRPctManApp[i] * z.InitGrP
        z.GRInitBarnP[i] = z.GRAccManAppP[i] - z.GRAppManP[i]
        if z.GRInitBarnP[i] < 0:
            z.GRInitBarnP[i] = 0

        z.GRAppManFC[i] = z.GRPctManApp[i] * z.InitGrFC
        z.GRInitBarnFC[i] = z.GRAccManAppFC[i] - z.GRAppManFC[i]
        if z.GRInitBarnFC[i] < 0:
            z.GRInitBarnFC[i] = 0

    # Recalculate AEU using the TotAEU from the animal file and the total area of the basin in Acres
    if z.TotLAEU > 0:
        z.AEU = z.TotLAEU / (z.AreaTotal * 2.471)
    else:
        z.AEU = 0

    # Recalculate Sed A Factor using updated AEU value based on animal data
    z.SedAFactor = ((0.00467 * z.PcntUrbanArea) +
                    (0.000863 * z.AEU) +
                    (0.000001 * z.AvCN) +
                    (0.000425 * z.AvKF) +
                    (0.000001 * z.AvSlope) - 0.000036) * z.SedAAdjust

    if z.SedAFactor < 0.00001:
        z.SedAFactor = 0.00001

    if z.AttenFlowDist > 0 and z.AttenFlowVel > 0:
        z.FlowDays = z.AttenFlowDist / (z.AttenFlowVel * 24)
    else:
        z.FlowDays = 0

    z.AttenN = z.FlowDays * z.AttenLossRateN
    z.AttenP = z.FlowDays * z.AttenLossRateP
    z.AttenTSS = z.FlowDays * z.AttenLossRateTSS
    z.AttenPath = z.FlowDays * z.AttenLossRatePath

    # Calculate retention coefficients
    z.RetentFactorN = (1 - (z.ShedAreaDrainLake * z.RetentNLake))
    z.RetentFactorP = (1 - (z.ShedAreaDrainLake * z.RetentPLake))
    z.RetentFactorSed = (1 - (z.ShedAreaDrainLake * z.RetentSedLake))


def VersionMatch(TranVersionNo, VersionPatternRegex):
    pattern = '^{}$'.format(VersionPatternRegex)
    return re.match(pattern, TranVersionNo)
