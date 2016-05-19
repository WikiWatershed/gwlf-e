# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

"""
Imported from CalcCNErosRunoffSed.bas
"""

import math
import logging

from .enums import GrowFlag, LandUse


log = logging.getLogger(__name__)


def CalcCN(z, i, Y, j):
    """
    z - data model (public variables)
    i - month
    Y - year
    j - number of days in month
    """
    log.debug('CalcCN')

    z.UrbanQTotal = 0
    z.UncontrolledQ = 0
    z.RetentionEff = 0

    # Calculate Curve Number (CN)
    for l in range(z.NRur):
        z.Qrun = 0
        grow_factor = GrowFlag.intval(z.Grow[i])

        if z.CN[l] > 0:
            if z.Melt <= 0:
                if grow_factor > 0:
                    # growing season
                    if z.AMC5 >= 5.33:
                        z.CNum = z.NewCN[2][l]
                    elif z.AMC5 < 3.56:
                        z.CNum = z.NewCN[0][l] + (z.CN[l] - z.NewCN[0][l]) * z.AMC5 / 3.56
                    else:
                        z.CNum = z.CN[l] + (z.NewCN[2][l] - z.CN[l]) * (z.AMC5 - 3.56) / 1.77
                else:
                    # dormant season
                    if z.AMC5 >= 2.79:
                        z.CNum = z.NewCN[2][l]
                    elif z.AMC5 < 1.27:
                        z.CNum = z.NewCN[0][l] + (z.CN[l] - z.NewCN[0][l]) * z.AMC5 / 1.27
                    else:
                        z.CNum = z.CN[l] + (z.NewCN[2][l] - z.CN[l]) * (z.AMC5 - 1.27) / 1.52
            else:
                z.CNum = z.NewCN[2][l]

            z.Retention = 2540 / z.CNum - 25.4
            if z.Retention < 0:
                z.Retention = 0

            # z.Water balance and runoff calculation
            if z.Water >= 0.2 * z.Retention:
                z.Qrun = (z.Water - 0.2 * z.Retention) ** 2 / (z.Water + 0.8 * z.Retention)
                z.RuralQTotal += z.Qrun * z.Area[l] / z.RurAreaTotal
                z.RurQRunoff[l][i] += z.Qrun
                # TODO: (what is done with "DayQRunoff"? - appears not to be used)
                z.DayQRunoff[Y][i][j] = z.Qrun
                # TODO: (What is done with "AgQRunoff? - apparently nothing)
                if z.Landuse[l] is LandUse.CROPLAND:
                    # (Maybe used for STREAMPLAN?)
                    z.AgQTotal += z.Qrun * z.Area[l]
                    z.AgQRunoff[l][i] += z.Qrun
                elif z.Landuse[l] is LandUse.HAY_PAST:
                    z.AgQTotal += z.Qrun * z.Area[l]
                    z.AgQRunoff[l][i] += z.Qrun
                elif z.Landuse[l] is LandUse.TURFGRASS:
                    z.AgQTotal += z.Qrun * z.Area[l]
                    z.AgQRunoff[l][i] += z.Qrun
            else:
                z.Qrun = 0

        # EROSION, SEDIMENT WASHOFF FOR RURAL AND URBAN LANDUSE
        z.RurEros = 1.32 * z.Erosiv * z.KF[l] * z.LS[l] * z.C[l] * z.P[l] * z.Area[l]

        z.Erosion[Y][i] = z.Erosion[Y][i] + z.RurEros
        z.ErosWashoff[l][i] = z.ErosWashoff[l][i] + z.RurEros
        z.DayErWashoff[l][Y][i][j] = z.RurEros

        if z.SedDelivRatio == 0:
            z.SedDelivRatio = 0.0001

    for l in range(z.NRur, z.NLU):
        z.QrunI[l] = 0
        z.QrunP[l] = 0
        z.WashImperv[l] = 0
        z.WashPerv[l] = 0

    for q in range(z.Nqual):
        z.NetSolidLoad[q] = 0
        z.NetDisLoad[q] = 0

    if z.Water < 0.05:
        BasinWater(z, i, Y, j)
        return

    for l in range(z.NRur, z.NLU):
        grow_factor = GrowFlag.intval(z.Grow[i])

        # Find curve number
        if z.CNI[1][l] > 0:
            if z.Melt <= 0:
                if grow_factor > 0:
                    # Growing season
                    if z.AMC5 >= 5.33:
                        z.CNumImperv = z.CNI[2][l]
                    elif z.AMC5 < 3.56:
                        z.CNumImperv = z.CNI[0][l] + (z.CNI[1][l] - z.CNI[0][l]) * z.AMC5 / 3.56
                    else:
                        z.CNumImperv = z.CNI[1][l] + (z.CNI[2][l] - z.CNI[1][l]) * (z.AMC5 - 3.56) / 1.77
                else:
                    # Dormant season
                    if z.AMC5 >= 2.79:
                        z.CNumImperv = z.CNI[2][l]
                    elif z.AMC5 < 1.27:
                        z.CNumImperv = z.CNI[0][l] + (z.CNI[1][l] - z.CNI[0][l]) * z.AMC5 / 1.27
                    else:
                        z.CNumImperv = z.CNI[1][l] + (z.CNI[2][l] - z.CNI[1][l]) * (z.AMC5 - 1.27) / 1.52
            else:
                z.CNumImperv = z.CNI[2][l]

            z.CNumImpervReten = 2540 / z.CNumImperv - 25.4
            if z.CNumImpervReten < 0:
                z.CNumImpervReten = 0

            if z.Water >= 0.2 * z.CNumImpervReten:
                z.QrunI[l] = (z.Water - 0.2 * z.CNumImpervReten) ** 2 / (z.Water + 0.8 * z.CNumImpervReten)

        if z.CNP[1][l] > 0:
            if z.Melt <= 0:
                if grow_factor > 0:
                    # Growing season
                    if z.AMC5 >= 5.33:
                        z.CNumPerv = z.CNP[2][l]
                    elif z.AMC5 < 3.56:
                        z.CNumPerv = z.CNP[0][l] + (z.CNP[1][l] - z.CNP[0][l]) * z.AMC5 / 3.56
                    else:
                        z.CNumPerv = z.CNP[1][l] + (z.CNP[2][l] - z.CNP[1][l]) * (z.AMC5 - 3.56) / 1.77
                else:
                    # Dormant season
                    if z.AMC5 >= 2.79:
                        z.CNumPerv = z.CNP[2][l]
                    elif z.AMC5 < 1.27:
                        z.CNumPerv = z.CNP[0][l] + (z.CNP[1][l] - z.CNP[0][l]) * z.AMC5 / 1.27
                    else:
                        z.CNumPerv = z.CNP[1][l] + (z.CNP[2][l] - z.CNP[1][l]) * (z.AMC5 - 1.27) / 1.52
            else:
                z.CNumPerv = z.CNP[2][l]

            z.CNumPervReten = 2540 / z.CNumPerv - 25.4
            if z.CNumPervReten < 0:
                z.CNumPervReten = 0

            if z.Water >= 0.2 * z.CNumPervReten:
                z.QrunP[l] = (z.Water - 0.2 * z.CNumPervReten) ** 2 / (z.Water + 0.8 * z.CNumPervReten)

        lu = l - z.NRur

        if z.UrbAreaTotal > 0:
            z.UrbanQTotal += ((z.QrunI[l] * (z.Imper[l] * (1 - z.ISRR[lu]) * (1 - z.ISRA[lu]))
                              + z.QrunP[l] * (1 - (z.Imper[l] * (1 - z.ISRR[lu]) * (1 - z.ISRA[lu]))))
                              * z.Area[l] / z.UrbAreaTotal)

        z.UncontrolledQ += ((z.QrunI[l] * (z.Imper[l] * (1 - z.ISRR[lu]) * (1 - z.ISRA[lu]))
                            + z.QrunP[l] * (1 - (z.Imper[l] * (1 - z.ISRR[lu]) * (1 - z.ISRA[lu]))))
                            * z.Area[l] / z.AreaTotal)

        z.WashImperv[l] = (1 - math.exp(-1.81 * z.QrunI[l])) * z.ImpervAccum[l]
        z.ImpervAccum[l] -= z.WashImperv[l]

        z.WashPerv[l] = (1 - math.exp(-1.81 * z.QrunP[l])) * z.PervAccum[l]
        z.PervAccum[l] -= z.WashPerv[l]

        z.UrbQRunoff[l][i] += (z.QrunI[l] * (z.Imper[l] * (1 - z.ISRR[lu]) * (1 - z.ISRA[lu]))
                               + z.QrunP[l] * (1 - (z.Imper[l] * (1 - z.ISRR[lu]) * (1 - z.ISRA[lu]))))

    z.AdjUrbanQTotal = z.UrbanQTotal

    # Runoff retention
    if z.Qretention > 0:
        if z.UrbanQTotal > 0:
            if z.UrbanQTotal <= z.Qretention * z.PctAreaInfil:
                z.RetentionEff = 1
                z.AdjUrbanQTotal = 0
            else:
                z.RetentionEff = z.Qretention * z.PctAreaInfil / z.UrbanQTotal
                z.AdjUrbanQTotal -= z.Qretention * z.PctAreaInfil

    BasinWater(z, i, Y, j)


def BasinWater(z, i, Y, j):
    # Detention basin water balance
    if z.BasinArea > 0:
        z.BasinInflow = z.UrbAreaTotal * 10000 * (z.AdjUrbanQTotal / 100)

        if z.BasinInflow >= 0.5 * z.BasinVol and z.BasinInflow >= 0.1 * z.Capacity:
            z.Mixing = 1
        else:
            z.Mixing = 0

        z.BasinVol += z.BasinPrec - z.ETDetentBasin + z.BasinInflow
        if z.BasinVol < 0:
            z.BasinVol = 0

        # Basin cleaning
        if z.CleanMon > 0:
            threshold = z.BasinDeadStorage + 0.1 * (z.Capacity - z.BasinDeadStorage)
            # TODO: What is `i`?
            if z.CleanSwitch == 0 and i >= z.CleanMon and z.BasinVol < threshold:
                for q in range(z.Nqual):
                    z.SolidBasinMass[q] = 0
                    z.DisBasinMass[q] = 0
                z.CleanSwitch = 1

        z.ActiveVol = z.BasinVol - z.BasinDeadStorage
        if z.ActiveVol < 0:
            z.ActiveVol = 0
        if z.ActiveVol > z.Capacity - z.BasinDeadStorage:
            z.ActiveVol = z.Capacity - z.BasinDeadStorage

        z.Head = z.ActiveVol / z.BasinArea

        z.Discharge = 382700 * z.OutletCoef * math.sqrt(z.Head)
        if z.Discharge > z.ActiveVol:
            z.Discharge = z.ActiveVol

        z.Overflow = z.BasinVol - z.Discharge - z.Capacity
        if z.Overflow < 0:
            z.Overflow = 0

        z.OutFlow = z.Overflow + z.Discharge
        if z.BasinVol > 0:
            z.OutflowFract = z.OutFlow / z.BasinVol
            if z.OutflowFract > 1:
                z.OutflowFract = 1
        else:
            z.OutflowFract = 0

        z.BasinVol -= z.OutFlow
        z.AdjUrbanQTotal *= z.OutflowFract

    # BELOW ARE CALCULATIONS FOR URBAN LOADS
    # MAYBE THEY SHOULD BE IN "CALCULATE LOADS" SUBROUTINE???
    z.DissolvedLoad = 0
    z.SolidLoad = 0
    z.UrbLoadRed = 0

    if z.AdjUrbanQTotal > 0.001:
        for l in range(z.NRur, z.NLU):
            for q in range(z.Nqual):
                z.SolidBasinMass[q] = 0
                z.DisBasinMass[q] = 0

                if z.Storm > 0:
                    z.UrbLoadRed = (z.Water / z.Storm) * z.UrbBMPRed[l][q]
                else:
                    z.UrbLoadRed = 0

                if z.Water > z.Storm:
                    z.UrbLoadRed = z.UrbBMPRed[l][q]

                # TODO: Should 11 be NRur + 1?
                # What is this trying to do?
                lu = l - 11

                if z.Area[l] > 0:
                    z.SurfaceLoad = (((z.LoadRateImp[l][q] * z.WashImperv[l] * ((z.Imper[l] * (1 - z.ISRR[lu]) * (1 - z.ISRA[lu]))
                                       * (z.SweepFrac[i] + ((1 - z.SweepFrac[i]) * ((1 - z.UrbSweepFrac) * z.Area[l]) / z.Area[l])))
                                      + z.LoadRatePerv[l][q] * z.WashPerv[l] * (1 - (z.Imper[l] * (1 - z.ISRR[lu]) * (1 - z.ISRA[lu]))))
                                      * z.Area[l]) - z.UrbLoadRed)
                else:
                    z.SurfaceLoad = 0

                if z.SurfaceLoad < 0:
                    z.SurfaceLoad = 0

                z.DisSurfLoad = z.DisFract[l][q] * z.SurfaceLoad

                # Apply Bioretention and/or Stream Buffer BMP
                z.SurfaceLoad *= (1 - z.RetentionEff) * (1 - (z.FilterEff * z.PctStrmBuf))
                z.DisSurfLoad *= (1 - z.RetentionEff) * (1 - (z.FilterEff * z.PctStrmBuf))

                # Apply sediment detention basin BMP
                if z.BasinArea > 0 and z.Area[l] > 0:
                    z.SolidBasinMass[q] += z.SurfaceLoad - z.DisSurfLoad
                    z.DisBasinMass[q] += z.DisSurfLoad

                    z.DissolvedLoad = z.OutflowFract * z.DisBasinMass[q]
                    z.SolidLoad = z.Mixing * z.OutflowFract * z.SolidBasinMass[q]

                    z.SolidBasinMass[q] -= z.SolidLoad
                    z.DisBasinMass[q] -= z.DissolvedLoad

                    z.SurfaceLoad -= z.DissolvedLoad + z.SolidLoad
                    z.DisSurfLoad -= z.DissolvedLoad

                    z.LuLoad[Y][l][q] += z.DissolvedLoad + z.SolidLoad
                    z.LuDisLoad[Y][l][q] += z.DissolvedLoad

                    z.NetDisLoad[q] += z.DissolvedLoad
                    z.NetSolidLoad[q] += z.SolidLoad
                else:
                    z.LuLoad[Y][l][q] += z.SurfaceLoad
                    z.LuDisLoad[Y][l][q] += z.DisSurfLoad

                    z.NetDisLoad[q] += z.DisSurfLoad
                    z.NetSolidLoad[q] += z.SurfaceLoad - z.DisSurfLoad

    for q in range(z.Nqual):
        z.Load[Y][i][q] += z.NetDisLoad[q] + z.NetSolidLoad[q]
        z.DisLoad[Y][i][q] += z.NetDisLoad[q]

        if z.Load[Y][i][q] < 0:
            z.Load[Y][i][q] = 0

        if z.DisLoad[Y][i][q] < 0:
            z.DisLoad[Y][i][q] = 0

    # WATERSHED TOTALS
    if z.RurAreaTotal > 0:
        z.RuralQTotal *= z.RurAreaTotal / z.AreaTotal
    else:
        z.RuralQTotal = 0

    if z.UrbAreaTotal > 0:
        z.UrbanQTotal *= z.UrbAreaTotal / z.AreaTotal
    else:
        z.UrbanQTotal = 0

    if z.UrbAreaTotal > 0:
        z.AdjUrbanQTotal *= z.UrbAreaTotal / z.AreaTotal
    else:
        z.AdjUrbanQTotal = 0

    if z.AgAreaTotal > 0:
        z.AgQTotal = z.AgQTotal / z.AgAreaTotal
    else:
        z.AgQTotal = 0

    z.QTotal = z.UrbanQTotal + z.RuralQTotal
    # Assume 20% reduction of runoff with urban wetlands
    z.AdjQTotal = (z.AdjUrbanQTotal * (1 - (z.n25b * 0.2))) + z.RuralQTotal

    z.SedTrans[Y][i] += z.AdjQTotal ** 1.67

    # Calculate monthly runoff for year Y and month i
    if z.AdjQTotal > 0:
        z.Runoff[Y][i] += z.AdjQTotal
    else:
        z.Runoff[Y][i] += z.QTotal

    z.RuralRunoff[Y][i] += z.RuralQTotal
    z.UrbanRunoff[Y][i] += z.UrbanQTotal
    # TODO: (Are z.AgRunoff and z.AgQTotal actually in cm?)
    z.AgRunoff[Y][i] += z.AgQTotal

    # Convert Urban runoff from cm to Liters
    # TODO: (Maybe use z.UrbanRunoff[y][i] instead in the above equation)
    z.UrbRunoffLiter[Y][i] = (z.UrbanRunoff[Y][i] / 100) * z.UrbAreaTotal * 10000 * 1000

    # Calculate Daily runoff (used in output for daily flow file)
    if z.AdjQTotal > 0:
        z.DayRunoff[Y][i][j] = z.AdjQTotal
    elif z.QTotal > 0:
        z.DayRunoff[Y][i][j] = z.QTotal
    else:
        z.DayRunoff[Y][i][j] = 0
