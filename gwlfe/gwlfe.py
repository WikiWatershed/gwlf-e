#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

"""
Runs the GWLF-E MapShed model.

Imported from GWLF-E.frm
"""

import logging

import numpy as np
from DailyArrayConverter import get_value_for_yesterday

from .enums import ETflag, GrowFlag
from . import ReadGwlfDataFile
from . import PrelimCalculations
from . import CalcCnErosRunoffSed
from . import AFOS
from . import CalcLoads
from . import StreamBank
from . import AnnualMeans
from . import WriteOutputFiles
import Precipitation
import ET
import PtSrcFlow
from InitSnow import InitSnow
from Water import Water
from Erosiv import Erosiv
from NLU import NLU
from CNI import CNI
from CNP import CNP
from LU import LU
from LU_1 import LU_1
from GrowFactor import GrowFactor
from Retention import Retention
from QrunP import QrunP
from QrunI import QrunI
from Qrun import Qrun
from UrbAreaTotal import UrbAreaTotal
from UrbanQTotal import UrbanQTotal
from AreaTotal import AreaTotal
from UrbanQTotal_1 import UrbanQTotal_1
from AdjUrbanQTotal import AdjUrbanQTotal
from AdjUrbanQTotal_1 import AdjUrbanQTotal_1
from RurAreaTotal import RurAreaTotal
from RuralQTotal import RuralQTotal
from CNum import CNum
from Melt import Melt
from AMC5 import AMC5
from NewCN import NewCN
from AgAreaTotal import AgAreaTotal
from AgQTotal import AgQTotal
from QTotal import QTotal
from AgRunoff import AgRunoff
from AdjQTotal import AdjQTotal
from TileDrainRO import TileDrainRO
from Runoff import Runoff
from AEU import AEU
from AEU import TotAEU
from AEU import TotLAEU
from AEU import TotPAEU
from PcntUrbanArea import PcntUrbanArea
from AvCNUrb import AvCNUrb
from AvCNRur import AvCNRur
from AvCN import AvCN
from SedAFactor import SedAFactor
from QTotal import QTotal
from AdjUrbanQTotal_1 import AdjUrbanQTotal_1
from AdjQTotal import AdjQTotal
from RuralQTotal import RuralQTotal
from AgAreaTotal import AgAreaTotal
from TileDrainRO import TileDrainRO
from Runoff import Runoff
from Infiltration import Infiltration
from UnsatStor import UnsatStor
from Percolation import Percolation
from ET_2 import ET_2
# from SatStor import SatStor
# from DeepSeep import DeepSeep
from GrFlow import GrFlow
from Flow import Flow
from GroundWatLE import GroundWatLE
from GwAgLE import GwAgLE
from TileDrainGW import TileDrainGW
from GroundWatLE_2 import GroundWatLE_2

log = logging.getLogger(__name__)


# @time_function
def run(z):
    log.debug('Running model...')

    # Raise exception instead of printing a warning for floating point
    # overflow, underflow, and division by 0 errors.
    np.seterr(all='raise')

    # MODEL CALCULATIONS FOR EACH YEAR OF ANALYSIS - WATER BALANCE,
    # NUTRIENTS AND SEDIMENT LOADS

    z.Precipitation = Precipitation.Precipitation(z.NYrs, z.DaysMonth, z.Prec)
    # z.Precipitation = Precipitation.Precipitation_2(z.Prec)
    # if (z.Precipitation.any() == z.Precipitation_vect.any()):
    # print ('True')

    # DailyET_Part1 = ET.DailyET(z.NYrs,z.DaysMonth,z.Temp,z.DayHrs,z.KV,z.PcntET,z.ETFlag)
    # z.DaysMonth = HashableArray(z.DaysMonth)
    # z.Temp = HashableArray(z.Temp)
    # z.Prec = HashableArray(z.Prec)

    DailyET_Part1 = ET.DailyET_2(z.Temp, z.KV, z.PcntET, z.DayHrs)

    z.PtSrcFlow = PtSrcFlow.PtSrcFlow_2(z.NYrs, z.PointFlow)

    z.InitSnow = InitSnow(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec)

    z.Water = Water(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec)

    z.Erosiv = Erosiv(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.Acoef)

    z.NLU = NLU(z.NRur, z.NUrb)

    z.CNI = CNI(z.NRur, z.NUrb, z.CNI_0)

    z.CNP = CNP(z.NRur, z.NUrb, z.CNP_0)

    z.lu = LU(z.NRur, z.NUrb)

    z.lu_1 = LU_1(z.NRur, z.NUrb)

    z.GrowFactor = GrowFactor(z.Grow)

    z.Retention = Retention(z.NYrs, z.DaysMonth, z.Temp, z.Prec, z.InitSnow_0, z.AntMoist_0, z.NRur, z.NUrb, z.CN,
                            z.Grow)

    z.QrunP = QrunP(z.NYrs, z.DaysMonth, z.NRur, z.NUrb, z.Temp, z.InitSnow_0, z.Prec, z.CNP_0, z.AntMoist_0, z.Grow)

    z.QrunI = QrunI(z.NYrs, z.DaysMonth, z.NRur, z.NUrb, z.Temp, z.InitSnow_0, z.Prec, z.CNI_0, z.AntMoist_0, z.Grow)

    z.Qrun = Qrun(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.CN, z.AntMoist_0, z.Grow)

    z.UrbAreaTotal = UrbAreaTotal(z.NRur, z.NUrb, z.Area)

    z.AreaTotal = AreaTotal(z.NRur, z.NUrb, z.Area)

    z.UrbanQTotal = UrbanQTotal(z.NYrs, z.DaysMonth, z.NRur, z.NUrb, z.Temp, z.InitSnow_0, z.Prec, z.Area, z.CNI_0,
                                z.AntMoist_0, z.Grow, z.CNP_0, z.Imper, z.ISRR, z.ISRA)

    z.UrbanQTotal_1 = UrbanQTotal_1(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                                    z.AntMoist_0, z.Grow,
                                    z.CNP_0, z.Imper, z.ISRR, z.ISRA)

    z.AEU = AEU(z.NumAnimals, z.AvgAnimalWt, z.NRur, z.NUrb, z.Area)

    z.TotAEU = TotAEU(z.NumAnimals, z.AvgAnimalWt)
    z.TotLAEU = TotLAEU(z.NumAnimals, z.AvgAnimalWt)

    z.TotPAEU = TotPAEU(z.NumAnimals, z.AvgAnimalWt)

    z.PcntUrbanArea = PcntUrbanArea(z.NRur, z.NUrb, z.Area)

    z.AvCNUrb = AvCNUrb(z.NRur, z.NUrb, z.CNI_0, z.CNP_0, z.Imper, z.Area)

    z.RurAreaTotal = RurAreaTotal(z.NRur, z.Area)

    z.AvCNRur = AvCNRur(z.NRur, z.Area, z.CN)

    z.AvCN = AvCN(z.NRur, z.NUrb, z.CNI_0, z.CNP_0, z.CN, z.Imper, z.Area)

    z.SedAFactor = SedAFactor(z.NumAnimals, z.AvgAnimalWt, z.NRur, z.NUrb, z.CNI_0, z.CNP_0, z.CN, z.Imper, z.Area
                              , z.SedAFactor_0, z.AvKF, z.AvSlope, z.SedAAdjust)

    z.QTotal = QTotal(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0,
                      z.Grow, z.CNP_0, z.Imper,
                      z.ISRR, z.ISRA, z.CN)

    z.AdjUrbanQTotal_1 = AdjUrbanQTotal_1(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
                                          z.CNI_0, z.AntMoist_0, z.Grow, z.CNP_0,
                                          z.Imper, z.ISRR, z.ISRA, z.Qretention, z.PctAreaInfil)

    z.AdjQTotal = AdjQTotal(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                            z.AntMoist_0, z.Grow, z.CNP_0, z.Imper,
                            z.ISRR, z.ISRA, z.Qretention, z.PctAreaInfil, z.n25b, z.CN)

    z.RuralQTotal = RuralQTotal(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.CN, z.NUrb, z.AntMoist_0,
                                z.Grow, z.Area)

    z.AgAreaTotal = AgAreaTotal(z.NRur, z.Landuse, z.Area)

    z.TileDrainRO = TileDrainRO(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.CN, z.AntMoist_0, z.NUrb,
                                z.Grow, z.Landuse, z.Area, z.TileDrainDensity)

    z.Runoff = Runoff(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0,
                      z.Grow, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention, z.PctAreaInfil, z.n25b, z.CN, z.Landuse,
                      z.TileDrainDensity)

    z.Infiltration = Infiltration(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow, z.CNP_0, z.Imper,
                                  z.ISRR, z.ISRA, z.CN)

    z.UnsatStor = UnsatStor(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow, z.CNP_0, z.Imper,
              z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap)

    z.Percolation = Percolation(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow, z.CNP_0, z.Imper,
           z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap)

    z.ET_2 = ET_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow, z.CNP_0, z.Imper,
         z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap)

    # z.SatStor = SatStor(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow, z.CNP_0, z.Imper,
    #         z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0, z.RecessionCoef, z.SeepCoef)
    #
    # z.DeepSeep = DeepSeep(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow, z.CNP_0, z.Imper,
    #          z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0, z.RecessionCoef, z.SeepCoef)

    z.GrFlow = GrFlow(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0,
                      z.Grow, z.CNP_0, z.Imper,
                      z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0,
                      z.RecessionCoef, z.SeepCoef)

    z.Flow = Flow(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow, z.CNP_0, z.Imper,
         z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0, z.RecessionCoef, z.SeepCoef)

    z.GroundWatLE = GroundWatLE(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow, z.CNP_0, z.Imper,
           z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0, z.RecessionCoef, z.SeepCoef)

    z.GwAgLE = GwAgLE(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow, z.CNP_0, z.Imper,
           z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0, z.RecessionCoef, z.SeepCoef, z.Landuse)

    z.TileDrainGW = TileDrainGW(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow, z.CNP_0, z.Imper,
                z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0, z.RecessionCoef, z.SeepCoef,
                z.Landuse, z.TileDrainDensity)

    z.GroundWatLE_2 = GroundWatLE_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow, z.CNP_0, z.Imper,
                  z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0, z.RecessionCoef, z.SeepCoef,
                  z.Landuse, z.TileDrainDensity)


    # --------- run the remaining parts of the model ---------------------

    ReadGwlfDataFile.ReadAllData(z)

    # CALCLULATE PRELIMINARY INITIALIZATIONS AND VALUES FOR
    # WATER BALANCE AND NUTRIENTS
    PrelimCalculations.InitialCalculations(z)

    # temp_AMC5 = z.AMC5
    # z.AMC5 = np.zeros((z.NYrs,12,31))
    # z.AMC5[0][0][0] = temp_AMC5

    # z.UnsatStor_temp = z.UnsatStor_0

    # z.SatStor_test = z.SatStor_0

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
                z.ErosWashoff[l, i] = 0
                z.RurQRunoff[l, i] = 0
                z.UrbQRunoff[l, i] = 0
                z.LuErosion[Y, l] = 0

            # DAILY CALCULATIONS
            for j in range(z.DaysMonth[Y][i]):
                # DAILYWEATHERANALY TEMP[Y][I][J], PREC[Y][I][J]
                # ***** BEGIN WEATHER DATA ANALYSIS *****
                z.DailyTemp = z.Temp[Y][i][j]
                # z.DailyPrec = z.Prec[Y][i][j]
                # z.Melt = 0
                # z.Rain = 0
                # z.Water = 0
                # z.Erosiv = 0
                z.ET = 0
                # z.QTotal = 0
                # z.AgQTotal = 0
                # z.RuralQTotal = 0
                # z.UrbanQTotal = 0 # duplicate

                # Question: Are these values supposed to accumulate for each
                # day, each month, and each year? Or should these be
                # re-initialized to a default value at some point?
                for l in range(z.NLU):
                    z.ImpervAccum[l] = (z.ImpervAccum[l] * np.exp(-0.12) +
                                        (1 / 0.12) * (1 - np.exp(-0.12)))
                    z.PervAccum[l] = (z.PervAccum[l] * np.exp(-0.12) +
                                      (1 / 0.12) * (1 - np.exp(-0.12)))

                # TODO: If Water is <= 0.01, then CalcCNErosRunoffSed
                # never executes, and CNum will remain undefined.
                # What should the default value for CNum be in this case?
                # z.CNum = 0

                # RAIN , SNOWMELT, EVAPOTRANSPIRATION (ET)
                # print(z.InitSnow,get_value_for_yesterday(z.InitSnow_2,z.InitSnow_0,Y,i,j,z.NYrs,z.DaysMonth))
                # if z.DailyTemp > 0 and get_value_for_yesterday(z.InitSnow, z.InitSnow_0, Y, i, j, z.NYrs,
                #                                                z.DaysMonth) > 0.001:
                #     z.Melt = 0.45 * z.DailyTemp
                # else:
                #     z.Melt = 0

                # if z.DailyTemp > 0 and get_value_for_yesterday(z.InitSnow, z.InitSnow_0, Y, i, j, z.NYrs,
                #                                                z.DaysMonth) > 0.001 and z.Melt[Y][i][
                #     j] > get_value_for_yesterday(
                #     z.InitSnow, z.InitSnow_0, Y, i, j, z.NYrs, z.DaysMonth):
                #     z.Melt_1 = get_value_for_yesterday(z.InitSnow, z.InitSnow_0, Y, i, j, z.NYrs, z.DaysMonth)
                # else:
                #     z.Melt_1 = z.Melt[Y][i][j]

                # AVAILABLE WATER CALCULATION
                # z.Water = z.Rain[Y][i][j] + z.Melt_1[Y][i][j]
                # z.DailyWater[Y][i][j] = z.Water[Y][i][j]

                # if z.DailyTemp <= 0:
                #     z.InitSnow_2[Y][i][j] = get_value_for_yesterday(z.InitSnow_2,z.InitSnow_0,Y,i,j,z.NYrs,z.DaysMonth) + z.DailyPrec
                # else:
                #     if get_value_for_yesterday(z.InitSnow_2,z.InitSnow_0,Y,i,j,z.NYrs,z.DaysMonth) > 0.001:
                #         if(z.Melt > get_value_for_yesterday(z.InitSnow_2, z.InitSnow_0, Y, i, j, z.NYrs, z.DaysMonth)):
                #             z.InitSnow_2[Y][i][j] = 0
                #         else:
                #             z.InitSnow_2[Y][i][j] = get_value_for_yesterday(z.InitSnow_2, z.InitSnow_0, Y, i, j, z.NYrs,
                #                                                             z.DaysMonth) - z.Melt
                #     else:
                #         z.InitSnow_2[Y][i][j] = get_value_for_yesterday(z.InitSnow_2,z.InitSnow_0,Y,i,j,z.NYrs,z.DaysMonth)
                # print(z.InitSnow_3[Y][i][j],z.InitSnow_2[Y][i][j] )

                # if z.DailyTemp > 0 and get_value_for_yesterday(z.InitSnow, z.InitSnow_0, Y, i, j, z.NYrs,
                #                                                z.DaysMonth) > 0.001:
                #     z.MeltPest[Y][i][j] = z.Melt[Y][i][j]
                # else:
                #     z.MeltPest[Y][i][j] = 0
                # if z.DailyTemp > 0 and get_value_for_yesterday(z.InitSnow, z.InitSnow_0, Y, i, j, z.NYrs, z.DaysMonth) > 0.001:
                #         if z.Melt[Y][i][j] > get_value_for_yesterday(z.InitSnow, z.InitSnow_0, Y, i, j, z.NYrs,
                #                                                      z.DaysMonth):
                #             z.MeltPest[Y][i][j] = get_value_for_yesterday(z.InitSnow, z.InitSnow_0, Y, i, j, z.NYrs,
                #                                                           z.DaysMonth)
                #         else:
                #             z.MeltPest[Y][i][j] = z.Melt[Y][i][j]
                # else:
                #     z.MeltPest[Y][i][j] = 0

                # Compute erosivity when erosion occurs, i.e., with rain and no InitSnow left
                # if z.DailyTemp > 0:
                #     if (get_value_for_yesterday(z.InitSnow, z.InitSnow_0, Y, i, j, z.NYrs, z.DaysMonth) > 0.001):
                #         if z.Rain[Y][i][j] > 0 and get_value_for_yesterday(z.InitSnow, z.InitSnow_0, Y, i, j, z.NYrs,
                #                                                            z.DaysMonth) - z.Melt_1[Y][i][j] < 0.001:
                #             z.Erosiv = 6.46 * z.Acoef[i] * z.Rain[Y][i][j] ** 1.81
                #     else:
                #         if z.Rain[Y][i][j] > 0 and get_value_for_yesterday(z.InitSnow, z.InitSnow_0, Y, i, j, z.NYrs,
                #                                                            z.DaysMonth) < 0.001:
                #             z.Erosiv = 6.46 * z.Acoef[i] * z.Rain[Y][i][j] ** 1.81

                # IF WATER AVAILABLE, THEN CALL SUB TO COMPUTE CN, RUNOFF,
                # EROSION AND SEDIMENT
                if z.Temp[Y][i][j] > 0 and z.Water[Y][i][j] > 0.01:
                    CalcCnErosRunoffSed.CalcCN(z, i, Y, j)
                else:
                    pass

                # print("n-1 init snow (",Y,i,j,")",z.InitSnow)

                # DAILY CN
                # z.DailyCN[Y][i][j] = z.CNum

                # UPDATE ANTECEDENT RAIN+MELT CONDITION
                # Subtract AMC5 by the sum of AntMoist (day 5) and Water
                # z.AMC5_2 = z.AMC5_2 - z.AntMoist[4] + z.Water[Y][i][j]
                # z.DailyAMC5[Y][i][j] = z.AMC5

                # Shift AntMoist values to the right.
                # z.AntMoist[4] = z.AntMoist[3]
                # z.AntMoist[3] = z.AntMoist[2]
                # z.AntMoist[2] = z.AntMoist[1]
                # z.AntMoist[1] = z.AntMoist[0]
                # z.AntMoist[0] = z.Water[Y][i][j]

                # print(z.AMC5_2,z.AMC5[Y][i][j])

                # CALCULATE ET FROM SATURATED VAPOR PRESSURE,
                # HAMON (1961) METHOD
                # if z.ETFlag is ETflag.HAMON_METHOD:
                #     if z.DailyTemp > 0:
                #         z.SatVaPressure = (33.8639 * ((0.00738 * z.DailyTemp +
                #                            0.8072) ** 8 - 0.000019 *
                #                            np.absolute(1.8 * z.DailyTemp + 48) +
                #                            0.001316))
                #         z.PotenET = (0.021 * z.DayHrs[i] ** 2 * z.SatVaPressure
                #                      / (z.DailyTemp + 273))
                #         z.ET = z.KV[i] * z.PotenET * z.PcntET[i]

                # Daily ET calculation
                # z.DailyET[Y][i][j] = z.ET
                # if (z.DailyET.any() == DailyET_Part1.any()):
                # print ('True')
                z.ET = DailyET_Part1[Y][i][j]
                z.DailyET[Y][i][j] = z.ET

                # ***** END WEATHER DATA ANALYSIS *****

                # ***** WATERSHED WATER BALANCE *****

                # if z.QTotal[Y][i][j] <= z.Water[Y][i][j]:
                #     z.Infiltration = z.Water[Y][i][j] - z.QTotal[Y][i][j]

                # z.GrFlow_test = z.RecessionCoef * z.SatStor_test
                # z.DeepSeep = z.SeepCoef * z.SatStor_test
                #
                # print("GrFlow orig = ", z.GrFlow_test,"GrFlow new = ", z.GrFlow[Y][i][j])
                # print(z.GrFlow_test == z.GrFlow[Y][i][j])

                # CALCULATE EVAPOTRANSPIRATION, Percolation, AND THE
                # NEXT DAY'S UNSATURATED STORAGE AS LIMITED BY THE UNSATURATED
                # ZONE MAXIMUM WATER CAPACITY

                # z.UnsatStor_temp = z.UnsatStor_temp + z.Infiltration[Y][i][j]

                # Calculate water balance for non-Pesticide componenets
                # if z.ET >= z.UnsatStor_temp:
                #     z.ET = z.UnsatStor_temp
                #     z.UnsatStor_temp = 0
                # else:
                #     z.UnsatStor_temp = z.UnsatStor_temp - z.ET

                # Obtain the Percolation, adjust precip and UnsatStor values
                # if z.UnsatStor_temp > z.MaxWaterCap:
                #     z.Percolation_2 = z.UnsatStor_temp - z.MaxWaterCap
                #     z.Perc[Y][i][j] = z.UnsatStor_temp - z.MaxWaterCap # TODO Perc is the same exact thing as Percolation
                #     z.UnsatStor_temp = z.UnsatStor_temp - z.Percolation_2
                # else:
                #     z.Percolation_2 = 0
                #     z.Perc[Y][i][j] = 0

                z.PercCm[Y][i][j] = z.Percolation[Y][i][j] / 100

                # print("UnsatStor orig = ", z.UnsatStor_temp, "UnsatStor new = ", z.UnsatStor[Y][i][j])
                # print(z.UnsatStor_temp == z.UnsatStor[Y][i][j])
                # print("Infiltration = ", z.Infiltration[Y][i][j])
                # print("MaxWaterCap = ", z.MaxWaterCap)

                # print("Percolation orig = ", z.Percolation_2, "Percolation new = ", z.Percolation[Y][i][j])
                # print(z.Percolation_2 == z.Percolation[Y][i][j])

                # CALCULATE STORAGE IN SATURATED ZONES AND GROUNDWATER
                # DISCHARGE
                # z.SatStor_test = z.SatStor_test + z.Percolation[Y][i][j] - z.GrFlow_test - z.DeepSeep
                # if z.SatStor_test < 0:
                #     z.SatStor_test = 0

                # z.Flow = z.QTotal[Y][i][j] + z.GrFlow[Y][i][j]

                z.DailyFlow[Y][i][j] = z.DayRunoff[Y][i][j] + z.GrFlow[Y][i][j]

                z.DailyFlowGPM[Y][i][j] = z.Flow[Y][i][j] * 0.00183528 * z.TotAreaMeters
                z.DailyGrFlow[Y][i][j] = z.GrFlow[Y][i][j]  # (for daily load calculations)

                # MONTHLY FLOW
                z.MonthFlow[Y][i] = z.MonthFlow[Y][i] + z.DailyFlow[Y][i][j]

                # CALCULATE TOTALS
                # z.Precipitation[Y][i] = z.Precipitation[Y][i] + z.Prec[Y][i][j]
                z.Evapotrans[Y][i] = z.Evapotrans[Y][i] + z.ET_2[Y][i][j]

                z.StreamFlow[Y][i] = z.StreamFlow[Y][i] + z.Flow[Y][i][j]

                # z.GroundWatLE[Y][i] = z.GroundWatLE[Y][i] + z.GrFlow[Y][i][j]

                # grow_factor = GrowFlag.intval(z.Grow[i])

                # CALCULATE DAILY NUTRIENT LOAD FROM PONDING SYSTEMS
                z.PondNitrLoad = (z.NumPondSys[i] *
                                  (z.NitrSepticLoad - z.NitrPlantUptake * z.GrowFactor[i]))
                z.PondPhosLoad = (z.NumPondSys[i] *
                                  (z.PhosSepticLoad - z.PhosPlantUptake * z.GrowFactor[i]))

                # UPDATE MASS BALANCE ON PONDED EFFLUENT
                if z.Temp[Y][i][j] <= 0 or z.InitSnow[Y][i][j] > 0:

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

                # grow_factor = GrowFlag.intval(z.Grow[i]) # duplicate

                # Obtain the monthly Normal Nitrogen
                z.MonthNormNitr[i] = (z.MonthNormNitr[i] + z.NitrSepticLoad -
                                      z.NitrPlantUptake * z.GrowFactor[i])

                # 0.56 IS ATTENUATION FACTOR FOR SOIL LOSS
                # 0.66 IS ATTENUATION FACTOR FOR SUBSURFACE FLOW LOSS
                z.MonthShortNitr[i] = (z.MonthShortNitr[i] + z.NitrSepticLoad -
                                       z.NitrPlantUptake * z.GrowFactor[i])
                z.MonthShortPhos[i] = (z.MonthShortPhos[i] + z.PhosSepticLoad -
                                       z.PhosPlantUptake * z.GrowFactor[i])
                z.MonthDischargeNitr[i] = z.MonthDischargeNitr[i] + z.NitrSepticLoad
                z.MonthDischargePhos[i] = z.MonthDischargePhos[i] + z.PhosSepticLoad

            # CALCULATE WITHDRAWAL AND POINT SOURCE FLOW VALUES
            z.Withdrawal[Y][i] = (z.Withdrawal[Y][i] + z.StreamWithdrawal[i] +
                                  z.GroundWithdrawal[i])
            # z.PtSrcFlow[Y][i] = z.PtSrcFlow[Y][i] + z.PointFlow[i]

            # # CALCULATE THE SURFACE RUNOFF PORTION OF TILE DRAINAGE
            # z.TileDrainRO[Y][i] = (z.AgRunoff[Y][i] * z.TileDrainDensity)

            # CALCULATE SUBSURFACE PORTION OF TILE DRAINAGE
            # if z.AreaTotal > 0:
            #     z.GwAgLE[Y][i] = (z.GwAgLE[Y][i] + (z.GroundWatLE[Y][i] *
            #                                         (z.AgAreaTotal / z.AreaTotal)))
            # z.TileDrainGW[Y][i] = (z.TileDrainGW[Y][i] + [z.GwAgLE[Y][i] *
            #                                               z.TileDrainDensity])

            # ADD THE TWO COMPONENTS OF TILE DRAINAGE FLOW
            z.TileDrain[Y][i] = (z.TileDrain[Y][i] + z.TileDrainRO[Y][i] +
                                 z.TileDrainGW[Y][i])

            # ADJUST THE GROUNDWATER FLOW
            # z.GroundWatLE[Y][i] = z.GroundWatLE[Y][i] - z.TileDrainGW[Y][i]
            # if z.GroundWatLE[Y][i] < 0:
            #     z.GroundWatLE[Y][i] = 0

            # print("GroundWatLE orig = ", z.GroundWatLE[Y][i], "GroundWatLE new = ", z.GroundWatLE_2_temp[Y][i])
            # print(z.GroundWatLE[Y][i] == z.GroundWatLE_2_temp[Y][i])

            # # ADJUST THE SURFACE RUNOFF
            # z.Runoff[Y][i] = z.Runoff[Y][i] - z.TileDrainRO[Y][i]

            # if z.Runoff[Y][i] < 0:
            #     z.Runoff[Y][i] = 0

        # CALCULATE ANIMAL FEEDING OPERATIONS OUTPUT
        AFOS.AnimalOperations(z, Y)

        # CALCULATE NUTRIENT AND SEDIMENT LOADS
        CalcLoads.CalculateLoads(z, Y)

        # CALCULATE STREAM BANK EROSION
        StreamBank.CalculateStreamBankEros(z, Y)

        # CALCULATE FINAL ANNUAL MEAN LOADS
        AnnualMeans.CalculateAnnualMeanLoads(z, Y)

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

    z.AvStreamFlowSum = (z.AvRunoffSum + z.AvGroundWaterSum +
                         z.AvPtSrcFlowSum + z.AvTileDrainSum -
                         z.AvWithdrawalSum)

    log.debug("Model run complete for " + str(z.NYrs) + " years of data.")

    output = WriteOutputFiles.WriteOutput(z)
    # WriteOutputFiles.WriteOutputSumFiles()
    return output
