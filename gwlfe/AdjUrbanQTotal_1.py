import numpy as np
from Timer import time_function
from AdjUrbanQTotal import AdjUrbanQTotal
from UrbAreaTotal import UrbAreaTotal
from AreaTotal import AreaTotal
from Water import Water
from Memoization import memoize


@memoize
def AdjUrbanQTotal_1(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0,
                     Imper, ISRR, ISRA, Qretention, PctAreaInfil):
    result = np.zeros((NYrs, 12, 31))
    adj_urban_q_total = AdjUrbanQTotal(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                                       Grow, CNP_0, Imper,
                                       ISRR, ISRA, Qretention, PctAreaInfil)
    urb_area_total = UrbAreaTotal(NRur, NUrb, Area)
    area_total = AreaTotal(NRur, NUrb, Area)
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    result[Y][i][j] = adj_urban_q_total[Y][i][j] * area_total / urb_area_total
                    # TODO: when I broke this cycle, the only way I could think to do this was to undo the calculation done at the end of adj_urban_q_total. Hopefully there is a better way
    return result


def AdjUrbanQTotal_1_2():
    pass
