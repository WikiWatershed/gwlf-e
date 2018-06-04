import numpy as np

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


def NConc_2(NRur, NUrb, NitrConc, ManNitr, ManuredAreas, FirstManureMonth, LastManureMonth, FirstManureMonth2,
            LastManureMonth2):
    if (FirstManureMonth < 0 and FirstManureMonth2 < 0 and LastManureMonth < 0 and LastManureMonth2 < 0):
        return np.reshape(np.repeat(NitrConc[None, :], repeats=12, axis=0), (12, -1))
    else:
        nlu = NLU(NRur, NUrb)
        result = np.reshape(np.repeat(NitrConc, repeats=12, axis=0), (12, nlu))
        result[FirstManureMonth:LastManureMonth, :ManuredAreas] = ManNitr
        result[FirstManureMonth2:LastManureMonth2, :ManuredAreas] = ManNitr
        return result
