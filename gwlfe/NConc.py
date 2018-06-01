import numpy as np
from Timer import time_function
from Memoization import memoize
from NLU import NLU


def NConc(NRur, NUrb, NitrConc, ManNitr, ManuredAreas, FirstManureMonth, LastManureMonth, FirstManureMonth2,
          LastManureMonth2):
    nlu = NLU(NRur, NUrb)
    result = np.zeros((12, nlu))
    for i in range(12):
        for l in range(NRur):
            result[i][l] = NitrConc[l]
            if l < ManuredAreas and i >= FirstManureMonth and i <= LastManureMonth:
                result[i][l] = ManNitr[l]
            if l < ManuredAreas and i >= FirstManureMonth2 and i <= LastManureMonth2:
                result[i][l] = ManNitr[l]
    return result


def NConc_2():
    pass
