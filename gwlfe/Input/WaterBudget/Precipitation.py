from numpy import average
from numpy import float64
from numpy import sum
from numpy import zeros

from gwlfe.Memoization import memoize


def Precipitation(NYrs, DaysMonth, Prec):  # TODO: change internal "Precipitation" to "result"
    Precipitation = zeros((NYrs, 12))
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                Precipitation[Y][i] = Precipitation[Y][i] + Prec[Y][i][j]
    return Precipitation


@memoize
def Precipitation_f(Prec):
    return sum(Prec, dtype=float64, axis=(2))


@memoize
def AvPrecipitation_f(Precipitation):
    return average(Precipitation, axis=0)
