import numpy as np
from Timer import time_function

def memoize(f):
    """ Memoization decorator for functions taking one or more arguments. """
    class memodict(dict):
        def __init__(self, f):
            self.f = f
        def __call__(self, *args):
            return self[args]
        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret
    return memodict(f)

def InitSnow(NYrs, DaysMonth, InitSnow_0, Temp, Prec):
    result = np.zeros((NYrs, 12, 31))
    yesterday = InitSnow_0
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):

                if Temp[Y][i][j] <= 0:
                    result[Y][i][j] = yesterday + Prec[Y][i][j]
                else:
                    if yesterday > 0.001:
                        result[Y][i][j] = max(yesterday - 0.45 * Temp[Y][i][j], 0)
                    else:
                        result[Y][i][j] = yesterday
                yesterday = result[Y][i][j]
    return result


def InitSnow_2():
    pass
