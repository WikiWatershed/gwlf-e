from numpy import sum as npsum
from numpy import zeros

from gwlfe.Output.Loading.StreamBankN_1 import StreamBankN_1
from gwlfe.Output.Loading.StreamBankN_1 import StreamBankN_1_f


def AvStreamBankNSum(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                     ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef,
                     Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow, StreamWithdrawal,
                     GroundWithdrawal, NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF, AvSlope,
                     SedAAdjust, StreamLength, n42b, n46c, n85d, AgLength, n42, n54, n85, UrbBankStab, SedNitr,
                     BankNFrac, n69c, n45, n69):
    AvStreamBankN = zeros(12)
    for Y in range(NYrs):
        for i in range(12):
            AvStreamBankN[i] += \
                StreamBankN_1(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area,
                              CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN,
                              UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                              RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse,
                              TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
                              NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF,
                              AvSlope, SedAAdjust, StreamLength, n42b, AgLength,
                              UrbBankStab, SedNitr, BankNFrac, n69c, n45, n69, n46c, n42)[Y][i] / NYrs
    return sum(AvStreamBankN)


def AvStreamBankNSum_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                       Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef,
                       SeepCoef, Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow, StreamWithdrawal,
                       GroundWithdrawal, NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF, AvSlope,
                       SedAAdjust, StreamLength, n42b, n46c, n85d, AgLength, n42, n54, n85, UrbBankStab, SedNitr,
                       BankNFrac, n69c, n45, n69):
    return npsum(StreamBankN_1_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                                 CNP_0, Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                                 RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity,
                                 PointFlow, StreamWithdrawal, GroundWithdrawal, NumAnimals, AvgAnimalWt,
                                 StreamFlowVolAdj,
                                 SedAFactor_0, AvKF, AvSlope, SedAAdjust, StreamLength, n42b, AgLength,
                                 UrbBankStab, SedNitr, BankNFrac, n69c, n45, n69, n46c, n42)) / NYrs
