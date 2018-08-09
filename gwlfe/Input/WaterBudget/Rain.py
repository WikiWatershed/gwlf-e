from numpy import where
from numpy import zeros

from gwlfe.Memoization import memoize


def Rain_inner(NYrs, DaysMonth, Temp, Prec):
    result = zeros((NYrs, 12, 31))
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                result[Y][i][j] = 0
                if Temp[Y][i][j] <= 0:
                    pass
                else:
                    result[Y][i][j] = Prec[Y][i][j]
    return result


@memoize
def Rain(NYrs, DaysMonth, Temp, Prec):
    return Rain_inner(NYrs, DaysMonth, Temp, Prec)


@memoize
def Rain_f(Temp, Prec):
    return where(Temp <= 0, 0, Prec)
