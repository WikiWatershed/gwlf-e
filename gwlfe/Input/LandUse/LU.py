from numpy import zeros

from gwlfe.Input.LandUse.NLU import NLU
from gwlfe.Memoization import memoize


@memoize
def LU(NRur, NUrb):
    nlu = NLU(NRur, NUrb)
    result = zeros((nlu,)).astype("int")
    for l in range(NRur, nlu):
        result[l] = l - NRur
    return result

# @time_function
# lu is faster than lu_f
# def lu_f(NRur, NUrb):
#     nlu = NLU(NRur, NUrb)
#     result = np.zeros((nlu,)).astype("int")
#     result[NRur:nlu] = np.asarray(range(NRur, nlu)) - NRur
#     return result
