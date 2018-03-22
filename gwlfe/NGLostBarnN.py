import numpy as np
from Timer import time_function
import LossFactAdj


def NGLostBarnN(NYrs, NGInitBarnN, NGBarnNRate, Precipitation, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN):
    result = np.zeros((NYrs, 12))
    lossFactAdj = LossFactAdj.LossFactAdj(NYrs, Precipitation, DaysMonth)
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = (NGInitBarnN[i] * NGBarnNRate[i] * lossFactAdj[Y][i]
                            - NGInitBarnN[i] * NGBarnNRate[i] * lossFactAdj[Y][i] * AWMSNgPct * NgAWMSCoeffN
                            + NGInitBarnN[i] * NGBarnNRate[i] * lossFactAdj[Y][i] * RunContPct * RunConCoeffN)
            if result[Y][i] > NGInitBarnN[i]:
                result[Y][i] = NGInitBarnN[i]
            if result[Y][i] < 0:
                result[Y][i] = 0
    return result


def NGLostBarnN_2(NYrs, NGInitBarnN, NGBarnNRate, Precipitation, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN):
    lossFactAdj = LossFactAdj.LossFactAdj(NYrs, Precipitation, DaysMonth)
    result = ( np.tile(NGInitBarnN, NYrs) * np.tile(NGBarnNRate,NYrs) * np.ndarray.flatten(lossFactAdj) * (1 - (AWMSNgPct * NgAWMSCoeffN) + (RunContPct * RunConCoeffN)  ) )
    result = np.minimum(result, np.tile( NGInitBarnN, NYrs ) )
    result = np.maximum(result,0)
    return np.reshape(result,(NYrs,12))
