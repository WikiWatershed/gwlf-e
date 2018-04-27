import numpy as np
from Timer import time_function
from NLU import NLU
from Memoization import memoize


@memoize
def LU(NRur, NUrb):
    nlu = NLU(NRur, NUrb)
    result = np.zeros((nlu,)).astype("int")
    for l in range(NRur, nlu):
        result[l] = l - NRur
    return result


def lu_2():
    pass
