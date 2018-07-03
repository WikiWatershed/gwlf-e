from numpy import where
from numpy import zeros

from gwlfe.Memoization import memoize
# from Timer import time_function
from gwlfe.MultiUse_Fxns.Discharge.StreamFlow import StreamFlow
from gwlfe.MultiUse_Fxns.Discharge.StreamFlow import StreamFlow_f


@memoize
def StreamFlowLE(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                 ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef
                 , Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow, StreamWithdrawal,
                 GroundWithdrawal):
    result = zeros((NYrs, 12))
    streamflow = StreamFlow(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                            Imper,
                            ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef,
                            SeepCoef
                            , Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow, StreamWithdrawal,
                            GroundWithdrawal)
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = streamflow[Y][i]
            if result[Y][i] < 0:
                result[Y][i] = 0
    return result


def StreamFlowLE_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                   ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef,
                   Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow, StreamWithdrawal,
                   GroundWithdrawal):
    streamflow = StreamFlow_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                              CNP_0,
                              Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                              RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity,
                              PointFlow, StreamWithdrawal, GroundWithdrawal)
    return where(streamflow > 0, streamflow, 0)
