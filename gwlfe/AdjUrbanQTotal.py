import numpy as np
from Timer import time_function
from Water import Water
from UrbanQTotal import UrbanQTotal
from UrbAreaTotal import UrbAreaTotal
from AreaTotal import AreaTotal
from Memoization import memoize


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


def AdjUrbanQTotal_2():
    pass
