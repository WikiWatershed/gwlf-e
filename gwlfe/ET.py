from .enums import ETflag
import numpy as np
from Timer import time_function
from Memoization import memoize


@memoize
def DailyET(NYrs, DaysMonth, Temp, DayHrs, KV, PcntET, ETFlag):
    result = np.zeros((NYrs, 12, 31))
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
                                                    np.absolute(1.8 * DailyTemp + 48) +
                                                    0.001316))
                        PotenET = (0.021 * DayHrs[i] ** 2 * SatVaPressure / (DailyTemp + 273))
                        ET = KV[i] * PotenET * PcntET[i]
                        result[Y][i][j] = ET
    return result


@memoize
def SatVaPressure(Temp):
    return (33.8639 * ((0.00738 * Temp + 0.8072) ** 8 - 0.000019 * np.absolute(1.8 * Temp + 48) + 0.001316))


@memoize
def PotentET(DayHrs, Temp):
    return np.multiply(0.021 * ((DayHrs ** 2).reshape(12, 1)), SatVaPressure(Temp)) / (Temp + 273)


@memoize
def DailyET_2(Temp, KV, PcntET, DayHrs):
    return np.where(Temp > 0, np.multiply((KV * PcntET).reshape(12, 1), PotentET(DayHrs, Temp)), 0)
