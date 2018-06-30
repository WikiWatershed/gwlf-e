from numpy import resize
from numpy import where
from numpy import zeros

from gwlfe.Memoization import memoize
from gwlfe.MultiUse_Fxns.Erosion.Erosion import Erosion
from gwlfe.MultiUse_Fxns.Erosion.Erosion import Erosion_f
from gwlfe.MultiUse_Fxns.Erosion.SedDelivRatio import SedDelivRatio
from gwlfe.Output.Loading.SedYield_1 import SedYield_1
from gwlfe.Output.Loading.SedYield_1 import SedYield_1_f


@memoize
def Erosion_1(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
              Grow_0, CNP_0, Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
              RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow,
              StreamWithdrawal, GroundWithdrawal, NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0,
              AvKF, AvSlope, SedAAdjust, StreamLength, n42b, n46c, n85d, AgLength, n42, n45, n85, UrbBankStab,
              SedDelivRatio_0, Acoef, KF, LS, C, P):
    result = zeros((NYrs, 12))
    seddelivratio = SedDelivRatio(SedDelivRatio_0)
    erosion = Erosion(NYrs, DaysMonth, Temp, InitSnow_0, Prec, Acoef, NRur, KF, LS, C, P, Area)
    sedyield = SedYield_1(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                          Grow_0, CNP_0, Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                          RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow,
                          StreamWithdrawal, GroundWithdrawal, NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0,
                          AvKF, AvSlope, SedAAdjust, StreamLength, n42b, n46c, n85d, AgLength, n42, n45, n85,
                          UrbBankStab, Acoef, KF, LS, C, P, SedDelivRatio_0)
    for Y in range(NYrs):
        for i in range(12):
            if seddelivratio > 0 and erosion[Y][i] < sedyield[Y][i]:
                result[Y][i] = sedyield[Y][i] / seddelivratio
            else:
                result[Y][i] = erosion[Y][i]
    return result


@memoize
def Erosion_1_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                Grow_0, CNP_0, Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow,
                StreamWithdrawal, GroundWithdrawal, NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0,
                AvKF, AvSlope, SedAAdjust, StreamLength, n42b, n46c, n85d, AgLength, n42, n45, n85, UrbBankStab,
                SedDelivRatio_0, Acoef, KF, LS, C, P):
    seddelivratio = resize(SedDelivRatio(SedDelivRatio_0), (NYrs, 12))
    erosion = Erosion_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, Acoef, NRur, KF, LS, C, P, Area)
    sedyield = SedYield_1_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                            Grow_0, CNP_0, Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap,
                            SatStor_0,
                            RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity,
                            PointFlow,
                            StreamWithdrawal, GroundWithdrawal, NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0,
                            AvKF, AvSlope, SedAAdjust, StreamLength, n42b, n46c, n85d, AgLength, n42, n45, n85,
                            UrbBankStab, Acoef, KF, LS, C, P, SedDelivRatio_0)
    return where((seddelivratio > 0) & (erosion < sedyield), sedyield / seddelivratio, erosion)
