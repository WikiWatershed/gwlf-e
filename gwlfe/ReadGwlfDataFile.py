# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

"""
Initialize variables and perfom some preliminary calculations.

Imported from ReadAllDataFiles.bas
"""

import logging

from .enums import SweepType, YesOrNo
from . import PrelimQualCalculations


log = logging.getLogger(__name__)


def ReadAllData(z):
    log.debug('ReadAllData')

    # If RunQual output is requested, then redim RunQual values
    PrelimQualCalculations.ReDimRunQualVars()

    # Set the Total AEU to the value from the Animal Density layer

    for i in range(12):
        z.AnnDayHrs += z.DayHrs[i]

    for l in range(z.NRur):
        z.AreaTotal += z.Area[l]
        z.RurAreaTotal += z.Area[l]

    for l in range(z.NRur, z.NLU):
        z.AreaTotal += z.Area[l]
        z.UrbAreaTotal += z.Area[l]

    z.TotAreaMeters = z.AreaTotal * 10000

    # Get the area weighted average CN for rural areas
    z.AvCNRur = 0
    for l in range(z.NRur):
        # Calculate average area weighted CN and KF
        z.AvCNRur += z.CN[l] * z.Area[l] / z.RurAreaTotal

    # Get the area weighted average CN for urban areas
    z.AvCNUrb = 0
    for l in range(z.NRur, z.NLU):
        # Calculate average area-weighted CN for urban areas
        if z.UrbAreaTotal > 0:
            z.AvCNUrb += ((z.Imper[l] * z.CNI[1][l]
                          + (1 - z.Imper[l]) * z.CNP[1][l])
                          * z.Area[l] / z.UrbAreaTotal)

    # Calculate the average CN and percent urban area
    z.AvCN = ((z.AvCNRur * z.RurAreaTotal / z.AreaTotal) +
              (z.AvCNUrb * z.UrbAreaTotal / z.AreaTotal))

    z.PcntUrbanArea = z.UrbAreaTotal / z.AreaTotal

    if z.SepticFlag is YesOrNo.YES:
        for i in range(12):
            z.SepticsDay[i] = (z.NumNormalSys[i] + z.NumPondSys[i] +
                               z.NumShortSys[i] + z.NumDischargeSys[i])

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
    z.AEU1 = ((z.NumAnimals[2] / 2) * (z.AvgAnimalWt[2]) / 1000) + ((z.NumAnimals[3] / 2) * (z.AvgAnimalWt[3]) / 1000)
    z.AEU2 = (z.NumAnimals[7] * z.AvgAnimalWt[7]) / 1000
    z.AEU3 = (z.NumAnimals[5] * z.AvgAnimalWt[5]) / 1000
    z.AEU4 = (z.NumAnimals[4] * z.AvgAnimalWt[4]) / 1000
    z.AEU5 = (z.NumAnimals[6] * z.AvgAnimalWt[6]) / 1000
    z.AEU6 = (z.NumAnimals[0] * z.AvgAnimalWt[0]) / 1000
    z.AEU7 = (z.NumAnimals[1] * z.AvgAnimalWt[1]) / 1000

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
