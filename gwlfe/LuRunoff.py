import numpy as np
from Timer import time_function
from Memoization import memoize
from UrbQRunoff import UrbQRunoff_2
from UrbQRunoff import UrbQRunoff
from NLU import NLU
from RurQRunoff import RurQRunoff_2
from RurQRunoff import RurQRunoff


def LuRunoff(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, CNI_0, CNP_0,
             AntMoist_0, Grow_0, Imper, ISRR, ISRA, CN):
    result = np.zeros((NYrs, 16))
    nlu = NLU(NRur, NUrb)
    urb_q_runoff = UrbQRunoff(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, CNI_0, CNP_0,
                              AntMoist_0, Grow_0, Imper, ISRR, ISRA)
    rur_q_runoff = RurQRunoff(NYrs, DaysMonth, InitSnow_0, Temp, Prec, AntMoist_0, NRur, NUrb, CN, Grow_0)
    for Y in range(NYrs):
        for i in range(12):
            # Calculate landuse runoff for rural areas
            for l in range(NRur):
                result[Y][l] += rur_q_runoff[Y][l][i]
        for i in range(12):
            # Calculate landuse runoff for urban areas
            for l in range(NRur, nlu):
                result[Y][l] += urb_q_runoff[Y][l][i]
    return result

@memoize
def LuRunoff_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, CNI_0, CNP_0,
               AntMoist_0, Grow_0, Imper, ISRR, ISRA, CN):
    return np.hstack(
        (np.sum(RurQRunoff_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec, AntMoist_0, NRur, NUrb, CN, Grow_0), axis=1),
         np.sum(UrbQRunoff_2(NYrs, DaysMonth, InitSnow_0, Temp, Prec, NRur, NUrb, CNI_0, CNP_0,
                             AntMoist_0, Grow_0, Imper, ISRR, ISRA), axis=1),
         ))
