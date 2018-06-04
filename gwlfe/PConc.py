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

def PConc_2(NRur, NUrb, PhosConc, ManPhos, ManuredAreas, FirstManureMonth, LastManureMonth, FirstManureMonth2,
          LastManureMonth2):
    if(FirstManureMonth < 0 and FirstManureMonth2 < 0 and LastManureMonth < 0 and LastManureMonth2 < 0):
        return np.reshape(np.repeat(PhosConc[None,:], repeats=12, axis=0), (12, -1))
    else:
        nlu = NLU(NRur, NUrb)
        result = np.reshape(np.repeat(PhosConc, repeats=12, axis=0), (12, nlu))
        result[FirstManureMonth:LastManureMonth, :ManuredAreas] = ManPhos
        result[FirstManureMonth2:LastManureMonth2, :ManuredAreas] = ManPhos
        return result