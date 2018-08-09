from numpy import zeros

from gwlfe.Memoization import memoize
from gwlfe.Output.Loading.SedYield import SedYield
from gwlfe.Output.Loading.SedYield import SedYield_f
from gwlfe.Output.Loading.StreamBankEros_1 import StreamBankEros_1
from gwlfe.Output.Loading.StreamBankEros_1 import StreamBankEros_1_f


@memoize
def SedYield_1(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
               Grow_0, CNP_0, Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
               RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow,
               StreamWithdrawal, GroundWithdrawal, NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0,
               AvKF, AvSlope, SedAAdjust, StreamLength, n42b, n46c, n85d, AgLength, n42, n45, n85, UrbBankStab,
               Acoef, KF, LS, C, P, SedDelivRatio_0):
    result = zeros((NYrs, 12))
    sedyield = SedYield(NYrs, DaysMonth, Temp, InitSnow_0, Prec, Acoef, NRur, KF, LS, C, P, Area, NUrb, CNI_0,
                        AntMoist_0, Grow_0,
                        ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN, CNP_0, Imper, SedDelivRatio_0)
    streambankeros_f = StreamBankEros_1(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                                        Grow_0, CNP_0, Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs,
                                        MaxWaterCap, SatStor_0,
                                        RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse,
                                        TileDrainDensity, PointFlow,
                                        StreamWithdrawal, GroundWithdrawal, NumAnimals, AvgAnimalWt, StreamFlowVolAdj,
                                        SedAFactor_0,
                                        AvKF, AvSlope, SedAAdjust, StreamLength, n42b, n46c, n85d, AgLength, n42, n45,
                                        n85, UrbBankStab)
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = sedyield[Y][i] + streambankeros_f[Y][i] / 1000
    return result


@memoize
def SedYield_1_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                 Grow_0, CNP_0, Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                 RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow,
                 StreamWithdrawal, GroundWithdrawal, NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0,
                 AvKF, AvSlope, SedAAdjust, StreamLength, n42b, n46c, n85d, AgLength, n42, n45, n85, UrbBankStab,
                 Acoef, KF, LS, C, P, SedDelivRatio_0):
    return SedYield_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, Acoef, NRur, KF, LS, C, P, Area, NUrb, CNI_0, AntMoist_0,
                      Grow_0, ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN, CNP_0, Imper,
                      SedDelivRatio_0) + StreamBankEros_1_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area,
                                                            CNI_0, AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN,
                                                            UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                                                            RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b,
                                                            Landuse, TileDrainDensity, PointFlow, StreamWithdrawal,
                                                            GroundWithdrawal, NumAnimals, AvgAnimalWt, StreamFlowVolAdj,
                                                            SedAFactor_0, AvKF, AvSlope, SedAAdjust, StreamLength, n42b,
                                                            n46c, n85d, AgLength, n42, n45, n85, UrbBankStab) / 1000
