import numpy as np
from Timer import time_function
from Memoization import memoize


#RurAreaTotal is faster
@memoize
# @time_function
def RurAreaTotal(NRur, Area):
    result = 0
    for l in range(NRur):
        result += Area[l]
    return result

# @memoize
# @time_function
def RurAreaTotal_2(NRur, Area):
    return np.sum(Area[0:NRur])
