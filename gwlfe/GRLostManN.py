import numpy as np
from Timer import time_function
import LossFactAdj

def GRLostManN(NYrs, GRAppManN, GRAppNRate, Precipitation, DaysMonth, GRPctSoilIncRate):
    result = np.zeros((NYrs, 12))
    lossFactAdj = LossFactAdj.LossFactAdj(NYrs, Precipitation, DaysMonth)
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = (GRAppManN[i] * GRAppNRate[i] * lossFactAdj[Y][i] * (1 - GRPctSoilIncRate[i]))
            if result[Y][i] > GRAppManN[i]:
                result[Y][i] = GRAppManN[i]
            if result[Y][i] < 0:
                result[Y][i] = 0
    return result


def GRLostManN_2(NYrs, GRAppManN, GRAppNRate, Precipitation, DaysMonth, GRPctSoilIncRate):
    lossFactAdj = LossFactAdj.LossFactAdj(NYrs, Precipitation, DaysMonth)
    result = (np.tile( GRAppManN,NYrs) * np.tile( GRAppNRate, NYrs) * np.ndarray.flatten(lossFactAdj) * np.tile(( 1 - GRPctSoilIncRate),NYrs ))
    result = np.minimum(result, np.tile( GRAppManN, NYrs ) )
    result = np.maximum(result,0)
    return np.reshape(result,(NYrs,12))