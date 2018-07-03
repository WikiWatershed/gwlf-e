from numpy import sum
from numpy import zeros

from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.Erosion.Erosion_1 import Erosion_1
from gwlfe.MultiUse_Fxns.Erosion.Erosion_1 import Erosion_1_f


def AvErosion(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
              Grow_0, CNP_0, Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
              RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow,
              StreamWithdrawal, GroundWithdrawal, NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0,
              AvKF, AvSlope, SedAAdjust, StreamLength, n42b, n46c, n85d, AgLength, n42, n45, n85, UrbBankStab,
              SedDelivRatio_0, Acoef, KF, LS, C, P):
    result = zeros(12)
    erosion = Erosion_1(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                        Grow_0, CNP_0, Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                        RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow,
                        StreamWithdrawal, GroundWithdrawal, NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0,
                        AvKF, AvSlope, SedAAdjust, StreamLength, n42b, n46c, n85d, AgLength, n42, n45, n85, UrbBankStab,
                        SedDelivRatio_0, Acoef, KF, LS, C, P)
    for Y in range(NYrs):
        for i in range(12):
            result[i] += erosion[Y][i] / NYrs
    return result


@memoize
def AvErosion_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                Grow_0, CNP_0, Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow,
                StreamWithdrawal, GroundWithdrawal, NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0,
                AvKF, AvSlope, SedAAdjust, StreamLength, n42b, n46c, n85d, AgLength, n42, n45, n85, UrbBankStab,
                SedDelivRatio_0, Acoef, KF, LS, C, P):
    return sum(Erosion_1_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                           Grow_0, CNP_0, Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap,
                           SatStor_0,
                           RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity,
                           PointFlow,
                           StreamWithdrawal, GroundWithdrawal, NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0,
                           AvKF, AvSlope, SedAAdjust, StreamLength, n42b, n46c, n85d, AgLength, n42, n45, n85,
                           UrbBankStab,
                           SedDelivRatio_0, Acoef, KF, LS, C, P), axis=0) / NYrs
