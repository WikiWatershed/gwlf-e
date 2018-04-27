import numpy as np
from Timer import time_function
from enums import GrowFlag
from Memoization import memoize


@memoize
def GrowFactor(Grow):
    result = np.zeros((12,))
    for i in range(12):
        result[i] = GrowFlag.intval(Grow[i])  # TODO: seems like there is some inefficency left in Grow
    return result


def GrowFactor_2():
    pass
