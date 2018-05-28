import numpy as np
from Timer import time_function
from enums import GROWING_SEASON
from numba import jit
from enums import GrowFlag
from Grow import Grow_2

# @time_function
from Memoization import memoize


# @jit(cache=True, nopython = True)
@memoize
def GrowFactor(Grow):
    result = np.zeros((12,))
    for i in range(12):
        result[i] = Grow[i]==GROWING_SEASON  # TODO: seems like there is some inefficency left in Grow
    return result
#GrowFactor function is more effiecient than GrowFactor_2
# @time_function
# @jit
def GrowFactor_2(Grow_0):
    return Grow_2(Grow_0)
