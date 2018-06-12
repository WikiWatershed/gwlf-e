# from Timer import time_function
from Memoization import memoize
from StreamFlowLE import StreamFlowLE
from StreamFlowLE import StreamFlowLE_2
from TotAreaMeters import TotAreaMeters
from numpy import zeros


@memoize
def StreamFlowVol(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                  ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef
                  , Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow, StreamWithdrawal,
                  GroundWithdrawal):
    # CALCULATE THE VOLUMETRIC STREAM Flow
    result = zeros((NYrs, 12))
    streamflowle = StreamFlowLE(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                                CNP_0, Imper,
                                ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef,
                                SeepCoef
                                , Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow,
                                StreamWithdrawal, GroundWithdrawal)
    totareameters = TotAreaMeters(NRur, NUrb, Area)
    for Y in range(NYrs):
        for i in range(12):
            # CALCULATE THE VOLUMETRIC STREAM Flow
            result[Y][i] = ((streamflowle[Y][i] / 100) * totareameters) / (86400 * DaysMonth[Y][i])
    return result


def StreamFlowVol_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                    ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef,
                    Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow, StreamWithdrawal,
                    GroundWithdrawal):
    streamflowle = StreamFlowLE_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                                  CNP_0, Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                                  RecessionCoef, SeepCoef, Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity,
                                  PointFlow, StreamWithdrawal, GroundWithdrawal)
    totareameters = TotAreaMeters(NRur, NUrb, Area)
    return streamflowle / 100 * totareameters / (86400 * DaysMonth)
