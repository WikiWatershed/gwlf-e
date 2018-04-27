import numpy as np
from Timer import time_function
from Memoization import memoize


@memoize
def NLU(NRur, NUrb):
    result = NRur + NUrb
    return result


def NLU_2():
    pass
