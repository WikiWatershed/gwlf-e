from numpy import repeat
from numpy import zeros

from NLU import NLU


def NConc(NRur, NUrb, NitrConc, ManNitr, ManuredAreas, FirstManureMonth, LastManureMonth, FirstManureMonth2,
          LastManureMonth2):
    nlu = NLU(NRur, NUrb)
    result = zeros((12, nlu))
    for i in range(12):
        for l in range(NRur):
            result[i][l] = NitrConc[l]
            if l < ManuredAreas and i >= FirstManureMonth and i <= LastManureMonth:
                result[i][l] = ManNitr[l]
            if l < ManuredAreas and i >= FirstManureMonth2 and i <= LastManureMonth2:
                result[i][l] = ManNitr[l]
    return result


def NConc_f(NRur, NUrb, NitrConc, ManNitr, ManuredAreas, FirstManureMonth, LastManureMonth, FirstManureMonth2,
            LastManureMonth2):
    if (FirstManureMonth < 0 or FirstManureMonth2 < 0 or LastManureMonth < 0 or LastManureMonth2 < 0):
        # return np.reshape(np.repeat(NitrConc[None, :], repeats=12, axis=0), (12, -1))
        return repeat(NitrConc[None,:],12,axis = 0)

    else:
        nlu = NLU(NRur, NUrb)
        result = repeat(NitrConc[None,:],12, axis =0)
        result[FirstManureMonth:LastManureMonth+1, :ManuredAreas] = ManNitr
        result[FirstManureMonth2:LastManureMonth2+1, :ManuredAreas] = ManNitr
        return result
