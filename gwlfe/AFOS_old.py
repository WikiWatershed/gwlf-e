# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .Input.LandUse.TotAreaMeters import TotAreaMeters
from .MultiUse_Fxns.Discharge.StreamFlow_1 import StreamFlow_1_f
from .MultiUse_Fxns.LossFactAdj import LossFactAdj_f
from .MultiUse_Fxns.Runoff.UrbRunoffLiter import UrbRunoffLiter_f

"""
Imported from AFOS.bas
"""

import logging

log = logging.getLogger(__name__)


def AnimalOperations(z, Y):
    for i in range(12):
        z.NGLostManP[Y][i] = (z.NGAppManP[i] * z.NGAppPRate[i] * LossFactAdj_f(z.Prec, z.DaysMonth)[Y][i]
                              * (1 - z.NGPctSoilIncRate[i]))

        if z.NGLostManP[Y][i] > z.NGAppManP[i]:
            z.NGLostManP[Y][i] = z.NGAppManP[i]
        if z.NGLostManP[Y][i] < 0:
            z.NGLostManP[Y][i] = 0

        z.NGLostManFC[Y][i] = (z.NGAppManFC[i] * z.NGAppFCRate[i] * LossFactAdj_f(z.Prec, z.DaysMonth)[Y][i]
                               * (1 - z.NGPctSoilIncRate[i]))

        if z.NGLostManFC[Y][i] > z.NGAppManFC[i]:
            z.NGLostManFC[Y][i] = z.NGAppManFC[i]
        if z.NGLostManFC[Y][i] < 0:
            z.NGLostManFC[Y][i] = 0

        z.NGLostBarnP[Y][i] = (z.NGInitBarnP[i] * z.NGBarnPRate[i] * LossFactAdj_f(z.Prec, z.DaysMonth)[Y][i]
                               - z.NGInitBarnP[i] * z.NGBarnPRate[i] * LossFactAdj_f(z.Prec, z.DaysMonth)[Y][
                                   i] * z.AWMSNgPct * z.NgAWMSCoeffP
                               + z.NGInitBarnP[i] * z.NGBarnPRate[i] * LossFactAdj_f(z.Prec, z.DaysMonth)[Y][
                                   i] * z.RunContPct * z.RunConCoeffP)

        if z.NGLostBarnP[Y][i] > z.NGInitBarnP[i]:
            z.NGLostBarnP[Y][i] = z.NGInitBarnP[i]
        if z.NGLostBarnP[Y][i] < 0:
            z.NGLostBarnP[Y][i] = 0

        z.NGLostBarnFC[Y][i] = (z.NGInitBarnFC[i] * z.NGBarnFCRate[i] * LossFactAdj_f(z.Prec, z.DaysMonth)[Y][i]
                                - z.NGInitBarnFC[i] * z.NGBarnFCRate[i] * LossFactAdj_f(z.Prec, z.DaysMonth)[Y][
                                    i] * z.AWMSNgPct * z.NgAWMSCoeffP
                                + z.NGInitBarnFC[i] * z.NGBarnFCRate[i] * LossFactAdj_f(z.Prec, z.DaysMonth)[Y][
                                    i] * z.RunContPct * z.RunConCoeffP)

        if z.NGLostBarnFC[Y][i] > z.NGInitBarnFC[i]:
            z.NGLostBarnFC[Y][i] = z.NGInitBarnFC[i]
        if z.NGLostBarnFC[Y][i] < 0:
            z.NGLostBarnFC[Y][i] = 0

        # Grazing animal losses

        z.GRLostManP[Y][i] = (z.GRAppManP[i] * z.GRAppPRate[i] * LossFactAdj_f(z.Prec, z.DaysMonth)[Y][i]
                              * (1 - z.GRPctSoilIncRate[i]))

        if z.GRLostManP[Y][i] > z.GRAppManP[i]:
            z.GRLostManP[Y][i] = z.GRAppManP[i]
        if z.GRLostManP[Y][i] < 0:
            z.GRLostManP[Y][i] = 0

        z.GRLostManFC[Y][i] = (z.GRAppManFC[i] * z.GRAppFCRate[i] * LossFactAdj_f(z.Prec, z.DaysMonth)[Y][i]
                               * (1 - z.GRPctSoilIncRate[i]))

        if z.GRLostManFC[Y][i] > z.GRAppManFC[i]:
            z.GRLostManFC[Y][i] = z.GRAppManFC[i]
        if z.GRLostManFC[Y][i] < 0:
            z.GRLostManFC[Y][i] = 0

        z.GRLostBarnP[Y][i] = (z.GRInitBarnP[i] * z.GRBarnPRate[i] * LossFactAdj_f(z.Prec, z.DaysMonth)[Y][i]
                               - z.GRInitBarnP[i] * z.GRBarnPRate[i] * LossFactAdj_f(z.Prec, z.DaysMonth)[Y][
                                   i] * z.AWMSGrPct * z.GrAWMSCoeffP
                               + z.GRInitBarnP[i] * z.GRBarnPRate[i] * LossFactAdj_f(z.Prec, z.DaysMonth)[Y][
                                   i] * z.RunContPct * z.RunConCoeffP)

        if z.GRLostBarnP[Y][i] > z.GRInitBarnP[i]:
            z.GRLostBarnP[Y][i] = z.GRInitBarnP[i]
        if z.GRLostBarnP[Y][i] < 0:
            z.GRLostBarnP[Y][i] = 0

        z.GRLostBarnFC[Y][i] = (z.GRInitBarnFC[i] * z.GRBarnFCRate[i] * LossFactAdj_f(z.Prec, z.DaysMonth)[Y][i]
                                - z.GRInitBarnFC[i] * z.GRBarnFCRate[i] * LossFactAdj_f(z.Prec, z.DaysMonth)[Y][
                                    i] * z.AWMSGrPct * z.GrAWMSCoeffP
                                + z.GRInitBarnFC[i] * z.GRBarnFCRate[i] * LossFactAdj_f(z.Prec, z.DaysMonth)[Y][
                                    i] * z.RunContPct * z.RunConCoeffP)

        if z.GRLostBarnFC[Y][i] > z.GRInitBarnFC[i]:
            z.GRLostBarnFC[Y][i] = z.GRInitBarnFC[i]
        if z.GRLostBarnFC[Y][i] < 0:
            z.GRLostBarnFC[Y][i] = 0

        z.GRLossP[Y][i] = ((z.GrazingP[i] - z.GRStreamP[i])
                           * z.GrazingPRate[i] * LossFactAdj_f(z.Prec, z.DaysMonth)[Y][i])

        if z.GRLossP[Y][i] > (z.GrazingP[i] - z.GRStreamP[i]):
            z.GRLossP[Y][i] = (z.GrazingP[i] - z.GRStreamP[i])
        if z.GRLossP[Y][i] < 0:
            z.GRLossP[Y][i] = 0

        z.GRLossFC[Y][i] = ((z.GrazingFC[i] - z.GRStreamFC[i])
                            * z.GrazingFCRate[i] * LossFactAdj_f(z.Prec, z.DaysMonth)[Y][i])

        if z.GRLossFC[Y][i] > (z.GrazingFC[i] - z.GRStreamFC[i]):
            z.GRLossFC[Y][i] = (z.GrazingFC[i] - z.GRStreamFC[i])
        if z.GRLossFC[Y][i] < 0:
            z.GRLossFC[Y][i] = 0

        # Total animal related losses

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

        z.PtFlowLiters = (z.PointFlow[i] / 100) * TotAreaMeters(z.NRur, z.NUrb, z.Area) * 1000

        # Get the wildlife orgs
        z.WWOrgs[Y][i] = z.PtFlowLiters * (z.WWTPConc * 10) * (1 - z.InstreamDieoff)
        z.SSOrgs[Y][i] = (z.SepticOrgsDay
                          * z.SepticsDay[i]
                          * z.DaysMonth[Y][i]
                          * z.SepticFailure
                          * (1 - z.InstreamDieoff))

        if LossFactAdj_f(z.Prec, z.DaysMonth)[Y][i] * (1 - z.WuDieoff) > 1:
            z.UrbOrgs[Y][i] = (z.UrbRunoffLiter[Y][i]
                               * (z.UrbEMC * 10)
                               * (1 - z.InstreamDieoff))
            z.WildOrgs[Y][i] = (z.WildOrgsDay
                                * z.DaysMonth[Y][i]
                                * z.WildDensity
                                * z.ForestAreaTotalSqMi
                                * (1 - z.InstreamDieoff))
        else:
            z.UrbOrgs[Y][i] = (
                    UrbRunoffLiter_f(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.NUrb, z.Area,
                                     z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA)[Y][i]
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

        z.CMStream[Y][i] = (StreamFlow_1_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
                                           z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
                                           z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap,
                                           z.SatStor_0, z.RecessionCoef, z.SeepCoef)[Y][i] / 100) * TotAreaMeters(
            z.NRur, z.NUrb, z.Area)

        if z.CMStream[Y][i] > 0:
            z.OrgConc[Y][i] = (z.TotalOrgs[Y][i] / (z.CMStream[Y][i] * 1000)) / 10
        else:
            z.OrgConc[Y][i] = 0
