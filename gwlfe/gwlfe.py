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
from . import AFOS_old
from . import CalcLoads
from . import StreamBank
from . import AnnualMeans
from . import WriteOutputFiles
import Precipitation
import ET
import PtSrcFlow
from InitSnow import InitSnow_2
from Water import Water
from Water import Water_2
from Erosiv import Erosiv
from NLU import NLU
from CNI import CNI
from CNP import CNP
from LU import LU
from LU_1 import LU_1
from GrowFactor import GrowFactor_2
from Retention import Retention
from Retention import Retention_2
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
from TotAEU import TotAEU
from AEU import TotLAEU
from TotPAEU import TotPAEU
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
from ET_2 import ET_2_2
# from SatStor import SatStor
# from DeepSeep import DeepSeep
from GrFlow import GrFlow
from Flow import Flow
from GroundWatLE import GroundWatLE
from GwAgLE import GwAgLE
from TileDrainGW import TileDrainGW
from GroundWatLE_2 import GroundWatLE_2
from TileDrain import TileDrain
from Withdrawal import Withdrawal
from StreamFlow import StreamFlow
from StreamFlowLE import StreamFlowLE
from TotAreaMeters import TotAreaMeters
from StreamFlowVol import StreamFlowVol
from LE import LE
from StreamBankEros import StreamBankEros
from SURBBANK import SURBBANK
from SEDSTAB import SEDSTAB
from AGSTRM import AGSTRM
from SEDFEN import SEDFEN
from StreamBankEros_2 import StreamBankEros_2
from SedTrans import SedTrans
from RurEros import RurEros
from BSed import BSed
from SedDelivRatio import SedDelivRatio
# from ErosionSedYield import ErosionSedYield
from Erosion import Erosion
from SedYield import SedYield
from SedYield_2 import SedYield_2
from Erosion_2 import Erosion_2
from UncontrolledQ import UncontrolledQ
from RetentionEff import RetentionEff
from WashPerv import WashPerv
from WashImperv import WashImperv
from RurQRunoff import RurQRunoff
from ErosWashoff import ErosWashoff
from UrbQRunoff import UrbQRunoff

log = logging.getLogger(__name__)

# @time_function
def run(z):
    log.debug('Running model...')

    # Raise exception instead of printing a warning for floating point
    # overflow, underflow, and division by 0 errors.
    np.seterr(all='raise')

    # MODEL CALCULATIONS FOR EACH YEAR OF ANALYSIS - WATER BALANCE,
    # NUTRIENTS AND SEDIMENT LOADS

    z.Retention = Retention_2(z.NYrs, z.DaysMonth, z.Temp, z.Prec, z.InitSnow_0, z.AntMoist_0, z.NRur, z.NUrb, z.CN,
                            z.Grow_0)

    z.QrunP = QrunP(z.NYrs, z.DaysMonth, z.NRur, z.NUrb, z.Temp, z.InitSnow_0, z.Prec, z.CNP_0, z.AntMoist_0, z.Grow_0)

    z.QrunI = QrunI(z.NYrs, z.DaysMonth, z.NRur, z.NUrb, z.Temp, z.InitSnow_0, z.Prec, z.CNI_0, z.AntMoist_0, z.Grow_0)

    z.Qrun = Qrun(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.CN, z.AntMoist_0, z.Grow_0)

    z.UrbAreaTotal = UrbAreaTotal(z.NRur, z.NUrb, z.Area)

    z.AreaTotal = AreaTotal(z.NRur, z.NUrb, z.Area)

    z.UrbanQTotal = UrbanQTotal(z.NYrs, z.DaysMonth, z.NRur, z.NUrb, z.Temp, z.InitSnow_0, z.Prec, z.Area, z.CNI_0,
                                z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA)

    z.UrbanQTotal_1 = UrbanQTotal_1(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                                    z.AntMoist_0, z.Grow_0,
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
                      z.Grow_0, z.CNP_0, z.Imper,
                      z.ISRR, z.ISRA, z.CN)

    z.AdjUrbanQTotal_1 = AdjUrbanQTotal_1(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area,
                                          z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0,
                                          z.Imper, z.ISRR, z.ISRA, z.Qretention, z.PctAreaInfil)

    z.AdjQTotal = AdjQTotal(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                            z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
                            z.ISRR, z.ISRA, z.Qretention, z.PctAreaInfil, z.n25b, z.CN)

    z.RuralQTotal = RuralQTotal(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.CN, z.NUrb, z.AntMoist_0,
                                z.Grow_0, z.Area)

    z.AgAreaTotal = AgAreaTotal(z.NRur, z.Landuse, z.Area)

    z.TileDrainRO = TileDrainRO(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.CN, z.AntMoist_0, z.NUrb,
                                z.Grow_0, z.Landuse, z.Area, z.TileDrainDensity)

    z.Runoff = Runoff(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0,
                      z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention, z.PctAreaInfil, z.n25b, z.CN, z.Landuse,
                      z.TileDrainDensity)

    z.Infiltration = Infiltration(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
                                  z.ISRR, z.ISRA, z.CN)

    z.UnsatStor = UnsatStor(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
              z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap)

    z.Percolation = Percolation(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
           z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap)

    z.ET_2 = ET_2_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
         z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap)

    # z.SatStor = SatStor(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
    #         z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0, z.RecessionCoef, z.SeepCoef)
    #
    # z.DeepSeep = DeepSeep(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
    #          z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0, z.RecessionCoef, z.SeepCoef)

    z.GrFlow = GrFlow(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0,
                      z.Grow_0, z.CNP_0, z.Imper,
                      z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0,
                      z.RecessionCoef, z.SeepCoef)

    z.Flow = Flow(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
         z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0, z.RecessionCoef, z.SeepCoef)

    z.GroundWatLE = GroundWatLE(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
           z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0, z.RecessionCoef, z.SeepCoef)

    z.GwAgLE = GwAgLE(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
           z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0, z.RecessionCoef, z.SeepCoef, z.Landuse)

    z.TileDrainGW = TileDrainGW(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
                z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0, z.RecessionCoef, z.SeepCoef,
                z.Landuse, z.TileDrainDensity)

    z.GroundWatLE_2 = GroundWatLE_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
                  z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0, z.RecessionCoef, z.SeepCoef,
                  z.Landuse, z.TileDrainDensity)

    z.TileDrain = TileDrain(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
              z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0, z.RecessionCoef, z.SeepCoef, z.Landuse,
              z.TileDrainDensity)

    z.Withdrawal = Withdrawal(z.NYrs, z.StreamWithdrawal, z.GroundWithdrawal)

    z.StreamFlow = StreamFlow(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
               z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0, z.RecessionCoef, z.SeepCoef
               , z.Qretention, z.PctAreaInfil, z.n25b, z.Landuse, z.TileDrainDensity, z.PointFlow, z.StreamWithdrawal,
               z.GroundWithdrawal)

    z.StreamFlowLE = StreamFlowLE(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
               z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0, z.RecessionCoef, z.SeepCoef
               , z.Qretention, z.PctAreaInfil, z.n25b, z.Landuse, z.TileDrainDensity, z.PointFlow, z.StreamWithdrawal,
               z.GroundWithdrawal)

    z.TotAreaMeters = TotAreaMeters(z.NRur, z.NUrb, z.Area)

    z.StreamFlowVol = StreamFlowVol(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
                  z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0, z.RecessionCoef, z.SeepCoef
                  , z.Qretention, z.PctAreaInfil, z.n25b, z.Landuse, z.TileDrainDensity, z.PointFlow, z.StreamWithdrawal,
                  z.GroundWithdrawal)

    z.LE = LE(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
       z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0, z.RecessionCoef, z.SeepCoef
       , z.Qretention, z.PctAreaInfil, z.n25b, z.Landuse, z.TileDrainDensity, z.PointFlow, z.StreamWithdrawal, z.GroundWithdrawal
       , z.NumAnimals, z.AvgAnimalWt, z.StreamFlowVolAdj, z.SedAFactor_0, z.AvKF, z.AvSlope, z.SedAAdjust)

    z.StreamBankEros = StreamBankEros(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
                   z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0, z.RecessionCoef, z.SeepCoef
                   , z.Qretention, z.PctAreaInfil, z.n25b, z.Landuse, z.TileDrainDensity, z.PointFlow, z.StreamWithdrawal,
                   z.GroundWithdrawal
                   , z.NumAnimals, z.AvgAnimalWt, z.StreamFlowVolAdj, z.SedAFactor_0, z.AvKF, z.AvSlope, z.SedAAdjust, z.StreamLength)

    z.SURBBANK = SURBBANK(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
                   z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0, z.RecessionCoef, z.SeepCoef
                   , z.Qretention, z.PctAreaInfil, z.n25b, z.Landuse, z.TileDrainDensity, z.PointFlow, z.StreamWithdrawal,
                   z.GroundWithdrawal
                   , z.NumAnimals, z.AvgAnimalWt, z.StreamFlowVolAdj, z.SedAFactor_0, z.AvKF, z.AvSlope, z.SedAAdjust, z.StreamLength
                   , z.UrbBankStab, z.n42b, z.n85d)

    z.SEDSTAB = SEDSTAB(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
                   z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0, z.RecessionCoef, z.SeepCoef
                   , z.Qretention, z.PctAreaInfil, z.n25b, z.Landuse, z.TileDrainDensity, z.PointFlow, z.StreamWithdrawal,
                   z.GroundWithdrawal
                   , z.NumAnimals, z.AvgAnimalWt, z.StreamFlowVolAdj, z.SedAFactor_0, z.AvKF, z.AvSlope, z.SedAAdjust, z.StreamLength
                               , z.n42b, z.n46c, z.n85d)

    z.AGSTRM = AGSTRM(z.AgLength, z.StreamLength)

    z.SEDFEN = SEDFEN(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
                   z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0, z.RecessionCoef, z.SeepCoef
                   , z.Qretention, z.PctAreaInfil, z.n25b, z.Landuse, z.TileDrainDensity, z.PointFlow, z.StreamWithdrawal,
                   z.GroundWithdrawal
                   , z.NumAnimals, z.AvgAnimalWt, z.StreamFlowVolAdj, z.SedAFactor_0, z.AvKF, z.AvSlope, z.SedAAdjust, z.StreamLength
                      , z.AgLength, z.n42, z.n45, z.n85)

    z.StreamBankEros_2 = StreamBankEros_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
                   z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0, z.RecessionCoef, z.SeepCoef
                   , z.Qretention, z.PctAreaInfil, z.n25b, z.Landuse, z.TileDrainDensity, z.PointFlow, z.StreamWithdrawal,
                   z.GroundWithdrawal
                   , z.NumAnimals, z.AvgAnimalWt, z.StreamFlowVolAdj, z.SedAFactor_0, z.AvKF, z.AvSlope, z.SedAAdjust, z.StreamLength
                     , z.n42b, z.n46c, z.n85d, z.AgLength, z.n42, z.n45, z.n85, z.UrbBankStab)

    z.SedTrans = SedTrans(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
             z.ISRR, z.ISRA, z.Qretention, z.PctAreaInfil, z.n25b, z.CN)

    z.RurEros = RurEros(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.Acoef, z.NRur, z.KF, z.LS, z.C, z.P, z.Area)

    z.BSed = BSed(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper,
         z.ISRR, z.ISRA, z.Qretention, z.PctAreaInfil, z.n25b, z.CN)

    z.SedDelivRatio = SedDelivRatio(z.SedDelivRatio_0)

    # z.SedYield_temp = ErosionSedYield(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.Acoef, z.NRur, z.KF, z.LS, z.C, z.P, z.Area, z.SedDelivRatio_0,
    #                 z.NUrb, z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.Qretention, z.PctAreaInfil, z.n25b, z.CN,
    #                 z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs, z.MaxWaterCap, z.SatStor_0, z.RecessionCoef, z.SeepCoef,
    #                 z.Landuse, z.TileDrainDensity, z.PointFlow, z.StreamWithdrawal, z.GroundWithdrawal,
    #                 z.NumAnimals, z.AvgAnimalWt, z.StreamFlowVolAdj, z.SedAFactor_0, z.AvKF, z.AvSlope, z.SedAAdjust, z.StreamLength,
    #                 z.n42b, z.n46c, z.n85d, z.AgLength, z.n42, z.n45, z.n85, z.UrbBankStab)
    # TODO This is just a temporary variable to help with testing, can be deleted / is not actually used in model

    z.Erosion = Erosion(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.Acoef, z.NRur, z.KF, z.LS, z.C, z.P,
                        z.Area)

    z.SedYield = SedYield(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.Acoef, z.NRur, z.KF, z.LS, z.C, z.P,
                          z.Area, z.NUrb, z.CNI_0, z.AntMoist_0, z.Grow_0,
                          z.ISRR, z.ISRA, z.Qretention, z.PctAreaInfil, z.n25b, z.CN, z.CNP_0, z.Imper,
                          z.SedDelivRatio_0)

    z.SedYield_2 = SedYield_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                              z.AntMoist_0,
                              z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs,
                              z.MaxWaterCap, z.SatStor_0,
                              z.RecessionCoef, z.SeepCoef, z.Qretention, z.PctAreaInfil, z.n25b, z.Landuse,
                              z.TileDrainDensity, z.PointFlow,
                              z.StreamWithdrawal, z.GroundWithdrawal, z.NumAnimals, z.AvgAnimalWt, z.StreamFlowVolAdj,
                              z.SedAFactor_0,
                              z.AvKF, z.AvSlope, z.SedAAdjust, z.StreamLength, z.n42b, z.n46c, z.n85d, z.AgLength,
                              z.n42, z.n45, z.n85, z.UrbBankStab,
                              z.Acoef, z.KF, z.LS, z.C, z.P, z.SedDelivRatio_0)

    z.Erosion_2 = Erosion_2(z.NYrs, z.DaysMonth, z.Temp, z.InitSnow_0, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0,
                            z.AntMoist_0,
                            z.Grow_0, z.CNP_0, z.Imper, z.ISRR, z.ISRA, z.CN, z.UnsatStor_0, z.KV, z.PcntET, z.DayHrs,
                            z.MaxWaterCap, z.SatStor_0,
                            z.RecessionCoef, z.SeepCoef, z.Qretention, z.PctAreaInfil, z.n25b, z.Landuse,
                            z.TileDrainDensity, z.PointFlow,
                            z.StreamWithdrawal, z.GroundWithdrawal, z.NumAnimals, z.AvgAnimalWt, z.StreamFlowVolAdj,
                            z.SedAFactor_0,
                            z.AvKF, z.AvSlope, z.SedAAdjust, z.StreamLength, z.n42b, z.n46c, z.n85d, z.AgLength, z.n42,
                            z.n45, z.n85, z.UrbBankStab,
                            z.SedDelivRatio_0, z.Acoef, z.KF, z.LS, z.C, z.P)

    z.UncontrolledQ = UncontrolledQ(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.NUrb, z.Area, z.CNI_0, z.CNP_0, z.AntMoist_0, z.Grow_0, z.Imper,
                  z.ISRR, z.ISRA)

    z.RetentionEff = RetentionEff(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.Qretention, z.NRur, z.NUrb, z.Area, z.CNI_0, z.AntMoist_0, z.Grow_0, z.CNP_0,
                 z.Imper, z.ISRR, z.ISRA, z.PctAreaInfil)

    z.WashPerv = WashPerv(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.CNP_0, z.AntMoist_0, z.Grow, z.NRur, z.NUrb)

    z.WashImperv = WashImperv(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.CNI_0, z.AntMoist_0, z.Grow, z.NRur, z.NUrb)

    z.RurQRunoff = RurQRunoff(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.AntMoist_0, z.NRur, z.NUrb, z.CN, z.Grow)

    z.ErosWashoff = ErosWashoff(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.NUrb, z.Acoef, z.KF, z.LS, z.C, z.P, z.Area)

    z.UrbQRunoff = UrbQRunoff(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec, z.NRur, z.NUrb, z.CNI_0, z.CNP_0, z.AntMoist_0, z.Grow, z.Imper, z.ISRR, z.ISRA)


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
                # z.ErosWashoff[l, i] = 0
                # z.RurQRunoff[l, i] = 0
                # z.UrbQRunoff[l, i] = 0
                z.LuErosion[Y, l] = 0

            # DAILY CALCULATIONS
            for j in range(z.DaysMonth[Y][i]):
                # DAILYWEATHERANALY TEMP[Y][I][J], PREC[Y][I][J]
                # ***** BEGIN WEATHER DATA ANALYSIS *****
                # Question: Are these values supposed to accumulate for each
                # day, each month, and each year? Or should these be
                # re-initialized to a default value at some point?
                # for l in range(z.NLU):
                #     z.ImpervAccum[l] = (z.ImpervAccum[l] * np.exp(-0.12) +
                #                         (1 / 0.12) * (1 - np.exp(-0.12)))
                #     # print("PervAccum old b4 = ", z.PervAccum[l], "PervAccum new b4 = ", z.WashPerv_temp[l])
                #     z.PervAccum[l] = (z.PervAccum[l] * np.exp(-0.12) +
                #                       (1 / 0.12) * (1 - np.exp(-0.12)))
                    # print("PervAccum old after = ", z.PervAccum[l], "PervAccum new after = ", z.WashPerv_temp[l])

                # TODO: If Water is <= 0.01, then CalcCNErosRunoffSed
                # never executes, and CNum will remain undefined.
                # What should the default value for CNum be in this case?

                # IF WATER AVAILABLE, THEN CALL SUB TO COMPUTE CN, RUNOFF,
                # EROSION AND SEDIMENT
                if z.Temp[Y][i][j] > 0 and Water_2(z.NYrs, z.DaysMonth, z.InitSnow_0, z.Temp, z.Prec)[Y][i][j] > 0.01:
                    CalcCnErosRunoffSed.CalcCN(z, i, Y, j)
                else:
                    pass

                # ***** END WEATHER DATA ANALYSIS *****

                # ***** WATERSHED WATER BALANCE *****

                z.PercCm[Y][i][j] = z.Percolation[Y][i][j] / 100

                z.DailyFlow[Y][i][j] = z.DayRunoff[Y][i][j] + z.GrFlow[Y][i][j]

                z.DailyFlowGPM[Y][i][j] = z.Flow[Y][i][j] * 0.00183528 * z.TotAreaMeters
                z.DailyGrFlow[Y][i][j] = z.GrFlow[Y][i][j]  # (for daily load calculations)

                # MONTHLY FLOW
                z.MonthFlow[Y][i] = z.MonthFlow[Y][i] + z.DailyFlow[Y][i][j]

                # CALCULATE TOTALS
                # z.Evapotrans[Y][i] = z.Evapotrans[Y][i] + z.ET_2[Y][i][j]

                # CALCULATE DAILY NUTRIENT LOAD FROM PONDING SYSTEMS
                z.PondNitrLoad = (z.NumPondSys[i] *
                                  (z.NitrSepticLoad - z.NitrPlantUptake * GrowFactor_2(z.Grow_0)[i]))
                z.PondPhosLoad = (z.NumPondSys[i] *
                                  (z.PhosSepticLoad - z.PhosPlantUptake * GrowFactor_2(z.Grow_0)[i]))

                # UPDATE MASS BALANCE ON PONDED EFFLUENT
                if z.Temp[Y][i][j] <= 0 or InitSnow_2(z.NYrs,z.DaysMonth,z.InitSnow_0,z.Temp,z.Prec)[Y][i][j] > 0:

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
                                      z.NitrPlantUptake * z.GrowFactor[i])

                # 0.56 IS ATTENUATION FACTOR FOR SOIL LOSS
                # 0.66 IS ATTENUATION FACTOR FOR SUBSURFACE FLOW LOSS
                z.MonthShortNitr[i] = (z.MonthShortNitr[i] + z.NitrSepticLoad -
                                       z.NitrPlantUptake * z.GrowFactor[i])
                z.MonthShortPhos[i] = (z.MonthShortPhos[i] + z.PhosSepticLoad -
                                       z.PhosPlantUptake * z.GrowFactor[i])
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
