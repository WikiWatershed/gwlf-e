import numpy as np
from Timer import time_function
from Memoization import memoize
from Water import Water
from AdjQTotal import AdjQTotal
from QTotal import QTotal


@memoize
def DayRunoff(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
              ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN):
    result = np.zeros((NYrs, 12, 31))
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    adjqtotal = AdjQTotal(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
              ISRR, ISRA, Qretention, PctAreaInfil, n25b, CN)
    qtotal = QTotal(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
           ISRR, ISRA, CN)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    if adjqtotal[Y][i][j] > 0:
                        result[Y][i][j] = adjqtotal[Y][i][j]
                    elif qtotal[Y][i][j] > 0:
                        result[Y][i][j] = qtotal[Y][i][j]
                    else:
                        result[Y][i][j] = 0
                else:
                    pass
    return result


def DayRunoff_2():
    pass
