from .enums import ETflag
import numpy as np
import Timer

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


def DailyET_2(Temp, KV, PcntET, DayHrs):
    SatVaPressure = (33.8639 * ((0.00738 * Temp + 0.8072) ** 8 - 0.000019 * np.absolute(1.8 * Temp + 48) + 0.001316))
    PotentET = np.multiply((DayHrs ** 2).reshape(12, 1), SatVaPressure) / (Temp + 273)
    ET = np.multiply((KV * PcntET).reshape(12, 1), PotentET)
    TempCondition = np.where(Temp>0, ET, 0)
    return TempCondition

if __name__ == "__main__":
    from os import sys, path
    print(path.dirname(path.dirname(path.abspath(__file__))))
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    from gwlfe import Parser
    Timer.compare_function_calls('DailyET(z.NYrs,z.DaysMonth,z.Temp,z.DayHrs,z.KV,z.PcntET,z.ETFlag)','ET.DailyET_2(z.Temp,z.KV,z.PcntET,z.DayHrs)')
    pass