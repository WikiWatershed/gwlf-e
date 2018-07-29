from numpy import zeros

from gwlfe.Output.Loading.StreamBankN import StreamBankN
from gwlfe.Output.Loading.StreamBankN import StreamBankN_f


def NURBBANK(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area,
             CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN,
             UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
             RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse,
             TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
             NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF,
             AvSlope, SedAAdjust, StreamLength, n42b, UrbBankStab, SedNitr, BankNFrac, n69c):
    result = zeros((NYrs, 12))
    streambank_n = StreamBankN(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area,
                               CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN,
                               UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                               RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse,
                               TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
                               NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF,
                               AvSlope, SedAAdjust, StreamLength, SedNitr, BankNFrac)
    for Y in range(NYrs):
        for i in range(12):
            if n42b > 0:
                result[Y][i] = (UrbBankStab / n42b) * streambank_n[Y][i] * n69c
    return result


def NURBBANK_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area,
               CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN,
               UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
               RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse,
               TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
               NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF,
               AvSlope, SedAAdjust, StreamLength, n42b, UrbBankStab, SedNitr, BankNFrac, n69c):
    if n42b > 0:
        return (UrbBankStab / n42b) * StreamBankN_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area,
                                                    CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN,
                                                    UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                                                    RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse,
                                                    TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
                                                    NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF,
                                                    AvSlope, SedAAdjust, StreamLength, SedNitr, BankNFrac) * n69c
    else:
        return zeros((NYrs, 12))
