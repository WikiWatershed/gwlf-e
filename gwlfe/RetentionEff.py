import numpy as np
from Timer import time_function
from Memoization import memoize
from Water import Water
from UrbanQTotal import UrbanQTotal
from Water import Water_2
from UrbanQTotal import UrbanQTotal_2


# @memoize
@time_function
def RetentionEff(NYrs, DaysMonth, InitSnow_0, Temp, Prec, Qretention, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper, ISRR, ISRA, PctAreaInfil):
    result = 0
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    urbanqtotal = UrbanQTotal(NYrs, DaysMonth, NRur, NUrb, Temp, InitSnow_0, Prec, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper, ISRR,
                ISRA)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    if water[Y][i][j] < 0.05:
                        pass
                    else:
                        if Qretention > 0:
                            if urbanqtotal[Y][i][j] > 0:
                                if urbanqtotal[Y][i][j] <= Qretention * PctAreaInfil:
                                    result = 1
                                else:
                                    result = Qretention * PctAreaInfil / urbanqtotal[Y][i][j]
                else:
                    pass
    return result


def RetentionEff_3(NYrs, DaysMonth, InitSnow_0, Temp, Prec, Qretention, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper, ISRR, ISRA, PctAreaInfil):
    result = np.zeros((NYrs, 12, 31))
    water = Water_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    urbanqtotal = UrbanQTotal_2(NYrs, DaysMonth, NRur, NUrb, Temp, InitSnow_0, Prec, Area, CNI_0, AntMoist_0, Grow, CNP_0,
                              Imper, ISRR, ISRA)
    result[np.where((Temp>0) & (water > 0.05) & (Qretention>0) & (urbanqtotal > 0 ) & (urbanqtotal <= Qretention * PctAreaInfil))] = 1
    result[np.where((Temp>0) & (water > 0.05) & (Qretention>0) & (urbanqtotal > 0 ) & (urbanqtotal > Qretention * PctAreaInfil))] = \
        Qretention * PctAreaInfil/ urbanqtotal[np.where((Temp>0) & (water > 0.05) & (Qretention>0) & (urbanqtotal > 0 ) & (urbanqtotal > Qretention * PctAreaInfil))]
    np.nonzero(result)
    return
@time_function
def RetentionEff_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec, Qretention, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper, ISRR, ISRA, PctAreaInfil):
    water = Water_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    urbanqtotal = UrbanQTotal_2(NYrs, DaysMonth, NRur, NUrb, Temp, InitSnow_0, Prec, Area, CNI_0, AntMoist_0, Grow, CNP_0,
                              Imper, ISRR, ISRA)
    try:
        test = urbanqtotal[np.where((Temp>0) & (water > 0.05) & (Qretention>0) & (urbanqtotal > 0 ))][::-1]
        if test <=  Qretention * PctAreaInfil:
            return 1
        else:
            return Qretention * PctAreaInfil / test
    except IndexError:
        return 0