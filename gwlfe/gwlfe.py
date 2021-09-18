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

from numpy import zeros
from numpy import seterr

from . import ReadGwlfDataFile
from . import PrelimCalculations
from . import AFOS_old
from . import CalcLoads
from . import StreamBank
from . import AnnualMeans
from . import WriteOutputFiles
from .Input.WaterBudget.InitSnow import InitSnow_f
from .Input.WaterBudget.GrowFactor import GrowFactor_f
from .Input.LandUse.TotAreaMeters import TotAreaMeters
from .Input.LandUse.Ag.AvTileDrain import AvTileDrain_f
from .Input.WaterBudget.AvWithdrawal import AvWithdrawal_f
from .Input.WaterBudget.AvGroundWater import AvGroundWater_f
from .MultiUse_Fxns.Runoff.AvRunoff import AvRunoff_f
from .Memoization import resetMemoization

log = logging.getLogger(__name__)


def run(z):
    resetMemoization()

    log.debug('Running model...')

    # Raise exception instead of printing a warning for floating point
    # overflow, underflow, and division by 0 errors.
    seterr(all='raise')

    # MODEL CALCULATIONS FOR EACH YEAR OF ANALYSIS - WATER BALANCE,
    # NUTRIENTS AND SEDIMENT LOADS
    ReadGwlfDataFile.ReadAllData(z)

    # --------- run the remaining parts of the model ---------------------

    # CALCLULATE PRELIMINARY INITIALIZATIONS AND VALUES FOR
    # WATER BALANCE AND NUTRIENTS
    PrelimCalculations.InitialCalculations(z)

    for Y in range(z.NYrs):
        # Initialize monthly septic system variables
        z.MonthPondNitr = zeros(12)
        z.MonthPondPhos = zeros(12)
        z.MonthNormNitr = zeros(12)
        z.MonthShortNitr = zeros(12)
        z.MonthShortPhos = zeros(12)
        z.MonthDischargeNitr = zeros(12)
        z.MonthDischargePhos = zeros(12)

        # FOR EACH MONTH...
        for i in range(12):
            # LOOP THROUGH NUMBER OF LANDUSES IN THE BASIN TO GET QRUNOFF
            for l in range(z.NLU):
                z.QRunoff[l, i] = 0
                z.AgQRunoff[l, i] = 0

            # DAILY CALCULATIONS
            for j in range(z.DaysMonth[Y][i]):
                # ***** END WEATHER DATA ANALYSIS *****

                # ***** WATERSHED WATER BALANCE *****

                z.PondNitrLoad = (z.NumPondSys[i] *
                                  (z.NitrSepticLoad - z.NitrPlantUptake * GrowFactor_f(z.Grow_0)[i]))
                z.PondPhosLoad = (z.NumPondSys[i] *
                                  (z.PhosSepticLoad - z.PhosPlantUptake * GrowFactor_f(z.Grow_0)[i]))

                # UPDATE MASS BALANCE ON PONDED EFFLUENT
                if (z.Temp[Y][i][j] <= 0 or InitSnow_f(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec)[Y][i][j] > 0):

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

                # Obtain the monthly Normal Nitrogen
                z.MonthNormNitr[i] = (z.MonthNormNitr[i] + z.NitrSepticLoad -
                                      z.NitrPlantUptake * GrowFactor_f(z.Grow_0)[i])

                # 0.56 IS ATTENUATION FACTOR FOR SOIL LOSS
                # 0.66 IS ATTENUATION FACTOR FOR SUBSURFACE FLOW LOSS
                z.MonthShortNitr[i] = (z.MonthShortNitr[i] + z.NitrSepticLoad -
                                       z.NitrPlantUptake * GrowFactor_f(z.Grow_0)[i])
                z.MonthShortPhos[i] = (z.MonthShortPhos[i] + z.PhosSepticLoad -
                                       z.PhosPlantUptake * GrowFactor_f(z.Grow_0)[i])
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
                AvRunoff_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                           z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention, z.PctAreaInfil,
                           z.n25b, z.CN, z.Landuse, z.TileDrainDensity)[i] +
                AvGroundWater_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                                z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV,
                                z.PcntET, z.DayHrs, z.MaxWaterCap,
                                z.SatStor_0, z.RecessionCoef, z.SeepCoef, z.Landuse, z.TileDrainDensity)[i] +
                z.AvPtSrcFlow[i] +
                AvTileDrain_f(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
                              z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
                              z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap,
                              z.SatStor_0, z.RecessionCoef, z.SeepCoef,
                              z.Landuse, z.TileDrainDensity)[i] -
                AvWithdrawal_f(z.NYrs, z.StreamWithdrawal, z.GroundWithdrawal)[i])

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
    return output, z
