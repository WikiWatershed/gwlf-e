import numpy as np
from Timer import time_function
from Memoization import memoize


@memoize
def FilterEff(FilterWidth):
    if FilterWidth <= 30:
        result = FilterWidth / 30
    else:
        result = 1
    return result


def FilterEff_2():
    pass
