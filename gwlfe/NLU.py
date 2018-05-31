import numpy as np
from Timer import time_function
from numba import jit

from Memoization import memoize


@memoize
def NLU(NRur, NUrb):
    return NRur + NUrb


# def NLU_2():
#     pass
