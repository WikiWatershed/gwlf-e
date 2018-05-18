import numpy as np
from Timer import time_function
from AdjQTotal import AdjQTotal
from QTotal import QTotal
from TileDrainRO import TileDrainRO
from Memoization import memoize
from AdjQTotal import AdjQTotal_2
from QTotal import QTotal_2
from TileDrainRO import TileDrainRO_2
from numba import jit

@time_function
def Runoff(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
           ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN, Landuse, TileDrainDensity):
    result = np.zeros((NYrs, 12))
    adj_q_total = AdjQTotal(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0,
                            Imper,
                            ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN)
    q_total = QTotal(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
                     ISRR, ISRA, CN)
    tile_drain_ro = TileDrainRO(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, CN, AntMoist_0, NUrb, Grow, Landuse,
                                Area,
                                TileDrainDensity)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if adj_q_total[Y][i][j] > 0:
                    result[Y][i] += adj_q_total[Y][i][j]
                else:
                    result[Y][i] += q_total[Y][i][j]
                    # ADJUST THE SURFACE RUNOFF
            result[Y][i] = result[Y][i] - tile_drain_ro[Y][i]
            if result[Y][i] < 0:
                result[Y][i] = 0
    return result

@time_function
@jit
def Runoff_1(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
           ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN, Landuse, TileDrainDensity):
    result = np.zeros((NYrs, 12))
    adj_q_total = AdjQTotal_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0,
                            Imper,
                            ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN)
    q_total = QTotal_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
                     ISRR, ISRA, CN)
    tile_drain_ro = TileDrainRO_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, CN, AntMoist_0, NUrb, Grow, Landuse,
                                Area,
                                TileDrainDensity)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if adj_q_total[Y][i][j] > 0:
                    result[Y][i] += adj_q_total[Y][i][j]
                else:
                    result[Y][i] += q_total[Y][i][j]
                    # ADJUST THE SURFACE RUNOFF
            result[Y][i] = result[Y][i] - tile_drain_ro[Y][i]
            if result[Y][i] < 0:
                result[Y][i] = 0
    return result

@time_function
def Runoff_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
           ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN, Landuse, TileDrainDensity):
    result = np.zeros((NYrs, 12,31))
    adj_q_total = AdjQTotal_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0,
                            Imper,
                            ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN)
    q_total = QTotal_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
                     ISRR, ISRA, CN)
    tile_drain_ro = TileDrainRO_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, CN, AntMoist_0, NUrb, Grow, Landuse,
                                Area,
                                TileDrainDensity)
    result = np.where(adj_q_total>0,adj_q_total,q_total)
    result = np.sum(result, axis=2) - tile_drain_ro
    result[result<0] = 0
    return result
