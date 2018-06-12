from numpy import zeros

# from Timer import time_function
from InitSnow import InitSnow
from Melt import Melt
from Memoization import memoize


# Not used in other calculations
@memoize
def MeltPest(NYrs, DaysMonth, InitSnow_0, Temp, Prec):
    result = zeros((NYrs, 12, 31))
    init_snow = InitSnow(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    init_snow_yesterday = InitSnow_0
    melt = Melt(NYrs, DaysMonth, Temp, InitSnow_0, Prec)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and init_snow_yesterday > 0.001:
                    if melt[Y][i][j] > init_snow_yesterday:
                        # TODO: code seems to run fine with with only these three condidtions anded together
                        result[Y][i][j] = init_snow_yesterday
                    else:
                        result[Y][i][j] = melt[Y][i][j]
                else:
                    result[Y][i][j] = 0
                init_snow_yesterday = init_snow[Y][i][j]
    return result


def MeltPest_2():
    pass
