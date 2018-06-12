import numpy as np
# from Timer import time_function
from Memoization import memoize
from SedYield_1 import SedYield_1_2


@memoize
def AvSedYield(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
               Grow_0, CNP_0, Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
               RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow,
               StreamWithdrawal, GroundWithdrawal, NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0,
               AvKF, AvSlope, SedAAdjust, StreamLength, n42b, n46c, n85d, AgLength, n42, n45, n85, UrbBankStab,
               Acoef, KF, LS, C, P, SedDelivRatio_0):
    result = np.zeros(12)
    sedyeild = SedYield_1_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                            Grow_0, CNP_0, Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap,
                            SatStor_0,
                            RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity,
                            PointFlow,
                            StreamWithdrawal, GroundWithdrawal, NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0,
                            AvKF, AvSlope, SedAAdjust, StreamLength, n42b, n46c, n85d, AgLength, n42, n45, n85,
                            UrbBankStab,
                            Acoef, KF, LS, C, P, SedDelivRatio_0)
    for Y in range(NYrs):
        for i in range(12):
            result[i] += sedyeild[Y][i] / NYrs
    return result


@memoize
def AvSedYield_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                 Grow_0, CNP_0, Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                 RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow,
                 StreamWithdrawal, GroundWithdrawal, NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0,
                 AvKF, AvSlope, SedAAdjust, StreamLength, n42b, n46c, n85d, AgLength, n42, n45, n85, UrbBankStab,
                 Acoef, KF, LS, C, P, SedDelivRatio_0):
    return np.sum(
        SedYield_1_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                     Grow_0, CNP_0, Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                     RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow,
                     StreamWithdrawal, GroundWithdrawal, NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0,
                     AvKF, AvSlope, SedAAdjust, StreamLength, n42b, n46c, n85d, AgLength, n42, n45, n85, UrbBankStab,
                     Acoef, KF, LS, C, P, SedDelivRatio_0),
        axis=0) / NYrs
