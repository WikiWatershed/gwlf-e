from numpy import zeros

from gwlfe.Input.LandUse.Ag.AGSTRM import AGSTRM
from gwlfe.Input.LandUse.Ag.AGSTRM import AGSTRM_f
from gwlfe.Output.Loading.StreamBankEros import StreamBankEros
from gwlfe.Output.Loading.StreamBankEros import StreamBankEros_f


def SEDFEN(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
           CNP_0, Imper,
           ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
           RecessionCoef, SeepCoef
           , Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow,
           StreamWithdrawal, GroundWithdrawal
           , NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF, AvSlope,
           SedAAdjust, StreamLength, AgLength, n42, n45, n85):
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
    agstrm = AGSTRM(AgLength, StreamLength)
    for Y in range(NYrs):
        for i in range(12):
            if n42 > 0:
                result[Y][i] = (n45 / n42) * streambankeros[Y][i] * agstrm * n85
    return result


def SEDFEN_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
             CNP_0, Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
             RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow,
             StreamWithdrawal, GroundWithdrawal, NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF, AvSlope,
             SedAAdjust, StreamLength, AgLength, n42, n45, n85):
    streambankeros = StreamBankEros_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                                      Grow_0,
                                      CNP_0, Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap,
                                      SatStor_0, RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse,
                                      TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal, NumAnimals,
                                      AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF, AvSlope, SedAAdjust,
                                      StreamLength)
    agstrm = AGSTRM_f(AgLength, StreamLength)
    if n42 > 0:
        return (n45 / n42) * streambankeros * agstrm * n85
    else:
        return zeros((NYrs, 12))
