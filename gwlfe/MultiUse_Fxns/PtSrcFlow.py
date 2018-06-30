from numpy import repeat
from numpy import zeros

from gwlfe.Memoization import memoize


@memoize
def PtSrcFlow(NYrs, PointFlow):
    result = zeros((NYrs, 12))
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = result[Y][i] + PointFlow[i]
    return result


def PtSrcFlow_f(NYrs, PointFlow):
    return repeat(PointFlow[:, None], NYrs, axis=1).T


def AvPtSrcFlow(NYrs, PtSrcFlow):
    result = zeros((12,))
    for Y in range(NYrs):
        for i in range(12):
            result[i] += PtSrcFlow[Y][i] / NYrs
    return result


@memoize
def AvPtSrcFlow_f(PointFlow):
    return PointFlow
