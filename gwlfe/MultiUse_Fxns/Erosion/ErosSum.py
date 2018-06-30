from numpy import sum
from numpy import zeros

from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.Erosion.Erosion_1 import Erosion_1
from gwlfe.MultiUse_Fxns.Erosion.Erosion_1 import Erosion_1_f


@memoize
def ErosSum(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0,
            AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET,
            DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef, Qretention, PctAreaInfil,
            n25b, Landuse, TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
            NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF, AvSlope, SedAAdjust,
            StreamLength, n42b, n46c, n85d, AgLength, n42, n45, n85, UrbBankStab,
            SedDelivRatio_0, Acoef, KF, LS, C, P):
    result = zeros((NYrs,))
    for Y in range(NYrs):
        result[Y] = 0
        for i in range(12):
            result[Y] += Erosion_1(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0,
                                   AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET,
                                   DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef, Qretention, PctAreaInfil,
                                   n25b, Landuse, TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
                                   NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF, AvSlope, SedAAdjust,
                                   StreamLength, n42b, n46c, n85d, AgLength, n42, n45, n85, UrbBankStab,
                                   SedDelivRatio_0, Acoef, KF, LS, C, P)[Y][i]

    return result


@memoize
def ErosSum_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0,
              AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET,
              DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef, Qretention, PctAreaInfil,
              n25b, Landuse, TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
              NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF, AvSlope, SedAAdjust,
              StreamLength, n42b, n46c, n85d, AgLength, n42, n45, n85, UrbBankStab,
              SedDelivRatio_0, Acoef, KF, LS, C, P):
    return sum(Erosion_1_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0,
                           AntMoist_0, Grow_0, CNP_0, Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET,
                           DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef, Qretention, PctAreaInfil,
                           n25b, Landuse, TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal,
                           NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF, AvSlope, SedAAdjust,
                           StreamLength, n42b, n46c, n85d, AgLength, n42, n45, n85, UrbBankStab,
                           SedDelivRatio_0, Acoef, KF, LS, C, P), axis=1)
