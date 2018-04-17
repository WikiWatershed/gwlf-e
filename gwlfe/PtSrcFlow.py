import numpy as np
from Timer import time_function


def PtSrcFlow(NYrs, PointFlow):
    result = np.zeros((NYrs, 12))
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = result[Y][i] + PointFlow[i]
    return result


def PtSrcFlow_2(NYrs, PointFlow):
    return np.repeat(PointFlow[:, None], NYrs, axis=1).T


def AvPtSrcFlow(NYrs, PtSrcFlow):
    result = np.zeros((12,))
    for Y in range(NYrs):
        for i in range(12):
            result[i] += PtSrcFlow[Y][i] / NYrs
    return result


def AvPtSrcFlow_2(PointFlow):
    return PointFlow
