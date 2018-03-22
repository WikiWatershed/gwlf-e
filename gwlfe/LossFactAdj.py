import numpy as np
from Timer import time_function


def LossFactAdj(NYrs, Precipitation, DaysMonth):
    result = np.zeros((NYrs, 12))
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = (Precipitation[Y][i] / DaysMonth[Y][i]) / 0.3301
    return result


def LossFactAdj_2(NYrs, Precipitation, DaysMonth):
    result = Precipitation / DaysMonth / 0.3301
    return result
