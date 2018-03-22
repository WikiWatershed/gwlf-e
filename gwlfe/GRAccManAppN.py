import numpy as np
from Timer import time_function
from GrazingN import GrazingN


def GRAccManAppN(InitGrN, GRPctManApp, PctGrazing):
    result = np.zeros((12,))
    grazing_n = GrazingN(PctGrazing,InitGrN)
    for i in range(12):
        result[i] = (result[i] + (InitGrN / 12)
                     - (GRPctManApp[i] * InitGrN) - GrazingN[i])
        if result[i] < 0:
            result[i] = 0
    return result

def GRAccManAppN_2(InitGrN, GRPctManApp, GrazingN):
    result = (np.repeat(InitGrN/12,12) ) - (GRPctManApp * np.repeat(InitGrN,12)) - GrazingN
    result = np.maximum(result,0)
    return result
