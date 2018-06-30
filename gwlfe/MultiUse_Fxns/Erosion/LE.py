from numpy import zeros

from gwlfe.MultiUse_Fxns.Discharge.StreamFlowVol import StreamFlowVol
from gwlfe.MultiUse_Fxns.Discharge.StreamFlowVol import StreamFlowVol_f
from gwlfe.MultiUse_Fxns.Erosion.SedAFactor import SedAFactor
from gwlfe.MultiUse_Fxns.Erosion.SedAFactor import SedAFactor_f


def LE(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
       ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef
       , Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal
       , NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF, AvSlope, SedAAdjust):
    result = zeros((NYrs, 12))
    sedafactor = SedAFactor(NumAnimals, AvgAnimalWt, NRur, NUrb, CNI_0, CNP_0, CN, Imper, Area, SedAFactor_0, AvKF,
                            AvSlope, SedAAdjust)
    streamflowvol = StreamFlowVol(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                                  CNP_0, Imper,
                                  ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                                  RecessionCoef, SeepCoef
                                  , Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow,
                                  StreamWithdrawal, GroundWithdrawal)
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = sedafactor * (StreamFlowVolAdj * (streamflowvol[Y][i] ** 0.6))
    return result


def LE_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
         ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef
         , Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal
         , NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF, AvSlope, SedAAdjust):
    sedafactor = SedAFactor_f(NumAnimals, AvgAnimalWt, NRur, NUrb, CNI_0, CNP_0, CN, Imper, Area, SedAFactor_0, AvKF,
                              AvSlope,
                              SedAAdjust)  # TODO: this has apparently been vectorized but is on a different branch
    streamflowvol = StreamFlowVol_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                                    Grow_0,
                                    CNP_0, Imper,
                                    ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                                    RecessionCoef, SeepCoef
                                    , Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow,
                                    StreamWithdrawal, GroundWithdrawal)
    return sedafactor * StreamFlowVolAdj * streamflowvol ** 0.6
