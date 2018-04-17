import numpy as np
from Timer import time_function


def RurAreaTotal(NRur, Area):
    result = 0
    for l in range(NRur):
        result += Area[l]
    return result


def RurAreaTotal_2():
    pass
