import numpy as np
from Timer import time_function
from Memoization import memoize
from RurQRunoff import RurQRunoff
from RurQRunoff import RurQRunoff_2
from PConc import PConc
from PConc import PConc_2


@memoize
def pRunoff(NYrs, DaysMonth, InitSnow_0, Temp, Prec, AntMoist_0, NRur, NUrb, CN, Grow_0, Area, PhosConc, ManuredAreas,
            FirstManureMonth, LastManureMonth, ManPhos, FirstManureMonth2,
            LastManureMonth2):
    result = np.zeros((NYrs, 12,10))
    rur_q_runoff = RurQRunoff(NYrs, DaysMonth, InitSnow_0, Temp, Prec, AntMoist_0, NRur, NUrb, CN, Grow_0)
    p_conc = PConc(NRur, NUrb, PhosConc, ManPhos, ManuredAreas, FirstManureMonth, LastManureMonth, FirstManureMonth2,
                   LastManureMonth2)
    for Y in range(NYrs):
        for i in range(12):
            for l in range(NRur):
                # += changed to =
                result[Y][i][l] = 0.1 * p_conc[i][l] * rur_q_runoff[Y][l][i] * Area[l]
    return result


@memoize
def pRunoff_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec, AntMoist_0, NRur, NUrb, CN, Grow_0, Area, PhosConc, ManuredAreas,
              FirstManureMonth, LastManureMonth, ManPhos, FirstManureMonth2, LastManureMonth2):
    p_conc = PConc_2(NRur, NUrb, PhosConc, ManPhos, ManuredAreas, FirstManureMonth, LastManureMonth, FirstManureMonth2,
                   LastManureMonth2)[:, :NRur]
    rur_q_runoff = RurQRunoff_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec, AntMoist_0, NRur, NUrb, CN, Grow_0)
    return 0.1 * np.sum(p_conc * rur_q_runoff * Area[:NRur], axis=2)
