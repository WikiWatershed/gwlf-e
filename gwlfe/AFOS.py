# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

"""
Imported from AFOS.bas
"""


def AnimalOperations(z, y):
    print('AnimalOperations')

    for i in range(12):
        z.LossFactAdj[y][i] = (z.Precipitation[y][i] / z.DaysMonth[y][i]) / 0.3301

        # Non-grazing animal losses
        z.NGLostManN[y][i] = (z.NGAppManN[i] * z.NGAppNRate[i] * z.LossFactAdj[y][i]
                              * (1 - z.NGPctSoilIncRate[i]))

        if z.NGLostManN[y][i] > z.NGAppManN[i]:
            z.NGLostManN[y][i] = z.NGAppManN[i]
        if z.NGLostManN[y][i] < 0:
            z.NGLostManN[y][i] = 0

        z.NGLostManP[y][i] = (z.NGAppManP[i] * z.NGAppPRate[i] * z.LossFactAdj[y][i]
                              * (1 - z.NGPctSoilIncRate[i]))

        if z.NGLostManP[y][i] > z.NGAppManP[i]:
            z.NGLostManP[y][i] = z.NGAppManP[i]
        if z.NGLostManP[y][i] < 0:
            z.NGLostManP[y][i] = 0

        z.NGLostManFC[y][i] = (z.NGAppManFC[i] * z.NGAppFCRate[i] * z.LossFactAdj[y][i]
                               * (1 - z.NGPctSoilIncRate[i]))

        if z.NGLostManFC[y][i] > z.NGAppManFC[i]:
            z.NGLostManFC[y][i] = z.NGAppManFC[i]
        if z.NGLostManFC[y][i] < 0:
            z.NGLostManFC[y][i] = 0

        z.NGLostBarnN[y][i] = (z.NGInitBarnN[i] * z.NGBarnNRate[i] * z.LossFactAdj[y][i]
                               - z.NGInitBarnN[i] * z.NGBarnNRate[i] * z.LossFactAdj[y][i] * z.AWMSNgPct * z.NgAWMSCoeffN
                               + z.NGInitBarnN[i] * z.NGBarnNRate[i] * z.LossFactAdj[y][i] * z.RunContPct * z.RunConCoeffN)

        if z.NGLostBarnN[y][i] > z.NGInitBarnN[i]:
            z.NGLostBarnN[y][i] = z.NGInitBarnN[i]
        if z.NGLostBarnN[y][i] < 0:
            z.NGLostBarnN[y][i] = 0

        z.NGLostBarnP[y][i] = (z.NGInitBarnP[i] * z.NGBarnPRate[i] * z.LossFactAdj[y][i]
                               - z.NGInitBarnP[i] * z.NGBarnPRate[i] * z.LossFactAdj[y][i] * z.AWMSNgPct * z.NgAWMSCoeffP
                               + z.NGInitBarnP[i] * z.NGBarnPRate[i] * z.LossFactAdj[y][i] * z.RunContPct * z.RunConCoeffP)

        if z.NGLostBarnP[y][i] > z.NGInitBarnP[i]:
            z.NGLostBarnP[y][i] = z.NGInitBarnP[i]
        if z.NGLostBarnP[y][i] < 0:
            z.NGLostBarnP[y][i] = 0

        z.NGLostBarnFC[y][i] = (z.NGInitBarnFC[i] * z.NGBarnFCRate[i] * z.LossFactAdj[y][i]
                                - z.NGInitBarnFC[i] * z.NGBarnFCRate[i] * z.LossFactAdj[y][i] * z.AWMSNgPct * z.NgAWMSCoeffP
                                + z.NGInitBarnFC[i] * z.NGBarnFCRate[i] * z.LossFactAdj[y][i] * z.RunContPct * z.RunConCoeffP)

        if z.NGLostBarnFC[y][i] > z.NGInitBarnFC[i]:
            z.NGLostBarnFC[y][i] = z.NGInitBarnFC[i]
        if z.NGLostBarnFC[y][i] < 0:
            z.NGLostBarnFC[y][i] = 0

        # Grazing animal losses
        z.GRLostManN[y][i] = (z.GRAppManN[i] * z.GRAppNRate[i] * z.LossFactAdj[y][i]
                              * (1 - z.GRPctSoilIncRate[i]))

        if z.GRLostManN[y][i] > z.GRAppManN[i]:
            z.GRLostManN[y][i] = z.GRAppManN[i]
        if z.GRLostManN[y][i] < 0:
            z.GRLostManN[y][i] = 0

        z.GRLostManP[y][i] = (z.GRAppManP[i] * z.GRAppPRate[i] * z.LossFactAdj[y][i]
                              * (1 - z.GRPctSoilIncRate[i]))

        if z.GRLostManP[y][i] > z.GRAppManP[i]:
            z.GRLostManP[y][i] = z.GRAppManP[i]
        if z.GRLostManP[y][i] < 0:
            z.GRLostManP[y][i] = 0

        z.GRLostManFC[y][i] = (z.GRAppManFC[i] * z.GRAppFCRate[i] * z.LossFactAdj[y][i]
                               * (1 - z.GRPctSoilIncRate[i]))

        if z.GRLostManFC[y][i] > z.GRAppManFC[i]:
            z.GRLostManFC[y][i] = z.GRAppManFC[i]
        if z.GRLostManFC[y][i] < 0:
            z.GRLostManFC[y][i] = 0

        z.GRLostBarnN[y][i] = (z.GRInitBarnN[i] * z.GRBarnNRate[i] * z.LossFactAdj[y][i]
                               - z.GRInitBarnN[i] * z.GRBarnNRate[i] * z.LossFactAdj[y][i] * z.AWMSGrPct * z.GrAWMSCoeffN
                               + z.GRInitBarnN[i] * z.GRBarnNRate[i] * z.LossFactAdj[y][i] * z.RunContPct * z.RunConCoeffN)

        if z.GRLostBarnN[y][i] > z.GRInitBarnN[i]:
            z.GRLostBarnN[y][i] = z.GRInitBarnN[i]
        if z.GRLostBarnN[y][i] < 0:
            z.GRLostBarnN[y][i] = 0

        z.GRLostBarnP[y][i] = (z.GRInitBarnP[i] * z.GRBarnPRate[i] * z.LossFactAdj[y][i]
                               - z.GRInitBarnP[i] * z.GRBarnPRate[i] * z.LossFactAdj[y][i] * z.AWMSGrPct * z.GrAWMSCoeffP
                               + z.GRInitBarnP[i] * z.GRBarnPRate[i] * z.LossFactAdj[y][i] * z.RunContPct * z.RunConCoeffP)

        if z.GRLostBarnP[y][i] > z.GRInitBarnP[i]:
            z.GRLostBarnP[y][i] = z.GRInitBarnP[i]
        if z.GRLostBarnP[y][i] < 0:
            z.GRLostBarnP[y][i] = 0

        z.GRLostBarnFC[y][i] = (z.GRInitBarnFC[i] * z.GRBarnFCRate[i] * z.LossFactAdj[y][i]
                                - z.GRInitBarnFC[i] * z.GRBarnFCRate[i] * z.LossFactAdj[y][i] * z.AWMSGrPct * z.GrAWMSCoeffP
                                + z.GRInitBarnFC[i] * z.GRBarnFCRate[i] * z.LossFactAdj[y][i] * z.RunContPct * z.RunConCoeffP)

        if z.GRLostBarnFC[y][i] > z.GRInitBarnFC[i]:
            z.GRLostBarnFC[y][i] = z.GRInitBarnFC[i]
        if z.GRLostBarnFC[y][i] < 0:
            z.GRLostBarnFC[y][i] = 0

        z.GRLossN[y][i] = ((z.GrazingN[i] - z.GRStreamN[i])
                           * z.GrazingNRate[i] * z.LossFactAdj[y][i])

        if z.GRLossN[y][i] > (z.GrazingN[i] - z.GRStreamN[i]):
            z.GRLossN[y][i] = (z.GrazingN[i] - z.GRStreamN[i])
        if z.GRLossN[y][i] < 0:
            z.GRLossN[y][i] = 0

        z.GRLossP[y][i] = ((z.GrazingP[i] - z.GRStreamP[i])
                           * z.GrazingPRate[i] * z.LossFactAdj[y][i])

        if z.GRLossP[y][i] > (z.GrazingP[i] - z.GRStreamP[i]):
            z.GRLossP[y][i] = (z.GrazingP[i] - z.GRStreamP[i])
        if z.GRLossP[y][i] < 0:
            z.GRLossP[y][i] = 0

        z.GRLossFC[y][i] = ((z.GrazingFC[i] - z.GRStreamFC[i])
                            * z.GrazingFCRate[i] * z.LossFactAdj[y][i])

        if z.GRLossFC[y][i] > (z.GrazingFC[i] - z.GRStreamFC[i]):
            z.GRLossFC[y][i] = (z.GrazingFC[i] - z.GRStreamFC[i])
        if z.GRLossFC[y][i] < 0:
            z.GRLossFC[y][i] = 0

        # Total animal related losses
        z.AnimalN[y][i] = (z.NGLostManN[y][i]
                           + z.GRLostManN[y][i]
                           + z.NGLostBarnN[y][i]
                           + z.GRLostBarnN[y][i]
                           + z.GRLossN[y][i]
                           + z.GRStreamN[i])

        z.AnimalP[y][i] = ((z.NGLostManP[y][i]
                           + z.GRLostManP[y][i]
                           + z.NGLostBarnP[y][i]
                           + z.GRLostBarnP[y][i]
                           + z.GRLossP[y][i]
                           + z.GRStreamP[i])
                           - ((z.NGLostManP[y][i] + z.NGLostBarnP[y][i]) * z.PhytasePct * z.PhytaseCoeff))

        z.AnimalFC[y][i] = (z.NGLostManFC[y][i]
                            + z.GRLostManFC[y][i]
                            + z.NGLostBarnFC[y][i]
                            + z.GRLostBarnFC[y][i]
                            + z.GRLossFC[y][i]
                            + z.GRStreamFC[i])

        # CACULATE PATHOGEN LOADS
        z.ForestAreaTotalSqMi = 0
        z.ForestAreaTotalSqMi = (z.ForestAreaTotal * 0.01) / 2.59

        z.PtFlowLiters = (z.PointFlow[i] / 100) * z.TotAreaMeters * 1000

        # Get the wildlife orgs
        z.WWOrgs[y][i] = z.PtFlowLiters * (z.WWTPConc * 10) * (1 - z.InstreamDieoff)
        z.SSOrgs[y][i] = (z.SepticOrgsDay
                          * z.SepticsDay[i]
                          * z.DaysMonth[y][i]
                          * z.SepticFailure
                          * (1 - z.InstreamDieoff))

        if z.LossFactAdj[y][i] * (1 - z.WuDieoff) > 1:
            z.UrbOrgs[y][i] = (z.UrbRunoffLiter[y][i]
                               * (z.UrbEMC * 10)
                               * (1 - z.InstreamDieoff))
            z.WildOrgs[y][i] = (z.WildOrgsDay
                                * z.DaysMonth[y][i]
                                * z.WildDensity
                                * z.ForestAreaTotalSqMi
                                * (1 - z.InstreamDieoff))
        else:
            z.UrbOrgs[y][i] = (z.UrbRunoffLiter[y][i]
                               * (z.UrbEMC * 10)
                               * (1 - z.WuDieoff)
                               * (1 - z.InstreamDieoff))
            z.WildOrgs[y][i] = (z.WildOrgsDay
                                * z.DaysMonth[y][i]
                                * z.WildDensity
                                * z.ForestAreaTotalSqMi
                                * (1 - z.WuDieoff)
                                * (1 - z.InstreamDieoff))

        # Get the total orgs
        z.TotalOrgs[y][i] = (z.WWOrgs[y][i]
                             + z.SSOrgs[y][i]
                             + z.UrbOrgs[y][i]
                             + z.WildOrgs[y][i]
                             + z.AnimalFC[y][i])

        z.CMStream[y][i] = (z.StreamFlow[y][i] / 100) * z.TotAreaMeters

        if z.CMStream[y][i] > 0:
            z.OrgConc[y][i] = (z.TotalOrgs[y][i] / (z.CMStream[y][i] * 1000)) / 10
        else:
            z.OrgConc[y][i] = 0
