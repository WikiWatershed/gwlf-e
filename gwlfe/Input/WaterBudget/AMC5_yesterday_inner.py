from numba.pycc import CC
from numpy import zeros

cc = CC('AMC5_yesterday_inner_compiled')


@cc.export('AMC5_yesterday_inner', '(int64, int64[:,::1], float64[::1], float64[:,:,::1])')
def AMC5_yesterday_inner(NYrs, DaysMonth, AntMoist_0, water):
    result = zeros((NYrs, 12, 31))
    AntMoist1 = zeros((5,))
    AMC5 = 0
    for k in range(5):
        AMC5 += AntMoist_0[k]
        AntMoist1[k] = AntMoist_0[k]
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                result[Y][i][j] = AMC5
                AMC5 = AMC5 - AntMoist1[4] + water[Y][i][j]
                AntMoist1[4] = AntMoist1[3]
                AntMoist1[3] = AntMoist1[2]
                AntMoist1[2] = AntMoist1[1]
                AntMoist1[1] = AntMoist1[0]
                AntMoist1[0] = water[Y][i][j]
    return result
