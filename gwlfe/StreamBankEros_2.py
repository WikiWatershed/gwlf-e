import numpy as np
from Timer import time_function
from StreamBankEros import StreamBankEros
from SEDSTAB import SEDSTAB
from SEDFEN import SEDFEN
from SURBBANK import SURBBANK
from Memoization import memoize


@memoize
def StreamBankEros_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
                     ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef,
                     Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow, StreamWithdrawal,
                     GroundWithdrawal, NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF, AvSlope,
                     SedAAdjust, StreamLength, n42b, n46c, n85d, AgLength, n42, n45, n85, UrbBankStab):
    result = np.zeros((NYrs, 12))
    streambankeros = StreamBankEros(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow,
                                    CNP_0, Imper,
                                    ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                                    RecessionCoef, SeepCoef
                                    , Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow,
                                    StreamWithdrawal, GroundWithdrawal
                                    , NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF, AvSlope,
                                    SedAAdjust, StreamLength)
    sedstab = SEDSTAB(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow,
                      CNP_0, Imper,
                      ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                      RecessionCoef, SeepCoef
                      , Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow,
                      StreamWithdrawal, GroundWithdrawal
                      , NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF, AvSlope,
                      SedAAdjust, StreamLength, n42b, n46c, n85d)
    sedfen = SEDFEN(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow,
                    CNP_0, Imper,
                    ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                    RecessionCoef, SeepCoef
                    , Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow,
                    StreamWithdrawal, GroundWithdrawal
                    , NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF, AvSlope,
                    SedAAdjust, StreamLength, AgLength, n42, n45, n85)
    surbbank = SURBBANK(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0,
                        Imper,
                        ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef
                        , Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow, StreamWithdrawal,
                        GroundWithdrawal
                        , NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF, AvSlope, SedAAdjust,
                        StreamLength
                        , UrbBankStab, n42b, n85d)
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = streambankeros[Y][i] - (sedstab[Y][i] + sedfen[Y][i] + surbbank[Y][i])
            if result[Y][i] < 0:
                result[Y][i] = 0
    return result


def StreamBankEros_2_2():
    pass
