# from Timer import time_function
# from Memoization import memoize
# from Water import Water
# from RuralQTotal import RuralQTotal


# @memoize
# def RuralRunoff(NYrs, DaysMonth, InitSnow_0, Temp, Prec,  NRur, CN, NUrb, AntMoist_0, Grow_0, Area):
#     result = np.zeros((NYrs, 12))
#     water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
#     ruralqtotal = RuralQTotal(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, CN, NUrb, AntMoist_0, Grow_0, Area)
#     for Y in range(NYrs):
#         for i in range(12):
#             for j in range(DaysMonth[Y][i]):
#                 if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
#                     result[Y][i] += ruralqtotal[Y][i][j]
#                 else:
#                     pass
#     return result
#
#
# def RuralRunoff_f():
#     pass
