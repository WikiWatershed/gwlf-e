# from Timer import time_function
from gwlfe.Memoization import memoize


@memoize
def AGSTRM(AgLength, StreamLength):
    result = 0.0
    result = AgLength / StreamLength if StreamLength > 0 else 0
    return result

@memoize
def AGSTRM_f(AgLength, StreamLength):
    if(StreamLength > 0):
        return AgLength / StreamLength
    else:
        return 0
