from numpy import zeros

from gwlfe.Output.Loading.StreamBankN import StreamBankN
from gwlfe.Output.Loading.StreamBankN import StreamBankN_f


def NSTAB(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area,
          CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN,
          UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
          RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse,
          TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
          NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF,
          AvSlope, SedAAdjust, StreamLength, n42b, n46c, SedNitr, BankNFrac, n69c):
    result = zeros((NYrs, 12))
    streabank_n = StreamBankN(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area,
                              CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN,
                              UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                              RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse,
                              TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
                              NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF,
                              AvSlope, SedAAdjust, StreamLength, SedNitr, BankNFrac)

    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = 0
            if n42b > 0:
                result[Y][i] = (n46c / n42b) * streabank_n[Y][i] * n69c
    return result


def NSTAB_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area,
            CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN,
            UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
            RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse,
            TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
            NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF,
            AvSlope, SedAAdjust, StreamLength, n42b, n46c, SedNitr, BankNFrac, n69c):
    if n42b > 0:
        return (n46c / n42b) * StreamBankN_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area,
                                             CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN,
                                             UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                                             RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse,
                                             TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
                                             NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF,
                                             AvSlope, SedAAdjust, StreamLength, SedNitr, BankNFrac) * n69c
    else:
        return zeros((NYrs, 12))
