# from Memoization import memoize
# # from Timer import time_function
# from Percolation import Percolation
# from Percolation import Percolation_2
#
# try:
#     raise ImportError
#     from DeepSeep_inner_compiled import DeepSeep_inner
# except ImportError:
#     print("Unable to import compiled DeepSeep_inner, using slower version")
#     from DeepSeep_inner import DeepSeep_inner
#
#
# @memoize
# def DeepSeep(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
#              ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef):
#     result = np.zeros((NYrs, 12, 31))
#     grflow = np.zeros((NYrs, 12, 31))
#     satstor = np.zeros((NYrs, 12, 31))
#     percolation = Percolation(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
#                               CNP_0,
#                               Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap)
#     satstor_carryover = SatStor_0
#     for Y in range(NYrs):
#         for i in range(12):
#             for j in range(DaysMonth[Y][i]):
#                 satstor[Y][i][j] = satstor_carryover
#                 grflow[Y][i][j] = RecessionCoef * satstor[Y][i][j]
#                 result[Y][i][j] = SeepCoef * satstor[Y][i][j]
#                 satstor[Y][i][j] = satstor[Y][i][j] + percolation[Y][i][j] - grflow[Y][i][j] - result[Y][i][j]
#                 if satstor[Y][i][j] < 0:
#                     satstor[Y][i][j] = 0
#                 satstor_carryover = satstor[Y][i][j]
#     return result
#
#
# # @memoize
# def DeepSeep_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0, CNP_0, Imper,
#                ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef):
#     percolation = Percolation_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow_0,
#                                 CNP_0, Imper, ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap)
#     DeepSeep_inner(NYrs, SatStor_0, DaysMonth, RecessionCoef, SeepCoef, percolation)
#     print(DeepSeep_inner.inspect_types())
#     return DeepSeep_inner(NYrs, SatStor_0, DaysMonth, RecessionCoef, SeepCoef, percolation)[0]
