#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

"""
Runs the GWLF-E MapShed model.

Imported from GWLF-E.frm
"""

import numpy as np

from . import ReadGwlfDataFile
from . import PrelimCalculations
from . import CalcCnErosRunoffSed
from . import AFOS
from . import CalcLoads
from . import StreamBank
from . import AnnualMeans
from . import WriteOutputFiles


def run(z):
    print('Running model...')

    ReadGwlfDataFile.ReadAllData(z)

    # CALCLULATE PRELIMINARY INITIALIZATIONS AND VALUES FOR
    # WATER BALANCE AND NUTRIENTS
    PrelimCalculations.InitialCalculations(z)

    # MODEL CALCULATIONS FOR EACH YEAR OF ANALYSIS - WATER BALANCE,
    # NUTRIENTS AND SEDIMENT LOADS

    for y in range(z.NYrs):
        # FOR EACH MONTH...
        for i in range(12):
            # Initialize monthly septic system variables
            # LOOP THROUGH NUMBER OF LANDUSES IN THE BASIN TO GET QRUNOFF
            for l in range(z.NLU):
                z.QRunoff[l, i] = 0
                z.AgQRunoff[l, i] = 0
                z.ErosWashoff[l, i] = 0
                z.RurQRunoff[l, i] = 0
                z.UrbQRunoff[l, i] = 0
                z.LuErosion[y, l] = 0

            # DAILY CALCULATIONS
            # TODO: J should start at 1, but I changed
            # it to 0 so that the code executes with fake
            # data. Otherwise range is 1 to 1.
            for j in range(z.DaysMonth[y, i]):
                # GET THE DAYS OF THE YEAR
                if (z.DayYr + 1) > z.DaysYear[y]:
                    z.DayYr = 0
                z.DayYr = z.DayYr + 1

                # DAILYWEATHERANALY TEMP[y, I, J], PREC[y, I, J]
                # ***** BEGIN WEATHER DATA ANALYSIS *****
                z.DailyTemp = z.Temp[y, i, j]
                z.DailyPrec = z.Prec[y, i, j]
                z.PestTemp[y, i, j] = z.Temp[y, i, j]
                z.PestPrec[y, i, j] = z.Prec[y, i, j]
                z.Melt = 0
                z.Rain = 0
                z.Water = 0
                z.ET = 0
                z.QTotal = 0
                z.MeltPest[y, i, j] = 0

                for l in range(z.NLU):
                    z.ImpervAccum[l] = (z.ImpervAccum[l] * np.exp(-0.12) +
                                        (1 / 0.12) * (1 - np.exp(-0.12)))
                    z.PervAccum[l] = (z.PervAccum[l] * np.exp(-0.12) +
                                      (1 / 0.12) * (1 - np.exp(-0.12)))

                # RAIN , SNOWMELT, EVAPOTRANSPIRATION (ET)
                if z.DailyTemp <= 0:
                    z.InitSnow = z.InitSnow + z.DailyPrec
                else:
                    z.Rain = z.DailyPrec
                    if z.InitSnow > 0.001:
                        # A DEGREE-DAY INITSNOW MELT, BUT NO MORE THAN EXISTED
                        # INITSNOW
                        z.Melt = 0.45 * z.DailyTemp
                        z.MeltPest[y, i, j] = z.Melt
                        if z.Melt > z.InitSnow:
                            z.Melt = z.InitSnow
                            z.MeltPest[y, i, j] = z.InitSnow
                        z.InitSnow = z.InitSnow - z.Melt
                    else:
                        z.MeltPest[y, i, j] = 0

                    # AVAILABLE WATER CALCULATION
                    z.Water = z.Rain + z.Melt
                    z.DailyWater[y, i, j] = z.Water

                    # IF WATER AVAILABLE, THEN CALL SUB TO COMPUTE CN, RUNOFF,
                    # EROSION AND SEDIMENT

                    # XXX: This variable is set conditionally in CalcCnErosRunoffSed.CalcCN,
                    # but is referenced later even if it wasn't set. So we initialize here
                    # for safety.
                    z.CNum = 0

                    if z.Water > 0.01:
                        pass
                        # CalcCnErosRunoffSed.CalcCN(z, i, y, j)

                    # DAILY CN
                    z.DailyCN[y, i, j] = z.CNum

                    # UPDATE ANTECEDENT RAIN+MELT CONDITION
                    z.AMC5 = z.AMC5 - z.AntMoist[4] + z.Water
                    z.DailyAMC5[y, i, j] = z.AMC5
                    for k in range(1, 4):
                        z.AntMoist[5 - k] = z.AntMoist[4 - k]
                    z.AntMoist[0] = z.Water

                    # CALCULATE ET FROM SATURATED VAPOR PRESSURE,
                    # HAMON (1961) METHOD
                    if z.ETFlag == 0:
                        if z.DailyTemp > 0:
                            z.SatVaPressure = (33.8639 * ((0.00738 * z.DailyTemp +
                                               0.8072)**8 - 0.000019 *
                                               np.absolute(1.8 * z.DailyTemp + 48) +
                                               0.001316))
                            z.PotenET = (0.021 * z.DayHrs[i]**2 * z.SatVaPressure
                                         / (z.DailyTemp + 273))
                            z.ET = z.KV[i] * z.PotenET * z.PcntET[i]

                    # Daily ET calculation
                    z.DailyET[y, i, j] = z.ET

                    # ***** END WEATHER DATA ANALYSIS *****

                    # ***** WATERSHED WATER BALANCE *****

                    if z.QTotal <= z.Water:
                        z.Infiltration = z.Water - z.QTotal
                    z.GrFlow = z.RecessionCoef * z.SatStor
                    z.DeepSeep = z.SeepCoef * z.SatStor

                    # CALCULATE EVAPOTRANSPIRATION, Percolation, AND THE
                    # NEXT DAY'S UNSATURATED STORAGE AS LIMITED BY THE UNSATURATED
                    # ZONE MAXIMUM WATER CAPACITY

                    z.UnsatStor = z.UnsatStor + z.Infiltration

                    # Calculate water balance for non-Pesticide componenets
                    if z.ET >= z.UnsatStor:
                        z.ET = z.UnsatStor
                        z.UnsatStor = 0
                    else:
                        z.UnsatStor = z.UnsatStor - z.ET

                    # Obtain the Percolation, adjust precip and UnsatStor values
                    if z.UnsatStor > z.MaxWaterCap:
                        z.Percolation = z.UnsatStor - z.MaxWaterCap
                        z.Perc[y, i, j] = z.UnsatStor - z.MaxWaterCap
                        z.UnsatStor = z.UnsatStor - z.Percolation
                    else:
                        z.Percolation = 0
                        z.Perc[y, i, j] = 0
                    z.PercCm[y, i, j] = z.Percolation / 100

                    # CALCULATE STORAGE IN SATURATED ZONES AND GROUNDWATER
                    # DISCHARGE
                    z.SatStor = z.SatStor + z.Percolation - z.GrFlow - z.DeepSeep
                    if z.SatStor < 0:
                        z.SatStor = 0
                    z.Flow = z.QTotal + z.GrFlow
                    z.DailyFlow[y, i, j] = z.DayRunoff[y, i, j] + z.GrFlow

                    z.DailyFlowGPM[y, i, j] = z.Flow * 0.00183528 * z.TotAreaMeters
                    z.DailyGrFlow[y, i, j] = z.GrFlow  # (for daily load calculations)

                    # MONTHLY FLOW
                    z.MonthFlow[y, i] = z.MonthFlow[y, i] + z.DailyFlow[y, i, j]

                    # CALCULATE TOTALS
                    z.Precipitation[y, i] = z.Precipitation[y, i] + z.Prec[y, i, j]
                    z.Evapotrans[y, i] = z.Evapotrans[y, i] + z.ET
                    z.StreamFlow[y, i] = z.StreamFlow[y, i] + z.Flow
                    z.GroundWatLE[y, i] = z.GroundWatLE[y, i] + z.GrFlow

                    # CALCULATE DAILY NUTRIENT LOAD FROM PONDING SYSTEMS
                    z.PondNitrLoad = (z.NumPondSys[i] *
                                      (z.NitrSepticLoad - z.NitrPlantUptake * z.Grow[i]))
                    z.PondPhosLoad = (z.NumPondSys[i] *
                                      (z.PhosSepticLoad - z.PhosPlantUptake * z.Grow[i]))

                    # UPDATE MASS BALANCE ON PONDED EFFLUENT
                    if z.Temp[y, i, j] <= 0 or z.InitSnow > 0:

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
                                          z.NitrPlantUptake * z.Grow[i])

                    # 0.56 IS ATTENUATION FACTOR FOR SOIL LOSS
                    # 0.66 IS ATTENUATION FACTOR FOR SUBSURFACE FLOW LOSS
                    z.MonthShortNitr[i] = (z.MonthShortNitr[i] + z.NitrSepticLoad -
                                           z.NitrPlantUptake * z.Grow[i])
                    z.MonthShortPhos[i] = (z.MonthShortPhos[i] + z.PhosSepticLoad -
                                           z.PhosPlantUptake * z.Grow[i])
                    z.MonthDischargeNitr[i] = z.MonthDischargeNitr[i] + z.NitrSepticLoad
                    z.MonthDischargePhos[i] = z.MonthDischargePhos[i] + z.PhosSepticLoad

                    # CALCULATE WITHDRAWAL AND POINT SOURCE FLOW VALUES
                    z.Withdrawal[y, i] = (z.Withdrawal[y, i] + z.StreamWithdrawal[i] +
                                          z.GroundWithdrawal[i])
                    z.PtSrcFlow[y, i] = z.PtSrcFlow[y, i] + z.PointFlow[i]

                    # CALCULATE THE SURFACE RUNOFF PORTION OF TILE DRAINAGE
                    z.TileDrainRO[y, i] = (z.TileDrainRO[y, i] + [z.AgRunoff[y, i] *
                                           z.TileDrainDensity])

                    # CALCULATE SUBSURFACE PORTION OF TILE DRAINAGE
                    z.GwAgLE[y, i] = (z.GwAgLE[y, i] + (z.GroundWatLE[y, i] *
                                      (z.AgAreaTotal / z.AreaTotal)))
                    z.TileDrainGW[y, i] = (z.TileDrainGW[y, i] + [z.GwAgLE[y, i] *
                                           z.TileDrainDensity])

                    # ADD THE TWO COMPONENTS OF TILE DRAINAGE FLOW
                    z.TileDrain[y, i] = (z.TileDrain[y, i] + z.TileDrainRO[y, i] +
                                         z.TileDrainGW[y, i])

                    # ADJUST THE GROUNDWATER FLOW
                    z.GroundWatLE[y, i] = z.GroundWatLE[y, i] - z.TileDrainGW[y, i]
                    if z.GroundWatLE[y, i] < 0:
                        z.GroundWatLE[y, i] = 0

                    # ADJUST THE SURFACE RUNOFF
                    z.Runoff[y, i] = z.Runoff[y, i] - z.TileDrainRO[y, i]

                    if z.Runoff[y, i] < 0:
                        z.Runoff[y, i] = 0

                    # CALCULATE ANIMAL FEEDING OPERATIONS OUTPUT
                    AFOS.AnimalOperations(z, y)

                    # CALCULATE NUTRIENT AND SEDIMENT LOADS
                    CalcLoads.CalculateLoads(z, y)

                    # CALCULATE STREAM BANK EROSION
                    StreamBank.CalculateStreamBankEros(z, y)

                    # CALCULATE FINAL ANNUAL MEAN LOADS
                    AnnualMeans.CalculateAnnualMeanLoads(z, y)

            # CALCULATE FINAL MONTHLY AND ANNUAL WATER BALANCE FOR
            # AVERAGE STREAM FLOW

            for i in range(12):
                z.AvStreamFlow[i] = (z.AvRunoff[i] + z.AvGroundWater[i] +
                                     z.AvPtSrcFlow[i] + z.AvTileDrain[i] -
                                     z.AvWithdrawal[i])

                z.AvCMStream[i] = (z.AvStreamFlow[i] / 100) * z.TotAreaMeters
                if z.AvCMStream[i] > 0:
                    z.AvOrgConc[i] = (z.AvTotalOrgs[i] / (z.AvCMStream[i] * 1000)) / 10
                else:
                    z.AvOrgConc[i] = 0
            z.AvOrgConc[0] = 0

    print("Model run complete for " + str(z.NYrs) + " years of data.")

    output = WriteOutputFiles.WriteOutput(z)
    # WriteOutputFiles.WriteOutputSumFiles()

    print(output)
    print('Done')
