import numpy as np
from Timer import time_function
from NLU import NLU


def NewCN(NRur, NUrb, CN):
    nlu = NLU(NRur, NUrb)
    result = np.zeros((3, nlu))
    for l in range(NRur):
        result[0][l] = CN[l] / (2.334 - 0.01334 * CN[l])
        result[2][l] = CN[l] / (0.4036 + 0.0059 * CN[l])
        if result[2][l] > 100:
            result[2][l] = 100
    return result


def NewCN_2():
    pass
