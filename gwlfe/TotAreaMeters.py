import numpy as np
from Timer import time_function
from AreaTotal import AreaTotal


def TotAreaMeters(NRur, NUrb, Area):
    result = 0.0
    areatotal = AreaTotal(NRur, NUrb, Area)
    result = areatotal * 10000
    return result


def TotAreaMeters_2():
    pass
