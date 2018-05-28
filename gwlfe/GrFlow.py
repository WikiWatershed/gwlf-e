import numpy as np
from numba import jit
from Timer import time_function
from Percolation import Percolation
from Percolation import Percolation_2
from DeepSeep import DeepSeep_inner
from Memoization import memoize


@memoize
def GrFlow(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
           ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef):
    result = np.zeros((NYrs, 12, 31))
    deepseep = np.zeros((NYrs, 12, 31))
    satstor = np.zeros((NYrs, 12, 31))
    percolation = Percolation(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0,
                              Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap)
    satstor_carryover = SatStor_0
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                satstor[Y][i][j] = satstor_carryover
                result[Y][i][j] = RecessionCoef * satstor[Y][i][j]
                deepseep[Y][i][j] = SeepCoef * satstor[Y][i][j]
                satstor[Y][i][j] = satstor[Y][i][j] + percolation[Y][i][j] - result[Y][i][j] - deepseep[Y][i][j]
                if satstor[Y][i][j] < 0:
                    satstor[Y][i][j] = 0
                satstor_carryover = satstor[Y][i][j]
    return result


# @jit(cache=True, nopython=True)#using deep seep inner because the calculations are linked
# def GrFlow_inner(NYrs, SatStor_0, DaysMonth, RecessionCoef, SeepCoef, percolation):
#     result = np.zeros((NYrs, 12, 31))
#     satstor_carryover = SatStor_0
#     for Y in range(NYrs):
#         for i in range(12):
#             for j in range(DaysMonth[Y][i]):
#                 result[Y][i][j] = RecessionCoef * satstor_carryover
#                 satstor_carryover = satstor_carryover + percolation[Y][i][j] - result[Y][i][j] - SeepCoef * \
#                                     satstor_carryover
#                 if satstor_carryover < 0:
#                     satstor_carryover = 0
#     return result


@memoize
def GrFlow_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
             ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef):
    percolation = Percolation_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow,
                                CNP_0,
                                Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap)

    return DeepSeep_inner(NYrs, SatStor_0, DaysMonth, RecessionCoef, SeepCoef, percolation)[1]
