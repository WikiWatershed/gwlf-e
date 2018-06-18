from numba.pycc import CC
from numpy import zeros

cc = CC('Percolation_inner_compiled')


@cc.export('Percolation_inner', '(int64, float64, int64[:,::1], float64, float64[:,:,::1], float64[:,:,::1])')
def Percolation_inner(NYrs, UnsatStor_0, DaysMonth, MaxWaterCap, infiltration, et):
    result = zeros((NYrs, 12, 31))
    percolation = zeros((NYrs, 12, 31))
    unsatstor_carryover = UnsatStor_0
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                result[Y][i][j] = unsatstor_carryover
                result[Y][i][j] = result[Y][i][j] + infiltration[Y][i][j]
                if et[Y][i][j] >= result[Y][i][j]:
                    result[Y][i][j] = 0
                else:
                    result[Y][i][j] = result[Y][i][j] - et[Y][i][j]
                if result[Y][i][j] > MaxWaterCap:
                    percolation[Y][i][j] = result[Y][i][j] - MaxWaterCap
                    result[Y][i][j] = MaxWaterCap
                else:
                    pass
                unsatstor_carryover = result[Y][i][j]
    return percolation
