#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

"""
Runs the GWLF-E MapShed model.

Imported from GWLF-E.frm
"""

import logging

import numpy as np

from .enums import GrowFlag
import ReadGwlfDataFile
import PrelimCalculations
import AFOS_old
import CalcLoads
import StreamBank
import AnnualMeans
import WriteOutputFiles
from InitSnow import InitSnow_2
from GrowFactor import GrowFactor_2
from TotAreaMeters import TotAreaMeters
from AvTileDrain import AvTileDrain_2
from AvWithdrawal import AvWithdrawal_2
from AvGroundWater import AvGroundWater_2
from AvRunoff import AvRunoff_2
from LuTotNitr import LuTotNitr_2
from LuTotPhos import LuTotPhos_2
from Load import Load_2
from DisLoad import DisLoad_2

log = logging.getLogger(__name__)


# @time_function
def run(z):
    log.debug('Running model...')

    # Raise exception instead of printing a warning for floating point
    # overflow, underflow, and division by 0 errors.
    np.seterr(all='raise')

    # MODEL CALCULATIONS FOR EACH YEAR OF ANALYSIS - WATER BALANCE,
    # NUTRIENTS AND SEDIMENT LOADS
    ReadGwlfDataFile.ReadAllData(z)

    # --------- run the remaining parts of the model ---------------------

    # z.LuTotNitr[:, :z.NRur] = LuTotNitr_2(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.AntMoist_0, z.NRur,
    #                                       z.NUrb, z.CN, z.Grow_0, z.Area, z.NitrConc, z.ManNitr, z.ManuredAreas,
    #                                       z.FirstManureMonth, z.LastManureMonth, z.FirstManureMonth2,
    #                                       z.LastManureMonth2, z.SedDelivRatio_0, z.KF, z.LS, z.C,
    #                                       z.P, z.SedNitr, z.Acoef)

    z.LuTotNitr = LuTotNitr_2(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.AntMoist_0, z.NRur, z.NUrb, z.CN, z.Grow_0,
                                       z.Area, z.NitrConc, z.ManNitr, z.ManuredAreas, z.FirstManureMonth, z.LastManureMonth,
                                       z.FirstManureMonth2, z.LastManureMonth2, z.SedDelivRatio_0, z.KF, z.LS, z.C, z.P, z.SedNitr, z.CNP_0, z.Imper, z.ISRR, z.ISRA,
                                       z.Qretention, z.PctAreaInfil, z.LoadRateImp, z.LoadRatePerv, z.Storm, z.UrbBMPRed, z.FilterWidth, z.PctStrmBuf, z.Acoef,
                                       z.CNI_0, z.Nqual)

    z.LuTotPhos = LuTotPhos_2(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.AntMoist_0, z.NRur, z.NUrb, z.CN,
                                z.Grow_0, z.Area, z.PhosConc, z.ManPhos, z.ManuredAreas, z.FirstManureMonth,
                                z.LastManureMonth, z.FirstManureMonth2, z.LastManureMonth2, z.SedDelivRatio_0, z.KF,
                                z.LS, z.C, z.P, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention, z.PctAreaInfil, z.Nqual,
                                z.LoadRateImp, z.LoadRatePerv, z.Storm, z.UrbBMPRed, z.FilterWidth, z.PctStrmBuf,
                                z.Acoef, z.SedPhos, z.CNI_0)

    z.Load = Load_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0,
                        z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention, z.PctAreaInfil, z.Nqual, z.LoadRateImp,
                        z.SweepFrac, z.UrbSweepFrac, z.LoadRatePerv, z.Storm, z.UrbBMPRed, z.DisFract, z.FilterWidth, z.PctStrmBuf)




    z.DisLoad = DisLoad_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0,
                 z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention, z.PctAreaInfil, z.Nqual, z.LoadRateImp,
                 z.LoadRatePerv, z.Storm, z.UrbBMPRed, z.DisFract, z.FilterWidth, z.PctStrmBuf)

    # CALCLULATE PRELIMINARY INITIALIZATIONS AND VALUES FOR
    # WATER BALANCE AND NUTRIENTS
    PrelimCalculations.InitialCalculations(z)

    for Y in range(z.NYrs):
        # Initialize monthly septic system variables
        z.MonthPondNitr = np.zeros(12)
        z.MonthPondPhos = np.zeros(12)
        z.MonthNormNitr = np.zeros(12)
        z.MonthShortNitr = np.zeros(12)
        z.MonthShortPhos = np.zeros(12)
        z.MonthDischargeNitr = np.zeros(12)
        z.MonthDischargePhos = np.zeros(12)

        # FOR EACH MONTH...
        for i in range(12):
            # LOOP THROUGH NUMBER OF LANDUSES IN THE BASIN TO GET QRUNOFF
            for l in range(z.NLU):
                z.QRunoff[l, i] = 0
                z.AgQRunoff[l, i] = 0
                # z.ErosWashoff[l, i] = 0
                # z.RurQRunoff[l, i] = 0
                # z.UrbQRunoff[l, i] = 0
                # z.LuErosion[Y, l] = 0

            # DAILY CALCULATIONS
            for j in range(z.DaysMonth[Y][i]):
                # ***** END WEATHER DATA ANALYSIS *****

                # ***** WATERSHED WATER BALANCE *****

                z.PondNitrLoad = (z.NumPondSys[i] *
                                  (z.NitrSepticLoad - z.NitrPlantUptake * GrowFactor_2(z.Grow_0)[i]))
                z.PondPhosLoad = (z.NumPondSys[i] *
                                  (z.PhosSepticLoad - z.PhosPlantUptake * GrowFactor_2(z.Grow_0)[i]))

                # UPDATE MASS BALANCE ON PONDED EFFLUENT
                if (z.Temp[Y][i][j] <= 0 or InitSnow_2(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec)[Y][i][j] > 0):

                    # ALL INPUTS GO TO FROZEN STORAGE
                    z.FrozenPondNitr = z.FrozenPondNitr + z.PondNitrLoad
                    z.FrozenPondPhos = z.FrozenPondPhos + z.PondPhosLoad

                    # NO NUTIENT OVERFLOW
                    z.NitrPondOverflow = 0
                    z.PhosPondOverflow = 0
                else:
                    z.NitrPondOverflow = z.FrozenPondNitr + z.PondNitrLoad
                    z.PhosPondOverflow = z.FrozenPondPhos + z.PondPhosLoad
                    z.FrozenPondNitr = 0
                    z.FrozenPondPhos = 0

                # Obtain the monthly Pond nutrients
                z.MonthPondNitr[i] = z.MonthPondNitr[i] + z.NitrPondOverflow
                z.MonthPondPhos[i] = z.MonthPondPhos[i] + z.PhosPondOverflow

                # grow_factor = GrowFlag.intval(z.Grow_0[i]) # duplicate

                # Obtain the monthly Normal Nitrogen
                z.MonthNormNitr[i] = (z.MonthNormNitr[i] + z.NitrSepticLoad -
                                      z.NitrPlantUptake * GrowFactor_2(z.Grow_0)[i])

                # 0.56 IS ATTENUATION FACTOR FOR SOIL LOSS
                # 0.66 IS ATTENUATION FACTOR FOR SUBSURFACE FLOW LOSS
                z.MonthShortNitr[i] = (z.MonthShortNitr[i] + z.NitrSepticLoad -
                                       z.NitrPlantUptake * GrowFactor_2(z.Grow_0)[i])
                z.MonthShortPhos[i] = (z.MonthShortPhos[i] + z.PhosSepticLoad -
                                       z.PhosPlantUptake * GrowFactor_2(z.Grow_0)[i])
                z.MonthDischargeNitr[i] = z.MonthDischargeNitr[i] + z.NitrSepticLoad
                z.MonthDischargePhos[i] = z.MonthDischargePhos[i] + z.PhosSepticLoad

        # CALCULATE ANIMAL FEEDING OPERATIONS OUTPUT
        AFOS_old.AnimalOperations(z, Y)

        # CALCULATE NUTRIENT AND SEDIMENT LOADS
        CalcLoads.CalculateLoads(z, Y)

        # CALCULATE STREAM BANK EROSION
        StreamBank.CalculateStreamBankEros(z, Y)

        # CALCULATE FINAL ANNUAL MEAN LOADS
        AnnualMeans.CalculateAnnualMeanLoads(z, Y)

    # CALCULATE FINAL MONTHLY AND ANNUAL WATER BALANCE FOR
    # AVERAGE STREAM FLOW

    for i in range(12):
        z.AvStreamFlow[i] = (
                AvRunoff_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                           z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention, z.PctAreaInfil,
                           z.n25b, z.CN, z.Landuse, z.TileDrainDensity)[i] +
                AvGroundWater_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                                z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV,
                                z.PcntET, z.DayHrs, z.MaxWaterCap,
                                z.SatStor_0, z.RecessionCoef, z.SeepCoef, z.Landuse, z.TileDrainDensity)[i] +
                z.AvPtSrcFlow[i] +
                AvTileDrain_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
                              z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
                              z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap,
                              z.SatStor_0, z.RecessionCoef, z.SeepCoef,
                              z.Landuse, z.TileDrainDensity)[i] -
                AvWithdrawal_2(z.NYrs, z.StreamWithdrawal, z.GroundWithdrawal)[i])

        z.AvCMStream[i] = (z.AvStreamFlow[i] / 100) * TotAreaMeters(z.NRur, z.NUrb, z.Area)
        if z.AvCMStream[i] > 0:
            z.AvOrgConc[i] = (z.AvTotalOrgs[i] / (z.AvCMStream[i] * 1000)) / 10
        else:
            z.AvOrgConc[i] = 0
    z.AvOrgConc[0] = 0

    z.AvStreamFlowSum = (z.AvRunoffSum + z.AvGroundWaterSum +
                         z.AvPtSrcFlowSum + z.AvTileDrainSum -
                         z.AvWithdrawalSum)

    log.debug("Model run complete for " + str(z.NYrs) + " years of data.")

    output = WriteOutputFiles.WriteOutput(z)
    # WriteOutputFiles.WriteOutputSumFiles()
    return output
