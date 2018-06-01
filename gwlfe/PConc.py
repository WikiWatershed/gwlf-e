import numpy as np
from Timer import time_function
from Memoization import memoize
from NLU import NLU


def PConc(NRur, NUrb, PhosConc, ManPhos, ManuredAreas, FirstManureMonth, LastManureMonth, FirstManureMonth2,
          LastManureMonth2):
    nlu = NLU(NRur, NUrb)
    result = np.zeros((12, nlu))
    for i in range(12):
        for l in range(NRur):
            result[i][l] = PhosConc[l]
            # MANURE SPREADING DAYS FOR FIRST SPREADING PERIOD
            if l < ManuredAreas and i >= FirstManureMonth and i <= LastManureMonth:
                result[i][l] = ManPhos[l]
            # MANURE SPREADING DAYS FOR SECOND SPREADING PERIOD
            if l < ManuredAreas and i >= FirstManureMonth2 and i <= LastManureMonth2:
                result[i][l] = ManPhos[l]
    return result


def PConc_2():
    pass
