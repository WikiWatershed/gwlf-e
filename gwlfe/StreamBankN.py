import numpy as np
# from Timer import time_function
from Memoization import memoize
from StreamBankEros import StreamBankEros
from StreamBankEros import StreamBankEros_2

@memoize
def StreamBankN(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area,
                CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN,
                UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse,
                TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
                NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF,
                AvSlope, SedAAdjust, StreamLength,SedNitr, BankNFrac):
    result = np.zeros((NYrs, 12))
    stream_bank_eros_2 = StreamBankEros(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area,
                                          CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN,
                                          UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                                          RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse,
                                          TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
                                          NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF,
                                          AvSlope, SedAAdjust, StreamLength)
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = stream_bank_eros_2[Y][i] * (SedNitr / 1000000) * BankNFrac
    return result

def StreamBankN_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area,
                CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN,
                UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse,
                TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
                NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF,
                AvSlope, SedAAdjust, StreamLength,SedNitr, BankNFrac):
    return StreamBankEros_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area,
                                        CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN,
                                        UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                                        RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse,
                                        TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
                                        NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF,
                                        AvSlope, SedAAdjust, StreamLength) * (SedNitr / 1000000) * BankNFrac
