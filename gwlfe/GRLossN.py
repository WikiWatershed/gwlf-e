import numpy as np
from Timer import time_function


def GRLossN(NYrs, GrazingN, GRStreamN, GrazingNRate, LossFactAdj):
    result = np.zeros((NYrs, 12))
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = ((GrazingN[i] - GRStreamN[i]) * GrazingNRate[i] * LossFactAdj[Y][i])
            if result[Y][i] > (GrazingN[i] - GRStreamN[i]):
                result[Y][i] = (GrazingN[i] - GRStreamN[i])
            if result[Y][i] < 0:
                result[Y][i] = 0
    return result


def GRLossN_2(NYrs, GrazingN, GRStreamN, GrazingNRate, LossFactAdj):
    result = ( np.tile( ( (GrazingN - GRStreamN) * GrazingNRate ), NYrs ) * np.ndarray.flatten(LossFactAdj))
    result = np.minimum(result, np.tile( (GrazingN-GRStreamN),NYrs))
    result = np.maximum(result, 0)
    return np.reshape(result,(NYrs,12))

