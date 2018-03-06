import numpy as np
from Timer import time_function


def GRAppManN(GRPctManApp, InitGrN):
    result = np.zeros((12,))
    for i in range(12):
        result[i] = GRPctManApp[i] * InitGrN
    return result


def GrAppManN_2():
    pass


def GrazingN(PctGrazing, InitGrN):
    result = np.zeros((12,))
    for i in range(12):
        result[i] = PctGrazing[i] * (InitGrN / 12)
    return result


def GrazingN_2():
    pass


def GRAccManAppN(InitGrN, GRPctManApp, GrazingN):
    result = np.zeros((12,))
    for i in range(12):
        result[i] = (result[i] + (InitGrN / 12)
                     - (GRPctManApp[i] * InitGrN) - GrazingN[i])
        if result[i] < 0:
            result[i] = 0
    return result


def GRAccManAppN_2():
    pass


def GRInitBarnN(GRAppManN, InitGrN, GRPctManApp, GrazingN):
    result = np.zeros((12,))
    grAccManAppN = GRAccManAppN(InitGrN, GRPctManApp, GrazingN)
    for i in range(12):
        result[i] = grAccManAppN[i] - GRAppManN[i]
    return result


def GRInitBarnN_2():
    pass
