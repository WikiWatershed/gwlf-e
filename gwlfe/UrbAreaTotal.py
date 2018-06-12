import numpy as np
# from Timer import time_function
from NLU import NLU
from Memoization import memoize

# @time_function
@memoize
def UrbAreaTotal(NRur,NUrb,Area):
    result = 0
    nlu = NLU(NRur,NUrb)
    for l in range(NRur, nlu):
        result += Area[l]
    return result


# Tried, it was slower. UrbAreaTotal is faster
# @time_function
#@memoize
def UrbAreaTotal_2(NRur,NUrb,Area):
    nlu = NLU(NRur, NUrb)
    return np.sum(Area[NRur:])