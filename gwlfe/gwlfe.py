#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

import numpy as np

from . import ReadGwlfDataFile
from . import PrelimCalculations
from . import CalcCnErosRunoffSed
from . import AFOS
from . import CalcLoads
from . import StreamBank
from . import AnnualMeans
from . import WriteOutputFiles


def run():
    print('Running model...')

    # Redimension the Summary Variables
    # SumPrecipitation = np.zeros(12)
    # SumEvapoTrans = np.zeros(12)
    # SumGroundWater = np.zeros(12)
    # SumRunoff = np.zeros(12)
    # SumStreamFlow = np.zeros(12)
    # SumPtSrcFlow = np.zeros(12)
    # SumTileDrain = np.zeros(12)
    # SumWithdrawal = np.zeros(12)
    # SumErosion = np.zeros(12)
    # SumSedYield = np.zeros(12)
    # SumDisNitr = np.zeros(12)
    # SumTotNitr = np.zeros(12)
    # SumDisPhos = np.zeros(12)
    # SumTotPhos = np.zeros(12)
    # SumTileDrainN = np.zeros(12)
    # SumTileDrainP = np.zeros(12)
    # SumTileDrainSed = np.zeros(12)
    # SumAnimalN = np.zeros(12)
    # SumAnimalP = np.zeros(12)
    # SumAnimalFC = np.zeros(12)
    # SumWWOrgs = np.zeros(12)
    # SumSSOrgs = np.zeros(12)
    # SumUrbOrgs = np.zeros(12)
    # SumWildOrgs = np.zeros(12)
    # SumTotalOrgs = np.zeros(12)
    # SumCMStream = np.zeros(12)
    # SumOrgConc = np.zeros(12)
    # SumErosionCon = np.zeros(12)
    # SumSedYieldCon = np.zeros(12)
    # SumStreamBankErosCon = np.zeros(12)
    # SumStreamBankNCon = np.zeros(12)
    # SumStreamBankPCon = np.zeros(12)
    # SumDisNitrCon = np.zeros(12)
    # SumTotNitrCon = np.zeros(12)
    # SumDisPhosCon = np.zeros(12)
    # SumTotPhosCon = np.zeros(12)
    # SumStreamBankEros = np.zeros(12)
    # SumStreamBankN = np.zeros(12)
    # SumStreamBankP = np.zeros(12)
    # SumArea = np.zeros(25)
    # SumLuRunoff = np.zeros(25)
    # SumLuErosion = np.zeros(25)
    # SumLuSedYield = np.zeros(25)
    # SumLuDisNitr = np.zeros(25)
    # SumLuTotNitr = np.zeros(25)
    # SumLuDisPhos = np.zeros(25)
    # SumLuTotPhos = np.zeros(25)
    # SumGroundNitr = np.zeros(12)
    # SumGroundPhos = np.zeros(12)
    # SumTotArea = 0
    # SumYrPointNitr = 0
    # SumYrPointPhos = 0
    # SumSeptNitr = 0
    # SumSeptPhos = 0
    # SumDailyTotArea = 0
    # SumFarmOrgs = 0
    # SumWWTPOrgs = 0
    # SumSeptOrgs = 0
    # SumUrbanOrgs = 0
    # SumWildlifeOrgs = 0
    # FirstRun = True

    # SumDailyTemp = np.zeros((50, 12, 31))
    # SumDailyPrec = np.zeros((50, 12, 31))
    # SumDailyET = np.zeros((50, 12, 31))
    # SumDayRunoff = np.zeros((50, 12, 31))
    # SumDailyFlow = np.zeros((50, 12, 31))
    # SumDailyFlowMGD = np.zeros((50, 12, 31))
    # SumDailyPtSrcFlow = np.zeros((50, 12, 31))
    # SumDailyFlowM3 = np.zeros((50, 12, 31))
    # SumDailyTSS = np.zeros((50, 12, 31))
    # SumDailyTSSmgl = np.zeros((50, 12, 31))
    # SumDailyTN = np.zeros((50, 12, 31))
    # SumDailyTNmgl = np.zeros((50, 12, 31))
    # SumDailyTP = np.zeros((50, 12, 31))
    # SumDailyTPmgl = np.zeros((50, 12, 31))
    # SumDailyPointN = np.zeros((50, 12, 31))
    # SumDailySepticN = np.zeros((50, 12, 31))
    # SumDailyAnimalN = np.zeros((50, 12, 31))
    # SumDailyStrmN = np.zeros((50, 12, 31))
    # SumDailyUplandN = np.zeros((50, 12, 31))
    # SumDailyGroundN = np.zeros((50, 12, 31))
    # SumDailyTileDrainN = np.zeros((50, 12, 31))
    # SumDailyPointP = np.zeros((50, 12, 31))
    # SumDailySepticP = np.zeros((50, 12, 31))
    # SumDailyAnimalP = np.zeros((50, 12, 31))
    # SumDailyStrmP = np.zeros((50, 12, 31))
    # SumDailyUplandP = np.zeros((50, 12, 31))
    # SumDailyGroundP = np.zeros((50, 12, 31))
    # SumDailyTileDrainP = np.zeros((50, 12, 31))

    # SumUAHPA = 0
    # SumUAHPS = 0
    # SumUAHPSLR = 0
    # SumUAHPN = 0
    # SumUAHPNLR = 0
    # SumUAHPP = 0
    # SumUAHPPLR = 0
    # SumUACPA = 0
    # SumUACPS = 0
    # SumUACPSLR = 0
    # SumUACPN = 0
    # SumUACPNLR = 0
    # SumUACPP = 0
    # SumUACPPLR = 0
    # SumUAFA = 0
    # SumUAFS = 0
    # SumUAFSLR = 0
    # SumUAFN = 0
    # SumUAFNLR = 0
    # SumUAFP = 0
    # SumUAFPLR = 0
    # SumUAWA = 0
    # SumUAWS = 0
    # SumUAWSLR = 0
    # SumUAWN = 0
    # SumUAWNLR = 0
    # SumUAWP = 0
    # SumUAWPLR = 0
    # SumUADA = 0
    # SumUADS = 0
    # SumUADSLR = 0
    # SumUADN = 0
    # SumUADNLR = 0
    # SumUADP = 0
    # SumUADPLR = 0
    # SumUATA = 0
    # SumUATS = 0
    # SumUATSLR = 0
    # SumUATN = 0
    # SumUATNLR = 0
    # SumUATP = 0
    # SumUATPLR = 0
    # SumUAOLA = 0
    # SumUAOLS = 0
    # SumUAOLSLR = 0
    # SumUAOLN = 0
    # SumUAOLNLR = 0
    # SumUAOLP = 0
    # SumUAOLPLR = 0
    # SumUABRA = 0
    # SumUABRS = 0
    # SumUABRSLR = 0
    # SumUABRN = 0
    # SumUABRNLR = 0
    # SumUABRP = 0
    # SumUABRPLR = 0
    # SumUASAA = 0
    # SumUASAS = 0
    # SumUASASLR = 0
    # SumUASAN = 0
    # SumUASANLR = 0
    # SumUASAP = 0
    # SumUASAPLR = 0
    # SumUAURA = 0
    # SumUAURS = 0
    # SumUAURSLR = 0
    # SumUAURN = 0
    # SumUAURNLR = 0
    # SumUAURP = 0
    # SumUAURPLR = 0
    # SumUALDMA = 0
    # SumUALDMS = 0
    # SumUALDMSLR = 0
    # SumUALDMN = 0
    # SumUALDMNLR = 0
    # SumUALDMP = 0
    # SumUALDMPLR = 0
    # SumUAMDMA = 0
    # SumUAMDMS = 0
    # SumUAMDMSLR = 0
    # SumUAMDMN = 0
    # SumUAMDMNLR = 0
    # SumUAMDMP = 0
    # SumUAMDMPLR = 0
    # SumUAHDMA = 0
    # SumUAHDMS = 0
    # SumUAHDMSLR = 0
    # SumUAHDMN = 0
    # SumUAHDMNLR = 0
    # SumUAHDMP = 0
    # SumUAHDMPLR = 0
    # SumUALDRA = 0
    # SumUALDRS = 0
    # SumUALDRSLR = 0
    # SumUALDRN = 0
    # SumUALDRNLR = 0
    # SumUALDRP = 0
    # SumUALDRPLR = 0
    # SumUAMDRA = 0
    # SumUAMDRS = 0
    # SumUAMDRSLR = 0
    # SumUAMDRN = 0
    # SumUAMDRNLR = 0
    # SumUAMDRP = 0
    # SumUAMDRPLR = 0
    # SumUAHDRA = 0
    # SumUAHDRS = 0
    # SumUAHDRSLR = 0
    # SumUAHDRN = 0
    # SumUAHDRNLR = 0
    # SumUAHDRP = 0
    # SumUAHDRPLR = 0
    # SumUAWTRA = 0
    # SumUAFAN = 0
    # SumUAFAP = 0
    # SumUATDS = 0
    # SumUATDN = 0
    # SumUATDP = 0
    # SumUASBS = 0
    # SumUASBN = 0
    # SumUASBP = 0
    # SumUAGWN = 0
    # SumUAGWP = 0
    # SumUAPSN = 0
    # SumUAPSP = 0
    # SumUASSN = 0
    # SumUASSP = 0
    # SumNumUAs = 0
    # SumUABasinArea = 0

    # SumUAId = np.zeros(100)
    # SumUAMData = np.zeros(100)
    # SumUAArea = np.zeros(100)
    # AnnSumPointNitr = np.zeros(12)
    # AnnSumPointPhos = np.zeros(12)
    # AnnSumPrecipitation = np.zeros((50, 12))
    # AnnSumEvapotrans = np.zeros((50, 12))
    # AnnSumGroundWatLE = np.zeros((50, 12))
    # AnnSumRunoff = np.zeros((50, 12))
    # AnnSumStreamFlow = np.zeros((50, 12))
    # AnnSumPtSrcFlow = np.zeros((50, 12))
    # AnnSumTileDrain = np.zeros((50, 12))
    # AnnSumWithdrawal = np.zeros((50, 12))
    # AnnSumErosion = np.zeros((50, 12))
    # AnnSumStreamBankEros = np.zeros((50, 12))
    # AnnSumSedYield = np.zeros((50, 12))
    # AnnSumGroundNitr = np.zeros((50, 12))
    # AnnSumGroundPhos = np.zeros((50, 12))
    # AnnSumDisNitr = np.zeros((50, 12))
    # AnnSumTotNitr = np.zeros((50, 12))
    # AnnSumDisPhos = np.zeros((50, 12))
    # AnnSumTotPhos = np.zeros((50, 12))
    # AnnSumStreamBankN = np.zeros((50, 12))
    # AnnSumStreamBankP = np.zeros((50, 12))
    # AnnSumTileDrainN = np.zeros((50, 12))
    # AnnSumTileDrainP = np.zeros((50, 12))
    # AnnSumTileDrainSed = np.zeros((50, 12))
    # AnnSumAnimalN = np.zeros((50, 12))
    # AnnSumAnimalP = np.zeros((50, 12))
    # AnnSumAnimalFC = np.zeros((50, 12))
    # AnnSumWWOrgs = np.zeros((50, 12))
    # AnnSumSSOrgs = np.zeros((50, 12))
    # AnnSumUrbOrgs = np.zeros((50, 12))
    # AnnSumWildOrgs = np.zeros((50, 12))
    # AnnSumTotalOrgs = np.zeros((50, 12))
    # AnnSumCMStream = np.zeros((50, 12))
    # AnnSumOrgConc = np.zeros((50, 12))
    # AnnSumLuRunoff = np.zeros((50, 25))
    # AnnSumLuErosion = np.zeros((50, 25))
    # AnnSumLuSedYield = np.zeros((50, 25))
    # AnnSumLuDisNitr = np.zeros((50, 25))
    # AnnSumLuTotNitr = np.zeros((50, 25))
    # AnnSumLuDisPhos = np.zeros((50, 25))
    # AnnSumLuTotPhos = np.zeros((50, 25))
    # AnnSumSepticNitr = np.zeros(50)
    # AnnSumSepticPhos = np.zeros(50)
    # AnnSumTotAnimalN = np.zeros(50)
    # AnnSumTotAnimalP = np.zeros(50)
    # AnnSumTotTileDrainSed = np.zeros(50)
    # AnnSumTotTileDrainN = np.zeros(50)
    # AnnSumTotTileDrainP = np.zeros(50)
    # AnnSumTotGroundNitr = np.zeros(50)
    # AnnSumTotGroundPhos = np.zeros(50)
    # AnnSumAnnPointNitr = np.zeros(50)
    # AnnSumAnnPointPhos = np.zeros(50)
    # AnnSumTotStreamBankEros = np.zeros(50)
    # AnnSumTotStreamBankN = np.zeros(50)
    # AnnSumTotStreamBankP = np.zeros(50)

    ReadGwlfDataFile.ReadAllData()

    # ########################- BEGIN MAIN GWLF RUN CODE -########################
    # #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
    # #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
    # ############################################################################

    # CALCLULATE PRELIMINARY INITIALIZATIONS AND VALUES FOR
    # WATER BALANCE AND NUTRIENTS
    PrelimCalculations.InitialCalculations()

    # MODEL CALCULATIONS FOR EACH YEAR OF ANALYSIS - WATER BALANCE,
    # NUTRIENTS AND SEDIMENT LOADS

    # TODO: Placeholder declaration
    NYrs = 10

    for y in range(0, NYrs):
        # TODO: Placeholder declarations.
        MonthPondNitr = np.zeros(12)
        MonthPondPhos = np.zeros(12)
        MonthNormNitr = np.zeros(12)
        MonthShortNitr = np.zeros(12)
        MonthShortPhos = np.zeros(12)
        MonthDischargeNitr = np.zeros(12)
        MonthDischargePhos = np.zeros(12)

        # FOR EACH MONTH...
        for i in range(0, 12):

            # Initialize monthly septic system variables
            # TODO: We many not need to initialize these.
            # Consider removing once these variables are
            # populated with real data.
            MonthPondNitr[i] = 0
            MonthPondPhos[i] = 0
            MonthNormNitr[i] = 0
            MonthShortNitr[i] = 0
            MonthShortPhos[i] = 0
            MonthDischargeNitr[i] = 0
            MonthDischargePhos[i] = 0

            # LOOP THROUGH NUMBER OF LANDUSES IN THE BASIN TO GET QRUNOFF
            # TODO: Placeholder declarations.
            NLU = 16
            QRunoff = np.zeros((12, 12))
            AgQRunoff = np.zeros((12, 12))
            ErosWashoff = np.zeros((12, 12))
            RurQRunoff = np.zeros((12, 12))
            UrbQRunoff = np.zeros((12, 12))
            LuErosion = np.zeros((12, 12))

            for l in range(0, NLU):
                QRunoff[l, i] = 0
                AgQRunoff[l, i] = 0
                ErosWashoff[l, i] = 0
                RurQRunoff[l, i] = 0
                UrbQRunoff[l, i] = 0
                LuErosion[y, l] = 0

            # TODO: Placeholder declarations.
            DayYr = 0
            DaysMonth = np.ones((12, 12), np.int8)
            DaysYear = np.ones(365)
            Temp = np.ones((100, 100, 100))
            Prec = np.ones((100, 100, 100))
            PestTemp = np.ones((100, 100, 100))
            MeltPest = np.ones((100, 100, 100))
            PestPrec = np.ones((100, 100, 100))
            TotAreaMeters = 1

            # DAILY CALCULATIONS
            # TODO: J should start at 1, but I changed
            # it to 0 so that the code executes with fake
            # data. Otherwise range is 1 to 1.
            for j in range(0, DaysMonth[y, i]):
                # GET THE DAYS OF THE YEAR
                if (DayYr + 1) > DaysYear[y]:
                    DayYr = 0
                DayYr = DayYr + 1

                # DAILYWEATHERANALY TEMP[y, I, J], PREC[y, I, J]
                # ***** BEGIN WEATHER DATA ANALYSIS *****
                DailyTemp = Temp[y, i, j]
                DailyPrec = Prec[y, i, j]
                PestTemp[y, i, j] = Temp[y, i, j]
                PestPrec[y, i, j] = Prec[y, i, j]
                Melt = 0
                Rain = 0
                Water = 0
                # Erosiv = 0
                ET = 0
                QTotal = 0
                # AgQTotal = 0
                # RuralQTotal = 0
                # UrbanQTotal = 0
                MeltPest[y, i, j] = 0
                # ETDetentBasin = 0
                # BasinPrec = 0
                # CSOFract = 0

                # TODO: Placeholder declarations
                BasinArea = 100
                DayHrs = np.zeros(24)

                # For detention basins
                if BasinArea > 0:
                    # BasinPrec = 0.01 * DailyPrec * BasinArea
                    if DailyTemp > 0:
                        pass
                        # SatVap = 33.8639 * ((0.00738 * DailyTemp + 0.8072)**8 -
                        #                     0.000019 * (1.8 * DailyTemp + 48) +
                        #                    0.001316)
                        # Evap = (0.021 * DayHrs[i]**2 * SatVap) / (DailyTemp + 273)
                        # ETDetentBasin = 0.01 * Evap * BasinArea

                # TODO: Placeholder declarations
                ImpervAccum = np.zeros(100)
                PervAccum = np.zeros(100)

                for l in range(0, NLU):
                    ImpervAccum[l] = (ImpervAccum[l] * np.exp(-0.12) +
                                      (1 / 0.12) * (1 - np.exp(-0.12)))
                    PervAccum[l] = (PervAccum[l] * np.exp(-0.12) +
                                    (1 / 0.12) * (1 - np.exp(-0.12)))

                # RAIN , SNOWMELT, EVAPOTRANSPIRATION (ET)
                # TODO: Placeholder declarations
                InitSnow = 0
                DailyWater = np.zeros((100, 100, 100))
                # Acoef = np.zeros(100)

                if DailyTemp <= 0:
                    InitSnow = InitSnow + DailyPrec
                else:
                    Rain = DailyPrec
                    if InitSnow > 0.001:
                        # A DEGREE-DAY INITSNOW MELT, BUT NO MORE THAN EXISTED
                        # INITSNOW
                        Melt = 0.45 * DailyTemp
                        MeltPest[y, i, j] = Melt
                        if Melt > InitSnow:
                            Melt = InitSnow
                            MeltPest[y, i, j] = InitSnow
                        InitSnow = InitSnow - Melt
                    else:
                        MeltPest[y, i, j] = 0

                    # AVAILABLE WATER CALCULATION
                    Water = Rain + Melt
                    DailyWater[y, i, j] = Water

                    # Compute erosivity when erosion occurs, i.e., with rain and
                    # no InitSnow left
                    if Rain > 0 and InitSnow < 0.001:
                        pass
                        # Erosiv = 6.46 * Acoef[i] * Rain**1.81

                    # IF WATER AVAILABLE, THEN CALL SUB TO COMPUTE CN, RUNOFF,
                    # EROSION AND SEDIMENT
                    if Water > 0.01:
                        CalcCnErosRunoffSed.CalcCN()

                    # TODO: Placeholder declarations
                    DailyCN = np.zeros((100, 100, 100))
                    CNum = 0
                    AMC5 = 0
                    AntMoist = np.zeros(100)
                    DailyAMC5 = np.zeros((100, 100, 100))
                    ETFlag = 0
                    KV = np.zeros(100)
                    PcntET = np.zeros(100)
                    DailyET = np.zeros((100, 100, 100))

                    # DAILY CN
                    DailyCN[y, i, j] = CNum

                    # UPDATE ANTECEDENT RAIN+MELT CONDITION
                    AMC5 = AMC5 - AntMoist[5] + Water
                    DailyAMC5[y, i, j] = AMC5
                    for k in range(0, 4):
                        AntMoist[6 - k] = AntMoist[5 - k]
                    AntMoist[1] = Water

                    # CALCULATE ET FROM SATURATED VAPOR PRESSURE,
                    # HAMON (1961) METHOD
                    if ETFlag == 0:
                        if DailyTemp > 0:
                            SatVaPressure = (33.8639 * ((0.00738 * DailyTemp +
                                             0.8072)**8 - 0.000019 *
                                             np.absolute(1.8 * DailyTemp + 48) +
                                             0.001316))
                            PotenET = (0.021 * DayHrs[i]**2 * SatVaPressure
                                       / (DailyTemp + 273))
                            ET = KV[i] * PotenET * PcntET[i]

                    # Daily ET calculation
                    DailyET[y, i, j] = ET

                    # ***** END WEATHER DATA ANALYSIS *****

                    # ***** WATERSHED WATER BALANCE *****
                    # TODO: Placeholder declarations
                    RecessionCoef = 0
                    SatStor = 0
                    SeepCoef = 0
                    UnsatStor = 0
                    MaxWaterCap = 0
                    Perc = np.zeros((100, 100, 100))
                    PercCm = np.zeros((100, 100, 100))
                    DailyFlow = np.zeros((100, 100, 100))
                    DayRunoff = np.zeros((100, 100, 100))
                    DailyFlowGPM = np.zeros((100, 100, 100))
                    DailyGrFlow = np.zeros((100, 100, 100))
                    MonthFlow = np.zeros((100, 100))
                    Precipitation = np.zeros((100, 100))
                    Evapotrans = np.zeros((100, 100))
                    StreamFlow = np.zeros((100, 100))
                    GroundWatLE = np.zeros((100, 100))
                    NumPondSys = np.zeros(100)
                    NitrSepticLoad = 0
                    NitrPlantUptake = 0
                    Grow = np.zeros(100)
                    PhosSepticLoad = 0
                    PhosPlantUptake = 0
                    FrozenPondNitr = 0
                    FrozenPondPhos = 0

                    if QTotal <= Water:
                        Infiltration = Water - QTotal
                    GrFlow = RecessionCoef * SatStor
                    DeepSeep = SeepCoef * SatStor

                    # CALCULATE EVAPOTRANSPIRATION, Percolation, AND THE
                    # NEXT DAY'S UNSATURATED STORAGE AS LIMITED BY THE UNSATURATED
                    # ZONE MAXIMUM WATER CAPACITY

                    UnsatStor = UnsatStor + Infiltration

                    # Calculate water balance for non-Pesticide componenets
                    if ET >= UnsatStor:
                        ET = UnsatStor
                        UnsatStor = 0
                    else:
                        UnsatStor = UnsatStor - ET

                    # Obtain the Percolation, adjust precip and UnsatStor values
                    if UnsatStor > MaxWaterCap:
                        Percolation = UnsatStor - MaxWaterCap
                        Perc[y, i, j] = UnsatStor - MaxWaterCap
                        UnsatStor = UnsatStor - Percolation
                    else:
                        Percolation = 0
                        Perc[y, i, j] = 0
                    PercCm[y, i, j] = Percolation / 100

                    # CALCULATE STORAGE IN SATURATED ZONES AND GROUNDWATER
                    # DISCHARGE
                    SatStor = SatStor + Percolation - GrFlow - DeepSeep
                    if SatStor < 0:
                        SatStor = 0
                    Flow = QTotal + GrFlow
                    DailyFlow[y, i, j] = DayRunoff[y, i, j] + GrFlow

                    DailyFlowGPM[y, i, j] = Flow * 0.00183528 * TotAreaMeters
                    DailyGrFlow[y, i, j] = GrFlow  # (for daily load calculations)

                    # MONTHLY FLOW
                    MonthFlow[y, i] = MonthFlow[y, i] + DailyFlow[y, i, j]

                    # CALCULATE TOTALS
                    Precipitation[y, i] = Precipitation[y, i] + Prec[y, i, j]
                    Evapotrans[y, i] = Evapotrans[y, i] + ET
                    StreamFlow[y, i] = StreamFlow[y, i] + Flow
                    GroundWatLE[y, i] = GroundWatLE[y, i] + GrFlow

                    # CALCULATE DAILY NUTRIENT LOAD FROM PONDING SYSTEMS
                    PondNitrLoad = (NumPondSys[i] *
                                    (NitrSepticLoad - NitrPlantUptake * Grow[i]))
                    PondPhosLoad = (NumPondSys[i] *
                                    (PhosSepticLoad - PhosPlantUptake * Grow[i]))

                    # UPDATE MASS BALANCE ON PONDED EFFLUENT
                    if Temp[y, i, j] <= 0 or InitSnow > 0:

                        # ALL INPUTS GO TO FROZEN STORAGE
                        FrozenPondNitr = FrozenPondNitr + PondNitrLoad
                        FrozenPondPhos = FrozenPondPhos + PondPhosLoad

                        # NO NUTIENT OVERFLOW
                        NitrPondOverflow = 0
                        PhosPondOverflow = 0
                    else:
                        NitrPondOverflow = FrozenPondNitr + PondNitrLoad
                        PhosPondOverflow = FrozenPondPhos + PondPhosLoad
                        FrozenPondNitr = 0
                        FrozenPondPhos = 0

                    # Obtain the monthly Pond nutrients
                    MonthPondNitr[i] = MonthPondNitr[i] + NitrPondOverflow
                    MonthPondPhos[i] = MonthPondPhos[i] + PhosPondOverflow

                    # Obtain the monthly Normal Nitrogen
                    MonthNormNitr[i] = (MonthNormNitr[i] + NitrSepticLoad -
                                        NitrPlantUptake * Grow[i])

                    # 0.56 IS ATTENUATION FACTOR FOR SOIL LOSS
                    # 0.66 IS ATTENUATION FACTOR FOR SUBSURFACE FLOW LOSS
                    MonthShortNitr[i] = (MonthShortNitr[i] + NitrSepticLoad -
                                         NitrPlantUptake * Grow[i])
                    MonthShortPhos[i] = (MonthShortPhos[i] + PhosSepticLoad -
                                         PhosPlantUptake * Grow[i])
                    MonthDischargeNitr[i] = MonthDischargeNitr[i] + NitrSepticLoad
                    MonthDischargePhos[i] = MonthDischargePhos[i] + PhosSepticLoad

                    # TODO: Placeholder declarations
                    Withdrawal = np.zeros((100, 100))
                    StreamWithdrawal = np.zeros(100)
                    GroundWithdrawal = np.zeros(100)
                    TileDrainRO = np.zeros((100, 100))
                    PtSrcFlow = np.zeros((100, 100))
                    PointFlow = np.zeros(100)
                    AgRunoff = np.zeros((100, 100))
                    TileDrainDensity = 0
                    GwAgLE = np.zeros((100, 100))
                    AgAreaTotal = 0
                    AreaTotal = 1
                    TileDrainGW = np.zeros((100, 100))
                    TileDrain = np.zeros((100, 100))
                    Runoff = np.zeros((100, 100))

                    # CALCULATE WITHDRAWAL AND POINT SOURCE FLOW VALUES
                    Withdrawal[y, i] = (Withdrawal[y, i] + StreamWithdrawal[i] +
                                        GroundWithdrawal[i])
                    PtSrcFlow[y, i] = PtSrcFlow[y, i] + PointFlow[i]

                    # CALCULATE THE SURFACE RUNOFF PORTION OF TILE DRAINAGE
                    TileDrainRO[y, i] = (TileDrainRO[y, i] + [AgRunoff[y, i] *
                                         TileDrainDensity])

                    # CALCULATE SUBSURFACE PORTION OF TILE DRAINAGE
                    GwAgLE[y, i] = (GwAgLE[y, i] + (GroundWatLE[y, i] *
                                    (AgAreaTotal / AreaTotal)))
                    TileDrainGW[y, i] = (TileDrainGW[y, i] + [GwAgLE[y, i] *
                                         TileDrainDensity])

                    # ADD THE TWO COMPONENTS OF TILE DRAINAGE FLOW
                    TileDrain[y, i] = (TileDrain[y, i] + TileDrainRO[y, i] +
                                       TileDrainGW[y, i])

                    # ADJUST THE GROUNDWATER FLOW
                    GroundWatLE[y, i] = GroundWatLE[y, i] - TileDrainGW[y, i]
                    if GroundWatLE[y, i] < 0:
                        GroundWatLE[y, i] = 0

                    # ADJUST THE SURFACE RUNOFF
                    Runoff[y, i] = Runoff[y, i] - TileDrainRO[y, i]

                    if Runoff[y, i] < 0:
                        Runoff[y, i] = 0

                    # CALCULATE ANIMAL FEEDING OPERATIONS OUTPUT
                    AFOS.AnimalOperations()

                    # CALCULATE NUTRIENT AND SEDIMENT LOADS
                    CalcLoads.CalculateLoads()

                    # CALCULATE STREAM BANK EROSION
                    StreamBank.CalculateStreamBankEros()

                    # CALCULATE FINAL ANNUAL MEAN LOADS
                    AnnualMeans.CalculateAnnualMeanLoads()

            # CALCULATE FINAL MONTHLY AND ANNUAL WATER BALANCE FOR
            # AVERAGE STREAM FLOW
            # TODO: Placeholder declarations
            AvStreamFlow = np.zeros(100)
            AvRunoff = np.zeros(100)
            AvGroundWater = np.zeros(100)
            AvPtSrcFlow = np.zeros(100)
            AvTileDrain = np.zeros(100)
            AvCMStream = np.zeros(100)
            AvOrgConc = np.zeros(100)
            AvTotalOrgs = np.zeros(100)
            AvWithdrawal = np.zeros(100)

            for i in range(0, 12):
                AvStreamFlow[i] = (AvRunoff[i] + AvGroundWater[i] +
                                   AvPtSrcFlow[i] + AvTileDrain[i] -
                                   AvWithdrawal[i])

                AvCMStream[i] = (AvStreamFlow[i] / 100) * TotAreaMeters
                if AvCMStream[i] > 0:
                    AvOrgConc[i] = (AvTotalOrgs[i] / (AvCMStream[i] * 1000)) / 10
                else:
                    AvOrgConc[i] = 0
            AvOrgConc[0] = 0

    # ##########################- END MAIN GWLF RUN CODE -########################
    # #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
    # #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
    # ############################################################################

    print("Model run complete for " + str(NYrs) + " years of data.")

    WriteOutputFiles.WriteOutput()
    WriteOutputFiles.WriteOutputSumFiles()

    print('Done')
