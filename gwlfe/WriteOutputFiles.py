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
    n2t = 0
    n6t = 0
    n13t = 0
    n24t = 0

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

    # XXX: These are not used in our port.
    # InitialAnimalN = z.n7b
    # InitialAnimalP = z.n14b

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

    # XXX: These are not used in our port
    # FinalAnimalN = z.n7b
    # FinalAnimalP = z.n14b

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

    # Reset the urban landuse values
    for l in range(z.NRur + 1, z.NLU):
        if "ld" in z.Landuse[l].lower() and z.n24b > 0:
            z.AvLuSedYield[l] = z.n2c * z.Area[l] / z.n24b
            z.AvLuTotNitr[l] = z.n6c * z.Area[l] / z.n24b
            z.AvLuTotPhos[l] = z.n13c * z.Area[l] / z.n24b
            z.AvLuDisNitr[l] = z.n6cdn * z.Area[l] / z.n24b
            z.AvLuDisPhos[l] = z.n13cdp * z.Area[l] / z.n24b

            if z.AvLuDisNitr[l] > z.AvLuTotNitr[l]:
                z.AvLuDisNitr[l] = z.AvLuTotNitr[l]
            if z.AvLuDisPhos[l] > z.AvLuTotPhos[l]:
                z.AvLuDisPhos[l] = z.AvLuTotPhos[l]

            if z.Area[l] > 0:
                z.AreaSum[0] = z.AreaSum[0] + z.Area[l]
        elif "hd" in z.Landuse[l].lower() or "md" in z.Landuse[l].lower() and (z.n23b > 0):
            z.AvLuSedYield[l] = z.n2b * z.Area[l] / z.n23b
            z.AvLuTotNitr[l] = z.n6b * z.Area[l] / z.n23b
            z.AvLuTotPhos[l] = z.n13b * z.Area[l] / z.n23b
            z.AvLuDisNitr[l] = z.n6bdn * z.Area[l] / z.n23b
            z.AvLuDisPhos[l] = z.n13bdp * z.Area[l] / z.n23b

            if z.AvLuDisNitr[l] > z.AvLuTotNitr[l]:
                z.AvLuDisNitr[l] = z.AvLuTotNitr[l]
            if z.AvLuDisPhos[l] > z.AvLuTotPhos[l]:
                z.AvLuDisPhos[l] = z.AvLuTotPhos[l]

            if z.Area[l] > 0:
                z.AreaSum[1] = z.AreaSum[1] + z.Area[l]

    z.n2c = round(z.n2c * SedConvert)
    z.n6c = round(z.n6c * NPConvert)
    z.n13c = round(z.n13c * NPConvert)

    z.n2b = round(z.n2b * SedConvert)
    z.n6b = round(z.n6b * NPConvert)
    z.n13b = round(z.n13b * NPConvert)

    # XXX: These are not used in our port
    # Final Upland loads
    # FinalUplandN = z.n5 + z.n6 + z.n6b + z.n6c + z.n6d + AvOtherLuNitr
    # FinalUplandP = z.n12 + z.n13 + z.n13b + z.n13c + z.n13d + AvOtherLuPhos
    # FinalUplandSed = z.n1 + z.n2 + z.n2b + z.n2c + z.n2d + AvOtherLuSed

    # TotalAreaAc = 0

    # FORMAT VALUES FOR PREDICT SCENARIO FILE
    z.n22 = round(z.AreaTotal, 0)

    # COMPLETE CALCULATING THE TOTAL SOURCE LOADS FOR SEDIMENT, N AND P
    AvTotalSed = (AvTotalSed + (((z.AvStreamBankEros[0] / 1000) +
                  ((z.AvTileDrainSed[0] / 1000)) * z.RetentFactorSed * (1 - z.AttenTSS))))
    AvDisN = (AvDisN + ((z.AvGroundNitr[0] + YrPointNitr + z.AvSeptNitr) *
              z.RetentFactorN * (1 - z.AttenN)))
    AvTotalN = (AvTotalN + ((z.AvStreamBankN[0] + (z.AvGroundNitr[0] + z.AvTileDrainN[0] +
                z.AvAnimalN[0] + YrPointNitr + z.AvSeptNitr) * z.RetentFactorN * (1 - z.AttenN))))
    AvDisP = AvDisP + ((z.AvGroundPhos[0] + YrPointPhos + z.AvSeptPhos) * z.RetentFactorP * (1 - z.AttenP))
    AvTotalP = (AvTotalP + ((z.AvStreamBankP[0] + (z.AvGroundPhos[0] + z.AvTileDrainP[0] +
                z.AvAnimalP[0] + YrPointPhos + z.AvSeptPhos) * z.RetentFactorP * (1 - z.AttenP))))

    # OBTAIN THE AVERAGE TOTAL MONTHLY LOADS
    AvMonDisN = 0
    AvMonTotN = 0
    AvMonDisP = 0
    AvMonTotP = 0
    AvMonSed = 0
    AvMonEros = 0

    for i in range(0, 12):
        AvMonEros = AvMonEros + z.AvErosion[i]
        AvMonSed = AvMonSed + (z.AvSedYield[i] * z.RetentFactorSed * (1 - z.AttenTSS))
        AvMonDisN = AvMonDisN + (z.AvDisNitr[i] * z.RetentFactorN * (1 - z.AttenN))
        AvMonTotN = AvMonTotN + (z.AvTotNitr[i] * z.RetentFactorN * (1 - z.AttenN))
        AvMonDisP = AvMonDisP + (z.AvDisPhos[i] * z.RetentFactorP * (1 - z.AttenP))
        AvMonTotP = AvMonTotP + (z.AvTotPhos[i] * z.RetentFactorP * (1 - z.AttenP))

    # XXX: These values are not used in our port
    # Obtain the reduction factor to adjust the monthly loads if Scenario reductions applied
    # AvErosFrac = 1
    # AvSedFrac = 1
    # AvTotNFrac = 1
    # AvTotPFrac = 1
    # AvDisNFrac = 1
    # AvDisPFrac = 1

    # if AvMonEros > 0:
    #    AvErosFrac = TotAvLuErosion / AvMonEros
    # else:
    #    AvErosFrac = 0
    # if AvMonSed > 0:
    #    AvSedFrac = AvTotalSed / AvMonSed
    # else:
    #    AvSedFrac = 0
    # if AvMonDisN > 0:
    #    AvDisNFrac = AvDisN / AvMonDisN
    # else:
    #    AvDisNFrac = 0
    # if AvMonTotN > 0:
    #    AvTotNFrac = AvTotalN / AvMonTotN
    # else:
    #    AvTotNFrac = 0
    # if AvMonDisP > 0:
    #    AvDisPFrac = AvDisP / AvMonDisP
    # else:
    #    AvDisPFrac = 0
    # if AvMonTotP > 0:
    #    AvTotPFrac = AvTotalP / AvMonTotP
    # else:
    #    AvTotPFrac = 0

    # OBTAIN THE MONTHLY SEPTIC SYSTEM AND SEWER POPULATION VALUES
    z.n47 = round(TotSeptSys / 12)
    z.n49 = round(TotSeptSys / 12)
    z.n53 = round(TotSewerSys / 12)

    # CONVERT GROUNDWATER N AND P REDUCED LOADS INTO ENGLISH UNIST FOR THE PREDICT SCENARIO FILE
    z.n9 = round(((z.AvGroundNitr[0] + z.AvTileDrainN[0]) * NPConvert * z.RetentFactorN * (1 - z.AttenN)))
    z.n16 = round(((z.AvGroundPhos[0] + z.AvTileDrainP[0]) * NPConvert * z.RetentFactorP * (1 - z.AttenP)))

    # CONVERT ANNUAL POINT N AND P TO ENGLISH UNITS
    z.n10 = round((YrPointNitr * NPConvert * z.RetentFactorN * (1 - z.AttenN)))
    z.n17 = round((YrPointPhos * NPConvert * z.RetentFactorP * (1 - z.AttenP)))

    # CONVERT AVERAGE SEPTIC N AND P TO ENGLISH UNITS
    z.n11 = round((z.AvSeptNitr * NPConvert * z.RetentFactorN * (1 - z.AttenN)))
    z.n18 = round((z.AvSeptPhos * NPConvert * z.RetentFactorP * (1 - z.AttenP)))

    # ENTER THE OTHER SEDIMENT, N AND P INTO FIELDS
    z.n3 = round(((AvOtherLuSed + ((z.AvTileDrainSed[0] * z.RetentFactorSed * (1 - z.AttenTSS)) / 1000)) * SedConvert))
    z.n7 = round((AvOtherLuNitr * z.RetentFactorN * (1 - z.AttenN) * NPConvert))
    z.n14 = round((AvOtherLuPhos * z.RetentFactorP * (1 - z.AttenP) * NPConvert))

    # ADD TURF TO HAY/PASTURE
    z.n2 = z.n2 + (n2t * SedConvert)
    z.n6 = z.n6 + (n6t * NPConvert)
    z.n13 = z.n13 + (n13t * NPConvert)
    z.n24 = z.n24 + n24t

    # Multiply sedimez.nt loads by 1000 to get them iz.nto Kg before writiz.ng to PRedICT sectioz.n of file
    z.n1 = z.n1 * 1000
    z.n2 = z.n2 * 1000
    z.n2b = z.n2b * 1000
    z.n2c = z.n2c * 1000
    z.n2d = z.n2d * 1000
    z.n3 = z.n3 * 1000

    # Obtain the totals for sed, z.n az.nd P
    z.n19 = z.n1 + z.n2 + z.n2b + z.n2c + z.n2d + z.n3 + z.n4
    z.n20 = z.n5 + z.n6 + z.n6b + z.n6c + z.n6d + z.n7 + z.n7b + z.n8 + z.n9 + z.n10 + z.n11
    z.n21 = z.n12 + z.n13 + z.n13b + z.n13c + z.n13d + z.n14 + z.n14b + z.n15 + z.n16 + z.n17 + z.n18

    # TODO: Port WriteDailyFlowFile if needed
    # WRITE OUTPUT TO THE FILE FOR DAILy Flow
    # WriteDailyFlowFile

    # SET THE SCENARIO VALUES TO LANDUSE LOADS\
    AvOtherLuSed = 0
    AvOtherLuNitr = 0
    AvOtherLuPhos = 0

    for y in range(0, z.NYrs):
        z.n2c = 0
        z.n6c = 0
        z.n13c = 0
        z.n2b = 0
        z.n6b = 0
        z.n13b = 0
        z.n6cdn = 0
        z.n13cdp = 0
        z.n6bdn = 0
        z.n13bdp = 0

        for l in range(0, z.NLU):
            z.LuRunoff[y, l] = round(z.LuRunoff[y, l])
            z.LuErosion[y, l] = round(z.LuErosion[y, l])
            z.LuSedYield[y, l] = round((z.LuSedYield[y, l] * z.RetentFactorSed * (1 - z.AttenTSS)))
            z.LuDisNitr[y, l] = round((z.LuDisNitr[y, l] * z.RetentFactorN * (1 - z.AttenN)))
            z.LuTotNitr[y, l] = round((z.LuTotNitr[y, l] * z.RetentFactorN * (1 - z.AttenN)))
            z.LuDisPhos[y, l] = round((z.LuDisPhos[y, l] * z.RetentFactorP * (1 - z.AttenP)))
            z.LuTotPhos[y, l] = round((z.LuTotPhos[y, l] * z.RetentFactorP * (1 - z.AttenP)))

            if z.Landuse[l].lower() == "hay/past":
                z.n2 = z.LuSedyield[y, l]
                z.n6 = z.LuTotNitr[y, l]
                z.n13 = z.LuTotPhos[y, l]
                z.n6dn = z.LuDisNitr[y, l]
                z.n13dp = z.LuDisPhos[y, l]
            elif z.Landuse[l].lower() == "cropland":
                z.n1 = z.LuSedyield[y, l]
                z.n5 = z.LuTotNitr[y, l]
                z.n12 = z.LuTotPhos[y, l]
                z.n5dn = z.LuDisNitr[y, l]
                z.n12dp = z.LuDisPhos[y, l]
            elif z.Landuse[l].lower() == "unpaved_rd":
                z.n2d = z.LuSedyield[y, l]
                z.n6d = z.LuTotNitr[y, l]
                z.n13d = z.LuTotPhos[y, l]
                z.n6ddn = z.LuDisNitr[y, l]
                z.n13ddp = z.LuDisPhos[y, l]
            elif z.Landuse[l].lower() == "turfgrass":
                z.n2t = z.LuSedYield[y, l]
                z.n6t = z.LuTotNitr[y, l]
                z.n13t = z.LuTotPhos[y, l]
            else:
                AvOtherLuSed = AvOtherLuSed + z.LuSedYield[y, l]
                AvOtherLuNitr = AvOtherLuNitr + z.LuTotNitr[y, l]
                AvOtherLuPhos = AvOtherLuPhos + z.LuTotPhos[y, l]

            if "ld" in z.Landuse[l].lower():
                z.n2c = z.n2c + z.LuSedYield[y, l]
                z.n6c = z.n6c + z.LuTotNitr[y, l]
                z.n13c = z.n13c + z.LuTotPhos[y, l]
                z.n6cdn = z.n6cdn + z.LuDisNitr[y, l]
                z.n13cdp = z.n13cdp + z.LuDisPhos[y, l]
            elif "hd" in z.Landuse[l].lower() or "md" in z.Landuse[l].lower():
                z.n2b = z.n2b + z.LuSedYield[y, l]
                z.n6b = z.n6b + z.LuTotNitr[y, l]
                z.n13b = z.n13b + z.LuTotPhos[y, l]
                z.n6bdn = z.n6bdn + z.LuDisNitr[y, l]
                z.n13bdp = z.n13bdp + z.LuDisPhos[y, l]

        # Convert animal loads into English units
        z.GRLBN = z.GRLostBarnN[y, 0]
        z.NGLBN = z.NGLostBarnN[y, 0]
        z.GRLBP = z.GRLostBarnP[y, 0]
        z.NGLBP = z.NGLostBarnP[y, 0]
        z.NGLManP = z.NGLostManP[y, 0]

        # Get the fecal coliform values
        z.NGLBFC = z.NGLostBarnFC[y, 0]
        z.GRLBFC = z.GRLostBarnFC[y, 0]
        z.GRSFC = z.AvGRStreamFC
        z.GRSN = z.AvGRStreamN
        z.GRSP = z.AvGRStreamP

        # Get the initial pathogen loads
        z.n139 = z.AnimalFC[y, 0]
        z.n140 = z.WWOrgs[y, 0]
        z.n146 = z.WWOrgs[y, 0]
        z.n141 = z.SSOrgs[y, 0]
        z.n147 = z.SSOrgs[y, 0]
        z.n142 = z.UrbOrgs[y, 0]
        z.n143 = z.WildOrgs[y, 0]
        z.n149 = z.WildOrgs[y, 0]

        # Initial pathogen total load
        z.n144 = z.n139 + z.n140 + z.n141 + z.n142 + z.n143

        # FARM ANIMAL LOADS
        n7b = z.AnimalN[y, 0]
        n14b = z.AnimalN[y, 0]

        # CONVERT AVERAGE STREAM BANK ERIOSION, N AND P TO ENGLISH UNITS
        z.n4 = round((z.StreamBankEros[y, 0] * z.RetentFactorSed * (1 - z.AttenTSS) * SedConvert))
        z.n8 = round((z.StreamBankN[y, 0] * NPConvert * z.RetentFactorN * (1 - z.AttenN)))
        z.n15 = round((z.StreamBankP[y, 0] * NPConvert * z.RetentFactorP * (1 - z.AttenP)))

        # PERFORM LOAD REDUCTIONS BASED ON BMPS IN SCENARIO FILE
        LoadReductions.AdjustScnLoads(z)

        # CONVERT AVERAGE STREAM BANK ERIOSION, N AND P TO ENGLISH UNITS
        z.StreamBankEros[y, 0] = z.n4
        z.StreamBankN[y, 0] = z.n8
        z.StreamBankP[y, 0] = z.n15

        z.AnimalFC[y, 0] = z.n145
        z.UrbOrgs[y, 0] = z.n148

        # Get the FC reduction for monthly loads
        UrbanFCFrac = 0
        FarmFCFrac = 0

        if z.n139 > 0:
            FarmFCFrac = z.n145 / z.n139
        if z.n142 > 0:
            UrbanFCFrac = z.n148 / z.n142

        for i in range(0, 12):
            z.AnimalFC[y, 0] = z.AnimalFC[y, 0] * FarmFCFrac
            z.UrbOrgs[y, 0] = z.UrbOrgs[y, 0] * UrbanFCFrac

        # Reduced total pathogen loads
        n150 = z.n145 + z.n146 + z.n147 + z.n148 + z.n149
        z.TotalOrgs[y, 0] = n150

        # FARM ANIMAL LOADS
        z.AnimalN[y, 0] = n7b
        z.AnimalN[y, 0] = n14b

        # FOR ALL LAND USES
        z.TotDisNitr = 0
        z.TotTotNitr = 0
        z.TotDisPhos = 0
        z.TotTotPhos = 0
        z.TotSedyield = 0

        for l in range(0, z.NLU):
            if z.Landuse[l].lower() == "hay/past":
                z.LuSedYield[y, l] = z.n2
                z.LuTotNitr[y, l] = z.n6
                z.LuTotPhos[y, l] = z.n13
                z.LuDisNitr[y, l] = z.n6dn
                z.LuDisPhos[y, l] = z.n13dp

                if z.LuDisNitr[y, l] > z.LuTotNitr[y, l]:
                    z.LuDisNitr[y, l] = z.LuTotNitr[y, l]
                if z.LuDisPhos[y, l] > z.LuTotPhos[y, l]:
                    z.LuDisPhos[y, l] = z.LuTotPhos[y, l]
            elif z.Landuse[l].lower() == "cropland":
                if z.LuDisNitr[y, l] > 0:
                    z.LuDisNitr[y, l] = z.LuDisNitr[y, l] * z.n5 / z.LuTotNitr[y, l]
                if z.LuDisPhos[y, l] > 0:
                    z.LuDisPhos[y, l] = z.LuDisPhos[y, l] * z.n12 / z.LuTotPhos[y, l]

                z.LuSedYield[y, l] = z.n1
                z.LuTotNitr[y, l] = z.n5
                z.LuTotPhos[y, l] = z.n12
                z.LuDisNitr[y, l] = z.n5dn
                z.LuDisPhos[y, l] = z.n12dp
            elif z.Landuse[l].lower() == "unpaved_rd":
                z.LuSedYield[y, l] = z.n2d
                z.LuTotNitr[y, l] = z.n6d
                z.LuTotPhos[y, l] = z.n13d
                z.LuDisNitr[y, l] = z.n6ddn
                z.LuDisPhos[y, l] = z.n13ddp

                if z.LuDisNitr[y, l] > z.LuTotNitr[y, l]:
                    z.LuDisNitr[y, l] = z.LuTotNitr[y, l]
                if z.LuDisPhos[y, l] > z.LuTotPhos[y, l]:
                    z.LuDisPhos[y, l] = z.LuTotPhos[y, l]

            if "ld" in z.Landuse[l].lower() and z.n24b > 0:
                z.LuSedYield[y, l] = z.n2c * z.Area[l] / z.n24b
                z.LuTotNitr[y, l] = z.n6c * z.Area[l] / z.n24b
                z.LuTotPhos[y, l] = z.n13c * z.Area[l] / z.n24b
                z.LuDisNitr[y, l] = z.n6cdn * z.Area[l] / z.n24b
                z.LuDisPhos[y, l] = z.n13cdp * z.Area[l] / z.n24b

                if z.LuDisNitr[y, l] > z.LuTotNitr[y, l]:
                    z.LuDisNitr[y, l] = z.LuTotNitr[y, l]
                if z.LuDisPhos[y, l] > z.LuTotPhos[y, l]:
                    z.LuDisPhos[y, l] = z.LuTotPhos[y, l]
            elif ("hd" in z.Landuse[l].lower() or "md" in z.Landuse[l]) and z.n23b > 0:
                z.LuSedYield[y, l] = z.n2b * z.Area[l] / z.n23b
                z.LuTotNitr[y, l] = z.n6b * z.Area[l] / z.n23b
                z.LuTotPhos[y, l] = z.n13b * z.Area[l] / z.n23b
                z.LuDisNitr[y, l] = z.n6bdn * z.Area[l] / z.n23b
                z.LuDisPhos[y, l] = z.n13bdp * z.Area[l] / z.n23b

                if z.LuDisNitr[y, l] > z.LuTotNitr[y, l]:
                    z.LuDisNitr[y, l] = z.LuTotNitr[y, l]
                if z.LuDisPhos[y, l] > z.LuTotPhos[y, l]:
                    z.LuDisPhos[y, l] = z.LuTotPhos[y, l]
            if z.LuDisNitr[y, l] > z.LuTotNitr[y, l]:
                z.LuDisNitr[y, l] = z.LuTotNitr[y, l]
            if z.LuDisPhos[y, l] > z.LuTotPhos[y, l]:
                z.LuDisPhos[y, l] = z.LuTotPhos[y, l]

    # WRITE THE RESULTS FILES INTO THE OUTPUT DIRECTORY IN METRIC UNITS
    # TODO: Skipping section that prepares and writes AnnualFile and AnnCsvFile
    # Lines ~630 - 921

    # WRITE THE SUMARY FILES TO THE OUTPUT DIRECTORY IN METRIC UNITS
    # TODO: For now, we are only writing the first chunk of AvgFile

    # Sum Variables for Aggregate Summary Ouput Files
    # if FirstRun: XXX: Commented out because we don't
    # have the concept of a "first run" in the port.
    SumNYrs = z.NYrs
    SumNRur = z.NRur
    SumNUrb = z.NUrb
    SumNLU = z.NLU
    # SumOpt = z.Opt
    SumWxYrBeg = z.WxYrBeg
    SumWxYrEnd = z.WxYrEnd

    if z.NYrs > SumNYrs:
        SumNYrs = z.NYrs
    if z.NRur > SumNRur:
        SumNRur = z.NRur
    if z.NUrb > SumNUrb:
        SumNUrb = z.NUrb
    if z.NLU > SumNLU:
        SumNLU = z.NLU
    # if z.Opt > SumOpt:
    #    SumOpt = z.Opt
    if z.WxYrBeg < SumWxYrBeg:
        SumWxYrBeg = z.WxYrBeg
    if z.WxYrEnd > SumWxYrEnd:
        SumWxYrEnd = z.WxYrEnd
    z.SumSedDelivRatio = z.SumSedDelivRatio + (z.SedDelivRatio * z.TotArea)

    output = {}

    # Equivalent to Line 927 of source
    output['meta'] = {
        'NYrs': z.NYrs,
        'NRur': z.NRur,
        'NUrb': z.NUrb,
        'NLU': z.NLU,
        'SedDelivRatio': z.SedDelivRatio,
        'WxYrBeg': z.WxYrBeg,
        'WxYrEnd': z.WxYrEnd,
    }

    output['monthly'] = []

    # Equivalent to lines 965 - 988 of source
    for i in range(0, 12):
        output['monthly'].append({
            'AvPrecipitation': z.AvPrecipitation[i],
            'AvEvapoTrans': z.AvEvapoTrans[i],
            'AvGroundWater': z.AvGroundWater[i],
            'AvRunoff': z.AvRunoff[i],
            'AvStreamFlow': z.AvStreamFlow[i],
            'AvPtSrcFlow': z.AvPtSrcFlow[i],
            'AvTileDrain': z.AvTileDrain[i],
            'AvWithdrawal': z.AvWithdrawal[i],
        })

    return output


def WriteOutputSumFiles():
    print('WriteOutputSumFiles')


def UrbanAreasOutput():
    print('UrbanAreasOutput')
