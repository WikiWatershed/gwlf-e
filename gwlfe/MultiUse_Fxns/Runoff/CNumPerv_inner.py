from numba.pycc import CC
from numpy import zeros

cc = CC('CNumPerv_inner_compiled')


@cc.export('CNumPerv_inner',
           '(int64, int64[:,::1], float64[:,:,::1], int64, int64, float64[:,::1], float64[:,:,::1], float64[:,:,::1], float64[::1], float64[:,:,::1])')
def CNumPerv_inner(NYrs, DaysMonth, Temp, NRur, nlu, cnp, water, melt, grow_factor, amc5):
    result = zeros((NYrs, 12, 31, nlu))
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    if water[Y][i][j] < 0.05:
                        pass
                    else:
                        for l in range(NRur, nlu):
                            if cnp[1][l] > 0:
                                if melt[Y][i][j] <= 0:
                                    if grow_factor[i] > 0:
                                        # Growing season
                                        if amc5[Y][i][j] >= 5.33:
                                            result[Y][i][j][l] = cnp[2][l]
                                        elif amc5[Y][i][j] < 3.56:
                                            result[Y][i][j][l] = cnp[0][l] + (
                                                    cnp[1][l] - cnp[0][l]) * amc5[Y][i][j] / 3.56
                                        else:
                                            result[Y][i][j][l] = cnp[1][l] + (cnp[2][l] - cnp[1][l]) * (
                                                    amc5[Y][i][j] - 3.56) / 1.77
                                    else:
                                        # Dormant season
                                        if amc5[Y][i][j] >= 2.79:
                                            result[Y][i][j][l] = cnp[2][l]
                                        elif amc5[Y][i][j] < 1.27:
                                            result[Y][i][j][l] = cnp[0][l] + (
                                                    cnp[1][l] - cnp[0][l]) * amc5[Y][i][j] / 1.27
                                        else:
                                            result[Y][i][j][l] = cnp[1][l] + (cnp[2][l] - cnp[1][l]) * (
                                                    amc5[Y][i][j] - 1.27) / 1.52
                                else:
                                    result[Y][i][j][l] = cnp[2][l]
    return result
