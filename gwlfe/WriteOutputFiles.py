# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

import logging

import numpy as np

from . import LoadReductions
from .enums import YesOrNo, LandUse


log = logging.getLogger(__name__)


CM_TO_M = 1 / 100
HA_TO_M2 = 10000
KG_TO_MG = 1000000
M3_TO_L = 1000
TONNE_TO_KG = 1000


def WriteOutput(z):
    log.debug('WriteOutput')

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

    AreaSum = np.zeros(12)

    # INSERT VALUES FOR BMP SCENARIO FILE FOR PREDICT APPLICATION
    for l in range(z.NLU):
        z.AvLuSedYield[l] = (z.AvLuSedYield[l] * z.RetentFactorSed) * (1 - z.AttenTSS)
        z.AvLuDisNitr[l] = (z.AvLuDisNitr[l] * z.RetentFactorN) * (1 - z.AttenN)
        z.AvLuTotNitr[l] = (z.AvLuTotNitr[l] * z.RetentFactorN) * (1 - z.AttenN)
        z.AvLuDisPhos[l] = (z.AvLuDisPhos[l] * z.RetentFactorP) * (1 - z.AttenP)
        z.AvLuTotPhos[l] = (z.AvLuTotPhos[l] * z.RetentFactorP) * (1 - z.AttenP)

    # SET THE SCENARIO VALUES TO LANDUSE LOADS
    for l in range(z.NRur):
        if z.Landuse[l] is LandUse.HAY_PAST:
            z.n2 = z.AvLuSedYield[l]
            z.n6 = z.AvLuTotNitr[l]
            z.n13 = z.AvLuTotPhos[l]
            z.n6dn = z.AvLuDisNitr[l]
            z.n13dp = z.AvLuDisPhos[l]
            z.n24 = round(z.Area[l])
        elif z.Landuse[l] is LandUse.CROPLAND:
            z.n1 = z.AvLuSedYield[l]
            z.n5 = z.AvLuTotNitr[l]
            z.n12 = z.AvLuTotPhos[l]
            z.n5dn = z.AvLuDisNitr[l]
            z.n12dp = z.AvLuDisPhos[l]
            z.n23 = round(z.Area[l])
        elif z.Landuse[l] is LandUse.TURFGRASS:
            z.n2t = z.AvLuSedYield[l]
            z.n6t = z.AvLuTotNitr[l]
            z.n13t = z.AvLuTotPhos[l]
            z.n24t = round(z.Area[l])
        elif z.Landuse[l] is LandUse.UNPAVED_ROAD:
            z.n2d = z.AvLuSedYield[l]
            z.n6d = z.AvLuTotNitr[l]
            z.n13d = z.AvLuTotPhos[l]
            z.n6ddn = z.AvLuDisNitr[l]
            z.n13ddp = z.AvLuDisPhos[l]
        else:
            AvOtherLuSed = AvOtherLuSed + z.AvLuSedYield[l]
            AvOtherLuNitr = AvOtherLuNitr + z.AvLuTotNitr[l]
            AvOtherLuPhos = AvOtherLuPhos + z.AvLuTotPhos[l]

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

    for l in range(z.NRur, z.NLU):
        if z.Landuse[l] in [LandUse.LD_MIXED, LandUse.LD_RESIDENTIAL]:
            z.n2c = z.n2c + z.AvLuSedYield[l]
            z.n6c = z.n6c + z.AvLuTotNitr[l]
            z.n13c = z.n13c + z.AvLuTotPhos[l]
            z.n6cdn = z.n6cdn + z.AvLuDisNitr[l]
            z.n13cdp = z.n13cdp + z.AvLuDisPhos[l]
            z.n24b = z.n24b + round(z.Area[l])
        elif z.Landuse[l] in [LandUse.MD_MIXED, LandUse.HD_MIXED,
                              LandUse.MD_RESIDENTIAL, LandUse.HD_RESIDENTIAL]:
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
    if z.SepticFlag is YesOrNo.YES:
        for i in range(12):
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
    z.GRLBN = z.AvGRLostBarnNSum
    z.NGLBN = z.AvNGLostBarnNSum
    z.GRLBP = z.AvGRLostBarnPSum
    z.NGLBP = z.AvNGLostBarnPSum
    z.NGLManP = z.AvNGLostManPSum

    # Get the fecal coliform values
    z.NGLBFC = z.AvNGLostBarnFCSum
    z.GRLBFC = z.AvGRLostBarnFCSum
    z.GRSFC = z.AvGRStreamFC
    z.GRSN = z.AvGRStreamN
    z.GRSP = z.AvGRStreamP

    # Get the initial pathogen loads
    z.n139 = z.AvAnimalFCSum
    z.n140 = z.AvWWOrgsSum
    z.n146 = z.AvWWOrgsSum
    z.n141 = z.AvSSOrgsSum
    z.n147 = z.AvSSOrgsSum
    z.n142 = z.AvUrbOrgsSum
    z.n143 = z.AvWildOrgsSum
    z.n149 = z.AvWildOrgsSum

    # FARM ANIMAL LOADS
    z.n7b = z.AvAnimalNSum
    z.n14b = z.AvAnimalPSum

    # XXX: These are not used in our port.
    # InitialAnimalN = z.n7b
    # InitialAnimalP = z.n14b

    # Get the AEUs
    z.n41j = round(z.TotLAEU)
    z.n41k = round(z.TotPAEU)
    z.n41l = round(z.TotAEU)

    # CONVERT AVERAGE STREAM BANK ERIOSION, N AND P TO ENGLISH UNITS
    z.n4 = round(z.AvStreamBankErosSum * z.RetentFactorSed * (1 - z.AttenTSS) * SedConvert)
    z.n8 = round(z.AvStreamBankNSum * NPConvert * z.RetentFactorN * (1 - z.AttenN))
    z.n15 = round(z.AvStreamBankPSum * NPConvert * z.RetentFactorP * (1 - z.AttenP))

    # PERFORM LOAD REDUCTIONS BASED ON BMPS IN SCENARIO FILE
    LoadReductions.AdjustScnLoads(z)

    # CONVERT AVERAGE STREAM BANK ERIOSION, N AND P TO ENGLISH UNITS
    z.AvStreamBankErosSum = z.n4
    z.AvStreamBankNSum = z.n8
    z.AvStreamBankPSum = z.n15

    z.AvAnimalFCSum = z.n145
    z.AvUrbOrgsSum = z.n148

    # Get the FC reduction for monthly loads
    UrbanFCFrac = 0
    FarmFCFrac = 0

    if z.n139 > 0:
        FarmFCFrac = z.n145 / z.n139
    if z.n142 > 0:
        UrbanFCFrac = z.n148 / z.n142

    for i in range(12):
        z.AvAnimalFC[i] = z.AvAnimalFC[i] * FarmFCFrac
        z.AvUrbOrgs[i] = z.AvUrbOrgs[i] * UrbanFCFrac

    # Reset the existing urban and animal FC loads to the reduced future loads, n145 and n148
    z.n139 = z.n145
    z.n142 = z.n148

    # Initial pathogen total load
    z.n144 = z.n139 + z.n140 + z.n141 + z.n142 + z.n143

    # Reduced total pathogen loads
    z.n150 = z.n145 + z.n146 + z.n147 + z.n148 + z.n149
    z.AvTotalOrgsSum = z.n150

    # FARM ANIMAL LOAD REDUCTION FOR N AND P
    z.AvAnimalNSum = z.n7b
    z.AvAnimalPSum = z.n14b
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
    for l in range(z.NLU):
        if z.Landuse[l] is LandUse.HAY_PAST:
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
                AreaSum[2] = AreaSum[2] + z.Area[l]
        elif z.Landuse[l] is LandUse.CROPLAND:
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
                AreaSum[3] = AreaSum[3] + z.Area[l]
        elif z.Landuse[l] is LandUse.UNPAVED_ROAD:
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
                AreaSum[6] = AreaSum[6] + z.Area[l]

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
    for l in range(z.NRur, z.NLU):
        if z.n24b > 0 and z.Landuse[l] in [LandUse.LD_MIXED, LandUse.LD_RESIDENTIAL]:
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
                AreaSum[0] = AreaSum[0] + z.Area[l]
        elif z.n23b > 0 and z.Landuse[l] in [LandUse.MD_MIXED, LandUse.HD_MIXED,
                                             LandUse.MD_RESIDENTIAL, LandUse.HD_RESIDENTIAL]:
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
                AreaSum[1] = AreaSum[1] + z.Area[l]

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
    AvTotalSed = (AvTotalSed + (((z.AvStreamBankErosSum / 1000) +
                  ((z.AvTileDrainSedSum / 1000)) * z.RetentFactorSed * (1 - z.AttenTSS))))
    AvDisN = (AvDisN + ((z.AvGroundNitrSum + YrPointNitr + z.AvSeptNitr) *
              z.RetentFactorN * (1 - z.AttenN)))
    AvTotalN = (AvTotalN + ((z.AvStreamBankNSum + (z.AvGroundNitrSum + z.AvTileDrainNSum +
                z.AvAnimalNSum + YrPointNitr + z.AvSeptNitr) * z.RetentFactorN * (1 - z.AttenN))))
    AvDisP = AvDisP + ((z.AvGroundPhosSum + YrPointPhos + z.AvSeptPhos) * z.RetentFactorP * (1 - z.AttenP))
    AvTotalP = (AvTotalP + ((z.AvStreamBankPSum + (z.AvGroundPhosSum + z.AvTileDrainPSum +
                z.AvAnimalPSum + YrPointPhos + z.AvSeptPhos) * z.RetentFactorP * (1 - z.AttenP))))

    # OBTAIN THE AVERAGE TOTAL MONTHLY LOADS
    AvMonDisN = 0
    AvMonTotN = 0
    AvMonDisP = 0
    AvMonTotP = 0
    AvMonSed = 0
    AvMonEros = 0

    for i in range(12):
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
    z.n9 = round(((z.AvGroundNitrSum + z.AvTileDrainNSum) * NPConvert * z.RetentFactorN * (1 - z.AttenN)))
    z.n16 = round(((z.AvGroundPhosSum + z.AvTileDrainPSum) * NPConvert * z.RetentFactorP * (1 - z.AttenP)))

    # CONVERT ANNUAL POINT N AND P TO ENGLISH UNITS
    z.n10 = round((YrPointNitr * NPConvert * z.RetentFactorN * (1 - z.AttenN)))
    z.n17 = round((YrPointPhos * NPConvert * z.RetentFactorP * (1 - z.AttenP)))

    # CONVERT AVERAGE SEPTIC N AND P TO ENGLISH UNITS
    z.n11 = round((z.AvSeptNitr * NPConvert * z.RetentFactorN * (1 - z.AttenN)))
    z.n18 = round((z.AvSeptPhos * NPConvert * z.RetentFactorP * (1 - z.AttenP)))

    # ENTER THE OTHER SEDIMENT, N AND P INTO FIELDS
    z.n3 = round(((AvOtherLuSed + ((z.AvTileDrainSedSum * z.RetentFactorSed * (1 - z.AttenTSS)) / 1000)) * SedConvert))
    z.n7 = round((AvOtherLuNitr * z.RetentFactorN * (1 - z.AttenN) * NPConvert))
    z.n14 = round((AvOtherLuPhos * z.RetentFactorP * (1 - z.AttenP) * NPConvert))

    # ADD TURF TO HAY/PASTURE
    z.n2 = z.n2 + (n2t * SedConvert)
    z.n6 = z.n6 + (n6t * NPConvert)
    z.n13 = z.n13 + (n13t * NPConvert)
    z.n24 = z.n24 + n24t

    # Multiply sediment loads by 1000 to get them into Kg before writing to PRedICT section of file
    z.n1 = z.n1 * 1000
    z.n2 = z.n2 * 1000
    z.n2b = z.n2b * 1000
    z.n2c = z.n2c * 1000
    z.n2d = z.n2d * 1000
    z.n3 = z.n3 * 1000

    # Obtain the totals for sed, z.n az.nd P
    # Obtain the totals for sed, N and P
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

    for y in range(z.NYrs):
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

        for l in range(z.NLU):
            z.LuRunoff[y][l] = round(z.LuRunoff[y][l])
            z.LuErosion[y][l] = round(z.LuErosion[y][l])
            z.LuSedYield[y][l] = round((z.LuSedYield[y][l] * z.RetentFactorSed * (1 - z.AttenTSS)))
            z.LuDisNitr[y][l] = round((z.LuDisNitr[y][l] * z.RetentFactorN * (1 - z.AttenN)))
            z.LuTotNitr[y][l] = round((z.LuTotNitr[y][l] * z.RetentFactorN * (1 - z.AttenN)))
            z.LuDisPhos[y][l] = round((z.LuDisPhos[y][l] * z.RetentFactorP * (1 - z.AttenP)))
            z.LuTotPhos[y][l] = round((z.LuTotPhos[y][l] * z.RetentFactorP * (1 - z.AttenP)))

            if z.Landuse[l] is LandUse.HAY_PAST:
                z.n2 = z.LuSedYield[y][l]
                z.n6 = z.LuTotNitr[y][l]
                z.n13 = z.LuTotPhos[y][l]
                z.n6dn = z.LuDisNitr[y][l]
                z.n13dp = z.LuDisPhos[y][l]
            elif z.Landuse[l] is LandUse.CROPLAND:
                z.n1 = z.LuSedYield[y][l]
                z.n5 = z.LuTotNitr[y][l]
                z.n12 = z.LuTotPhos[y][l]
                z.n5dn = z.LuDisNitr[y][l]
                z.n12dp = z.LuDisPhos[y][l]
            elif z.Landuse[l] is LandUse.UNPAVED_ROAD:
                z.n2d = z.LuSedYield[y][l]
                z.n6d = z.LuTotNitr[y][l]
                z.n13d = z.LuTotPhos[y][l]
                z.n6ddn = z.LuDisNitr[y][l]
                z.n13ddp = z.LuDisPhos[y][l]
            elif z.Landuse[l] is LandUse.TURFGRASS:
                z.n2t = z.LuSedYield[y][l]
                z.n6t = z.LuTotNitr[y][l]
                z.n13t = z.LuTotPhos[y][l]
            else:
                AvOtherLuSed = AvOtherLuSed + z.LuSedYield[y][l]
                AvOtherLuNitr = AvOtherLuNitr + z.LuTotNitr[y][l]
                AvOtherLuPhos = AvOtherLuPhos + z.LuTotPhos[y][l]

            if z.Landuse[l] in [LandUse.LD_MIXED, LandUse.LD_RESIDENTIAL]:
                z.n2c = z.n2c + z.LuSedYield[y][l]
                z.n6c = z.n6c + z.LuTotNitr[y][l]
                z.n13c = z.n13c + z.LuTotPhos[y][l]
                z.n6cdn = z.n6cdn + z.LuDisNitr[y][l]
                z.n13cdp = z.n13cdp + z.LuDisPhos[y][l]
            elif z.Landuse[l] in [LandUse.MD_MIXED, LandUse.HD_MIXED,
                                  LandUse.MD_RESIDENTIAL, LandUse.HD_RESIDENTIAL]:
                z.n2b = z.n2b + z.LuSedYield[y][l]
                z.n6b = z.n6b + z.LuTotNitr[y][l]
                z.n13b = z.n13b + z.LuTotPhos[y][l]
                z.n6bdn = z.n6bdn + z.LuDisNitr[y][l]
                z.n13bdp = z.n13bdp + z.LuDisPhos[y][l]

        # Convert animal loads into English units
        z.GRLBN = z.GRLostBarnNSum[y]
        z.NGLBN = z.NGLostBarnNSum[y]
        z.GRLBP = z.GRLostBarnPSum[y]
        z.NGLBP = z.NGLostBarnPSum[y]
        z.NGLManP = z.NGLostManPSum[y]

        # Get the fecal coliform values
        z.NGLBFC = z.NGLostBarnFCSum[y]
        z.GRLBFC = z.GRLostBarnFCSum[y]
        z.GRSFC = z.AvGRStreamFC
        z.GRSN = z.AvGRStreamN
        z.GRSP = z.AvGRStreamP

        # Get the initial pathogen loads
        z.n139 = z.AnimalFCSum[y]
        z.n140 = z.WWOrgsSum[y]
        z.n146 = z.WWOrgsSum[y]
        z.n141 = z.SSOrgsSum[y]
        z.n147 = z.SSOrgsSum[y]
        z.n142 = z.UrbOrgsSum[y]
        z.n143 = z.WildOrgsSum[y]
        z.n149 = z.WildOrgsSum[y]

        # Initial pathogen total load
        z.n144 = z.n139 + z.n140 + z.n141 + z.n142 + z.n143

        # FARM ANIMAL LOADS
        n7b = z.AnimalNSum[y]
        # BUG: This is a bug in the original code.
        # This should be AnimalPSum
        n14b = z.AnimalNSum[y]

        # CONVERT AVERAGE STREAM BANK ERIOSION, N AND P TO ENGLISH UNITS
        z.n4 = round((z.StreamBankErosSum[y] * z.RetentFactorSed * (1 - z.AttenTSS) * SedConvert))
        z.n8 = round((z.StreamBankNSum[y] * NPConvert * z.RetentFactorN * (1 - z.AttenN)))
        z.n15 = round((z.StreamBankPSum[y] * NPConvert * z.RetentFactorP * (1 - z.AttenP)))

        # PERFORM LOAD REDUCTIONS BASED ON BMPS IN SCENARIO FILE
        LoadReductions.AdjustScnLoads(z)

        # CONVERT AVERAGE STREAM BANK ERIOSION, N AND P TO ENGLISH UNITS
        z.StreamBankErosSum[y] = z.n4
        z.StreamBankNSum[y] = z.n8
        z.StreamBankPSum[y] = z.n15

        z.AnimalFCSum[y] = z.n145
        z.UrbOrgsSum[y] = z.n148

        # Get the FC reduction for monthly loads
        UrbanFCFrac = 0
        FarmFCFrac = 0

        if z.n139 > 0:
            FarmFCFrac = z.n145 / z.n139
        if z.n142 > 0:
            UrbanFCFrac = z.n148 / z.n142

        for i in range(12):
            z.AnimalFCSum[y] *= FarmFCFrac
            z.UrbOrgsSum[y] *= UrbanFCFrac

        # Reduced total pathogen loads
        n150 = z.n145 + z.n146 + z.n147 + z.n148 + z.n149
        z.TotalOrgsSum[y] = n150

        # FARM ANIMAL LOADS
        z.AnimalNSum[y] = n7b
        # BUG: This is a bug in the original code.
        # This should be AnimalPSum
        z.AnimalNSum[y] = n14b

        # FOR ALL LAND USES
        z.TotDisNitr = 0
        z.TotTotNitr = 0
        z.TotDisPhos = 0
        z.TotTotPhos = 0
        z.TotSedyield = 0

        for l in range(z.NLU):
            if z.Landuse[l] is LandUse.HAY_PAST:
                z.LuSedYield[y][l] = z.n2
                z.LuTotNitr[y][l] = z.n6
                z.LuTotPhos[y][l] = z.n13
                z.LuDisNitr[y][l] = z.n6dn
                z.LuDisPhos[y][l] = z.n13dp

                if z.LuDisNitr[y][l] > z.LuTotNitr[y][l]:
                    z.LuDisNitr[y][l] = z.LuTotNitr[y][l]
                if z.LuDisPhos[y][l] > z.LuTotPhos[y][l]:
                    z.LuDisPhos[y][l] = z.LuTotPhos[y][l]
            elif z.Landuse[l] is LandUse.CROPLAND:
                if z.LuDisNitr[y][l] > 0:
                    z.LuDisNitr[y][l] = z.LuDisNitr[y][l] * z.n5 / z.LuTotNitr[y][l]
                if z.LuDisPhos[y][l] > 0:
                    z.LuDisPhos[y][l] = z.LuDisPhos[y][l] * z.n12 / z.LuTotPhos[y][l]

                z.LuSedYield[y][l] = z.n1
                z.LuTotNitr[y][l] = z.n5
                z.LuTotPhos[y][l] = z.n12
                z.LuDisNitr[y][l] = z.n5dn
                z.LuDisPhos[y][l] = z.n12dp
            elif z.Landuse[l] is LandUse.UNPAVED_ROAD:
                z.LuSedYield[y][l] = z.n2d
                z.LuTotNitr[y][l] = z.n6d
                z.LuTotPhos[y][l] = z.n13d
                z.LuDisNitr[y][l] = z.n6ddn
                z.LuDisPhos[y][l] = z.n13ddp

                if z.LuDisNitr[y][l] > z.LuTotNitr[y][l]:
                    z.LuDisNitr[y][l] = z.LuTotNitr[y][l]
                if z.LuDisPhos[y][l] > z.LuTotPhos[y][l]:
                    z.LuDisPhos[y][l] = z.LuTotPhos[y][l]

            if z.n24b > 0 and z.Landuse[l] in [LandUse.LD_MIXED, LandUse.LD_RESIDENTIAL]:
                z.LuSedYield[y][l] = z.n2c * z.Area[l] / z.n24b
                z.LuTotNitr[y][l] = z.n6c * z.Area[l] / z.n24b
                z.LuTotPhos[y][l] = z.n13c * z.Area[l] / z.n24b
                z.LuDisNitr[y][l] = z.n6cdn * z.Area[l] / z.n24b
                z.LuDisPhos[y][l] = z.n13cdp * z.Area[l] / z.n24b

                if z.LuDisNitr[y][l] > z.LuTotNitr[y][l]:
                    z.LuDisNitr[y][l] = z.LuTotNitr[y][l]
                if z.LuDisPhos[y][l] > z.LuTotPhos[y][l]:
                    z.LuDisPhos[y][l] = z.LuTotPhos[y][l]
            elif z.n23b > 0 and z.Landuse[l] in [LandUse.MD_MIXED, LandUse.HD_MIXED,
                                                 LandUse.MD_RESIDENTIAL, LandUse.HD_RESIDENTIAL]:
                z.LuSedYield[y][l] = z.n2b * z.Area[l] / z.n23b
                z.LuTotNitr[y][l] = z.n6b * z.Area[l] / z.n23b
                z.LuTotPhos[y][l] = z.n13b * z.Area[l] / z.n23b
                z.LuDisNitr[y][l] = z.n6bdn * z.Area[l] / z.n23b
                z.LuDisPhos[y][l] = z.n13bdp * z.Area[l] / z.n23b

                if z.LuDisNitr[y][l] > z.LuTotNitr[y][l]:
                    z.LuDisNitr[y][l] = z.LuTotNitr[y][l]
                if z.LuDisPhos[y][l] > z.LuTotPhos[y][l]:
                    z.LuDisPhos[y][l] = z.LuTotPhos[y][l]
            if z.LuDisNitr[y][l] > z.LuTotNitr[y][l]:
                z.LuDisNitr[y][l] = z.LuTotNitr[y][l]
            if z.LuDisPhos[y][l] > z.LuTotPhos[y][l]:
                z.LuDisPhos[y][l] = z.LuTotPhos[y][l]

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

    # Which land use sources to include in the totals.
    sources = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

    # ha
    AreaTotal = sum(z.Area[l] for l in sources)

    # kg
    SumSed = sum(z.AvLuSedYield[l] for l in sources) * TONNE_TO_KG
    SumSed += z.AvStreamBankErosSum

    # kg
    SumNitr = sum(z.AvLuTotNitr[l] for l in sources)
    SumNitr += z.AvStreamBankNSum
    SumNitr += z.AvAnimalNSum * z.RetentFactorN * (1 - z.AttenN)
    SumNitr += z.AvGroundNitrSum * z.RetentFactorN * (1 - z.AttenN)
    SumNitr += YrPointNitr * z.RetentFactorN * (1 - z.AttenN)
    SumNitr += z.AvSeptNitr * z.RetentFactorN * (1 - z.AttenN)

    # kg
    SumPhos = sum(z.AvLuTotPhos[l] for l in sources)
    SumPhos += z.AvStreamBankPSum
    SumPhos += z.AvAnimalPSum * z.RetentFactorP * (1 - z.AttenP)
    SumPhos += z.AvGroundPhosSum * z.RetentFactorP * (1 - z.AttenP)
    SumPhos += YrPointPhos * z.RetentFactorP * (1 - z.AttenP)
    SumPhos += z.AvSeptPhos * z.RetentFactorP * (1 - z.AttenP)

    # m^3/year
    MeanFlow = (z.AvStreamFlowSum * CM_TO_M) * (AreaTotal * HA_TO_M2)

    # Find index of month with lowest mean flow.
    LowFlowMonth = z.AvStreamFlow.tolist().index(min(z.AvStreamFlow))

    # m^3/year
    MeanLowFlow = (z.AvStreamFlow[LowFlowMonth] * CM_TO_M) * (AreaTotal * HA_TO_M2)

    # m^3/second
    MeanFlowPS = MeanFlow / 31536000

    # kg/ha
    LoadingRateSed = SumSed / AreaTotal
    LoadingRateN = SumNitr / AreaTotal
    LoadingRateP = SumPhos / AreaTotal

    # mg/l
    ConcSed = (SumSed * KG_TO_MG) / (MeanFlow * M3_TO_L)
    ConcN = (SumNitr * KG_TO_MG) / (MeanFlow * M3_TO_L)
    ConcP = (SumPhos * KG_TO_MG) / (MeanFlow * M3_TO_L)

    # mg/l
    LFConcSed = (z.AvLuSedYield[LowFlowMonth] * KG_TO_MG) / (MeanLowFlow * M3_TO_L)
    LFConcN = (z.AvTotNitr[LowFlowMonth] * KG_TO_MG) / (MeanLowFlow * M3_TO_L)
    LFConcP = (z.AvTotPhos[LowFlowMonth] * KG_TO_MG) / (MeanLowFlow * M3_TO_L)

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

    output['AreaTotal'] = AreaTotal
    output['MeanFlow'] = MeanFlow
    output['MeanFlowPerSecond'] = MeanFlowPS

    # Equivalent to lines 965 - 988 of source
    output['monthly'] = []
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

    output['Loads'] = []
    output['Loads'].append({
        'Source': 'Hay/Pasture',
        'Sediment': z.AvLuSedYield[0] * TONNE_TO_KG,
        'TotalN': z.AvLuTotNitr[0],
        'TotalP': z.AvLuTotPhos[0],
    })
    output['Loads'].append({
        'Source': 'Cropland',
        'Sediment': z.AvLuSedYield[1] * TONNE_TO_KG,
        'TotalN': z.AvLuTotNitr[1],
        'TotalP': z.AvLuTotPhos[1],
    })
    # Forest
    output['Loads'].append({
        'Source': 'Wooded Areas',
        'Sediment': z.AvLuSedYield[2] * TONNE_TO_KG,
        'TotalN': z.AvLuTotNitr[2],
        'TotalP': z.AvLuTotPhos[2],
    })
    output['Loads'].append({
        'Source': 'Wetlands',
        'Sediment': z.AvLuSedYield[3] * TONNE_TO_KG,
        'TotalN': z.AvLuTotNitr[3],
        'TotalP': z.AvLuTotPhos[3],
    })
    output['Loads'].append({
        'Source': 'Open Land',
        'Sediment': z.AvLuSedYield[6] * TONNE_TO_KG,
        'TotalN': z.AvLuTotNitr[6],
        'TotalP': z.AvLuTotPhos[6],
    })
    # Bare Rock, Sandy Areas
    output['Loads'].append({
        'Source': 'Barren Areas',
        'Sediment': sum(z.AvLuSedYield[l] * TONNE_TO_KG for l in (7, 8)),
        'TotalN': sum(z.AvLuTotNitr[l] for l in (7, 8)),
        'TotalP': sum(z.AvLuTotPhos[l] for l in (7, 8)),
    })
    output['Loads'].append({
        'Source': 'Low-Density Mixed',
        'Sediment': z.AvLuSedYield[10] * TONNE_TO_KG,
        'TotalN': z.AvLuTotNitr[10],
        'TotalP': z.AvLuTotPhos[10],
    })
    output['Loads'].append({
        'Source': 'Medium-Density Mixed',
        'Sediment': z.AvLuSedYield[11] * TONNE_TO_KG,
        'TotalN': z.AvLuTotNitr[11],
        'TotalP': z.AvLuTotPhos[11],
    })
    output['Loads'].append({
        'Source': 'High-Density Mixed',
        'Sediment': z.AvLuSedYield[12] * TONNE_TO_KG,
        'TotalN': z.AvLuTotNitr[12],
        'TotalP': z.AvLuTotPhos[12],
    })
    # Disturbed, Turfgrass, Unpaved Road
    output['Loads'].append({
        'Source': 'Other Upland Areas',
        'Sediment': sum(z.AvLuSedYield[l] * TONNE_TO_KG for l in (4, 5, 9)),
        'TotalN': sum(z.AvLuTotNitr[l] for l in (4, 5, 9)),
        'TotalP': sum(z.AvLuTotPhos[l] for l in (4, 5, 9)),
    })
    output['Loads'].append({
        'Source': 'Farm Animals',
        'Sediment': 0,
        'TotalN': z.AvAnimalNSum * z.RetentFactorN * (1 - z.AttenN),
        'TotalP': z.AvAnimalPSum * z.RetentFactorP * (1 - z.AttenP),
    })
    output['Loads'].append({
        'Source': 'Stream Bank Erosion',
        'Sediment': z.AvStreamBankErosSum,
        'TotalN': z.AvStreamBankNSum,
        'TotalP': z.AvStreamBankPSum,
    })
    output['Loads'].append({
        'Source': 'Subsurface Flow',
        'Sediment': 0,
        'TotalN': z.AvGroundNitrSum * z.RetentFactorN * (1 - z.AttenN),
        'TotalP': z.AvGroundPhosSum * z.RetentFactorP * (1 - z.AttenP),
    })
    output['Loads'].append({
        'Source': 'Point Sources',
        'Sediment': 0,
        'TotalN': YrPointNitr * z.RetentFactorN * (1 - z.AttenN),
        'TotalP': YrPointPhos * z.RetentFactorP * (1 - z.AttenP),
    })
    output['Loads'].append({
        'Source': 'Septic Systems',
        'Sediment': 0,
        'TotalN': z.AvSeptNitr * z.RetentFactorN * (1 - z.AttenN),
        'TotalP': z.AvSeptPhos * z.RetentFactorP * (1 - z.AttenP),
    })
    output['Loads'].append({
        'Source': 'Total Loads',
        'Sediment': SumSed,
        'TotalN': SumNitr,
        'TotalP': SumPhos,
    })
    output['Loads'].append({
        'Source': 'Loading Rates',
        'Sediment': LoadingRateSed,
        'TotalN': LoadingRateN,
        'TotalP': LoadingRateP,
    })
    output['Loads'].append({
        'Source': 'Mean Annual Concentration',
        'Sediment': ConcSed,
        'TotalN': ConcN,
        'TotalP': ConcP,
    })
    output['Loads'].append({
        'Source': 'Mean Low-Flow Concentration',
        'Sediment': LFConcSed,
        'TotalN': LFConcN,
        'TotalP': LFConcP,
    })

    return output


def WriteOutputSumFiles():
    log.debug('WriteOutputSumFiles')


def UrbanAreasOutput():
    log.debug('UrbanAreasOutput')
