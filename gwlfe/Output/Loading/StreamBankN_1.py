from numpy import maximum
from numpy import zeros

from gwlfe.BMPs.AgAnimal.NFEN import NFEN
from gwlfe.BMPs.AgAnimal.NFEN import NFEN_f
from gwlfe.BMPs.Stream.NSTAB import NSTAB
from gwlfe.BMPs.Stream.NSTAB import NSTAB_f
from gwlfe.BMPs.Stream.NURBBANK import NURBBANK
from gwlfe.BMPs.Stream.NURBBANK import NURBBANK_f
from gwlfe.Memoization import memoize
from gwlfe.Output.Loading.StreamBankN import StreamBankN
from gwlfe.Output.Loading.StreamBankN import StreamBankN_f


@memoize
def StreamBankN_1(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area,
                  CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN,
                  UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                  RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse,
                  TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
                  NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF,
                  AvSlope, SedAAdjust, StreamLength, n42b, AgLength,
                  UrbBankStab, SedNitr, BankNFrac, n69c, n45, n69, n46c, n42):
    result = zeros((NYrs, 12))
    streambank_n = StreamBankN(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area,
                               CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN,
                               UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                               RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse,
                               TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
                               NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF,
                               AvSlope, SedAAdjust, StreamLength, SedNitr, BankNFrac)
    nstab = NSTAB(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area,
                  CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN,
                  UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                  RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse,
                  TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
                  NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF,
                  AvSlope, SedAAdjust, StreamLength, n42b, n46c, SedNitr, BankNFrac, n69c)

    nfen = NFEN(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area,
                CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN,
                UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse,
                TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
                NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF,
                AvSlope, SedAAdjust, StreamLength, AgLength,
                n42, SedNitr, BankNFrac, n45, n69)

    nurbbank = NURBBANK(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area,
                        CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN,
                        UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                        RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse,
                        TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
                        NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF,
                        AvSlope, SedAAdjust, StreamLength, n42b, UrbBankStab, SedNitr, BankNFrac, n69c)
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = streambank_n[Y][i] - (nstab[Y][i] + nfen[Y][i] + nurbbank[Y][i])
            if result[Y][i] < 0:
                result[Y][i] = 0
    return result


@memoize
def StreamBankN_1_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area,
                    CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN,
                    UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                    RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse,
                    TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
                    NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF,
                    AvSlope, SedAAdjust, StreamLength, n42b, AgLength,
                    UrbBankStab, SedNitr, BankNFrac, n69c, n45, n69, n46c, n42):
    streambank_n = StreamBankN_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area,
                                 CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN,
                                 UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                                 RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse,
                                 TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
                                 NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF,
                                 AvSlope, SedAAdjust, StreamLength, SedNitr, BankNFrac)
    nstab = NSTAB_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area,
                    CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN,
                    UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                    RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse,
                    TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
                    NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF,
                    AvSlope, SedAAdjust, StreamLength, n42b, n46c, SedNitr, BankNFrac, n69c)

    nfen = NFEN_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area,
                  CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN,
                  UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                  RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse,
                  TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
                  NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF,
                  AvSlope, SedAAdjust, StreamLength, AgLength,
                  n42, SedNitr, BankNFrac, n45, n69)

    nurbbank = NURBBANK_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area,
                          CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN,
                          UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                          RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse,
                          TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
                          NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF,
                          AvSlope, SedAAdjust, StreamLength, n42b, UrbBankStab, SedNitr, BankNFrac, n69c)

    return maximum(streambank_n - (nstab + nfen + nurbbank), 0)
