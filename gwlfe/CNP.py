import numpy as np
from Timer import time_function
from NLU import NLU


def CNP(NRur, NUrb, CNP_0):
    nlu = NLU(NRur, NUrb)
    result = np.zeros((3, nlu))
    for l in range(NRur, nlu):
        result[0][l] = CNP_0[1][l] / (2.334 - 0.01334 * CNP_0[1][1])
        result[1][l] = CNP_0[1][l]
        result[2][l] = CNP_0[1][l] / (0.4036 + 0.0059 * CNP_0[1][l])
    return result


def CNP_2():
    pass
