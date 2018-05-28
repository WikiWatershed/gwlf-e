# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

"""
Imported from CalcCNErosRunoffSed.bas
"""

import math
import logging
import numpy as np
from DailyArrayConverter import get_value_for_yesterday
from Water import Water_2
from LU import LU
from LU_1 import LU_1
from UrbAreaTotal import UrbAreaTotal_2
from UrbanQTotal_1 import UrbanQTotal_1_2

from .enums import GrowFlag, LandUse

log = logging.getLogger(__name__)


def CalcCN(z, i, Y, j):
    """
    z - data model (public variables)
    i - month
    Y - year
    j - number of days in month
    """
    # Calculate Curve Number (CN)
    # for l in range(z.NRur):
        # z.Qrun = 0
        # grow_factor = GrowFlag.intval(z.Grow_0[i])

        # if z.CN[l] > 0:
            # print("test2",z.CNum)
            # if z.Melt[Y][i][j] <= 0:
            #
            #     if grow_factor > 0:
            #         # print("test4")
            #         # growing season
            #         if get_value_for_yesterday(z.AMC5, 0, Y, i, j, z.NYrs, z.DaysMonth) >= 5.33:
            #             z.CNum = z.NewCN[2][l]
            #         elif get_value_for_yesterday(z.AMC5, 0, Y, i, j, z.NYrs, z.DaysMonth) < 3.56:
            #             z.CNum = z.NewCN[0][l] + (z.CN[l] - z.NewCN[0][l]) * get_value_for_yesterday(z.AMC5, 0, Y, i, j,
            #                                                                                          z.NYrs,
            #                                                                                          z.DaysMonth) / 3.56
            #         else:
            #             z.CNum = z.CN[l] + (z.NewCN[2][l] - z.CN[l]) * (
            #                         get_value_for_yesterday(z.AMC5, 0, Y, i, j, z.NYrs, z.DaysMonth) - 3.56) / 1.77
            #     else:
            #         # print("test5")
            #         # dormant season
            #         if get_value_for_yesterday(z.AMC5, 0, Y, i, j, z.NYrs, z.DaysMonth) >= 2.79:
            #             z.CNum = z.NewCN[2][l]
            #         elif get_value_for_yesterday(z.AMC5, 0, Y, i, j, z.NYrs, z.DaysMonth) < 1.27:
            #             z.CNum = z.NewCN[0][l] + (z.CN[l] - z.NewCN[0][l]) * get_value_for_yesterday(z.AMC5, 0, Y, i, j,
            #                                                                                          z.NYrs,
            #                                                                                          z.DaysMonth) / 1.27
            #         else:
            #             # print("test6")
            #             z.CNum = z.CN[l] + (z.NewCN[2][l] - z.CN[l]) * (
            #                         get_value_for_yesterday(z.AMC5, 0, Y, i, j, z.NYrs, z.DaysMonth) - 1.27) / 1.52
            #     # print("test3")
            # else:
            #     # print("test7")
            #     z.CNum = z.NewCN[2][l]
            # print(z.CNum,z.CNum_2[Y][i][j][l])
            # z.Retention = 2540 / z.CNum[Y][i][j][l] - 25.4
            # z.Retention = 2540 / z.CNum[Y][i][j][l] - 25.4
            # if z.Retention < 0:
            #     z.Retention = 0

            # z.Water balance and runoff calculation
            # if z.Water[Y][i][j] >= 0.2 * z.Retention[Y][i][j][l]:
            # if z.Water[Y][i][j] >= 0.2 * z.Retention[Y][i][j][l]:
                # z.Qrun = (z.Water[Y][i][j] - 0.2 * z.Retention[Y][i][j][l]) ** 2 / (
                #             z.Water[Y][i][j] + 0.8 * z.Retention[Y][i][j][l])
                # z.RuralQTotal += z.Qrun[Y][i][j][l] * z.Area[l] / z.RurAreaTotal
                # z.RurQRunoff[l][i] += z.Qrun[Y][i][j][l]
                # TODO: (what is done with "DayQRunoff"? - appears not to be used)
                # z.DayQRunoff[Y][i][j] = z.Qrun[Y][i][j][l]
                # TODO: (What is done with "AgQRunoff? - apparently nothing)
                # if z.Landuse[l] is LandUse.CROPLAND:
                #     # (Maybe used for STREAMPLAN?)
                #     z.AgQTotal += z.Qrun[Y][i][j][l] * z.Area[l]
                #     # z.AgQRunoff[l][i] += z.Qrun[Y][i][j][l]
                # elif z.Landuse[l] is LandUse.HAY_PAST:
                #     z.AgQTotal += z.Qrun[Y][i][j][l] * z.Area[l]
                #     # z.AgQRunoff[l][i] += z.Qrun[Y][i][j][l]
                # elif z.Landuse[l] is LandUse.TURFGRASS:
                #     z.AgQTotal += z.Qrun[Y][i][j][l] * z.Area[l]
                #     # z.AgQRunoff[l][i] += z.Qrun[Y][i][j][l]
            # else:
            #     z.Qrun[Y][i][j][l] = 0
        # else:
        #     pass
            # print("test1",z.CNum_2[Y][i][j-3][l])

        # EROSION, SEDIMENT WASHOFF FOR RURAL AND URBAN LANDUSE
        # z.RurEros = 1.32 * z.Erosiv[Y][i][j] * z.KF[l] * z.LS[l] * z.C[l] * z.P[l] * z.Area[l]

        # z.Erosion[Y][i] = z.Erosion[Y][i] + z.RurEros[Y][i][j][l]

        # z.ErosWashoff[l][i] = z.ErosWashoff[l][i] + z.RurEros[Y][i][j][l]
        # z.DayErWashoff[l][Y][i][j] = z.RurEros

        # if z.SedDelivRatio == 0:
        #     z.SedDelivRatio = 0.0001

    # for l in range(z.NRur, z.NLU):
        # z.QrunI[l] = 0
        # z.QrunP[l] = 0
        # z.WashImperv[l] = 0
        # z.WashPerv[l] = 0

    for q in range(z.Nqual):
        z.NetSolidLoad[q] = 0
        z.NetDisLoad[q] = 0
    # if z.Water[Y][i][j] < 0.05:
        # z.AdjUrbanQTotal = get_value_for_yesterday(z.AdjUrbanQTotal_1,0,Y,i,j,z.NYrs,z.DaysMonth)
        # pass
    # else:
    #     for l in range(z.NRur, z.NLU):
            # grow_factor = GrowFlag.intval(z.Grow_0[i])

            # Find curve number
            # if z.CNI[1][l] > 0:
            # if z.Melt[Y][i][j] <= 0:
            #     if z.GrowFactor[i] > 0:
            #         # Growing season
            #         if get_value_for_yesterday(z.AMC5, 0, Y, i, j, z.NYrs, z.DaysMonth) >= 5.33:
            #             z.CNumImperv = z.CNI[2][l]
            #         elif get_value_for_yesterday(z.AMC5, 0, Y, i, j, z.NYrs, z.DaysMonth) < 3.56:
            #             z.CNumImperv = z.CNI[0][l] + (z.CNI[1][l] - z.CNI[0][l]) * get_value_for_yesterday(z.AMC5, 0, Y,
            #                                                                                                i, j, z.NYrs,
            #                                                                                                z.DaysMonth) / 3.56
            #         else:
            #             z.CNumImperv = z.CNI[1][l] + (z.CNI[2][l] - z.CNI[1][l]) * (
            #                         get_value_for_yesterday(z.AMC5, 0, Y, i, j, z.NYrs, z.DaysMonth) - 3.56) / 1.77
            #     else:
            #         # Dormant season
            #         if get_value_for_yesterday(z.AMC5, 0, Y, i, j, z.NYrs, z.DaysMonth) >= 2.79:
            #             z.CNumImperv = z.CNI[2][l]
            #         elif get_value_for_yesterday(z.AMC5, 0, Y, i, j, z.NYrs, z.DaysMonth) < 1.27:
            #             z.CNumImperv = z.CNI[0][l] + (z.CNI[1][l] - z.CNI[0][l]) * get_value_for_yesterday(z.AMC5, 0, Y,
            #                                                                                                i, j, z.NYrs,
            #                                                                                                z.DaysMonth) / 1.27
            #         else:
            #             z.CNumImperv = z.CNI[1][l] + (z.CNI[2][l] - z.CNI[1][l]) * (
            #                         get_value_for_yesterday(z.AMC5, 0, Y, i, j, z.NYrs, z.DaysMonth) - 1.27) / 1.52
            # else:
            #     z.CNumImperv = z.CNI[2][l]

            # z.CNumImpervReten = 2540 / z.CNumImperv[Y][i][j][l] - 25.4
            # if z.CNumImpervReten < 0:
            #     z.CNumImpervReten = 0

            # if z.Water[Y][i][j] >= 0.2 * z.CNumImpervReten[Y][i][j][l]:
            #     z.QrunI[l] = (z.Water[Y][i][j] - 0.2 * z.CNumImpervReten[Y][i][j][l]) ** 2 / (
            #             z.Water[Y][i][j] + 0.8 * z.CNumImpervReten[Y][i][j][l])

            # if z.CNP[1][l] > 0:
            # if z.Melt[Y][i][j] <= 0:
            #     if z.GrowFactor[i] > 0:
            #         # Growing season
            #         if get_value_for_yesterday(z.AMC5, 0, Y, i, j, z.NYrs, z.DaysMonth) >= 5.33:
            #             z.CNumPerv[Y][i][j][l] = z.CNP[2][l]
            #         elif get_value_for_yesterday(z.AMC5, 0, Y, i, j, z.NYrs, z.DaysMonth) < 3.56:
            #             z.CNumPerv[Y][i][j][l] = z.CNP[0][l] + (z.CNP[1][l] - z.CNP[0][l]) * get_value_for_yesterday(z.AMC5, 0, Y,
            #                                                                                              i, j, z.NYrs,
            #                                                                                              z.DaysMonth) / 3.56
            #         else:
            #             z.CNumPerv[Y][i][j][l] = z.CNP[1][l] + (z.CNP[2][l] - z.CNP[1][l]) * (
            #                         get_value_for_yesterday(z.AMC5, 0, Y, i, j, z.NYrs, z.DaysMonth) - 3.56) / 1.77
            #     else:
            #         # Dormant season
            #         if get_value_for_yesterday(z.AMC5, 0, Y, i, j, z.NYrs, z.DaysMonth) >= 2.79:
            #             z.CNumPerv[Y][i][j][l] = z.CNP[2][l]
            #         elif get_value_for_yesterday(z.AMC5, 0, Y, i, j, z.NYrs, z.DaysMonth) < 1.27:
            #             z.CNumPerv[Y][i][j][l] = z.CNP[0][l] + (z.CNP[1][l] - z.CNP[0][l]) * get_value_for_yesterday(z.AMC5, 0, Y,
            #                                                                                              i, j, z.NYrs,
            #                                                                                              z.DaysMonth) / 1.27
            #         else:
            #             z.CNumPerv[Y][i][j][l] = z.CNP[1][l] + (z.CNP[2][l] - z.CNP[1][l]) * (
            #                         get_value_for_yesterday(z.AMC5, 0, Y, i, j, z.NYrs, z.DaysMonth) - 1.27) / 1.52
            # else:
            #     z.CNumPerv[Y][i][j][l] = z.CNP[2][l]

            # print(z.CNumPerv[Y][i][j][l],z.CNumPerv_2[Y][i][j][l])
            # assert(z.CNumPerv[Y][i][j]==z.CNumPerv_2[Y][i][j])

            # z.CNumPervReten = 2540 / z.CNumPerv[Y][i][j][l] - 25.4
            # if z.CNumPervReten < 0:
            #     z.CNumPervReten = 0

            # if z.Water[Y][i][j] >= 0.2 * z.CNumPervReten[Y][i][j][l]:
            #     z.QrunP[l] = (z.Water[Y][i][j] - 0.2 * z.CNumPervReten[Y][i][j][l]) ** 2 / (
            #             z.Water[Y][i][j] + 0.8 * z.CNumPervReten[Y][i][j][l])

            # lu = l - z.NRur

            # if z.UrbAreaTotal > 0:
            #     z.UrbanQTotal += ((z.QrunI[Y][i][j][l] * (z.Imper[l] * (1 - z.ISRR[z.lu[l]]) * (1 - z.ISRA[z.lu[l]]))
            #                        + z.QrunP[Y][i][j][l] * (
            #                                1 - (z.Imper[l] * (1 - z.ISRR[z.lu[l]]) * (1 - z.ISRA[z.lu[l]]))))
            #                       * z.Area[l] / z.UrbAreaTotal)

            # if z.AreaTotal > 0:
            #     z.UncontrolledQ += ((z.QrunI[Y][i][j][l] * (z.Imper[l] * (1 - z.ISRR[z.lu[l]]) *
            #                                                 (1 - z.ISRA[z.lu[l]])) + z.QrunP[Y][i][j][l] * (
            #                                  1 - (z.Imper[l] *
            #                                       (1 - z.ISRR[
            #                                           z.lu[
            #                                               l]]) * (
            #                                               1 -
            #                                               z.ISRA[
            #                                                   z.lu[
            #                                                       l]])))) *
            #                         z.Area[l] / z.AreaTotal)

            # z.WashImperv[l] = (1 - math.exp(-1.81 * z.QrunI[Y][i][j][l])) * z.ImpervAccum[l]
            # z.ImpervAccum[l] -= z.WashImperv[l]
            #
            # z.WashPerv[l] = (1 - math.exp(-1.81 * z.QrunP[Y][i][j][l])) * z.PervAccum[l]
            # z.PervAccum[l] -= z.WashPerv[l]
            #
            # print("WashImperv old = ", z.WashImperv[l], "WashImperv new = ", z.WashImperv_temp[Y][i][j][l])
            # print(z.WashImperv[l] == z.WashImperv_temp[Y][i][j][l])

            # print("WashPerv old = ", z.WashPerv[l], "WashPerv new = ", z.WashPerv_temp[Y][i][j][l])
            # print(z.WashPerv[l] == z.WashPerv_temp[Y][i][j][l])

            # z.UrbQRunoff[l][i] += (z.QrunI[Y][i][j][l] * (z.Imper[l] * (1 - z.ISRR[z.lu[l]]) * (1 - z.ISRA[z.lu[l]]))
            #                        + z.QrunP[Y][i][j][l] * (
            #                                1 - (z.Imper[l] * (1 - z.ISRR[z.lu[l]]) * (1 - z.ISRA[z.lu[l]]))))

        # z.AdjUrbanQTotal = z.UrbanQTotal[Y][i][j]

        # Runoff retention
        # if z.Qretention > 0:
        #     if z.UrbanQTotal[Y][i][j] > 0:
        #         if z.UrbanQTotal[Y][i][j] <= z.Qretention * z.PctAreaInfil:
        #             # z.RetentionEff = 1
        #             # z.AdjUrbanQTotal = 0
        #         else:
        #             z.RetentionEff = z.Qretention * z.PctAreaInfil / z.UrbanQTotal[Y][i][j]
        #             # z.AdjUrbanQTotal = z.UrbanQTotal[Y][i][j] - z.Qretention * z.PctAreaInfil

    BasinWater(z, i, Y, j)


def BasinWater(z, i, Y, j):
    # BELOW ARE CALCULATIONS FOR URBAN LOADS
    # MAYBE THEY SHOULD BE IN "CALCULATE LOADS" SUBROUTINE???
    z.DissolvedLoad = 0
    z.SolidLoad = 0
    z.UrbLoadRed = 0

    if z.AdjUrbanQTotal_1[Y][i][j] > 0.001:
        for l in range(z.NRur, z.NLU):
            for q in range(z.Nqual):
                z.SolidBasinMass[q] = 0
                z.DisBasinMass[q] = 0

                if z.Storm > 0:
                    z.UrbLoadRed = (z.Water[Y][i][j] / z.Storm) * z.UrbBMPRed[l][q]
                else:
                    z.UrbLoadRed = 0

                if Water_2(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec)[Y][i][j] > z.Storm:
                    z.UrbLoadRed = z.UrbBMPRed[l][q]

                # TODO: Should 11 be NRur + 1?
                # What is this trying to do?
                lu_1 = LU_1(z.NRur, z.NUrb)

                if z.Area[l] > 0:
                    z.SurfaceLoad = (((z.LoadRateImp[l][q] * z.WashImperv[Y][i][j][l] * (
                            (z.Imper[l] * (1 - z.ISRR[lu_1[l]]) * (1 - z.ISRA[lu_1[l]]))
                            * (z.SweepFrac[i] + (
                            (1 - z.SweepFrac[i]) * ((1 - z.UrbSweepFrac) * z.Area[l]) / z.Area[l])))
                                       + z.LoadRatePerv[l][q] * z.WashPerv[Y][i][j][l] * (
                                               1 - (z.Imper[l] * (1 - z.ISRR[lu_1[l]]) * (1 - z.ISRA[lu_1[l]]))))
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

    z.RuralRunoff[Y][i] += z.RuralQTotal[Y][i][j]
    z.UrbanRunoff[Y][i] += UrbanQTotal_1_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                                    z.AntMoist_0, z.Grow_0,
                                    z.CNP_0, z.Imper, z.ISRR, z.ISRA)[Y][i][j]
    # TODO: (Are z.AgRunoff and z.AgQTotal actually in cm?)
    # z.AgRunoff[Y][i] += z.AgQTotal[Y][i][j]

    # Convert Urban runoff from cm to Liters
    # TODO: (Maybe use z.UrbanRunoff[y][i] instead in the above equation)
    z.UrbRunoffLiter[Y][i] = (z.UrbanRunoff[Y][i] / 100) * UrbAreaTotal_2(z.NRur, z.NUrb, z.Area) * 10000 * 1000

    # Calculate Daily runoff (used in output for daily flow file)
    # if z.AdjQTotal[Y][i][j] > 0:
    #     z.DayRunoff[Y][i][j] = z.AdjQTotal[Y][i][j]
    # elif z.QTotal[Y][i][j] > 0:
    #     z.DayRunoff[Y][i][j] = z.QTotal[Y][i][j]
    # else:
    #     z.DayRunoff[Y][i][j] = 0
