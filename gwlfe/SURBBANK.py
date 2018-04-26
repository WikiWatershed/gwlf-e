import numpy as np
from Timer import time_function
from StreamBankEros import StreamBankEros


def SURBBANK(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
           ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef
                ,Qretention, PctAreaInfil, n25b,Landuse,TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal
                ,NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF, AvSlope, SedAAdjust, StreamLength
                , UrbBankStab, n42b, n85d):
    result = np.zeros((NYrs, 12))
    streambankeros = StreamBankEros(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
           ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef
               ,Qretention, PctAreaInfil, n25b,Landuse,TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal
               ,NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF, AvSlope, SedAAdjust, StreamLength)
    for Y in range(NYrs):
        for i in range(12):
            if n42b > 0:
                result[Y][i] = (UrbBankStab / n42b) * streambankeros[Y][i] * n85d
    return result


def SURBBANK_2():
    pass
