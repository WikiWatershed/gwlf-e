from numpy import repeat
from numpy import zeros

from gwlfe.Input.LandUse.NLU import NLU
from gwlfe.Memoization import memoize


def PConc(NRur, NUrb, PhosConc, ManPhos, ManuredAreas, FirstManureMonth, LastManureMonth, FirstManureMonth2,
          LastManureMonth2):
    nlu = NLU(NRur, NUrb)
    result = zeros((12, nlu))
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


@memoize
def PConc_f(NRur, NUrb, PhosConc, ManPhos, ManuredAreas, FirstManureMonth, LastManureMonth, FirstManureMonth2,
            LastManureMonth2):
    if (FirstManureMonth < 0 or FirstManureMonth2 < 0 or LastManureMonth < 0 or LastManureMonth2 < 0):
        return repeat(PhosConc[None, :], 12, axis=0)
    else:
        result = repeat(PhosConc[None, :], 12, axis=0)
        result[FirstManureMonth:LastManureMonth + 1, :ManuredAreas] = ManPhos
        result[FirstManureMonth2:LastManureMonth2 + 1, :ManuredAreas] = ManPhos
        return result
