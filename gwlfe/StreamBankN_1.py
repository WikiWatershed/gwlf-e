import numpy as np
# from Timer import time_function
from Memoization import memoize
from StreamBankN import StreamBankN
from StreamBankN import StreamBankN_2
from NSTAB import NSTAB
from NSTAB import NSTAB_2
from NFEN import NFEN
from NFEN import NFEN_2
from NURBBANK import NURBBANK
from NURBBANK import NURBBANK_2


@memoize
def StreamBankN_1(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area,
                    CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN,
                    UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                    RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse,
                    TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
                    NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF,
                    AvSlope, SedAAdjust, StreamLength, n42b, AgLength,
                    UrbBankStab, SedNitr, BankNFrac, n69c, n45, n69, n46c, n42):
    result = np.zeros((NYrs, 12))
    streambank_n = StreamBankN(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area,
                               CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN,
                               UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                               RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse,
                               TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
                               NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF,
                               AvSlope, SedAAdjust, StreamLength, SedNitr, BankNFrac)
    nstab = NSTAB(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area,
          CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN,
          UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
          RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse,
          TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
          NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF,
          AvSlope, SedAAdjust, StreamLength, n42b, n46c, SedNitr, BankNFrac, n69c)

    nfen = NFEN(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area,
         CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN,
         UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
         RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse,
         TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
         NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF,
         AvSlope, SedAAdjust, StreamLength, AgLength,
         n42, SedNitr, BankNFrac, n45, n69)

    nurbbank = NURBBANK(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area,
             CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN,
             UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
             RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse,
             TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
             NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF,
             AvSlope, SedAAdjust, StreamLength, n42b, UrbBankStab, SedNitr, BankNFrac, n69c)
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = streambank_n[Y][i] - (nstab[Y][i] + nfen[Y][i] + nurbbank[Y][i])
            if result[Y][i] < 0:
                result[Y][i] = 0
    return result

@memoize
def StreamBankN_1_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area,
                    CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN,
                    UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                    RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse,
                    TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
                    NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF,
                    AvSlope, SedAAdjust, StreamLength, n42b, AgLength,
                    UrbBankStab, SedNitr, BankNFrac, n69c, n45, n69, n46c, n42):
    streambank_n = StreamBankN_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area,
                                 CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN,
                                 UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                                 RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse,
                                 TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
                                 NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF,
                                 AvSlope, SedAAdjust, StreamLength, SedNitr, BankNFrac)
    nstab = NSTAB_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area,
            CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN,
            UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
            RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse,
            TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
            NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF,
            AvSlope, SedAAdjust, StreamLength, n42b, n46c, SedNitr, BankNFrac, n69c)

    nfen = NFEN_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area,
           CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN,
           UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
           RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse,
           TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
           NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF,
           AvSlope, SedAAdjust, StreamLength, AgLength,
           n42, SedNitr, BankNFrac, n45, n69)

    nurbbank = NURBBANK_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area,
               CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN,
               UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
               RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse,
               TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
               NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF,
               AvSlope, SedAAdjust, StreamLength, n42b, UrbBankStab, SedNitr, BankNFrac, n69c)

    return np.maximum(streambank_n - (nstab + nfen + nurbbank), 0)
