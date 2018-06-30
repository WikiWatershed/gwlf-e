from numpy import where
from numpy import zeros

from gwlfe.Input.WaterBudget.InitSnow import InitSnow
from gwlfe.Input.WaterBudget.InitSnowYesterday import InitSnowYesterday
from gwlfe.Input.WaterBudget.Melt_1 import Melt_1, Melt_1_f
from gwlfe.Input.WaterBudget.Rain import Rain, Rain_f
from gwlfe.Memoization import memoize


@memoize
def Erosiv(NYrs, DaysMonth, Temp, InitSnow_0, Prec, Acoef):
    result = zeros((NYrs, 12, 31))
    init_snow = InitSnow(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    init_snow_yesterday = InitSnow_0
    rain = Rain(NYrs, DaysMonth, Temp, Prec)
    melt_1 = Melt_1(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0:
                    if (init_snow_yesterday > 0.001):
                        if rain[Y][i][j] > 0 and init_snow_yesterday - melt_1[Y][i][j] < 0.001:
                            result[Y][i][j] = 6.46 * Acoef[i] * rain[Y][i][j] ** 1.81
                    else:
                        if rain[Y][i][j] > 0 and init_snow_yesterday < 0.001:
                            result[Y][i][j] = 6.46 * Acoef[i] * rain[Y][i][j] ** 1.81

                init_snow_yesterday = init_snow[Y][i][j]
    return result


def Erosiv_f(NYrs, DaysMonth, Temp, InitSnow_0, Prec, Acoef):
    result = zeros((NYrs, 12, 31))
    rain = Rain_f(Temp, Prec)
    init_snow_yesterday = InitSnowYesterday(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    melt_1 = Melt_1_f(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    erosiv = 6.46 * Acoef.reshape((12, 1)) * rain ** 1.81
    result[where((Temp > 0) & (init_snow_yesterday > 0.001) & (rain > 0) & (init_snow_yesterday - melt_1 < 0.001))] = \
    erosiv[where((Temp > 0) & (init_snow_yesterday > 0.001) & (rain > 0) & (init_snow_yesterday - melt_1 < 0.001))]
    result[where((Temp > 0) & (init_snow_yesterday <= 0.001) & (rain > 0))] = erosiv[
        where((Temp > 0) & (init_snow_yesterday <= 0.001) & (rain > 0))]
    return result
