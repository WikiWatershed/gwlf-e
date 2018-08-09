# from Timer import time_function
from numpy import zeros

from gwlfe.Input.LandUse.NLU import NLU
from gwlfe.Memoization import memoize


@memoize
def LU_1(NRur, NUrb):
    nlu = NLU(NRur, NUrb)
    result = zeros((nlu,)).astype("int")
    for l in range(NRur, nlu):
        result[l] = l - 11
    return result

# Tried, it was slower. LU_1 is faster
# def LU_1_f():
#     pass
