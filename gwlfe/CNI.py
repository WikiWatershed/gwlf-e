import numpy as np
from Timer import time_function
from NLU import NLU
from Memoization import memoize


@memoize
def CNI(NRur, NUrb, CNI_0):
    nlu = NLU(NRur, NUrb)
    result = np.zeros((3, nlu))
    for l in range(NRur, nlu):
        result[0][l] = CNI_0[1][l] / (2.334 - 0.01334 * CNI_0[1][1])
        result[1][l] = CNI_0[1][l]
        result[2][l] = CNI_0[1][l] / (0.4036 + 0.0059 * CNI_0[1][l])
    return result


def CNI_2():
    pass
