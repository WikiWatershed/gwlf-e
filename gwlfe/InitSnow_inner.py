from numba.pycc import CC
import numpy as np

cc = CC('InitSnow_2_inner_compiled')

@cc.export('InitSnow_2_inner', '(int64, int32[:,::1], int64, float64[:,:,::1], float64[:,:,::1])')
def InitSnow_2_inner(NYrs, DaysMonth, InitSnow_0, Temp, Prec):
    result = np.zeros((NYrs, 12, 31))
    yesterday = InitSnow_0
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] <= 0:
                    result[Y][i][j] = yesterday + Prec[Y][i][j]
                else:
                    if yesterday > 0.001:
                        result[Y][i][j] = max(yesterday - 0.45 * Temp[Y][i][j], 0)
                    else:
                        result[Y][i][j] = yesterday
                yesterday = result[Y][i][j]
    return result
