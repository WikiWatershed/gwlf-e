import numpy as np
from Timer import time_function
from Memoization import memoize
from SedDelivRatio import SedDelivRatio
from Erosion import Erosion
from SedYield_2 import SedYield_2


@memoize
def Erosion_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                        Grow, CNP_0, Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                        RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow,
                        StreamWithdrawal, GroundWithdrawal, NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0,
                        AvKF, AvSlope, SedAAdjust, StreamLength, n42b, n46c, n85d, AgLength, n42, n45, n85, UrbBankStab,
                        SedDelivRatio_0, Acoef, KF, LS, C, P):
    result = np.zeros((NYrs, 12))
    seddelivratio = SedDelivRatio(SedDelivRatio_0)
    erosion = Erosion(NYrs, DaysMonth, Temp, InitSnow_0, Prec, Acoef, NRur, KF, LS, C, P, Area)
    sedyield = SedYield_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                        Grow, CNP_0, Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                        RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow,
                        StreamWithdrawal, GroundWithdrawal, NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0,
                        AvKF, AvSlope, SedAAdjust, StreamLength, n42b, n46c, n85d, AgLength, n42, n45, n85, UrbBankStab)
    for Y in range(NYrs):
        for i in range(12):
            if seddelivratio > 0 and erosion[Y][i] < sedyield[Y][i]:
                result[Y][i] = sedyield[Y][i] / seddelivratio
            else:
                result[Y][i] = erosion[Y][i]
    return result


def Erosion_2_2():
    pass
