import numpy as np
from Timer import time_function


def AGSTRM(AgLength, StreamLength):
    result = 0.0
    result = AgLength / StreamLength if StreamLength > 0 else 0
    return result


def AGSTRM_2():
    pass
