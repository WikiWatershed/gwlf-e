from numpy import where
from numpy import zeros

from gwlfe.Input.WaterBudget.InitSnow import InitSnow
from gwlfe.Input.WaterBudget.InitSnowYesterday import InitSnowYesterday
from gwlfe.Input.WaterBudget.Melt import Melt, Melt_f
from gwlfe.Memoization import memoize


@memoize
def Melt_1(NYrs, DaysMonth, InitSnow_0, Temp, Prec):
    result = zeros((NYrs, 12, 31))
    init_snow = InitSnow(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    init_snow_yesterday = InitSnow_0
    melt = Melt(NYrs, DaysMonth, Temp, InitSnow_0, Prec)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and init_snow_yesterday > 0.001 and melt[Y][i][j] > init_snow_yesterday:
                    result[Y][i][j] = init_snow_yesterday
                else:
                    result[Y][i][j] = melt[Y][i][j]
                init_snow_yesterday = init_snow[Y][i][j]
    return result


@memoize
def Melt_1_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec):
    # result = np.zeros((NYrs, 12, 31))
    init_snow_yesterday = InitSnowYesterday(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    melt = Melt_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec)
    melt[where((Temp > 0) & (init_snow_yesterday > 0.001) & (melt > init_snow_yesterday))] = init_snow_yesterday[
        where((Temp > 0) & (init_snow_yesterday > 0.001) & (melt > init_snow_yesterday))]
    return melt
