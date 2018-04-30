import numpy as np
from Timer import time_function
from Memoization import memoize
from StreamBankEros_2 import StreamBankEros_2
from SedYield import SedYield


@memoize
def SedYield_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                        Grow, CNP_0, Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                        RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow,
                        StreamWithdrawal, GroundWithdrawal, NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0,
                        AvKF, AvSlope, SedAAdjust, StreamLength, n42b, n46c, n85d, AgLength, n42, n45, n85, UrbBankStab,
                        Acoef, KF, LS, C, P, SedDelivRatio_0):
    result = np.zeros((NYrs, 12))
    sedyield = SedYield(NYrs, DaysMonth, Temp, InitSnow_0, Prec, Acoef, NRur, KF, LS, C, P, Area, NUrb, CNI_0, AntMoist_0, Grow,
             ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN, CNP_0, Imper, SedDelivRatio_0)
    streambankeros_2 = StreamBankEros_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                        Grow, CNP_0, Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                        RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow,
                        StreamWithdrawal, GroundWithdrawal, NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0,
                        AvKF, AvSlope, SedAAdjust, StreamLength, n42b, n46c, n85d, AgLength, n42, n45, n85, UrbBankStab)
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = sedyield[Y][i] + streambankeros_2[Y][i] / 1000
    return result


def SedYield_2_2():
    pass
