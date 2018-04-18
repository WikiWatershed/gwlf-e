import numpy as np
from Timer import time_function
from Water import Water
from AdjUrbanQTotal import AdjUrbanQTotal
from RuralQTotal import RuralQTotal

def AdjQTotal(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
              ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN):
    result = np.zeros((NYrs,12,31))
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    adj_urban_q_total = AdjUrbanQTotal(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
                   ISRR, ISRA, Qretention, PctAreaInfil)
    rural_q_total = RuralQTotal(NYrs,DaysMonth,Temp,InitSnow_0,Prec,NRur,CN,NUrb,AntMoist_0, Grow,Area)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    # Assume 20% reduction of runoff with urban wetlands
                    result[Y][i][j] = (adj_urban_q_total[Y][i][j] * (1 - (n25b * 0.2))) + rural_q_total[Y][i][j]
    return result


def AdjQTotal_2():
    pass
