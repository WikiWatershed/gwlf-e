import copy

from numpy import zeros

from gwlfe.Input.WaterBudget.Water import Water
from gwlfe.Memoization import memoize


@memoize
def AntMoist(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0):
    result = zeros((NYrs, 12, 31))
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    AMC5 = 0
    AntMoist = copy.deepcopy(AntMoist_0)
    for k in range(5):
        AMC5 += AntMoist[k]
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                AMC5 = AMC5 - AntMoist[4] + water[Y][i][j]
                AntMoist[4] = AntMoist[3]
                AntMoist[3] = AntMoist[2]
                AntMoist[2] = AntMoist[1]
                AntMoist[1] = AntMoist[0]
                AntMoist[0] = water[Y][i][j]

                result[Y][i][j] = AMC5  # TODO: why did this fix the mismatch of amc5?
    return AntMoist


def AntMoist_f():
    pass
