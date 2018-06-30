from numpy import absolute
from numpy import multiply
from numpy import where
from numpy import zeros

from gwlfe.Memoization import memoize
from gwlfe.enums import ETflag


# @memoize #TODO: adding memoization causes this function to not pass the tests
def DailyET(NYrs, DaysMonth, Temp, DayHrs, KV, PcntET, ETFlag):
    result = zeros((NYrs, 12, 31))
    # CALCULATE ET FROM SATURATED VAPOR PRESSURE,
    # HAMON (1961) METHOD
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                DailyTemp = Temp[Y][i][j]
                if ETFlag is ETflag.HAMON_METHOD:
                    if DailyTemp > 0:
                        SatVaPressure = (33.8639 * ((0.00738 * DailyTemp +
                                                     0.8072) ** 8 - 0.000019 *
                                                    absolute(1.8 * DailyTemp + 48) +
                                                    0.001316))
                        PotenET = (0.021 * DayHrs[i] ** 2 * SatVaPressure / (DailyTemp + 273))
                        ET = KV[i] * PotenET * PcntET[i]
                        result[Y][i][j] = ET
    return result


@memoize
def SatVaPressure(Temp):
    return (33.8639 * ((0.00738 * Temp + 0.8072) ** 8 - 0.000019 * absolute(1.8 * Temp + 48) + 0.001316))


@memoize
def PotentET(DayHrs, Temp):
    return multiply(0.021 * ((DayHrs ** 2).reshape(12, 1)), SatVaPressure(Temp)) / (Temp + 273)


@memoize
def DailyET_f(Temp, KV, PcntET, DayHrs):
    return where(Temp > 0, multiply((KV * PcntET).reshape(12, 1), PotentET(DayHrs, Temp)), 0)
