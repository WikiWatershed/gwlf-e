import numpy as np
from Timer import time_function
from Memoization import memoize
from RurQRunoff import RurQRunoff
from RurQRunoff import RurQRunoff_2
from NConc import NConc
from NConc import NConc_2


@memoize
def nRunoff(NYrs, DaysMonth, InitSnow_0, Temp, Prec, AntMoist_0, NRur, NUrb, CN, Grow_0, Area, NitrConc,
            ManNitr, ManuredAreas, FirstManureMonth, LastManureMonth, FirstManureMonth2, LastManureMonth2):
    result = np.zeros((NYrs, 12))
    rur_q_runoff = RurQRunoff(NYrs, DaysMonth, InitSnow_0, Temp, Prec, AntMoist_0, NRur, NUrb, CN, Grow_0)
    n_conc = NConc(NRur, NUrb, NitrConc, ManNitr, ManuredAreas, FirstManureMonth, LastManureMonth, FirstManureMonth2,
                   LastManureMonth2)
    for Y in range(NYrs):
        for i in range(12):
            for l in range(NRur):
                result[Y][i] += 0.1 * n_conc[i][l] * rur_q_runoff[Y][l][i] * Area[l]
    return result


@memoize
def nRunoff_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec, AntMoist_0, NRur, NUrb, CN, Grow_0, Area, NitrConc,
              ManNitr, ManuredAreas, FirstManureMonth, LastManureMonth, FirstManureMonth2, LastManureMonth2):
    n_conc = NConc_2(NRur, NUrb, NitrConc, ManNitr, ManuredAreas, FirstManureMonth, LastManureMonth, FirstManureMonth2,
                   LastManureMonth2)[:, :NRur]

    return 0.1 * np.sum(n_conc *
                        RurQRunoff_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec, AntMoist_0, NRur, NUrb, CN,
                                     Grow_0) * Area[:NRur], axis=2)
