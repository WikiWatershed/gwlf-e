from numpy import zeros

from gwlfe.Input.LandUse.Ag.AGSTRM import AGSTRM
from gwlfe.Input.LandUse.Ag.AGSTRM import AGSTRM_f
from gwlfe.Output.Loading.StreamBankN import StreamBankN
from gwlfe.Output.Loading.StreamBankN import StreamBankN_f


def NFEN(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area,
         CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN,
         UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
         RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse,
         TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
         NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF,
         AvSlope, SedAAdjust, StreamLength, AgLength,
         n42, SedNitr, BankNFrac, n45, n69):
    result = zeros((NYrs, 12))
    streambank_n = StreamBankN(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area,
                               CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN,
                               UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                               RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse,
                               TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
                               NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF,
                               AvSlope, SedAAdjust, StreamLength, SedNitr, BankNFrac)

    agstrm = AGSTRM(AgLength, StreamLength)
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = 0
            if n42 > 0:
                result[Y][i] = (n45 / n42) * streambank_n[Y][i] * agstrm * n69
    return result


def NFEN_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area,
           CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN,
           UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
           RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse,
           TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
           NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF,
           AvSlope, SedAAdjust, StreamLength, AgLength,
           n42, SedNitr, BankNFrac, n45, n69):
    if n42 > 0:
        agstrm = AGSTRM_f(AgLength, StreamLength)
        streambank_n = StreamBankN_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area,
                                     CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN,
                                     UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                                     RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse,
                                     TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
                                     NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF,
                                     AvSlope, SedAAdjust, StreamLength, SedNitr, BankNFrac)
        return (n45 / n42) * streambank_n * agstrm * n69
    else:
        return zeros((NYrs, 12))
