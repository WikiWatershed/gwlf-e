import numpy as np

def Precipitation(NYrs, DaysMonth, Prec):
    Precipitation = np.zeros((NYrs,12))
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                Precipitation[Y][i] = Precipitation[Y][i] + Prec[Y][i][j]
    return Precipitation

def AvPrecipitation(NYrs, precipitation):
    result = [0]*12
    for Y in range(NYrs):
        for i in range(12):
            print(i)
            result[i] += precipitation[Y][i] / NYrs
    return result

def Prec_to_numpy(Prec):
    return np.array(Prec)
    # result = np.array((NYrs,31))

def Precipitation_2(Prec):
    fastPrecipitation = np.sum(Prec, axis=(2))
    return fastPrecipitation

