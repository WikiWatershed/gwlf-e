import numpy as np
from Timer import time_function
from Water import Water
from UrbanQTotal import UrbanQTotal
from UrbAreaTotal import UrbAreaTotal
from AreaTotal import AreaTotal
from Memoization import memoize
from Water import Water_2
from UrbanQTotal import UrbanQTotal_2
from UrbAreaTotal import UrbAreaTotal_2
from AreaTotal import AreaTotal_2
from numba import jit
import  DailyArrayConverter as DAC

# @time_function
@memoize
def AdjUrbanQTotal(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
                   ISRR, ISRA, Qretention, PctAreaInfil):
    result = np.zeros((NYrs, 12, 31))
    adj_urban_q_total = 0  # used because this is a buffered variable
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    urban_q_total = UrbanQTotal(NYrs, DaysMonth, NRur, NUrb, Temp, InitSnow_0, Prec, Area, CNI_0, AntMoist_0, Grow,
                                CNP_0, Imper, ISRR, ISRA)
    urb_area_total = UrbAreaTotal(NRur, NUrb, Area)
    area_total = AreaTotal(NRur, NUrb, Area)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    if water[Y][i][j] < 0.05:
                        # z.adj_urban_q_total = get_value_for_yesterday(z.adj_urban_q_total_1,0,Y,i,j,z.NYrs,z.DaysMonth)
                        pass
                    else:
                        adj_urban_q_total = urban_q_total[Y][i][j]
                        if Qretention > 0:
                            if urban_q_total[Y][i][j] > 0:
                                if urban_q_total[Y][i][j] <= Qretention * PctAreaInfil:
                                    adj_urban_q_total = 0
                                else:
                                    adj_urban_q_total = urban_q_total[Y][i][j] - Qretention * PctAreaInfil
                    if urb_area_total > 0:
                        adj_urban_q_total = adj_urban_q_total * urb_area_total / area_total
                    else:
                        adj_urban_q_total = 0
                else:
                    pass
                result[Y][i][j] = adj_urban_q_total
    return result



# @jit
# def AdjUrbanQTotal_2_inner(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
#                    ISRR, ISRA, Qretention, PctAreaInfil,water,urban_q_total,urb_area_total,area_total):
#     result = np.zeros((NYrs, 12, 31))
#     adj_urban_q_total = 0
#     urban_q_total = DAC.ymd_to_daily(urban_q_total, DaysMonth)
#     Temp = DAC.ymd_to_daily(Temp, DaysMonth)
#     water = DAC.ymd_to_daily(water, DaysMonth)
#     for j in range(len(urban_q_total)):
#         if Temp[j] > 0 and water[j] > 0.01:
#             if water[j] <0.05:
#                 pass
#             else:
#                 adj_urban_q_total = urban_q_total[j]
#                 if Qretention > 0 and urban_q_total[j] > 0:
#                     if urban_q_total[j] <= Qretention * PctAreaInfil:
#                         adj_urban_q_total = 0
#                     else:
#                         adj_urban_q_total = urban_q_total[j] - Qretention * PctAreaInfil
#             if urb_area_total > 0:
#                 adj_urban_q_total = adj_urban_q_total * urb_area_total / area_total
#             else:
#                 adj_urban_q_total = 0
#         else:
#             pass
#         result[j] = adj_urban_q_total
#     return DAC.daily_to_ymd(result,NYrs, DaysMonth)

@jit
def AdjUrbanQTotal_2_inner(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
                   ISRR, ISRA, Qretention, PctAreaInfil,water,urban_q_total,urb_area_total,area_total):
    result = np.zeros((NYrs, 12, 31))
    adj_urban_q_total = 0
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    if water[Y][i][j] < 0.05:
                        # z.adj_urban_q_total = get_value_for_yesterday(z.adj_urban_q_total_1,0,Y,i,j,z.NYrs,z.DaysMonth)
                        pass
                    else:
                        adj_urban_q_total = urban_q_total[Y][i][j]
                        if Qretention > 0 and urban_q_total[Y][i][j] > 0:
                            if urban_q_total[Y][i][j] <= Qretention * PctAreaInfil:
                                adj_urban_q_total = 0
                            else:
                                adj_urban_q_total = urban_q_total[Y][i][j] - Qretention * PctAreaInfil
                    if urb_area_total > 0:
                        adj_urban_q_total = adj_urban_q_total * urb_area_total / area_total
                    else:
                        adj_urban_q_total = 0
                else:
                    pass
                result[Y][i][j] = adj_urban_q_total
    return result


# @time_function
@memoize
def AdjUrbanQTotal_2(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
                   ISRR, ISRA, Qretention, PctAreaInfil):
    water = Water_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    urban_q_total = UrbanQTotal_2(NYrs, DaysMonth, NRur, NUrb, Temp, InitSnow_0, Prec, Area, CNI_0, AntMoist_0, Grow,
                                CNP_0, Imper, ISRR, ISRA)
    urb_area_total = UrbAreaTotal_2(NRur, NUrb, Area)
    area_total = AreaTotal_2(Area)
    return AdjUrbanQTotal_2_inner(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
                   ISRR, ISRA, Qretention, PctAreaInfil,water,urban_q_total,urb_area_total,area_total)
