# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

"""
Imported from CalcLoads.bas
"""


def CalculateLoads(z, Y):
    print('CalculateLoads')

    # CALCULATE THE MONTHLY WATER BALANCE FOR STREAM Flow FOR EACH YEAR OF THE ANALYSIS
    for i in range(12):
        z.StreamFlow[Y, i] = (z.Runoff[Y, i]
                              + z.GroundWatLE[Y, i]
                              + z.PtSrcFlow[Y, i]
                              + z.TileDrain[Y, i]
                              - z.Withdrawal[Y, i])

        z.StreamFlowLE[Y, i] = z.StreamFlow[Y, i]
        if z.StreamFlowLE[Y, i] < 0:
            z.StreamFlowLE[Y, i] = 0

    # ANNUAL WATER BALANCE CALCULATIONS
    for i in range(12):
        # Calculate landuse runoff for rural areas
        for l in range(z.NRur):
            z.LuRunoff[Y, l] += z.RurQRunoff[l, i]

        # Calculate landuse runoff for urban areas
        for l in range(z.NRur, z.NLU):
            z.LuRunoff[Y, l] += z.UrbQRunoff[l, i]

        z.Precipitation[Y, 0] += z.Precipitation[Y, i]
        z.Runoff[Y, 0] += z.Runoff[Y, i]
        z.GroundWatLE[Y, 0] += z.GroundWatLE[Y, i]
        z.Evapotrans[Y, 0] += z.Evapotrans[Y, i]
        z.PtSrcFlow[Y, 0] += z.PtSrcFlow[Y, i]
        z.Withdrawal[Y, 0] += z.Withdrawal[Y, i]
        z.StreamFlow[Y, 0] += z.StreamFlow[Y, i]

    # CALCULATE ANNUAL NITROGEN  LOADS FROM NORMAL SEPTIC SYSTEMS
    z.AnNormNitr = 0
    for i in range(12):
        z.AnNormNitr += z.MonthNormNitr[i] * z.NumNormalSys[i]

    z.CalendarYr = z.WxYrBeg + (Y - 1)

    # SEDIMENT YIELD AND TILE DRAINAGE
    for i in range(12):
        z.BSed[i] = 0
        for m in range(i, 12):
            z.BSed[i] += z.SedTrans[Y, m]
        for m in range(i):
            if z.BSed[m] > 0:
                z.SedYield[Y, i] += z.Erosion[Y, m] / z.BSed[m]

        z.SedYield[Y, i] = z.SedDelivRatio * z.SedTrans[Y, i] * z.SedYield[Y, i]
        z.SedYield[Y, 0] += z.SedYield[Y, i]
        z.Erosion[Y, 0] += z.Erosion[Y, i]

        # CALCULATION OF THE LANDUSE EROSION AND SEDIMENT YIELDS
        for l in range(z.NRur):
            z.LuErosion[Y, l] += z.ErosWashoff[l, i]
            z.LuSedYield[Y, l] = z.LuErosion[Y, l] * z.SedDelivRatio

        # Add in the urban calucation for sediment
        for l in range(z.NRur, z.NLU):
            z.UrbSedLoad[l, i] += z.LuLoad[Y, l, 2]

    # NUTRIENT FLUXES
    for i in range(12):
        for l in range(z.NRur):
            # RURAL DISSOLVED NUTRIENTS
            z.NConc = z.NitrConc[l]
            z.PConc = z.PhosConc[l]

            # MANURE SPREADING DAYS FOR FIRST SPREADING PERIOD
            if l < z.ManuredAreas and i >= z.FirstManureMonth and i <= z.LastManureMonth:
                z.NConc = z.ManNitr[l]
                z.PConc = z.ManPhos[l]

            # MANURE SPREADING DAYS FOR SECOND SPREADING PERIOD
            if l < z.ManuredAreas and i >= z.FirstManureMonth2 and i <= z.LastManureMonth2:
                z.NConc = z.ManNitr[l]
                z.PConc = z.ManPhos[l]

            nRunoff = 0.1 * z.NConc * z.RurQRunoff[l, i] * z.Area[l]
            pRunoff = 0.1 * z.PConc * z.RurQRunoff[l, i] * z.Area[l]

            z.DisNitr[Y, i] += nRunoff
            z.DisPhos[Y, i] += pRunoff
            z.LuTotNitr[Y, l] += nRunoff
            z.LuTotPhos[Y, l] += pRunoff
            z.LuDisNitr[Y, l] += nRunoff
            z.LuDisPhos[Y, l] += pRunoff

            # ADD SOLID RURAL NUTRIENTS
            z.LuTotNitr[Y, l] += 0.001 * z.SedDelivRatio * z.ErosWashoff[l, i] * z.SedNitr
            z.LuTotPhos[Y, l] += 0.001 * z.SedDelivRatio * z.ErosWashoff[l, i] * z.SedPhos

        z.TotNitr[Y, i] = z.DisNitr[Y, i] + 0.001 * z.SedNitr * z.SedYield[Y, i]
        z.TotPhos[Y, i] = z.DisPhos[Y, i] + 0.001 * z.SedPhos * z.SedYield[Y, i]

        # SUM TILE DRAIN N, P, AND SEDIMENT
        z.TileDrainN[Y, i] += ((((z.TileDrain[Y, i] / 100) * z.TotAreaMeters) * 1000) * z.TileNconc) / 1000000
        z.TileDrainP[Y, i] += ((((z.TileDrain[Y, i] / 100) * z.TotAreaMeters) * 1000) * z.TilePConc) / 1000000
        z.TileDrainSed[Y, i] += ((((z.TileDrain[Y, i] / 100) * z.TotAreaMeters) * 1000) * z.TileSedConc) / 1000000

        # ADD URBAN NUTRIENTS
        for l in range(z.NRur, z.NLU):
            z.LuTotNitr[Y, l] += z.LuLoad[Y, l, 0] / z.NYrs / 2
            z.LuTotPhos[Y, l] += z.LuLoad[Y, l, 1] / z.NYrs / 2
            z.LuDisNitr[Y, l] += z.LuDisLoad[Y, l, 1] / z.NYrs / 2
            z.LuDisPhos[Y, l] += z.LuDisLoad[Y, l, 2] / z.NYrs / 2
            z.LuSedYield[Y, l] += (z.LuLoad[Y, l, 2] / z.NYrs) / 1000 / 2

        z.DisNitr[Y, i] += z.DisLoad[Y, i, 1]
        z.DisPhos[Y, i] += z.DisLoad[Y, i, 2]
        z.TotNitr[Y, i] += z.Load[Y, i, 1]
        z.TotPhos[Y, i] += z.Load[Y, i, 2]

        # ADD UPLAND N and P LOADS
        z.UplandN[Y, i] = z.TotNitr[Y, i]
        z.UplandP[Y, i] = z.TotPhos[Y, i]

        # ADD GROUNDWATER, POINT SOURCES,
        z.GroundNitr[Y, i] = 0.1 * z.GrNitrConc * z.GroundWatLE[Y, i] * z.AreaTotal
        z.GroundPhos[Y, i] = 0.1 * z.GrPhosConc * z.GroundWatLE[Y, i] * z.AreaTotal
        z.DisNitr[Y, i] += z.GroundNitr[Y, i] + z.PointNitr[i]
        z.DisPhos[Y, i] += z.GroundPhos[Y, i] + z.PointPhos[i]
        z.TotNitr[Y, i] += z.GroundNitr[Y, i] + z.PointNitr[i]
        z.TotPhos[Y, i] += z.GroundPhos[Y, i] + z.PointPhos[i]

        # ADD SEPTIC SYSTEM SOURCES TO MONTHLY DISSOLVED NUTRIENT TOTALS
        if z.GroundWatLE[Y, 0] <= 0:
            z.GroundWatLE[Y, 0] = 0.0001

        z.MonthNormNitr[i] = z.AnNormNitr * z.GroundWatLE[Y, i] / z.GroundWatLE[Y, 0]

        z.DisSeptNitr = (z.MonthNormNitr[i]
                         + z.MonthPondNitr[i]
                         + z.MonthShortNitr[i] * z.NumShortSys[i]
                         + z.MonthDischargeNitr[i] * z.NumDischargeSys[i])

        z.DisSeptPhos = (z.MonthPondPhos[i]
                         + z.MonthShortPhos[i] * z.NumShortSys[i]
                         + z.MonthDischargePhos[i] * z.NumDischargeSys[i])

        # 0.59 IS ATTENUATION FACTOR FOR SOIL LOSS
        # 0.66 IS ATTENUATION FACTOR FOR SUBSURFACE FLOW LOSS
        z.DisSeptNitr /= 1000 * 0.59 * 0.66
        z.DisSeptPhos /= 1000

        z.DisNitr[Y, i] += z.DisSeptNitr
        z.DisPhos[Y, i] += z.DisSeptPhos
        z.TotNitr[Y, i] += z.DisSeptNitr
        z.TotPhos[Y, i] += z.DisSeptPhos
        z.SepticN[Y, i] += z.DisSeptNitr
        z.SepticP[Y, i] += z.DisSeptPhos

        # ANNUAL TOTALS
        z.DisNitr[Y, 0] += z.DisNitr[Y, i]
        z.DisPhos[Y, 0] += z.DisPhos[Y, i]
        z.TotNitr[Y, 0] += z.TotNitr[Y, i]
        z.TotPhos[Y, 0] += z.TotPhos[Y, i]

        # UPDATE ANNUAL SEPTIC SYSTEM LOADS
        z.SepticNitr[Y] += z.DisSeptNitr
        z.SepticPhos[Y] += z.DisSeptPhos

        # Annual pathogen totals
        z.AnimalFC[Y, 0] += z.AnimalFC[Y, i]
        z.WWOrgs[Y, 0] += z.WWOrgs[Y, i]
        z.SSOrgs[Y, 0] += z.SSOrgs[Y, i]
        z.UrbOrgs[Y, 0] += z.UrbOrgs[Y, i]
        z.WildOrgs[Y, 0] += z.WildOrgs[Y, i]
        z.TotalOrgs[Y, 0] += z.TotalOrgs[Y, i]
        z.CMStream[Y, 0] += z.CMStream[Y, i]
        z.OrgConc[Y, 0] += z.OrgConc[Y, i]

        # CALCULATE THE VOLUMETRIC STREAM Flow
        z.StreamFlowVol[Y, i] = ((z.StreamFlowLE[Y, i] / 100) * z.TotAreaMeters) / (86400 * z.DaysMonth[Y, i])
