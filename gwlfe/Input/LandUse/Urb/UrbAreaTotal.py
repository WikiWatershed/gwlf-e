from numpy import sum

from gwlfe.Input.LandUse.NLU import NLU
from gwlfe.Memoization import memoize


@memoize
def UrbAreaTotal(NRur, NUrb, Area):
    result = 0
    nlu = NLU(NRur, NUrb)
    for l in range(NRur, nlu):
        result += Area[l]
    return result


# Tried, it was slower. UrbAreaTotal is faster
@memoize
def UrbAreaTotal_f(NRur, NUrb, Area):
    return sum(Area[NRur:])
