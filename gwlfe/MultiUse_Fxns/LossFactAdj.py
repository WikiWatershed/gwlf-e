from Precipitation import Precipitation
from Precipitation import Precipitation_2
from ..Memoization import memoize

from numpy import zeros


def LossFactAdj(NYrs, Prec, DaysMonth):
    result = zeros((NYrs, 12))
    precipitation = Precipitation(NYrs, DaysMonth, Prec)
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = (precipitation[Y][i] / DaysMonth[Y][i]) / 0.3301
    return result

@memoize
def LossFactAdj_2(Prec, DaysMonth):
    return Precipitation_2(Prec) / DaysMonth / 0.3301
