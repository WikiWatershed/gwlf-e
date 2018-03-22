import numpy as np
from Timer import time_function
import LossFactAdj

def NGLostManN(NYrs, NGAppManN, NGAppNRate, Precipitation, DaysMonth, NGPctSoilIncRate):
    # Non-grazing animal losses
    result = np.zeros((NYrs, 12))
    lossFactAdj = LossFactAdj.LossFactAdj(NYrs, Precipitation, DaysMonth)
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = (NGAppManN[i] * NGAppNRate[i] * lossFactAdj[Y][i]
                            * (1 - NGPctSoilIncRate[i]))
            if result[Y][i] > NGAppManN[i]:
                result[Y][i] = NGAppManN[i]
            if result[Y][i] < 0:
                result[Y][i] = 0
    return result


def NGLostManN_2(NYrs, NGAppManN, NGAppNRate, Prec, DaysMonth, NGPctSoilIncRate):
    lossFactAdj = LossFactAdj.LossFactAdj(NYrs, Prec, DaysMonth)
    result = np.tile(NGAppManN * NGAppNRate * ( 1 - NGPctSoilIncRate ) ,NYrs) * np.ndarray.flatten(lossFactAdj)
    result = np.minimum(result, np.tile( NGAppManN, NYrs))
    result = np.maximum(result, 0)
    return np.reshape(result,(NYrs,12))
