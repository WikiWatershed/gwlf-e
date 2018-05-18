import numpy as np
from Timer import time_function
from NLU import NLU
from Memoization import memoize


@memoize
# @time_function
def AreaTotal(NRur, NUrb, Area):
    result = 0
    nlu = NLU(NRur, NUrb)
    for l in range(NRur):
        result += Area[l]
    for l in range(NRur, nlu):
        result += Area[l]
    return result

# @time_function
@memoize
def AreaTotal_2(Area):
    return np.sum(Area)