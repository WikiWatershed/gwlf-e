from numba.pycc import CC
from numpy import zeros

cc = CC('CNum_inner_compiled')


@cc.export('CNum_inner',
           '(int64, int64[:,::1],float64[:,:,::1],float64[::1],int64,float64[:,:,::1],float64[:,::1],float64[:,:,::1],boolean[::1],float64[:,:,::1])')
def CNum_inner(NYrs, DaysMonth, Temp, CN, NRur, melt_pest, newcn, amc5, grow_factor, water):
    result = zeros((NYrs, 12, 31, NRur))  # TODO: should we just generalize to NLU?
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:  # forgot this
                    for l in range(NRur):
                        if CN[l] > 0:
                            if melt_pest[Y][i][j] <= 0:
                                if grow_factor[i] == True:
                                    # growing season
                                    if amc5[Y][i][j] >= 5.33:  # forgot "get value from yesterday"
                                        result[Y][i][j][l] = newcn[2][l]
                                    elif amc5[Y][i][j] < 3.56:
                                        result[Y][i][j][l] = newcn[0][l] + (
                                                CN[l] - newcn[0][l]) * amc5[Y][i][j] / 3.56
                                    else:
                                        result[Y][i][j][l] = CN[l] + (newcn[2][l] - CN[l]) * (
                                                amc5[Y][i][j] - 3.56) / 1.77
                                else:
                                    # dormant season
                                    if amc5[Y][i][j] >= 2.79:
                                        result[Y][i][j][l] = newcn[2][l]
                                    elif amc5[Y][i][j] < 1.27:
                                        result[Y][i][j][l] = newcn[0][l] + (
                                                CN[l] - newcn[0][l]) * amc5[Y][i][j] / 1.27
                                    else:
                                        result[Y][i][j][l] = CN[l] + (newcn[2][l] - CN[l]) * (
                                                amc5[Y][i][j] - 1.27) / 1.52
                            else:
                                result[Y][i][j][l] = newcn[2][l]
    return result
