# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

"""
Imported from AFOS.bas
"""

import logging


log = logging.getLogger(__name__)


def AnimalOperations(z, Y):
    log.debug('AnimalOperations')

    for i in range(12):
        z.LossFactAdj[Y][i] = (z.Precipitation[Y][i] / z.DaysMonth[Y][i]) / 0.3301

        # Non-grazing animal losses
        z.NGLostManN[Y][i] = (z.NGAppManN[i] * z.NGAppNRate[i] * z.LossFactAdj[Y][i]
                              * (1 - z.NGPctSoilIncRate[i]))

        if z.NGLostManN[Y][i] > z.NGAppManN[i]:
            z.NGLostManN[Y][i] = z.NGAppManN[i]
        if z.NGLostManN[Y][i] < 0:
            z.NGLostManN[Y][i] = 0

        z.NGLostManP[Y][i] = (z.NGAppManP[i] * z.NGAppPRate[i] * z.LossFactAdj[Y][i]
                              * (1 - z.NGPctSoilIncRate[i]))

        if z.NGLostManP[Y][i] > z.NGAppManP[i]:
            z.NGLostManP[Y][i] = z.NGAppManP[i]
        if z.NGLostManP[Y][i] < 0:
            z.NGLostManP[Y][i] = 0

        z.NGLostManFC[Y][i] = (z.NGAppManFC[i] * z.NGAppFCRate[i] * z.LossFactAdj[Y][i]
                               * (1 - z.NGPctSoilIncRate[i]))

        if z.NGLostManFC[Y][i] > z.NGAppManFC[i]:
            z.NGLostManFC[Y][i] = z.NGAppManFC[i]
        if z.NGLostManFC[Y][i] < 0:
            z.NGLostManFC[Y][i] = 0

        z.NGLostBarnN[Y][i] = (z.NGInitBarnN[i] * z.NGBarnNRate[i] * z.LossFactAdj[Y][i]
                               - z.NGInitBarnN[i] * z.NGBarnNRate[i] * z.LossFactAdj[Y][i] * z.AWMSNgPct * z.NgAWMSCoeffN
                               + z.NGInitBarnN[i] * z.NGBarnNRate[i] * z.LossFactAdj[Y][i] * z.RunContPct * z.RunConCoeffN)

        if z.NGLostBarnN[Y][i] > z.NGInitBarnN[i]:
            z.NGLostBarnN[Y][i] = z.NGInitBarnN[i]
        if z.NGLostBarnN[Y][i] < 0:
            z.NGLostBarnN[Y][i] = 0

        z.NGLostBarnP[Y][i] = (z.NGInitBarnP[i] * z.NGBarnPRate[i] * z.LossFactAdj[Y][i]
                               - z.NGInitBarnP[i] * z.NGBarnPRate[i] * z.LossFactAdj[Y][i] * z.AWMSNgPct * z.NgAWMSCoeffP
                               + z.NGInitBarnP[i] * z.NGBarnPRate[i] * z.LossFactAdj[Y][i] * z.RunContPct * z.RunConCoeffP)

        if z.NGLostBarnP[Y][i] > z.NGInitBarnP[i]:
            z.NGLostBarnP[Y][i] = z.NGInitBarnP[i]
        if z.NGLostBarnP[Y][i] < 0:
            z.NGLostBarnP[Y][i] = 0

        z.NGLostBarnFC[Y][i] = (z.NGInitBarnFC[i] * z.NGBarnFCRate[i] * z.LossFactAdj[Y][i]
                                - z.NGInitBarnFC[i] * z.NGBarnFCRate[i] * z.LossFactAdj[Y][i] * z.AWMSNgPct * z.NgAWMSCoeffP
                                + z.NGInitBarnFC[i] * z.NGBarnFCRate[i] * z.LossFactAdj[Y][i] * z.RunContPct * z.RunConCoeffP)

        if z.NGLostBarnFC[Y][i] > z.NGInitBarnFC[i]:
            z.NGLostBarnFC[Y][i] = z.NGInitBarnFC[i]
        if z.NGLostBarnFC[Y][i] < 0:
            z.NGLostBarnFC[Y][i] = 0

        # Grazing animal losses
        z.GRLostManN[Y][i] = (z.GRAppManN[i] * z.GRAppNRate[i] * z.LossFactAdj[Y][i]
                              * (1 - z.GRPctSoilIncRate[i]))

        if z.GRLostManN[Y][i] > z.GRAppManN[i]:
            z.GRLostManN[Y][i] = z.GRAppManN[i]
        if z.GRLostManN[Y][i] < 0:
            z.GRLostManN[Y][i] = 0

        z.GRLostManP[Y][i] = (z.GRAppManP[i] * z.GRAppPRate[i] * z.LossFactAdj[Y][i]
                              * (1 - z.GRPctSoilIncRate[i]))

        if z.GRLostManP[Y][i] > z.GRAppManP[i]:
            z.GRLostManP[Y][i] = z.GRAppManP[i]
        if z.GRLostManP[Y][i] < 0:
            z.GRLostManP[Y][i] = 0

        z.GRLostManFC[Y][i] = (z.GRAppManFC[i] * z.GRAppFCRate[i] * z.LossFactAdj[Y][i]
                               * (1 - z.GRPctSoilIncRate[i]))

        if z.GRLostManFC[Y][i] > z.GRAppManFC[i]:
            z.GRLostManFC[Y][i] = z.GRAppManFC[i]
        if z.GRLostManFC[Y][i] < 0:
            z.GRLostManFC[Y][i] = 0

        z.GRLostBarnN[Y][i] = (z.GRInitBarnN[i] * z.GRBarnNRate[i] * z.LossFactAdj[Y][i]
                               - z.GRInitBarnN[i] * z.GRBarnNRate[i] * z.LossFactAdj[Y][i] * z.AWMSGrPct * z.GrAWMSCoeffN
                               + z.GRInitBarnN[i] * z.GRBarnNRate[i] * z.LossFactAdj[Y][i] * z.RunContPct * z.RunConCoeffN)

        if z.GRLostBarnN[Y][i] > z.GRInitBarnN[i]:
            z.GRLostBarnN[Y][i] = z.GRInitBarnN[i]
        if z.GRLostBarnN[Y][i] < 0:
            z.GRLostBarnN[Y][i] = 0

        z.GRLostBarnP[Y][i] = (z.GRInitBarnP[i] * z.GRBarnPRate[i] * z.LossFactAdj[Y][i]
                               - z.GRInitBarnP[i] * z.GRBarnPRate[i] * z.LossFactAdj[Y][i] * z.AWMSGrPct * z.GrAWMSCoeffP
                               + z.GRInitBarnP[i] * z.GRBarnPRate[i] * z.LossFactAdj[Y][i] * z.RunContPct * z.RunConCoeffP)

        if z.GRLostBarnP[Y][i] > z.GRInitBarnP[i]:
            z.GRLostBarnP[Y][i] = z.GRInitBarnP[i]
        if z.GRLostBarnP[Y][i] < 0:
            z.GRLostBarnP[Y][i] = 0

        z.GRLostBarnFC[Y][i] = (z.GRInitBarnFC[i] * z.GRBarnFCRate[i] * z.LossFactAdj[Y][i]
                                - z.GRInitBarnFC[i] * z.GRBarnFCRate[i] * z.LossFactAdj[Y][i] * z.AWMSGrPct * z.GrAWMSCoeffP
                                + z.GRInitBarnFC[i] * z.GRBarnFCRate[i] * z.LossFactAdj[Y][i] * z.RunContPct * z.RunConCoeffP)

        if z.GRLostBarnFC[Y][i] > z.GRInitBarnFC[i]:
            z.GRLostBarnFC[Y][i] = z.GRInitBarnFC[i]
        if z.GRLostBarnFC[Y][i] < 0:
            z.GRLostBarnFC[Y][i] = 0

        z.GRLossN[Y][i] = ((z.GrazingN[i] - z.GRStreamN[i])
                           * z.GrazingNRate[i] * z.LossFactAdj[Y][i])

        if z.GRLossN[Y][i] > (z.GrazingN[i] - z.GRStreamN[i]):
            z.GRLossN[Y][i] = (z.GrazingN[i] - z.GRStreamN[i])
        if z.GRLossN[Y][i] < 0:
            z.GRLossN[Y][i] = 0

        z.GRLossP[Y][i] = ((z.GrazingP[i] - z.GRStreamP[i])
                           * z.GrazingPRate[i] * z.LossFactAdj[Y][i])

        if z.GRLossP[Y][i] > (z.GrazingP[i] - z.GRStreamP[i]):
            z.GRLossP[Y][i] = (z.GrazingP[i] - z.GRStreamP[i])
        if z.GRLossP[Y][i] < 0:
            z.GRLossP[Y][i] = 0

        z.GRLossFC[Y][i] = ((z.GrazingFC[i] - z.GRStreamFC[i])
                            * z.GrazingFCRate[i] * z.LossFactAdj[Y][i])

        if z.GRLossFC[Y][i] > (z.GrazingFC[i] - z.GRStreamFC[i]):
            z.GRLossFC[Y][i] = (z.GrazingFC[i] - z.GRStreamFC[i])
        if z.GRLossFC[Y][i] < 0:
            z.GRLossFC[Y][i] = 0

        # Total animal related losses
        z.AnimalN[Y][i] = (z.NGLostManN[Y][i]
                           + z.GRLostManN[Y][i]
                           + z.NGLostBarnN[Y][i]
                           + z.GRLostBarnN[Y][i]
                           + z.GRLossN[Y][i]
                           + z.GRStreamN[i])

        z.AnimalP[Y][i] = ((z.NGLostManP[Y][i]
                           + z.GRLostManP[Y][i]
                           + z.NGLostBarnP[Y][i]
                           + z.GRLostBarnP[Y][i]
                           + z.GRLossP[Y][i]
                           + z.GRStreamP[i])
                           - ((z.NGLostManP[Y][i] + z.NGLostBarnP[Y][i]) * z.PhytasePct * z.PhytaseCoeff))

        z.AnimalFC[Y][i] = (z.NGLostManFC[Y][i]
                            + z.GRLostManFC[Y][i]
                            + z.NGLostBarnFC[Y][i]
                            + z.GRLostBarnFC[Y][i]
                            + z.GRLossFC[Y][i]
                            + z.GRStreamFC[i])

        # CACULATE PATHOGEN LOADS
        z.ForestAreaTotalSqMi = 0
        z.ForestAreaTotalSqMi = (z.ForestAreaTotal * 0.01) / 2.59

        z.PtFlowLiters = (z.PointFlow[i] / 100) * z.TotAreaMeters * 1000

        # Get the wildlife orgs
        z.WWOrgs[Y][i] = z.PtFlowLiters * (z.WWTPConc * 10) * (1 - z.InstreamDieoff)
        z.SSOrgs[Y][i] = (z.SepticOrgsDay
                          * z.SepticsDay[i]
                          * z.DaysMonth[Y][i]
                          * z.SepticFailure
                          * (1 - z.InstreamDieoff))

        if z.LossFactAdj[Y][i] * (1 - z.WuDieoff) > 1:
            z.UrbOrgs[Y][i] = (z.UrbRunoffLiter[Y][i]
                               * (z.UrbEMC * 10)
                               * (1 - z.InstreamDieoff))
            z.WildOrgs[Y][i] = (z.WildOrgsDay
                                * z.DaysMonth[Y][i]
                                * z.WildDensity
                                * z.ForestAreaTotalSqMi
                                * (1 - z.InstreamDieoff))
        else:
            z.UrbOrgs[Y][i] = (z.UrbRunoffLiter[Y][i]
                               * (z.UrbEMC * 10)
                               * (1 - z.WuDieoff)
                               * (1 - z.InstreamDieoff))
            z.WildOrgs[Y][i] = (z.WildOrgsDay
                                * z.DaysMonth[Y][i]
                                * z.WildDensity
                                * z.ForestAreaTotalSqMi
                                * (1 - z.WuDieoff)
                                * (1 - z.InstreamDieoff))

        # Get the total orgs
        z.TotalOrgs[Y][i] = (z.WWOrgs[Y][i]
                             + z.SSOrgs[Y][i]
                             + z.UrbOrgs[Y][i]
                             + z.WildOrgs[Y][i]
                             + z.AnimalFC[Y][i])

        z.CMStream[Y][i] = (z.StreamFlow[Y][i] / 100) * z.TotAreaMeters

        if z.CMStream[Y][i] > 0:
            z.OrgConc[Y][i] = (z.TotalOrgs[Y][i] / (z.CMStream[Y][i] * 1000)) / 10
        else:
            z.OrgConc[Y][i] = 0
