import numpy as np
from Timer import time_function
from enums import GROWING_SEASON
from enums import GrowFlag
from Grow import Grow
from Grow import Grow_2

# @time_function
from Memoization import memoize


@memoize
def GrowFactor(Grow_0):
    result = np.zeros((12,))
    for i in range(12):
        result[i] = Grow_0[i] == GROWING_SEASON  # TODO: seems like there is some inefficency left in Grow_0
    return result


@memoize
def GrowFactor_2(Grow_0):
    return Grow_2(Grow_0)
