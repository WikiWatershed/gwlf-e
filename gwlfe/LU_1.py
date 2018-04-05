import numpy as np
from Timer import time_function
from NLU import NLU


def LU_1(NRur, NUrb):
    nlu = NLU(NRur, NUrb)
    result = np.zeros((nlu,)).astype("int")
    for l in range(NRur, nlu):
        result[l] = l - 11
    return result


def LU_1_2():
    pass
