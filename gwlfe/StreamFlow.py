import numpy as np
from Timer import time_function
from Flow import Flow
from Flow import Flow_2
from Runoff import Runoff
from Runoff import Runoff_2
from GroundWatLE_2 import GroundWatLE_2
from PtSrcFlow import PtSrcFlow
from PtSrcFlow import PtSrcFlow_2
from TileDrain import TileDrain
from TileDrain import TileDrain_2
from Withdrawal import Withdrawal
from Withdrawal import Withdrawal_2
from Memoization import memoize


@memoize
def StreamFlow(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
               ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef
               , Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow, StreamWithdrawal,
               GroundWithdrawal):
    result = np.zeros((NYrs, 12))
    flow = Flow(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef)
    runoff = Runoff(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                    ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN, Landuse, TileDrainDensity)
    groundwatle_2 = GroundWatLE_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                                  CNP_0, Imper,
                                  ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                                  RecessionCoef, SeepCoef, Landuse, TileDrainDensity)
    ptsrcflow = PtSrcFlow(NYrs, PointFlow)
    tiledrain = TileDrain(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                          Imper,
                          ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef,
                          SeepCoef, Landuse, TileDrainDensity)
    withdrawal = Withdrawal(NYrs, StreamWithdrawal, GroundWithdrawal)
    for Y in range(NYrs):
        for i in range(12):
            # for j in range(DaysMonth[Y][i]):
            #     result[Y][i] = result[Y][i] + flow[Y][i][j]  # This is weird, it seems to be immediately overwritten
            result[Y][i] = (runoff[Y][i]
                            + groundwatle_2[Y][i]
                            + ptsrcflow[Y][i]
                            + tiledrain[Y][i]
                            - withdrawal[Y][i])
    return result

@memoize
def StreamFlow_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                 ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef,
                 Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow, StreamWithdrawal,
                 GroundWithdrawal):
    runoff = Runoff_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
                      ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN, Landuse, TileDrainDensity)
    groundwatle_2 = GroundWatLE_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
                                  CNP_0, Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                                  RecessionCoef, SeepCoef, Landuse, TileDrainDensity)
    ptsrcflow = PtSrcFlow_2(NYrs, PointFlow)
    tiledrain = TileDrain_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0,
                            Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                            RecessionCoef,
                            SeepCoef, Landuse, TileDrainDensity)
    withdrawal = Withdrawal_2(NYrs, StreamWithdrawal, GroundWithdrawal)
    return runoff + groundwatle_2 + ptsrcflow + tiledrain - withdrawal
