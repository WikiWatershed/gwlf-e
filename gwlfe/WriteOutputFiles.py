# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

from . import LoadReductions


def WriteOutput(z):
    # DIMENSION VARIABLES FOR PREDICT CALCULATION AND SCENARIO FILE
    AvOtherLuSed = 0
    AvOtherLuNitr = 0
    AvOtherLuPhos = 0
    TotSewerSys = 0
    TotNormSys = 0
    TotShortSys = 0
    TotSeptSys = 0
    TotAvLuErosion = 0
    AvTotalSed = 0
    AvDisN = 0
    AvTotalN = 0
    AvDisP = 0
    AvTotalP = 0

    z.SumTotArea = z.SumTotArea + z.TotArea

    # INSERT VALUES FOR BMP SCENARIO FILE FOR PREDICT APPLICATION
    for l in range(0, z.NLU):
        z.AvLuSedYield[l] = (z.AvLuSedYield[l] * z.RetentFactorSed) * (1 - z.AttenTSS)
        z.AvLuDisNitr[l] = (z.AvLuDisNitr[l] * z.RetentFactorN) * (1 - z.AttenN)
        z.AvLuTotNitr[l] = (z.AvLuTotNitr[l] * z.RetentFactorN) * (1 - z.AttenN)
        z.AvLuDisPhos[l] = (z.AvLuDisPhos[l] * z.RetentFactorP) * (1 - z.AttenP)
        z.AvLuTotPhos[l] = (z.AvLuTotPhos[l] * z.RetentFactorP) * (1 - z.AttenP)

    # SET THE SCENARIO VALUES TO LANDUSE LOADS
    for l in range(0, z.NRur):
        if (z.Landuse[l].lower() == "hay/past"):
            z.n2 = z.AvLuSedYield[l]
            z.n6 = z.AvLuTotNitr[l]
            z.n13 = z.AvLuTotPhos[l]
            z.n6dn = z.AvLuDisNitr[l]
            z.n13dp = z.AvLuDisPhos[l]
            z.n24 = round(z.Area[l])
        elif (z.Landuse[l].lower() == "cropland"):
            z.n1 = z.AvLuSedYield[l]
            z.n5 = z.AvLuTotNitr[l]
            z.n12 = z.AvLuTotPhos[l]
            z.n5dn = z.AvLuDisNitr[l]
            z.n12dp = z.AvLuDisPhos[l]
            z.n23 = round(z.Area[l])
        elif (z.Landuse[l].lower() == "turfgrass"):
            z.n2t = z.AvLuSedYield[l]
            z.n6t = z.AvLuTotNitr[l]
            z.n13t = z.AvLuTotPhos[l]
            z.n24t = round(z.Area[l])
        elif (z.Landuse[l].lower() == "unpaved_road"):
            z.n2d = z.AvLuSedYield[l]
            z.n6d = z.AvLuTotNitr[l]
            z.n13d = z.AvLuTotPhos[l]
            z.n6ddn = z.AvLuDisNitr[l]
            z.n13ddp = z.AvLuDisPhos[l]
        else:
            AvOtherLuSed = AvOtherLuSed + z.AvLuSedYield[l]
            AvOtherLuNitr = AvOtherLuNitr + z.AvLuTotNitr[l]
            AvOtherLuPhos = AvOtherLuPhos + z.AvLuTotPhos[l]

    LoadReductions.AdjustScnLoads(z)

    z.n2c = 0
    z.n6c = 0
    z.n13c = 0
    z.n24b = 0
    z.n2b = 0
    z.n6b = 0
    z.n13b = 0
    z.n23b = 0
    z.n6cdn = 0
    z.n13cdp = 0
    z.n6bdn = 0
    z.n13bdp = 0

    for l in range(z.NRur + 1, z.NLU):
        if "ld" in z.Landuse[l].lower():
            z.n2c = z.n2c + z.AvLuSedYield[l]
            z.n6c = z.n6c + z.AvLuTotNitr[l]
            z.n13c = z.n13c + z.AvLuTotPhos[l]
            z.n6cdn = z.n6cdn + z.AvLuDisNitr[l]
            z.n13cdp = z.n13cdp + z.AvLuDisPhos[l]
            z.n24b = z.n24b + round(z.Area[l])
        elif "hd" in z.Landuse[l].lower() or "md" in z.Landuse[l].lower():
            z.n2b = z.n2b + z.AvLuSedYield[l]
            z.n6b = z.n6b + z.AvLuTotNitr[l]
            z.n13b = z.n13b + z.AvLuTotPhos[l]
            z.n6bdn = z.n6bdn + z.AvLuDisNitr[l]
            z.n13bdp = z.n13bdp + z.AvLuDisPhos[l]
            z.n23b = z.n23b + round(z.Area[l])

    # Initial Upland loads
    InitialUplandN = z.n5 + z.n6 + z.n6b + z.n6c + z.n6d + AvOtherLuNitr
    if InitialUplandN == 0:
        InitialUplandN = 0.00000000001  # Fix for Divide-by-Zero error
    InitialUplandP = z.n12 + z.n13 + z.n13b + z.n13c + z.n13d + AvOtherLuPhos
    if InitialUplandP == 0:
        InitialUplandP = 0.00000000001  # Fix for Divide-by-Zero error
    InitialUplandSed = z.n1 + z.n2 + z.n2b + z.n2c + z.n2d + AvOtherLuSed
    if InitialUplandSed == 0:
        InitialUplandSed = 0.00000000001  # Fix for Divide-by-Zero error

    # FOR POINT SOURCE
    YrPointNitr = 0
    YrPointPhos = 0
    for i in range(0, 12):
        YrPointNitr = YrPointNitr + z.PointNitr[i]
        YrPointPhos = YrPointPhos + z.PointPhos[i]

    # GET THE AVERAGE SEPTIC SYSTEM INFORMATION
    if z.SepticFlag == 1:
        for i in range(0, 12):
            TotSewerSys = TotSewerSys + z.NumSewerSys[i]
            TotNormSys = TotNormSys + z.NumNormalSys[i]
            TotShortSys = TotShortSys + z.NumShortSys[i]
            TotSeptSys = (TotSeptSys + z.NumNormalSys[i] + z.NumShortSys[i] +
                          z.NumPondSys[i] + z.NumDischargeSys[i])

    # Set the conversion factors from metric to english
    SedConvert = 1000
    SedConvert = 1
    NPConvert = 1

    # Get the animal nuntient loads
    z.GRLBN = z.AvGRLostBarnN[0]
    z.NGLBN = z.AvNGLostBarnN[0]
    z.GRLBP = z.AvGRLostBarnP[0]
    z.NGLBP = z.AvNGLostBarnP[0]
    z.NGLManP = z.AvNGLostManP[0]

    # Get the fecal coliform values
    z.NGLBFC = z.AvNGLostBarnFC[0]
    z.GRLBFC = z.AvGRLostBarnFC[0]
    z.GRSFC = z.AvGRStreamFC
    z.GRSN = z.AvGRStreamN
    z.GRSP = z.AvGRStreamP

    # Get the initial pathogen loads
    z.n139 = z.AvAnimalFC[0]
    z.n140 = z.AvWWOrgs[0]
    z.n146 = z.AvWWOrgs[0]
    z.n141 = z.AvSSOrgs[0]
    z.n147 = z.AvSSOrgs[0]
    z.n142 = z.AvUrbOrgs[0]
    z.n143 = z.AvWildOrgs[0]
    z.n149 = z.AvWildOrgs[0]

    # FARM ANIMAL LOADS
    z.n7b = z.AvAnimalN[0]
    z.n14b = z.AvAnimalP[0]

    InitialAnimalN = z.n7b
    InitialAnimalP = z.n14b

    # Get the AEUs
    z.n41j = round(z.TotLAEU)
    z.n41k = round(z.TotPAEU)
    z.n41l = round(z.TotAEU)

    # CONVERT AVERAGE STREAM BANK ERIOSION, N AND P TO ENGLISH UNITS
    z.n4 = round(z.AvStreamBankEros[0] * z.RetentFactorSed * (1 - z.AttenTSS) * SedConvert)
    z.n8 = round(z.AvStreamBankN[0] * NPConvert * z.RetentFactorN * (1 - z.AttenN))
    z.n15 = round(z.AvStreamBankP[0] * NPConvert * z.RetentFactorP * (1 - z.AttenP))

    # PERFORM LOAD REDUCTIONS BASED ON BMPS IN SCENARIO FILE
    LoadReductions.AdjustScnLoads(z)

    # CONVERT AVERAGE STREAM BANK ERIOSION, N AND P TO ENGLISH UNITS
    z.AvStreamBankEros[0] = z.n4
    z.AvStreamBankN[0] = z.n8
    z.AvStreamBankP[0] = z.n15

    z.AvAnimalFC[0] = z.n145
    z.AvUrbOrgs[0] = z.n148

    # Get the FC reduction for monthly loads
    UrbanFCFrac = 0
    FarmFCFrac = 0

    if z.n139 > 0:
        FarmFCFrac = z.n145 / z.n139
    if z.n142 > 0:
        UrbanFCFrac = z.n148 / z.n142

    for i in range(0, 12):
        z.AvAnimalFC[i] = z.AvAnimalFC[i] * FarmFCFrac
        z.AvUrbOrgs[i] = z.AvUrbOrgs[i] * UrbanFCFrac

    # Reset the existing urban and animal FC loads to the reduced future loads, n145 and n148
    z.n139 = z.n145
    z.n142 = z.n148

    # Initial pathogen total load
    z.n144 = z.n139 + z.n140 + z.n141 + z.n142 + z.n143

    # Reduced total pathogen loads
    z.n150 = z.n145 + z.n146 + z.n147 + z.n148 + z.n149
    z.AvTotalOrgs[0] = z.n150

    # FARM ANIMAL LOAD REDUCTION FOR N AND P
    z.AvAnimalN[0] = z.n7b
    z.AvAnimalP[0] = z.n14b
    z.n7b = z.n7b * NPConvert
    z.n14b = z.n14b * NPConvert

    FinalAnimalN = z.n7b
    FinalAnimalP = z.n14b

    z.GRLBN = z.GRLBN * NPConvert
    z.NGLBN = z.NGLBN * NPConvert
    z.GRLBP = z.GRLBP * NPConvert
    z.NGLBP = z.NGLBP * NPConvert
    z.NGLManP = z.NGLManP * NPConvert
    z.GRSN = z.AvGRStreamN * NPConvert
    z.GRSP = z.AvGRStreamP * NPConvert

    # RESET GWLF OUTPUT VALUES FOR RURAL LANDUSE TO REDUCED LOADS AND CONVERT SCENARIO VALUES
    for l in range(0, z.NLU):
        if (z.Landuse[l].lower() == "hay/past"):
            z.AvLuSedYield[l] = z.n2
            z.AvLuTotNitr[l] = z.n6
            z.AvLuTotPhos[l] = z.n13
            z.AvLuDisNitr[l] = z.n6dn
            z.AvLuDisPhos[l] = z.n13dp

            if z.AvLuDisNitr[l] > z.AvLuTotNitr[l]:
                z.AvLuDisNitr[l] = z.AvLuTotNitr[l]
            if z.AvLuDisPhos[l] > z.AvLuTotPhos[l]:
                z.AvLuDisPhos[l] = z.AvLuTotPhos[l]

            z.n2 = round(z.AvLuSedYield[l] * SedConvert)
            z.n6 = round(z.AvLuTotNitr[l] * NPConvert)
            z.n13 = round(z.AvLuTotPhos[l] * NPConvert)

            if z.Area[l] > 0:
                z.AreaSum[2] = z.AreaSum[2] + z.Area[l]
        elif (z.Landuse[l].lower() == "cropland"):
            z.AvLuSedYield[l] = z.n1
            z.AvLuTotNitr[l] = z.n5
            z.AvLuTotPhos[l] = z.n12
            z.AvLuDisNitr[l] = z.n5dn
            z.AvLuDisPhos[l] = z.n12dp

            if z.AvLuDisNitr[l] > z.AvLuTotNitr[l]:
                z.AvLuDisNitr[l] = z.AvLuTotNitr[l]
            if z.AvLuDisPhos[l] > z.AvLuTotPhos[l]:
                z.AvLuDisPhos[l] = z.AvLuTotPhos[l]

            z.n1 = round(z.AvLuSedYield[l] * SedConvert)
            z.n5 = round(z.AvLuTotNitr[l] * NPConvert)
            z.n12 = round(z.AvLuTotPhos[l] * NPConvert)

            if z.Area[l] > 0:
                z.AreaSum[3] = z.AreaSum[3] + z.Area[l]
        elif z.Landuse[l].lower() == "unpaved_road":
            z.AvLuSedYield[l] = z.n2d
            z.AvLuTotNitr[l] = z.n6d
            z.AvLuTotPhos[l] = z.n13d
            z.AvLuDisNitr[l] = z.n6ddn
            z.AvLuDisPhos[l] = z.n13ddp

            if z.AvLuDisNitr[l] > z.AvLuTotNitr[l]:
                z.AvLuDisNitr[l] = z.AvLuTotNitr[l]
            if z.AvLuDisPhos[l] > z.AvLuTotPhos[l]:
                z.AvLuDisPhos[l] = z.AvLuTotPhos[l]

            z.n2d = round(z.AvLuSedYield[l] * SedConvert)
            z.n6d = round(z.AvLuTotNitr[l] * NPConvert)
            z.n13d = round(z.AvLuTotPhos[l] * NPConvert)

            if z.Area[l] > 0:
                z.AreaSum[6] = z.AreaSum[6] + z.Area[l]

        if z.AvLuDisNitr[l] > z.AvLuTotNitr[l]:
            z.AvLuDisNitr[l] = z.AvLuTotNitr[l]
        if z.AvLuDisPhos[l] > z.AvLuTotPhos[l]:
            z.AvLuDisPhos[l] = z.AvLuTotPhos[l]

        # GET THE AVERAGE TOTAL LOADS BY SOURCE
        TotAvLuErosion = TotAvLuErosion + z.AvLuErosion[l]
        AvTotalSed = AvTotalSed + z.AvLuSedYield[l]
        AvDisN = AvDisN + z.AvLuDisNitr[l]
        AvTotalN = AvTotalN + z.AvLuTotNitr[l]
        AvDisP = AvDisP + z.AvLuDisPhos[l]
        AvTotalP = AvTotalP + z.AvLuTotPhos[l]


def WriteOutputSumFiles(z):
    output_sum = {}

    z.SumSedDelivRatio = z.SumSedDelivRatio / z.SumTotArea

    for i in range(0, 12):
        z.SumPrecipitation[i] = z.SumPrecipitation[i] / z.SumTotArea
        z.SumEvapoTrans[i] = z.SumEvapoTrans[i] / z.SumTotArea
        z.SumGroundWater[i] = z.SumGroundWater[i] / z.SumTotArea
        z.SumRunoff[i] = z.SumRunoff[i] / z.SumTotArea
        z.SumStreamFlow[i] = z.SumStreamFlow[i] / z.SumTotArea
        z.SumPtSrcFlow[i] = z.SumPtSrcFlow[i] / z.SumTotArea
        z.SumTileDrain[i] = z.SumTileDrain[i] / z.SumTotArea
        z.SumWithdrawal[i] = z.SumWithdrawal[i] / z.SumTotArea

        output_sum[i] = [
            z.SumPrecipitation[i],
            z.SumEvapoTrans[i],
            z.SumGroundWater[i],
            z.SumRunoff[i],
            z.SumStreamFlow[i],
            z.SumPtSrcFlow[i],
            z.SumTileDrain[i],
            z.SumWithdrawal[i],
        ]

    return output_sum


def UrbanAreasOutput():
    print('UrbanAreasOutput')
