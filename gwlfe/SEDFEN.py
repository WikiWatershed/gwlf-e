import numpy as np
from Timer import time_function
from StreamBankEros import StreamBankEros
from AGSTRM import AGSTRM
from Memoization import memoize


@memoize
def SEDFEN(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow,
           CNP_0, Imper,
           ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
           RecessionCoef, SeepCoef
           , Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow,
           StreamWithdrawal, GroundWithdrawal
           , NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF, AvSlope,
           SedAAdjust, StreamLength, AgLength, n42, n45, n85):
    result = np.zeros((NYrs, 12))
    streambankeros = StreamBankEros(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow,
                                    CNP_0, Imper,
                                    ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                                    RecessionCoef, SeepCoef
                                    , Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow,
                                    StreamWithdrawal, GroundWithdrawal
                                    , NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF, AvSlope,
                                    SedAAdjust, StreamLength)
    agstrm = AGSTRM(AgLength, StreamLength)
    for Y in range(NYrs):
        for i in range(12):
            if n42 > 0:
                result[Y][i] = (n45 / n42) * streambankeros[Y][i] * agstrm * n85
    return result


def SEDFEN_2():
    pass
