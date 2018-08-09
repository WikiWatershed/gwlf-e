from numpy import zeros

from gwlfe.Input.WaterBudget.Precipitation import Precipitation
from gwlfe.Input.WaterBudget.Precipitation import Precipitation_f
from gwlfe.Memoization import memoize


def LossFactAdj(NYrs, Prec, DaysMonth):
    result = zeros((NYrs, 12))
    precipitation = Precipitation(NYrs, DaysMonth, Prec)
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = (precipitation[Y][i] / DaysMonth[Y][i]) / 0.3301
    return result


@memoize
def LossFactAdj_f(Prec, DaysMonth):
    return Precipitation_f(Prec) / DaysMonth / 0.3301
