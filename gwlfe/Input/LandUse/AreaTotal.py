# from Timer import time_function
from gwlfe.Memoization import memoize
from gwlfe.Input.LandUse.NLU import NLU
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