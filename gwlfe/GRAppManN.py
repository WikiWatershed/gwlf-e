import numpy as np
from Timer import time_function


def GRAppManN(GRPctManApp, InitGrN):
    result = np.zeros((12,))
    for i in range(12):
        result[i] = GRPctManApp[i] * InitGrN
    return result


def GRAppManN_2(GRPctManApp, InitGrN):
    return GRPctManApp * InitGrN
