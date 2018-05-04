import numpy as np
from gwlfe.Timer import time_function

def Precipitation(NYrs, DaysMonth, Prec):#TODO: change internal "Precipitation" to "result"
    Precipitation = np.zeros((NYrs,12))
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                Precipitation[Y][i] = Precipitation[Y][i] + Prec[Y][i][j]
    return Precipitation

def Precipitation_2(Prec):
    return np.sum(Prec, axis=(2))


