from numba.pycc import CC
from numpy import zeros

cc = CC('UrbLoadRed_inner_compiled')


@cc.export('UrbLoadRed_inner',
           '(int64, int32[:,::1], float64[:,:,::1], int64, int64, int64, float64[:,::1], float64[:,:,::1], float64[:,:,::1], int64)')
def UrbLoadRed_inner(NYrs, DaysMonth, Temp, NRur, Nqual, Storm, UrbBMPRed, water, adjurbanqtotal, nlu):
    result = zeros((NYrs, 12, 31, 16, Nqual))
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    if adjurbanqtotal[Y][i][j] > 0.001:
                        for l in range(NRur, nlu):
                            for q in range(Nqual):
                                result[Y][i][j][l][q] = (water[Y][i][j] / Storm) * UrbBMPRed[l][q]
                                if water[Y][i][j] > Storm:
                                    result[Y][i][j][l][q] = UrbBMPRed[l][q]
                else:
                    pass
    return result
