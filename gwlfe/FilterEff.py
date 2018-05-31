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


#Both have same running time
@memoize
def FilterEff_2(FilterWidth):
    result = 1
    if FilterWidth <= 30:
        result = FilterWidth / 30
    return result
