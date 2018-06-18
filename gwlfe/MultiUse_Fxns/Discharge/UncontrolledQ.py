# # from Timer import time_function
# from Memoization import memoize
# from Water import Water
# from NLU import NLU
# from AreaTotal import AreaTotal
# from QrunI import QrunI
# from QrunP import QrunP
# from LU import LU


# @memoize
# def UncontrolledQ(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, Area, CNI_0, CNP_0, AntMoist_0, Grow_0, Imper, ISRR, ISRA):
#     result = 0
#     water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
#     nlu = NLU(NRur, NUrb)
#     areatotal = AreaTotal(NRur, NUrb, Area)
#     qruni = QrunI(NYrs, DaysMonth, NRur, NUrb, Temp, InitSnow_0, Prec, CNI_0, AntMoist_0, Grow_0)
#     qrunp = QrunP(NYrs, DaysMonth, NRur, NUrb, Temp, InitSnow_0, Prec, CNP_0, AntMoist_0, Grow_0)
#     lu = LU(NRur, NUrb)
#     for Y in range(NYrs):
#         for i in range(12):
#             for j in range(DaysMonth[Y][i]):
#                 if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
#                     if water[Y][i][j] < 0.05:
#                         pass
#                     else:
#                         for l in range(NRur, nlu):
#                             if areatotal > 0:
#                                 result += ((qruni[Y][i][j][l] * (Imper[l] * (1 - ISRR[lu[l]]) *
#                                       (1 - ISRA[lu[l]])) + qrunp[Y][i][j][l] *
#                                       (1 - (Imper[l] * (1 - ISRR[lu[l]]) * (1 - ISRA[lu[l]])))) *
#                                                     Area[l] / areatotal)
#                 else:
#                     pass
#
#     return result
#
#
# def UncontrolledQ_f():
#     pass
