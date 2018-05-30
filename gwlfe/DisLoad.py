import numpy as np
from Timer import time_function
from Memoization import memoize
from Water import Water
from NetDisLoad import NetDisLoad


@memoize
def DisLoad(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                        Grow, CNP_0, Imper, ISRR, ISRA, Qretention, PctAreaInfil, Nqual, LoadRateImp,
                        SweepFrac, UrbSweepFrac, LoadRatePerv, Storm, UrbBMPRed, DisFract, FilterWidth, PctStrmBuf):
    result = np.zeros((NYrs, 12, 3))
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    netdisload = NetDisLoad(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0,
                        Grow, CNP_0, Imper, ISRR, ISRA, Qretention, PctAreaInfil, Nqual, LoadRateImp,
                        SweepFrac, UrbSweepFrac, LoadRatePerv, Storm, UrbBMPRed, DisFract, FilterWidth, PctStrmBuf)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    for q in range(Nqual):
                        result[Y][i][q] += netdisload[Y][i][j][q]
                        if result[Y][i][q] < 0:
                            result[Y][i][q] = 0
                else:
                    pass
    return result


def DisLoad_2():
    pass
