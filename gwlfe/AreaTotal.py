# from Timer import time_function
from Memoization import memoize
from NLU import NLU
from numpy import sum

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
def AreaTotal_f(Area):
    return sum(Area)