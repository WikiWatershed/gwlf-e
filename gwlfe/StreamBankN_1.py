import numpy as np
from Timer import time_function
from Memoization import memoize
from StreamBankN import StreamBankN
from NSTAB import NSTAB
from NFEN import NFEN
from NURBBANK import NURBBANK


@memoize
def StreamBankN_1(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area,
                  CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN,
                  UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                  RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse,
                  TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
                  NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF,
                  AvSlope, SedAAdjust, StreamLength, n42b, n46c, n85d, AgLength,
                  n42, n54, n85, UrbBankStab, SedNitr, BankNFrac, n69c, n45, n69):
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
                  AvSlope, SedAAdjust, StreamLength, n42b, n46c, n85d, AgLength,
                  n42, n54, n85, UrbBankStab, SedNitr, BankNFrac, n69c)

    nfen = NFEN(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area,
                CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN,
                UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse,
                TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
                NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF,
                AvSlope, SedAAdjust, StreamLength, n42b, n46c, n85d, AgLength,
                n42, n54, n85, UrbBankStab, SedNitr, BankNFrac, n45, n69)

    nurbbank = NURBBANK(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area,
                        CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN,
                        UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                        RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse,
                        TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
                        NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF,
                        AvSlope, SedAAdjust, StreamLength, n42b, n46c, n85d, AgLength,
                        n42, n54, n85, UrbBankStab, SedNitr, BankNFrac, n69c)
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = streambank_n[Y][i] - (nstab[Y][i] + nfen[Y][i] + nurbbank[Y][i])
            if result[Y][i] < 0:
                result[Y][i] = 0
    return result


def StreamBankN_1_2():
    pass
