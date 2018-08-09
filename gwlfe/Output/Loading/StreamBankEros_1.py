from numpy import maximum
from numpy import zeros

from gwlfe.BMPs.Stream.SEDFEN import SEDFEN
from gwlfe.BMPs.Stream.SEDFEN import SEDFEN_f
from gwlfe.BMPs.Stream.SEDSTAB import SEDSTAB
from gwlfe.BMPs.Stream.SEDSTAB import SEDSTAB_f
from gwlfe.BMPs.Stream.SURBBANK import SURBBANK
from gwlfe.BMPs.Stream.SURBBANK import SURBBANK_f
from gwlfe.Memoization import memoize
from gwlfe.Output.Loading.StreamBankEros import StreamBankEros
from gwlfe.Output.Loading.StreamBankEros import StreamBankEros_f as StreamBankEros_f_actual


@memoize
def StreamBankEros_1(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                     ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef,
                     Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow, StreamWithdrawal,
                     GroundWithdrawal, NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF, AvSlope,
                     SedAAdjust, StreamLength, n42b, n46c, n85d, AgLength, n42, n45, n85, UrbBankStab):
    result = zeros((NYrs, 12))
    streambankeros = StreamBankEros(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                                    Grow_0,
                                    CNP_0, Imper,
                                    ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                                    RecessionCoef, SeepCoef
                                    , Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow,
                                    StreamWithdrawal, GroundWithdrawal
                                    , NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF, AvSlope,
                                    SedAAdjust, StreamLength)
    sedstab = SEDSTAB(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                      CNP_0, Imper,
                      ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                      RecessionCoef, SeepCoef
                      , Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow,
                      StreamWithdrawal, GroundWithdrawal
                      , NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF, AvSlope,
                      SedAAdjust, StreamLength, n42b, n46c, n85d)
    sedfen = SEDFEN(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                    CNP_0, Imper,
                    ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                    RecessionCoef, SeepCoef
                    , Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow,
                    StreamWithdrawal, GroundWithdrawal
                    , NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF, AvSlope,
                    SedAAdjust, StreamLength, AgLength, n42, n45, n85)
    surbbank = SURBBANK(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
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


@memoize
def StreamBankEros_1_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                       Imper,
                       ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef,
                       Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow, StreamWithdrawal,
                       GroundWithdrawal, NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF, AvSlope,
                       SedAAdjust, StreamLength, n42b, n46c, n85d, AgLength, n42, n45, n85, UrbBankStab):
    streambankeros = StreamBankEros_f_actual(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0,
                                             AntMoist_0, Grow_0,
                                             CNP_0, Imper,
                                             ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                                             RecessionCoef, SeepCoef
                                             , Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow,
                                             StreamWithdrawal, GroundWithdrawal
                                             , NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF, AvSlope,
                                             SedAAdjust, StreamLength)

    sedstab = SEDSTAB_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                        CNP_0, Imper,
                        ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                        RecessionCoef, SeepCoef
                        , Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow,
                        StreamWithdrawal, GroundWithdrawal
                        , NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF, AvSlope,
                        SedAAdjust, StreamLength, n42b, n46c, n85d)
    sedfen = SEDFEN_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                      CNP_0, Imper,
                      ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                      RecessionCoef, SeepCoef
                      , Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow,
                      StreamWithdrawal, GroundWithdrawal
                      , NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF, AvSlope,
                      SedAAdjust, StreamLength, AgLength, n42, n45, n85)
    surbbank = SURBBANK_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                          Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef,
                          SeepCoef, Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow,
                          StreamWithdrawal, GroundWithdrawal, NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0,
                          AvKF, AvSlope, SedAAdjust, StreamLength, UrbBankStab, n42b, n85d)
    return maximum(streambankeros - (sedstab + sedfen + surbbank), 0)
