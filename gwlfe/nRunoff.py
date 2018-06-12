from numpy import zeros

# from Timer import time_function
from Memoization import memoize
from NConc import NConc
from NConc import NConc_2
from RurQRunoff import RurQRunoff
from RurQRunoff import RurQRunoff_2


@memoize
def nRunoff(NYrs, DaysMonth, InitSnow_0, Temp, Prec, AntMoist_0, NRur, NUrb, CN, Grow_0, Area, NitrConc,
            ManNitr, ManuredAreas, FirstManureMonth, LastManureMonth, FirstManureMonth2, LastManureMonth2):
    result = zeros((NYrs, 12,10))
    rur_q_runoff = RurQRunoff(NYrs, DaysMonth, InitSnow_0, Temp, Prec, AntMoist_0, NRur, NUrb, CN, Grow_0)
    n_conc = NConc(NRur, NUrb, NitrConc, ManNitr, ManuredAreas, FirstManureMonth, LastManureMonth, FirstManureMonth2,
                   LastManureMonth2)
    for Y in range(NYrs):
        for i in range(12):
            for l in range(NRur):
                result[Y][i][l] = 0.1 * n_conc[i][l] * rur_q_runoff[Y][l][i] * Area[l]
    # += changed to =
    return result


@memoize
def nRunoff_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec, AntMoist_0, NRur, NUrb, CN, Grow_0, Area, NitrConc,
              ManNitr, ManuredAreas, FirstManureMonth, LastManureMonth, FirstManureMonth2, LastManureMonth2):
    n_conc = NConc_2(NRur, NUrb, NitrConc, ManNitr, ManuredAreas, FirstManureMonth, LastManureMonth, FirstManureMonth2,
                   LastManureMonth2)[:, :NRur]

    return 0.1 * n_conc * RurQRunoff_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec, AntMoist_0, NRur, NUrb, CN,
                                     Grow_0) * Area[:NRur]
